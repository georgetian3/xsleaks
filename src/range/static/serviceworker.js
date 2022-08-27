'use strict';

self.addEventListener('install', function() {
    self.skipWaiting();
});

self.addEventListener('fetch', function(e) {
  let url = new URL(e.request.url);
  let urlParams = new URLSearchParams(url.search);
  let size = Number(urlParams.get('size'));
  let body = 'A'.repeat(size);
  if (e.request.headers.get('range') === 'bytes=0-') {
  	e.respondWith(new Response(
      body,
      {
        status: 206,
        headers: {'Content-Range': 'bytes 0-1337/13370'}
      }
    ));
  }
});
