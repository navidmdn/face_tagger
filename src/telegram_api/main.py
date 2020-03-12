from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler
from src.telegram_api import config as bot_config
from src.telegram_api.app import api


def run():
    print("running bot API.")
    updater = Updater(bot_config.ACCESS_TOKEN)

    updater.dispatcher.add_handler(CommandHandler('addimg', api.add_img))
    updater.dispatcher.add_handler(CommandHandler('reset', api.reset))
    updater.dispatcher.add_handler(MessageHandler(None, api.admin_msg))
    # updater.dispatcher.add_handler(CommandHandler('start', api.start))
    # updater.dispatcher.add_handler(CommandHandler('daily', api.daily))
    # updater.dispatcher.add_handler(CommandHandler('weekly', api.weekly))
    #
    #
    # updater.dispatcher.add_handler(CallbackQueryHandler(api.collect_fap_statistics, pattern="{};[0-9]+;[0-9]+;[0-9]+".
    #                                                     format(chat_config.CALLBACK_QUERY_KEY_FAP_STATISTICS)))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    run()
