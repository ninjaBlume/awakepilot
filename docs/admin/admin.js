(() => {
  'use strict';
  // Static hosting cannot set frame-ancestors headers. Keep the form disabled
  // until this check, and fail closed if embedded in any frame.
  if (window.top !== window.self) {
    document.body.textContent = 'Yönetim panelini kendi sekmesinde aç.';
    return;
  }
  const apiOrigin = 'https://api-awakepilot.codentum.net';
  const el = id => document.getElementById(id);
  const topics = {bug: 'Hata bildirimi', suggestion: 'Öneri', general: 'Genel'};
  const dateTime = new Intl.DateTimeFormat('tr-TR', {dateStyle: 'medium', timeStyle: 'short', timeZone: 'Europe/Istanbul'});
  const dateOnly = new Intl.DateTimeFormat('tr-TR', {day: 'numeric', month: 'short', timeZone: 'UTC'});
  const integer = value => Math.max(0, Math.floor(Number(value) || 0));
  let token = '', messages = [], requestNumber = 0, controller, timer, loading = false;
  function status(text, error = false) {
    el('status').textContent = text;
    el('status').classList.toggle('error', error);
  }
  function busy(value) {
    loading = value;
    el('login-button').disabled = value;
    el('refresh').disabled = value;
    el('results').setAttribute('aria-busy', String(value));
  }
  function lock(message = '') {
    token = ''; messages = []; requestNumber++;
    controller?.abort(); controller = undefined;
    clearInterval(timer); timer = undefined;
    el('key').value = '';
    el('feedback').replaceChildren(); el('chart').replaceChildren(); el('daily-rows').replaceChildren();
    for (const id of ['count-1', 'count-7', 'count-30', 'feedback-total']) el(id).textContent = '—';
    el('asof').textContent = ''; el('chart-start').textContent = ''; el('visible-count').textContent = '0 mesaj';
    el('results').hidden = true; el('logout').hidden = true; el('login-section').hidden = false;
    el('search').value = ''; el('category').value = 'all';
    busy(false); status(message, Boolean(message));
  }
  async function api(path, access, signal) {
    const response = await fetch(apiOrigin + '/admin/' + path, {
      headers: {Authorization: 'Bearer ' + access}, cache: 'no-store', credentials: 'omit', redirect: 'error', signal
    });
    if (!response.ok) {
      const error = new Error(response.status === 401 ? 'Yönetim anahtarı geçersiz. Tekrar giriş yap.' : response.status === 429 ? 'Çok sık yenileme yapıldı. Bir dakika sonra tekrar dene.' : 'Veriler yenilenemedi. Bağlantını kontrol edip tekrar dene.');
      error.status = response.status;
      throw error;
    }
    return response.json();
  }
  function renderTrend(daily) {
    const rows = Array.isArray(daily) ? daily : [];
    const svgNS = 'http://www.w3.org/2000/svg';
    const svg = document.createElementNS(svgNS, 'svg');
    svg.setAttribute('viewBox', '0 0 900 150'); svg.setAttribute('preserveAspectRatio', 'none'); svg.setAttribute('role', 'img');
    svg.setAttribute('aria-label', 'Son 30 günün günlük aktif gönüllü kurulumları. Ayrıntılar günlük sayılar tablosunda.');
    const baseline = document.createElementNS(svgNS, 'line');
    for (const [key, value] of Object.entries({x1: 0, y1: 140, x2: 900, y2: 140, class: 'chart-baseline'})) baseline.setAttribute(key, value);
    svg.append(baseline);
    const max = Math.max(1, ...rows.map(row => integer(row.count))), width = 900 / Math.max(1, rows.length);
    const table = document.createDocumentFragment();
    rows.forEach((row, index) => {
      const count = integer(row.count), label = dateOnly.format(new Date(row.day + 'T00:00:00Z'));
      const bar = document.createElementNS(svgNS, 'rect'), title = document.createElementNS(svgNS, 'title');
      const height = count ? Math.max(3, count / max * 122) : 1;
      for (const [key, value] of Object.entries({x: index * width + 4, y: 140 - height, width: Math.max(1, width - 8), height, rx: 3, class: 'chart-bar'})) bar.setAttribute(key, value);
      title.textContent = label + ': ' + count + ' kurulum'; bar.append(title); svg.append(bar);
      const tr = document.createElement('tr'), day = document.createElement('td'), number = document.createElement('td');
      day.textContent = label; number.textContent = count; tr.append(day, number); table.append(tr);
    });
    el('chart').replaceChildren(svg); el('daily-rows').replaceChildren(table);
    el('chart-start').textContent = rows.length ? dateOnly.format(new Date(rows[0].day + 'T00:00:00Z')) : '';
  }
  function renderFeedback() {
    const query = el('search').value.trim().toLocaleLowerCase('tr-TR'), category = el('category').value;
    const visible = messages.filter(item => (category === 'all' || item.category === category) &&
      [item.message, item.email, item.version, item.language].join(' ').toLocaleLowerCase('tr-TR').includes(query));
    el('visible-count').textContent = visible.length + ' mesaj';
    const list = document.createDocumentFragment();
    for (const item of visible) {
      const article = document.createElement('article'); article.className = 'feedback-item';
      const head = document.createElement('div'); head.className = 'message-head';
      const topic = document.createElement('span'); topic.className = 'topic ' + (Object.hasOwn(topics, item.category) ? item.category : 'general');
      topic.textContent = topics[item.category] || topics.general;
      const date = document.createElement('time'); date.dateTime = item.created_at; date.textContent = dateTime.format(new Date(item.created_at));
      head.append(topic, date);
      const message = document.createElement('pre'); message.className = 'message-text'; message.textContent = item.message;
      const meta = document.createElement('div'); meta.className = 'message-meta';
      const version = document.createElement('span'); version.textContent = item.version ? 'Sürüm ' + item.version : 'Sürüm belirtilmemiş';
      const language = document.createElement('span'); language.textContent = 'Dil: ' + item.language; meta.append(version, language);
      if (item.email) {
        const email = document.createElement('a'); email.href = 'mailto:' + encodeURIComponent(item.email); email.textContent = item.email; meta.append(email);
      }
      article.append(head, message, meta); list.append(article);
    }
    if (!visible.length) {
      const empty = document.createElement('div'); empty.className = 'empty';
      const symbol = document.createElement('div'); symbol.className = 'empty-symbol'; symbol.setAttribute('aria-hidden', 'true'); symbol.textContent = '↗';
      const title = document.createElement('h3'); title.textContent = messages.length ? 'Bu aramada mesaj bulunamadı' : 'Henüz geri bildirim yok';
      const detail = document.createElement('p'); detail.textContent = messages.length ? 'Aramayı veya konu filtresini değiştirerek tekrar dene.' : 'Uygulama veya web sitesindeki formdan gelen mesajlar burada görünecek.';
      empty.append(symbol, title, detail); list.append(empty);
    }
    el('feedback').replaceChildren(list);
  }
  async function refresh() {
    if (!token || loading) return;
    const access = token, number = ++requestNumber;
    controller = new AbortController(); const currentController = controller;
    busy(true); status('Veriler yükleniyor…');
    try {
      const [summary, inbox] = await Promise.all([api('summary', access, currentController.signal), api('feedback', access, currentController.signal)]);
      if (token !== access || requestNumber !== number) return;
      for (const days of [1, 7, 30]) el('count-' + days).textContent = integer(summary.activeInstallations[days]).toLocaleString('tr-TR');
      el('feedback-total').textContent = integer(summary.feedback?.total ?? inbox.feedback.length).toLocaleString('tr-TR');
      messages = inbox.feedback; renderFeedback(); renderTrend(summary.dailyInstallations);
      el('asof').textContent = 'Son güncelleme: ' + dateTime.format(new Date(summary.asOf)) + ' · Türkiye saati';
      el('login-section').hidden = true; el('results').hidden = false; el('logout').hidden = false;
      if (!timer) timer = setInterval(() => { if (document.visibilityState === 'visible') refresh(); }, 60000);
      status('');
    } catch (error) {
      if (token !== access || requestNumber !== number || error.name === 'AbortError') return;
      currentController.abort();
      if (error.status === 401) { lock(error.message); el('key').focus(); }
      else status(error.status ? error.message : el('results').hidden ? 'Veriler alınamadı. Bağlantını kontrol edip tekrar dene.' : 'Veriler yenilenemedi. Son başarılı kontrolün bilgileri gösteriliyor.', true);
    } finally {
      if (requestNumber === number) { busy(false); controller = undefined; }
    }
  }
  el('login').addEventListener('submit', event => {
    event.preventDefault(); const key = el('key').value.trim(); if (!key) return;
    lock(); token = key; refresh();
  });
  el('refresh').addEventListener('click', refresh);
  el('logout').addEventListener('click', () => { lock(); el('key').focus(); });
  el('search').addEventListener('input', renderFeedback);
  el('category').addEventListener('change', renderFeedback);
  window.addEventListener('pagehide', () => lock());
  el('key').disabled = false; el('login-button').disabled = false;
})();
