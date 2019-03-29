import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
import funcs
from smiles import smiles

# Initialize bot
bot = telebot.TeleBot(config.token)

# Add reaction inline markup keyboard
keyboard = funcs.make_kb(
    smiles["xd"]+"0", smiles["drunk"]+"0", smiles["gays"]+"0")

# Post simple text messages to channel with keyboard
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(config.channel, message.text, reply_markup=keyboard)

# Repost photos to channel with kb
@bot.message_handler(content_types=["photo"])
def respond_to_photo(message):
    bot.send_photo(
        config.channel, message.photo[-1].file_id, message.caption, reply_markup=keyboard)

# Show callback after pressing inline kb button
@bot.callback_query_handler(func=lambda call: True)
def answer_query(call):
    bot.answer_callback_query(call.id, text=call.data)

    # Write users reaction to reactions set
    funcs.read_chat_reacts(call.message.chat.id)
    funcs.add_to_set(call.message.chat.id, call.from_user.id,
                     call.message.message_id, call.data)

    # Recount every button's counter and create new kb
    first_line = keyboard.keyboard[0]
    new_but_1 = first_line[0]["text"][:-1] + str(funcs.count_reacts(call.message.message_id,
                                                                    first_line[0]["callback_data"]))
    new_but_2 = first_line[1]["text"][:-1] + str(funcs.count_reacts(call.message.message_id,
                                                                    first_line[1]["callback_data"]))
    new_but_3 = first_line[2]["text"][:-1] + str(funcs.count_reacts(call.message.message_id,
                                                                    first_line[2]["callback_data"]))
    new_kb = funcs.make_kb(new_but_1, new_but_2, new_but_3)
    # Replace kb with new one
    try:
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id, reply_markup=new_kb)
    except:
        print(
            f"Failed to update keyboard(message {call.message.message_id})")


# If name == main ...
if __name__ == "__main__":
    bot.polling(none_stop=True)
