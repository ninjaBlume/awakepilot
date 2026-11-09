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
  if (!el('service-checks') || !el('state-filter')) {
    const link = document.createElement('a'); link.href = 'https://awakepilot.codentum.net/admin/?v=20261109-2';
    link.textContent = 'Panel güncellendi. Güncel paneli aç.';
    document.body.replaceChildren(link); return;
  }
  const topics = {bug: 'Hata bildirimi', suggestion: 'Öneri', general: 'Genel'};
  const states = {new:'Yeni',in_review:'İnceleniyor',resolved:'Çözüldü'};
  const dateTime = new Intl.DateTimeFormat('tr-TR', {dateStyle: 'medium', timeStyle: 'short', timeZone: 'Europe/Istanbul'});
  const dateOnly = new Intl.DateTimeFormat('tr-TR', {day: 'numeric', month: 'short', timeZone: 'UTC'});
  const integer = value => Math.max(0, Math.floor(Number(value) || 0));
  let token = '', messages = [], requestNumber = 0, sessionNumber = 0, controller, timer, loading = false;
  const drafts = new Map(), saveMessages = new Map(), saving = new Set(), saveControllers = new Set();
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
    token = ''; messages = []; requestNumber++; sessionNumber++;
    controller?.abort(); controller = undefined;
    for (const pending of saveControllers) pending.abort();
    saveControllers.clear(); saving.clear(); drafts.clear(); saveMessages.clear();
    clearInterval(timer); timer = undefined;
    el('key').value = '';
    el('feedback').replaceChildren(); el('chart').replaceChildren(); el('daily-rows').replaceChildren();
    for (const id of ['count-1', 'count-7', 'count-30', 'feedback-total']) el(id).textContent = '—';
    el('asof').textContent = ''; el('chart-start').textContent = ''; el('visible-count').textContent = '0 mesaj';
    el('service-checks').replaceChildren(); el('health-summary').textContent = 'Henüz kontrol edilmedi';
    el('health-summary').className = 'badge'; el('health-updated').textContent = '';
    el('release-version').textContent = '—'; el('release-published').textContent = 'Yayın bilgisi bekleniyor.'; el('release-link').hidden = true;
    for (const state of Object.keys(states)) el('state-'+state).textContent = '—';
    el('results').hidden = true; el('logout').hidden = true; el('login-section').hidden = false;
    el('search').value = ''; el('category').value = 'all'; el('state-filter').value = 'all';
    busy(false); status(message, Boolean(message));
  }
  async function api(path, access, signal, options = {}) {
    const response = await fetch(apiOrigin + '/admin/' + path, {
      method:options.body ? 'POST' : 'GET', body:options.body ? JSON.stringify(options.body) : undefined,
      headers: {Authorization: 'Bearer ' + access,...(options.body ? {'Content-Type':'application/json'} : {})}, cache: 'no-store', credentials: 'omit', redirect: 'error', signal
    });
    if (!response.ok) {
      const error = new Error(response.status === 401 ? 'Yönetim anahtarı geçersiz. Tekrar giriş yap.' : response.status === 429 ? 'Çok sık yenileme yapıldı. Bir dakika sonra tekrar dene.' : 'Veriler yenilenemedi. Bağlantını kontrol edip tekrar dene.');
      error.status = response.status;
      try { error.feedback = (await response.json()).feedback; } catch {}
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
  function renderSystem(data) {
    const checks = Array.isArray(data.checks) ? data.checks : [], list = document.createDocumentFragment();
    const labels = {ok:'Erişilebilir',error:'Sorun var',unknown:'Kontrol bekliyor'};
    for (const check of checks) {
      const row = document.createElement('div'); row.className = 'service-check'; row.setAttribute('role','listitem');
      const description = document.createElement('div'), name = document.createElement('strong'), detail = document.createElement('p');
      name.textContent = check.label; detail.textContent = check.detail; description.append(name,detail);
      const state = Object.hasOwn(labels,check.status) ? check.status : 'unknown';
      const badge = document.createElement('span'); badge.className = 'health-badge '+state; badge.textContent = labels[state];
      row.append(description,badge); list.append(row);
    }
    el('service-checks').replaceChildren(list);
    const good = checks.filter(check => check.status === 'ok').length;
    el('health-summary').textContent = good+'/'+checks.length+' erişim olumlu';
    el('health-summary').className = 'badge '+(checks.length && good === checks.length ? 'ok' : 'warning');
    el('health-updated').textContent = 'Son kontrol: '+dateTime.format(new Date(data.checkedAt));
    el('release-version').textContent = data.release?.version || '—';
    el('release-published').textContent = data.release?.publishedAt ? 'Yayın: '+dateTime.format(new Date(data.release.publishedAt)) : 'Yayın tarihi alınamadı.';
    el('release-link').hidden = !data.release;
    if (data.release && /^\d+\.\d+\.\d+$/.test(data.release.version)) el('release-link').href = 'https://awakepilot.codentum.net/tr/releases.html#v'+data.release.version.replaceAll('.','-');
  }
  function renderFeedback() {
    const active = document.activeElement, focusID = active?.id, selection = typeof active?.selectionStart === 'number' ? [active.selectionStart,active.selectionEnd] : null;
    const query = el('search').value.trim().toLocaleLowerCase('tr-TR'), category = el('category').value, stateFilter = el('state-filter').value;
    const visible = messages.filter(item => (category === 'all' || item.category === category) && (stateFilter === 'all' || (item.status || 'new') === stateFilter) &&
      [item.message, drafts.get(item.id)?.note ?? item.note, item.email, item.version, item.language].join(' ').toLocaleLowerCase('tr-TR').includes(query));
    el('visible-count').textContent = visible.length + ' mesaj';
    const list = document.createDocumentFragment();
    for (const item of visible) {
      const article = document.createElement('article'); article.className = 'feedback-item';
      const head = document.createElement('div'); head.className = 'message-head';
      const badges = document.createElement('div'); badges.className = 'message-badges';
      const topic = document.createElement('span'); topic.className = 'topic '+(Object.hasOwn(topics,item.category) ? item.category : 'general'); topic.textContent = topics[item.category] || topics.general;
      const workState = document.createElement('span'); workState.className = 'work-state '+(item.status || 'new'); workState.textContent = states[item.status] || states.new;
      badges.append(topic,workState);
      const date = document.createElement('time'); date.dateTime = item.created_at; date.textContent = dateTime.format(new Date(item.created_at)); head.append(badges,date);
      const message = document.createElement('pre'); message.className = 'message-text'; message.textContent = item.message;
      const meta = document.createElement('div'); meta.className = 'message-meta';
      const version = document.createElement('span'); version.textContent = item.version ? 'Sürüm '+item.version : 'Sürüm belirtilmemiş';
      const language = document.createElement('span'); language.textContent = 'Dil: '+item.language; meta.append(version,language);
      if (item.email) { const email = document.createElement('a'); email.href = 'mailto:'+encodeURIComponent(item.email); email.textContent = item.email; meta.append(email); }
      const form = document.createElement('form'); form.className = 'management';
      const stateLabel = document.createElement('label'); stateLabel.htmlFor = 'state-'+item.id; stateLabel.textContent = 'İnceleme durumu';
      const choice = document.createElement('select'); choice.id = stateLabel.htmlFor;
      for (const [value,label] of Object.entries(states)) { const option = document.createElement('option'); option.value = value; option.textContent = label; choice.append(option); }
      const draft = drafts.get(item.id); choice.value = draft?.status || item.status || 'new';
      const noteLabel = document.createElement('label'); noteLabel.htmlFor = 'note-'+item.id; noteLabel.textContent = 'Özel yönetim notu';
      const note = document.createElement('textarea'); note.id = noteLabel.htmlFor; note.rows = 3; note.maxLength = 2000; note.placeholder = 'İnceleme notunu yaz…'; note.value = draft?.note ?? item.note ?? '';
      const hint = document.createElement('small'); hint.id = 'hint-'+item.id; hint.textContent = 'Yalnızca yönetim panelinde görünür. En fazla 2.000 karakter.'; note.setAttribute('aria-describedby',hint.id);
      const actions = document.createElement('div'); actions.className = 'management-actions';
      const save = document.createElement('button'); save.id = 'save-'+item.id; save.type = 'submit'; save.className = 'button secondary'; save.textContent = saving.has(item.id) ? 'Kaydediliyor…' : 'Kaydet'; save.disabled = !draft || saving.size > 0;
      const reset = document.createElement('button'); reset.type = 'button'; reset.className = 'button quiet'; reset.textContent = 'Son kaydı kullan'; reset.hidden = !draft; reset.disabled = saving.has(item.id);
      const result = document.createElement('p'); result.id = 'save-status-'+item.id; result.className = 'save-status'; result.setAttribute('role','status');
      result.textContent = saveMessages.get(item.id) || (draft ? 'Kaydedilmemiş değişiklik var.' : item.management_updated_at ? 'Son kayıt: '+dateTime.format(new Date(item.management_updated_at)) : 'Henüz yönetim notu eklenmemiş.');
      const edit = () => {
        const base = drafts.get(item.id) || {revision:item.revision || 0};
        const next = {status:choice.value,note:note.value,revision:base.revision};
        if (next.status === (item.status || 'new') && next.note === (item.note || '') && !saving.has(item.id)) drafts.delete(item.id);
        else drafts.set(item.id,next);
        saveMessages.delete(item.id); save.disabled = !drafts.has(item.id) || saving.size > 0; reset.hidden = !drafts.has(item.id);
        result.textContent = drafts.has(item.id) ? 'Kaydedilmemiş değişiklik var.' : 'Kaydedilmiş kayıt gösteriliyor.';
      };
      choice.addEventListener('change',edit); note.addEventListener('input',edit);
      reset.addEventListener('click',() => { if (!confirm('Kaydedilmemiş değişikliği bırakıp son kaydı kullanmak istiyor musun?')) return; drafts.delete(item.id); saveMessages.delete(item.id); renderFeedback(); });
      form.addEventListener('submit',event => { event.preventDefault(); saveFeedback(item.id); });
      actions.append(save,reset); form.append(stateLabel,choice,noteLabel,note,hint,actions,result); article.append(head,message,meta,form); list.append(article);
    }
    if (!visible.length) {
      const empty = document.createElement('div'); empty.className = 'empty';
      const symbol = document.createElement('div'); symbol.className = 'empty-symbol'; symbol.setAttribute('aria-hidden','true'); symbol.textContent = '↗';
      const title = document.createElement('h3'); title.textContent = messages.length ? 'Bu aramada mesaj bulunamadı' : 'Henüz geri bildirim yok';
      const detail = document.createElement('p'); detail.textContent = messages.length ? 'Aramayı veya filtreleri değiştirerek tekrar dene.' : 'Uygulama veya web sitesindeki formdan gelen mesajlar burada görünecek.';
      empty.append(symbol,title,detail); list.append(empty);
    }
    el('feedback').replaceChildren(list);
    if (focusID && (focusID.startsWith('note-') || focusID.startsWith('state-'))) {
      const field = el(focusID); field?.focus({preventScroll:true}); if (field && selection) field.setSelectionRange(...selection);
    }
  }
  async function saveFeedback(id) {
    const draft = drafts.get(id);
    if (!token || !draft || saving.size) return;
    if (draft.note.length>2000 || draft.note.includes('\0')) { saveMessages.set(id,'Not en fazla 2.000 karakter olmalı ve geçersiz karakter içermemeli.'); renderFeedback(); return; }
    const access = token, session = sessionNumber, snapshot = {...draft}, pending = new AbortController();
    saving.add(id); saveControllers.add(pending); saveMessages.delete(id); renderFeedback();
    try {
      const response = await api('feedback/update',access,pending.signal,{body:{id,...snapshot}});
      if (sessionNumber !== session || token !== access) return;
      // A read started before this write must not restore old management data.
      controller?.abort(); controller = undefined; requestNumber++; busy(false);
      messages = messages.map(item => item.id === id ? {...item,...response.feedback} : item);
      if (response.counts) renderCounts(response.counts);
      const current = drafts.get(id);
      if (current && current.status === snapshot.status && current.note === snapshot.note) drafts.delete(id);
      else if (current) drafts.set(id,{...current,revision:response.feedback.revision});
      saveMessages.set(id,drafts.has(id) ? 'Kayıt alındı; sonraki değişikliklerin henüz kaydedilmedi.' : 'Kaydedildi.');
    } catch (error) {
      if (sessionNumber !== session || token !== access || error.name === 'AbortError') return;
      if (error.status === 401) { lock(error.message); el('key').focus(); return; }
      if (error.status === 409 && error.feedback) {
        controller?.abort(); controller = undefined; requestNumber++; busy(false);
        messages = messages.map(item => item.id === id ? {...item,...error.feedback} : item);
        saveMessages.set(id,'Başka bir yerde güncellenmiş. Taslağın korunuyor; son kaydı kullanıp yeniden düzenle.');
      } else saveMessages.set(id,error.status === 404 ? 'Mesaj artık kayıtlı değil. Taslağın korunuyor.' : 'Kaydedilemedi. Taslağın korunuyor; tekrar deneyebilirsin.');
    } finally {
      if (sessionNumber === session) { saving.delete(id); saveControllers.delete(pending); renderFeedback(); }
    }
  }
  function renderCounts(counts) {
    el('feedback-total').textContent = integer(counts.total).toLocaleString('tr-TR');
    for (const state of Object.keys(states)) el('state-'+state).textContent = integer(counts[state]).toLocaleString('tr-TR');
  }
  async function refresh() {
    if (!token || loading) return;
    const access = token, number = ++requestNumber;
    controller = new AbortController(); const currentController = controller;
    busy(true); status('Veriler yükleniyor…');
    try {
      const results = await Promise.allSettled(['summary','feedback','system'].map(path => api(path,access,currentController.signal)));
      if (token !== access || requestNumber !== number) return;
      const unauthorized = results.find(result => result.status === 'rejected' && result.reason.status === 401);
      if (unauthorized) { lock(unauthorized.reason.message); el('key').focus(); return; }
      if (results.every(result => result.status === 'rejected')) throw results[0].reason;
      const [summary,inbox,system] = results;
      if (summary.status === 'fulfilled') {
        const data = summary.value;
        for (const days of [1,7,30]) el('count-'+days).textContent = integer(data.activeInstallations[days]).toLocaleString('tr-TR');
        renderCounts(data.feedback || {});
        renderTrend(data.dailyInstallations); el('asof').textContent = 'Son güncelleme: '+dateTime.format(new Date(data.asOf))+' · Türkiye saati';
      }
      if (inbox.status === 'fulfilled') { messages = inbox.value.feedback; renderFeedback(); }
      if (system.status === 'fulfilled') renderSystem(system.value);
      else { el('health-summary').textContent = 'Kontrol yenilenemedi'; el('health-summary').className = 'badge warning'; }
      el('login-section').hidden = true; el('results').hidden = false; el('logout').hidden = false;
      if (!timer) timer = setInterval(() => { if (document.visibilityState === 'visible') refresh(); },60000);
      status(results.some(result => result.status === 'rejected') ? 'Bazı bilgiler alınamadı. Son başarılı veriler korunuyor.' : '',results.some(result => result.status === 'rejected'));
    } catch (error) {
      if (token !== access || requestNumber !== number || error.name === 'AbortError') return;
      currentController.abort();
      status(error.status ? error.message : el('results').hidden ? 'Veriler alınamadı. Bağlantını kontrol edip tekrar dene.' : 'Veriler yenilenemedi. Son başarılı kontrolün bilgileri gösteriliyor.',true);
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
  el('state-filter').addEventListener('change', renderFeedback);
  window.addEventListener('pagehide', () => lock());
  el('key').disabled = false; el('login-button').disabled = false;
})();
