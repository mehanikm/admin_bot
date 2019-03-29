from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from smiles import smiles
import json


def make_kb(text_1, text_2, text_3):
    button_1 = InlineKeyboardButton(text_1, callback_data=smiles["xd"])
    button_2 = InlineKeyboardButton(
        text_2, callback_data=smiles["drunk"])
    button_3 = InlineKeyboardButton(
        text_3, callback_data="Lol you gay")
    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.add(button_1, button_2, button_3)
    return keyboard


def count_reacts(message_id, reaction):
    message_id = str(message_id)
    c = 0
    for value in messages[message_id].values():
        if value == reaction:
            c += 1
    return c


# Collect reactions
with open("reacts.json") as f:
    messages = dict(json.load(f))


def add_to_set(user, curr_mess, reaction):
    curr_mess = str(curr_mess)
    user = str(user)
    if curr_mess in messages:
        messages[curr_mess][user] = reaction
    else:
        messages[curr_mess] = {user: reaction}
    with open("reacts.json", "w") as f:
        json.dump(messages, f)
