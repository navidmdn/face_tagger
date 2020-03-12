from src.application.pending_face_handler import PendingFaceHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from src.telegram_api import config as bot_config
from src.telegram_api.app import messages
from src.telegram_api.app import state
from src.util.image import generate_file_name, load_from_path
import random

sessions = {}
pending_fh = PendingFaceHandler()


def admin_msg(bot, update):
    try:
        if update.effective_user.id not in bot_config.ADMIN_IDS:
            return
        print('admin @{} sent a message'.format(update.effective_user.username))
        if update.effective_user.username in sessions and \
                sessions[update.effective_user.username].status == state.WAITING_IMG:
            if update.message.photo:
                file = bot.getFile(update.message.photo[-1].file_id)
                dl_path = '{}/{}'.format(bot_config.DOWNLOAD_PATH, generate_file_name())
                file.download(dl_path)
                added = pending_fh.add_image(load_from_path(dl_path))
                if added == -1:
                    update.message.reply_text('no new faces detected!')
                else:
                    update.message.reply_text('new faces detected!')

    except Exception as e:
        print("FAILED")
        #todo
        pass


def add_img(bot, update):
    print('api addimg called by {}'.format(update.effective_user.username))
    try:
        if update.effective_user.id not in bot_config.ADMIN_IDS:
            return
        sessions[update.effective_user.username] = state.State('admin', status=state.WAITING_IMG)
        update.message.reply_text('Im ready boss!')
    except Exception as e:
        #TODO
        pass


def reset(bot, update):
    print('api reset called by {}'.format(update.effective_user.username))
    try:
        if update.effective_user.id not in bot_config.ADMIN_IDS:
            return
        sessions[update.effective_user.username] = state.State('admin', status=state.NORMAL_STATE)
        update.message.reply_text('Everything back to normal!')
    except Exception as e:
        #TODO
        pass
    pass


#
# def start(bot, update):
#     logger.info("Start API called by {}".format(update.effective_user.username))
#     try:
#         if update.effective_user.username not in bot_config.ALLOWED_USERNAMES:
#             update.message.reply_text(
#                 messages.fuck_off_not_allowed.
#                     format(update.effective_user.first_name))
#             return
#         result = fapper.register(update.effective_user, update.effective_chat.id)
#         if result is api_code.SUCCESS:
#             update.message.reply_text(
#                 messages.welcome_to_the_club.
#                     format(update.effective_user.first_name))
#         elif result is api_code.USER_ALREADY_EXISTS:
#             update.message.reply_text(messages.already_joined)
#     except Exception as e:
#         update.message.reply_text(messages.server_fault)
#         logger.info("exception in start: {}".format(e))
#
#
# def daily(bot, update):
#     logger.info("daily summary called by {}".format(update.effective_user.username))
#     try:
#         if update.effective_user.id not in bot_config.ADMIN_IDS:
#             return
#         users = fapper.get_allowed_users()
#         summary = fap.daily_summary(users)
#         for user in users:
#             logger.info('sending daily summary to {}'.format(user['username']))
#             bot.send_message(user['chat_id'], summary)
#     except Exception as e:
#         logger.info("Daily summary failed because {}".format(e))
#
#
# def weekly(bot, update):
#     logger.info("weekly summary called by {}".format(update.effective_user.username))
#     try:
#         if update.effective_user.id not in bot_config.ADMIN_IDS:
#             return
#         users = fapper.get_allowed_users()
#         summary, im_path = fap.weekly_summary(users)
#         for user in users:
#             logger.info('sending weekly summary to {}'.format(user['username']))
#             bot.send_photo(user['chat_id'], open(im_path, 'rb'), caption=summary)
#     except Exception as e:
#         logger.info("Weekly summary failed because {}".format(e))
#
#
# def fap_statistics_request(bot, chat_id):
#     qid = random.randint(1, 100000000)
#     key = chat_config.CALLBACK_QUERY_KEY_FAP_STATISTICS
#     bot.send_message(
#         chat_id=chat_id,
#         text=messages.how_many_faps,
#         reply_markup=InlineKeyboardMarkup([[
#             InlineKeyboardButton("1", callback_data='{};{};{};{}'.format(key, qid, chat_id, 1)),
#             InlineKeyboardButton("2", callback_data='{};{};{};{}'.format(key, qid, chat_id, 2)),
#             InlineKeyboardButton("3", callback_data='{};{};{};{}'.format(key, qid, chat_id, 3)),
#         ], [
#             InlineKeyboardButton("4", callback_data='{};{};{};{}'.format(key, qid, chat_id, 4)),
#             InlineKeyboardButton("5", callback_data='{};{};{};{}'.format(key, qid, chat_id, 5)),
#             InlineKeyboardButton("0", callback_data='{};{};{};{}'.format(key, qid, chat_id, 0)),
#         ]]))
#
#
# def forward(bot, update):
#     api_state.change_status(state.WAIT_FOR_FORWARD)
#
#
# def _broadcast(bot, msg):
#     for username in bot_config.ALLOWED_USERNAMES:
#         user = fapper.get_user_by_username(username)
#         if user is not None:
#             bot.send_message(chat_id=user['chat_id'], text=msg)
#     logger.info("message broadcasted msg={}".format(msg))
#
#
# def collect_fap_statistics(bot, update):
#     try:
#         _, qid, chat_id, cnt = update['callback_query']['data'].split(';')
#         cnt, qid = int(cnt), int(qid)
#         fap.submit_fap_count(qid, update.effective_user.id, cnt)
#         bot.send_message(chat_id=chat_id, text=fap.fap_motivation_based_on_fapp_count(cnt))
#         bot.answer_callback_query(update.callback_query.id)
#         log_text = "{} answered with {}.".format(update.effective_user.first_name, cnt)
#         bot.send_message(bot_config.ADMIN_IDS[0], text=log_text)
#         logger.info(log_text)
#     except Exception as e:
#         logger.info("error in collect_fap_statistics: {}".format(e))
#
#