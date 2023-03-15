// service-worker.js should be at the root of the project unlike other js files
importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.0.2/workbox-sw.js');
workbox.routing.registerRoute(
    ({request}) => true,
    new workbox.strategies.NetworkFirst()
)