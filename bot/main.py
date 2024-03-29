#
# Copyright 2019 Oskar Sharipov
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from telegram.ext import *
import sys
import logging


class MessageProcess:
    def start(self, update, context):
        answer = (
            'o/\n\n'
            'Forward post of public channel to get its link!\n\n'
            'This bot is developed with the problem that some Telegram clients '
            'make getting post link impossible. '
            'Source code is hosted here: https://github.com/igoose1/postlinkbot'
        )
        context.bot.send_message(
            chat_id=update.message.chat_id,
            text=answer
        )

    def post(self, update, context):
        message = update.message
        mid, chat = message.forward_from_message_id, message.forward_from_chat
        if mid is chat is None:
            answer = 'Forwarded message is not from public channel.'
        else:
            answer = f'https://t.me/{chat.username}/{mid}'

        context.bot.send_message(
            chat_id=update.message.chat_id,
            text=answer
        )


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

mp = MessageProcess()

if len(sys.argv) != 2:
    logging.error('Could not parse token.')
    logging.info('Set token as argument: python main.py TOKEN.')
    sys.exit(1)
token = sys.argv[1]
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

handlers = (
    CommandHandler(
        'start',
        mp.start
    ),
    MessageHandler(
        Filters.forwarded,
        mp.post
    )
)

for h in handlers:
    dispatcher.add_handler(h)

updater.start_polling()
logging.info('Bot started working.')
