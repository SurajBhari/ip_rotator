# IP Rotator

![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![Dynamic DNS](https://img.shields.io/badge/Dynamic-DNS-0A66C2?style=flat&logo=cloudflare&logoColor=white)
![name.com](https://img.shields.io/badge/name.com-API-003366?style=flat)

A **poor-man's dynamic DNS** — keep a domain pointed at a machine that has no static IP.

## The story

Around 2018–19 I urgently needed a static IP, but my ISP refused to provide one. So I built this: the client (the machine with the changing IP) periodically calls a small server, proving its identity with a shared secret. On each verified call, the server updates the **`A` record** for a domain to the client's current IP — so e.g. `server.surajbhari.info` always resolves to the right machine, no matter how often the IP changes.

## Two implementations

| Folder | Approach |
|--------|----------|
| `with_server/` | A long-running **server** (`server/server.py`) that you host somewhere stable; the **client** (`client/client.py`) checks in on a schedule. The server updates DNS via the [name.com API](https://www.name.com/account/settings/api). |
| `serverless/` | A **serverless** variant (`serverless/main.py`) so you don't need to keep a box running just to receive check-ins. |

## How to use

1. **Server side** — deploy the server part (or the serverless function). Set a strong shared `secret`, and add your [name.com API credentials](https://www.name.com/account/settings/api).
2. **Client side** — run the client on the machine with the changing IP, on a schedule (cron on Linux, Task Scheduler on Windows), so it keeps the DNS record current.

```bash
pip install -r requirements.txt
```
