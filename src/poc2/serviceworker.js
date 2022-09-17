'use strict';

var requested = Set()

self.addEventListener('install', function() {
    self.skipWaiting();
});

self.addEventListener('fetch', function(e) {
  let url = new URL(e.request.url);
  let urlParams = new URLSearchParams(url.search);
  let size = urlParams.get('size');
  let id = urlParams.get('id');
  let body = 'A'.repeat(Number(size));
  if (!requested.has(id)) {
    console.log('intercepted');
  	e.respondWith(new Response(body, {status: 206, headers: {'Content-Range': `bytes 0-${size - 1}/100000` }}));
  }
});
