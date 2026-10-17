/* Show only the price selected from the visitor connection's country. */
(() => {
  'use strict';
  const card = document.querySelector('[data-location-price]');
  if (!card) return;
  const amount = card.querySelector('[data-price-amount]');
  const unit = card.querySelector('[data-price-unit]');
  const status = card.querySelector('[data-price-status]');
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 8000);
  status.textContent = card.dataset.loading;
  fetch('https://api-awakepilot.codentum.net/v1/price', {
    cache: 'no-store', credentials: 'omit', signal: controller.signal
  }).then(async response => {
    if (!response.ok) throw new Error('Price unavailable');
    const price = await response.json();
    if (!/^[A-Z]{2}$/.test(price.country) || price.country === 'XX' ||
        !['USD', 'TRY'].includes(price.currency) || !Number.isSafeInteger(price.amount) ||
        price.amount <= 0 || typeof price.formatted !== 'string' || price.formatted.length > 24) {
      throw new Error('Invalid price');
    }
    amount.textContent = price.formatted;
    amount.hidden = unit.hidden = false;
    status.hidden = true;
  }).catch(() => {
    amount.textContent = '';
    amount.hidden = unit.hidden = true;
    status.textContent = card.dataset.error;
    status.hidden = false;
  }).finally(() => {
    clearTimeout(timeout);
    card.setAttribute('aria-busy', 'false');
  });
})();
