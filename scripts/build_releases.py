#!/usr/bin/env python3
"""Generate the Release notes pages (EN, DE, TR) from scripts/releases_data.py.

Header and footer are taken from each language's support page, so the new
pages always match the rest of the site. Run from the repository root:

    python3 scripts/build_releases.py
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from releases_data import LANGS, RELEASES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = "https://awakepilot.codentum.net/"
DOWNLOAD = "https://github.com/ninjaBlume/awakepilot/releases/latest/download/Awakepilot.dmg"
STYLES_VERSION = "20261008-2"


def inline(text: str) -> str:
    """Escape text, then apply `code` and **bold**."""
    out = html.escape(text, quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)


def fmt_date(lang: dict, ymd: tuple) -> str:
    year, month, day = ymd
    return lang["date_fmt"].format(day=day, month=lang["months"][month - 1], year=year)


def slug(version: str) -> str:
    return "v" + version.replace(".", "-")


def render_release(lang: dict, release: dict, latest: bool) -> str:
    data = release[lang_code]
    parts = [f'<article class="release{" release-latest" if latest else ""}" id="{slug(release["version"])}">']
    badge = f'<span class="release-badge">{html.escape(lang["latest"])}</span>' if latest else ""
    y, m, d = release["date"]
    parts.append(
        f'<header class="release-head"><h2>{release["version"]}</h2>{badge}'
        f'<time datetime="{y:04d}-{m:02d}-{d:02d}">{fmt_date(lang, release["date"])}</time></header>'
    )
    parts.append(f'<p class="release-summary">{inline(data["summary"])}</p>')
    for heading, body in data["sections"]:
        parts.append(f"<h3>{inline(heading)}</h3>")
        if isinstance(body, str):
            parts.append(f"<p>{inline(body)}</p>")
        else:
            parts.append("<ul>" + "".join(f"<li>{inline(item)}</li>" for item in body) + "</ul>")
    if "note" in data:
        title, text = data["note"]
        parts.append(f'<aside class="release-note"><strong>{inline(title)}</strong><p>{inline(text)}</p></aside>')
    parts.append("</article>")
    return "".join(parts)


def build(code: str) -> None:
    global lang_code
    lang_code = code
    lang = LANGS[code]
    folder = ROOT / lang["dir"]
    support = (folder / "support.html").read_text(encoding="utf8")

    html_open = re.match(r"(.*?<html[^>]*>)", support, re.S).group(1)
    header = re.search(r'<header class="site-header">.*?</header>', support, re.S).group(0)
    footer = re.search(r'<footer class="site-footer">.*?</footer>', support, re.S).group(0)

    # Header: language switcher points at the matching releases page; no nav item is "current".
    def fix_switcher(match: re.Match) -> str:
        return match.group(0).replace("support.html", "releases.html")

    header = re.sub(r'<div class="language-switcher".*?</div>', fix_switcher, header, flags=re.S)
    header = re.sub(r'(<div class="nav-links">.*?</div>)', lambda m: m.group(1).replace(' aria-current="page"', ""), header, count=1, flags=re.S)

    asset_prefix = "" if code == "en" else "../"
    page_url = ORIGIN + lang["prefix"] + "releases.html"
    alternates = "".join(
        f'\n  <link rel="alternate" hreflang="{c}" href="{ORIGIN}{LANGS[c]["prefix"]}releases.html">' for c in ("en", "de", "tr")
    )
    title = html.escape(lang["title"])
    description = html.escape(lang["description"])
    versions_nav = "".join(
        f'<a href="#{slug(r["version"])}">{r["version"]}{" · " + html.escape(lang["latest"]) if i == 0 else ""}</a>'
        for i, r in enumerate(RELEASES)
    )
    articles = "".join(render_release(lang, r, i == 0) for i, r in enumerate(RELEASES))
    skip = re.search(r'<a class="skip-link"[^>]*>[^<]*</a>', support).group(0)

    page = f"""{html_open}
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#0b1020"><title>{title}</title>
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{lang["locale"]}">
  <meta property="og:url" content="{page_url}">
  <meta property="og:image" content="{ORIGIN}assets/icon.png">
  <link rel="canonical" href="{page_url}">{alternates}
  <link rel="alternate" hreflang="x-default" href="{ORIGIN}releases.html">
  <link rel="icon" href="{asset_prefix}assets/icon.png"><link rel="apple-touch-icon" href="{asset_prefix}assets/icon.png"><link rel="stylesheet" href="{asset_prefix}styles.css?v={STYLES_VERSION}">
</head>
<body>
  {skip}
  {header}
  <main id="main">
    <section class="legal-hero shell"><span class="kicker">{html.escape(lang["kicker"])}</span><h1>{html.escape(lang["h1"])}</h1><p>{html.escape(lang["lead"])}</p>
      <div class="release-actions"><a class="button button-large" href="{DOWNLOAD}">{html.escape(lang["download"])}</a><a class="button button-ghost button-large" href="{lang["support_href"]}">{html.escape(lang["support"])}</a></div>
    </section>
    <div class="legal-layout shell">
      <aside class="legal-nav" aria-label="{html.escape(lang["index_label"])}">{versions_nav}</aside>
      <div class="release-list">{articles}</div>
    </div>
  </main>
  {footer}
</body>
</html>
"""
    (folder / "releases.html").write_text(page, encoding="utf8")
    print(f"wrote {lang['dir']}/releases.html")


for code in LANGS:
    build(code)
