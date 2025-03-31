# 🍪 Cookie Clicker Bot

This is an automated bot that plays [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/) using Selenium.

Every few milliseconds, the bot:
- Clicks the cookie furiously
- Every 4 seconds, checks for the most expensive buyable upgrade
- Buys the best one
- After 5 minutes, it prints your cookies-per-second (CPS)

## Requirements

- Python 3.10+
- Google Chrome
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed and on PATH
- Selenium (`pip install selenium`)

## How to Clone
```bash
git clone https://github.com/ajs2583/cookie-clicker-bot.git
cd cookie-clicker-bot
```

## How to Run

```bash
python bot.py
