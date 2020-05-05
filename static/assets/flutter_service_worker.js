'use strict';
const CACHE_NAME = 'flutter-app-cache';
const RESOURCES = {
  "assets/AssetManifest.json": "0cdffc2591abc0312fa0cb5af5ac178b",
"assets/assets/logo.png": "d4c939b7c1660129361d58230c82cf1c",
"assets/assets/rgpv_logo.png": "e221b3dd29cf2e2a0f255c6f467e9175",
"assets/assets/user.png": "54e9ec5365eeb967838ffd2a35eda50b",
"assets/FontManifest.json": "01700ba55b08a6141f33e168c4a6c22f",
"assets/fonts/MaterialIcons-Regular.ttf": "56d3ffdef7a25659eab6a68a3fbfaf16",
"assets/LICENSE": "5c5648ba8b227099a969149b1fdd90d8",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "115e937bb829a890521f72d2e664b632",
"favicon.png": "5dcef449791fa27946b3d35ad8803796",
"icons/Icon-192.png": "863c4bf673acc4ab8348409b2624bb51",
"icons/Icon-512.png": "6c8a19b69e2bb463934b6de2ba2d1a5d",
"index.html": "4ec4852b33dfd93dfed89d0bbc45c103",
"/": "4ec4852b33dfd93dfed89d0bbc45c103",
"main.dart.js": "aade71aab13718041e38d08545837a26",
"manifest.json": "97492ecbfc14905e3e5525773a30b79f",
"_redirects": "76c5cf5c09b14e38758ea51ea16d7503"
};

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (cacheName) {
      return caches.delete(cacheName);
    }).then(function (_) {
      return caches.open(CACHE_NAME);
    }).then(function (cache) {
      return cache.addAll(Object.keys(RESOURCES));
    })
  );
});

self.addEventListener('fetch', function (event) {
  event.respondWith(
    caches.match(event.request)
      .then(function (response) {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});
