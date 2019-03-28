import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from smiles import smiles

# Initialize bot
bot = telebot.TeleBot(config.token)

# Add reaction inline markup keyboard and 3 buttons
button_1 = InlineKeyboardButton(smiles["xd"], callback_data=smiles["xd"])
button_2 = InlineKeyboardButton(smiles["drunk"], callback_data=smiles["drunk"])
button_3 = InlineKeyboardButton(smiles["gays"], callback_data="Lol you gay")
keyboard = InlineKeyboardMarkup(row_width=3)
keyboard.add(button_1, button_2, button_3)

# Post simple text messages to channel with keyboard
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(config.channel, message.text, reply_markup=keyboard)


@bot.message_handler(content_types=["photo"])
def respond_to_photo(message):
    bot.send_photo(
        config.channel, message.photo[0].file_id, message.caption, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def answer_query(call):
    bot.answer_callback_query(call.id, text=call.data)


if __name__ == "__main__":
    bot.polling(none_stop=True)
