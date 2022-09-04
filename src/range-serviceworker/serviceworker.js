'use strict';

self.addEventListener("install", function() {
    self.skipWaiting();
});

self.addEventListener("fetch", function(e) {
  let url = new URL(e.request.url);
  console.log(url);
  if (e.request.headers.get("range") === "bytes=0-") {
    console.log('if');
    let urlParams = new URLSearchParams(url.search);
    e.respondWith(
      new Response(
        "A".repeat(Number(urlParams.get("size"))), 
        {status: 206, headers: {"Content-Range": "bytes 0-1337/13370" }}
      )
    );
  } else {
    console.log('else');
  }
});
