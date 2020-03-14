from telegram.ext import Updater, CommandHandler,\
    PrefixHandler, CallbackQueryHandler, MessageHandler
from src.telegram_api import config as bot_config
from src.telegram_api.app import api
from telegram.ext.filters import Filters


def run():
    print("running bot API.")
    updater = Updater(bot_config.ACCESS_TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', api.start))

    updater.dispatcher.add_handler(PrefixHandler('#', 'addimg', api.add_img))
    updater.dispatcher.add_handler(PrefixHandler('#', 'reset', api.reset))
    updater.dispatcher.add_handler(PrefixHandler('#', 'detect', api.detect))
    updater.dispatcher.add_handler(PrefixHandler('#', 'poke', api.ping))
    updater.dispatcher.add_handler(PrefixHandler('#', 'contrib', api.contribute))

    updater.dispatcher.add_handler(MessageHandler(Filters.photo, api.photo_msg))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, api.text_msg))
    #
    #
    # updater.dispatcher.add_handler(CallbackQueryHandler(api.collect_fap_statistics, pattern="{};[0-9]+;[0-9]+;[0-9]+".
    #                                                     format(chat_config.CALLBACK_QUERY_KEY_FAP_STATISTICS)))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    run()
