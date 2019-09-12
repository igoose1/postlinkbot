# Simple Telegram bot to get link of post or message

Telegram makes possible to use share links to show message from public channel or chat.
What Telegram did bad is its clients (e.g. official Telegram for Android) don't have this
function.

This simple bot written in Python was created with the function to overcome the lack.
It requires Python3.7 (sorry for using f'' but it's awesome) and python-telegram-bot
library. It has less than 60 lines (still a lot) of clear Python code and I hope
it will remain so.

## Launching

Be sure you have `python3.7` and python-telegram-bot (v. 12)

```
python -m pip install requirements.txt
```

Clone, go to repo and run bot with Telegram Bot token (can be given by
https://t.meBotFather).

```
python main.py TOKEN
```

To not keep token in mind I'm saving it in `token` file and run bot by nesting command.

```
python main.py $(cat token)
```

