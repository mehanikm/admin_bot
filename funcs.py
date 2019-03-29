from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from smiles import smiles
import json
import config


# Create keyboard
def make_kb(text_1, text_2, text_3):
    button_1 = InlineKeyboardButton(text_1, callback_data=smiles["xd"])
    button_2 = InlineKeyboardButton(
        text_2, callback_data=smiles["drunk"])
    button_3 = InlineKeyboardButton(
        text_3, callback_data="Lol you gay")
    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.add(button_1, button_2, button_3)
    return keyboard


# Count all reactions for certain message
def count_reacts(message_id, reaction):
    message_id = str(message_id)
    c = 0
    for value in messages[message_id].values():
        if value == reaction:
            c += 1
    return c


# Collect reactions
def read_chat_reacts(chat):
    global messages
    try:
        with open(f"reacts_{config.chats[chat]}.json") as f:
            messages = dict(json.load(f))
    except FileNotFoundError:
        messages = dict()


# Add reactions to set
def add_to_set(chat, user, curr_mess, reaction):
    curr_mess = str(curr_mess)
    user = str(user)
    if curr_mess in messages:
        messages[curr_mess][user] = reaction
    else:
        messages[curr_mess] = {user: reaction}
    with open(f"reacts_{config.chats[chat]}.json", "w") as f:
        json.dump(messages, f)
