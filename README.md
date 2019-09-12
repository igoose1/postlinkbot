# Simple Telegram bot to get link of post or message

Telegram makes possible to share links to redirect to the message from public channel.
What Telegram did bad is some its clients (e.g. official Telegram for Android) don't have
this function.

This simple bot written in Python was created with the function to overcome the lack. It
requires Python3.7 (sorry for using `f'{foo}'` but it's awesome) and python-telegram-bot
library. It has less than 60 lines (still a lot) of clear Python code and I hope it will
remain so.

Bot answers on /start command and on any forwarded message. If forwarded message can be
used to generate the link bot would answer with that link.

## Launching

Be sure you have `python3.7` and `python-telegram-bot` (v. 12)

```
python -m pip install requirements.txt
```

Clone, go to repo and run bot with Telegram Bot token (can be given by
https://t.me/BotFather).

```
python bot/main.py TOKEN
```

To not keep token in mind I'm saving it in `token` file and run bot by nesting command.

```
python bot/main.py $(cat token)
```

