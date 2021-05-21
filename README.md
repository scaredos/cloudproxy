# CloudProxy
A simple tool to use CloudFlare as a HTTP(S) web proxy

## Update
- With this new addition, the script for the cloudflare worker, you can fetch webpages while leaving your ip address hidden. 

## About CloudProxy
- CloudProxy is designed to use CloudFlare as a proxy to deliver requests to hosts that you are testing. It can be used to test hosts with DoS, bypass CloudFlare WAF, hosts that only allow traffic from CloudFlare, and many other things.
- To use CloudProxy, you need an active domain on CloudFlare. You also need the origin IP of a website on/off CloudFlare 
- This will not work in the target website has CloudFlare and you do not have the origin IP


![](cloudproxy_showcase.gif)
