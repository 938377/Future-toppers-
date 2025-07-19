(function() {
  const TRUSTED = "lksfy.com";
  const KEY = "verified_until";
  const HOURS = 24;

  const now = Date.now();
  const expiry = localStorage.getItem(KEY);

  if (expiry && parseInt(expiry) > now) {
    // Already verified
    return;
  }

  const ref = document.referrer;
  if (ref.includes(TRUSTED)) {
    localStorage.setItem(KEY, (now + HOURS * 60 * 60 * 1000).toString());
    return;
  }

  // Not verified, redirect to shortlink
  window.location.href = "https://lksfy.com/p861S";
})();
