# Ip Rotator
### What is it
around 2018-19 when i was in urgent need of a static ip. my isp constantly denied its possibility. I had an idea. that i tried to implement here.

This small scripts works by client constantly sending a request to server. to verify its real source it sends a password alongside. <br>
on verification the server proceeds to change `A` record for a domain to the ip of the client <br>
this way eg. `server.surajbhari.info` always point to correct ip.

### how to use it 
host the server part on your server. change the secret to something secret. for name.com credentials you can find them [here](https://www.name.com/account/settings/api) <br>

for client you can add a cronjob or something like task scheduler for windows.