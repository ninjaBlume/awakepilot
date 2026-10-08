(() => {
  'use strict';
  const form = document.getElementById('feedback-form');
  if (!form) return;
  const status = document.getElementById('feedback-status');
  const button = document.getElementById('feedback-send');
  let token = '', widget, id, snapshot = '', sending = false;
  const version = new URLSearchParams(window.location.search).get('version') || '';
  if (/^\d+\.\d+(\.\d+)?$/.test(version) && version.length <= 30) form.elements.version.value = version;
  const show = (message, error = false) => { status.textContent = message; status.classList.toggle('form-error',error); };
  window.awakepilotSecurityReady = () => {
    widget = window.turnstile.render('#security-check', {
      sitekey: form.dataset.sitekey, action:'feedback',size:'compact',
      language: document.documentElement.lang === 'az' ? 'en' : document.documentElement.lang.toLowerCase(),
      callback: value => {token=value;},
      'expired-callback': () => {token='';},
      'error-callback': () => { token='';show(form.dataset.challengeError,true); }
    });
  };
  const script = document.createElement('script');
  script.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?onload=awakepilotSecurityReady&render=explicit';
  script.async = true; script.onerror = () => show(form.dataset.challengeError,true);
  document.head.append(script);
  form.addEventListener('submit',async event => {
    event.preventDefault();
    if (sending || !form.reportValidity()) return;
    const fields={category:form.elements.category.value,message:form.elements.message.value.trim(),email:form.elements.email.value.trim(),version:form.elements.version.value,language:document.documentElement.lang,website:form.elements.website.value};
    if (fields.message.length < 10) {show(document.getElementById('message-hint').textContent,true);form.elements.message.focus();return;}
    const nextSnapshot=JSON.stringify(fields);
    if (nextSnapshot !== snapshot) { snapshot=nextSnapshot;id=crypto.randomUUID(); }
    if (!token) {show(form.dataset.challengeError,true);return;}
    sending=true;button.disabled=true;button.textContent=form.dataset.sending;show(form.dataset.sending);
    // Keep the submitted draft stable during the request and preserve it on any failure.
    const inputs=[...form.querySelectorAll('input,textarea,select')]; inputs.forEach(input=>input.disabled=true);
    try {
      const response=await fetch(form.dataset.endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({...fields,id,token}),signal:AbortSignal.timeout(20000)});
      const result=await response.json();
      if (!response.ok || result.ok !== true || result.id !== id) {
        const error=new Error(response.status===400 && result.error==='challenge'?form.dataset.challengeError:form.dataset.error);throw error;
      }
      form.reset();snapshot='';show(form.dataset.success+' '+form.dataset.reference+': '+result.id);status.focus();
    } catch(error) {
      show(error.message===form.dataset.challengeError?form.dataset.challengeError:form.dataset.error,true);
    } finally {
      sending=false;button.disabled=false;button.textContent=form.dataset.send;inputs.forEach(input=>input.disabled=false);
      token='';if(window.turnstile && widget !== undefined)window.turnstile.reset(widget);
    }
  });
})();
