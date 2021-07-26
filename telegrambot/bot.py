#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.
import logging
import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    CallbackContext,
    Filters
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
BEGIN, END, CONTINUE = range(3)

def build_keyboard(current_list: List[int]) -> InlineKeyboardMarkup:
    f = open('../intents.json',)
    data = json.load(f)
    options = [] 
    for option in data['menu']:
       options.append(InlineKeyboardButton(option['key'], callback_data=option))
    f.close()
    """Helper function to build the next inline keyboard."""
    return InlineKeyboardMarkup.from_column(
        [InlineKeyboardButton(str(i), callback_data=(i, current_list)) for i in range(1, 6)]
    )

def start(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    update.message.reply_text("Hey " + user.first_name + " how can i help you? ")

    return BEGIN

def begin(update: Update, context: CallbackContext) -> int:
    # send update.message.text to nlp - > nlp return id
    # return id
    print(update.message.text)

    return CONTINUE

def continue_conv(update: Update, context: CallbackContext) -> int:
    output = " Question "
    update.message.reply_text(output)
#     if not leaf bulid inline key by children tags
#     if redirect return redirect 
#     if array of answers random them
    if(update.message.text == 1) :
        return CONTINUE
    else:
        return END

def end(update: Update, context: CallbackContext) -> int:
    # print output
    print("finish")
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    TOKEN = "1901796693:AAGnJ7Fa81M4wfuUWxeh7dieUA3VizRvm-g"
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            BEGIN: [
                MessageHandler(Filters.text & ~Filters.command, begin)
            ],
            END: [
                MessageHandler(Filters.text & ~Filters.command, end)
            ],
            CONTINUE: [
                MessageHandler(Filters.text & ~Filters.command, continue_conv)
            ]
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()