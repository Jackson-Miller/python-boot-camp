import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


def get_word():
    """ Gets a random word from the word list and updates the card to show the details"""
    global timer, word_data
    window.after_cancel(timer)
    word_data = random.choice(word_list)

    canvas.itemconfig(card_bg, image=fcard_img)
    canvas.itemconfig(title_text, text="Spanish", fill="black")
    canvas.itemconfig(word_text, text=word_data["Spanish"], fill="black")
    timer = window.after(3000, show_translation, word_data["English"])


def show_translation(word):
    """ Flip the flashcard over and show the word in English """
    canvas.itemconfig(card_bg, image=bcard_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word, fill="white")


def knows_word():
    """ Remove the word from the word list """
    word_list.remove(word_data)
    data_frame = pandas.DataFrame(word_list)
    data_frame.to_csv("./data/words_to_learn.csv", index=False)
    get_word()


# Import language data
try:
    practice_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    csv_data = pandas.read_csv("./data/spanish_words.csv")
    word_list = csv_data.to_dict(orient="records")
else:
    word_list = practice_data.to_dict(orient="records")

word_data = {}

# UI Setup
window = Tk()
window.title("Spanish Flashcards")
fcard_img = PhotoImage(file="./images/card_front.png")
bcard_img = PhotoImage(file="./images/card_back.png")
green_button = PhotoImage(file="./images/right.png")
red_button = PhotoImage(file="./images/wrong.png")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.resizable(False, False)

# Flashcard
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_bg = canvas.create_image(400, 263, image=fcard_img)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = Button(image=red_button, relief="flat", highlightthickness=0, bd=0, command=get_word)
wrong_button.grid(row=1, column=0)
right_button = Button(image=green_button, relief="flat", highlightthickness=0, bd=0, command=knows_word)
right_button.grid(row=1, column=1)


# Start the game
timer = window.after(100, get_word)

window.mainloop()
