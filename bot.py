import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update, _):
    keyboard = (
        [
            InlineKeyboardButton("About my 👨‍💻", callback_data='Python june developer, had start in 2019'),
            InlineKeyboardButton("Why this bot? 🤖", callback_data='I wrote this bot for a test job'),
        ],
        [InlineKeyboardButton("Telegram 🛂", callback_data='https://t.me/maureryakov'),
         InlineKeyboardButton("Facebook 👤", callback_data='http://m.me/maureryakov'),
         InlineKeyboardButton("GitHub💻", callback_data='https://github.com/maureryakov')],

        [InlineKeyboardButton('Feedback📨', callback_data="mailto:maureryakov@iCloud.com")],
    )

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Hi 👋 I am a bot secretary 🤖 '
                              'for communication use the buttons👇Press to return 👉 /start', reply_markup=reply_markup)


def button(update, _):
    query = update.callback_query
    variant = query.data

    # `CallbackQueries` требует ответа, даже если
    # уведомление для пользователя не требуется, в противном
    #  случае у некоторых клиентов могут возникнуть проблемы.
    # смотри https://core.telegram.org/bots/api#callbackquery.
    query.answer()
    # редактируем сообщение, тем самым кнопки
    # в чате заменятся на этот ответ.
    query.edit_message_text(text=f"👉: {variant}")


def help_command(update, _):
    update.message.reply_text("Используйте `/start` для тестирования.")


if __name__ == '__main__':
    # Передайте токен вашего бота.
    updater = Updater("YYYYYYYYYYYYYYYYYYYY")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Запуск бота
    updater.start_polling()
    updater.idle()
