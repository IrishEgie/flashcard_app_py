from tkinter import *
from tkinter import messagebox
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ---------------------------- CSV FETCH ------------------------------- #
try:
# Load the CSV data into a DataFrame
    df = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    og_df = pd.read_csv('./data/french_words.csv')
    to_learn = og_df.to_dict(orient='records')
else:
    # Fetch both "French" and "English" columns
    to_learn = df.to_dict(orient='records')


def update_word():
    global current_card, flip_timer
    # Cancel any existing timer to flip card
    window.after_cancel(flip_timer)
    
    # Get a random French word and update current card
    current_card = rd.choice(to_learn)
    
    # Update the canvas text with the French word
    canvas_card.itemconfig(card_txt_lang, text="French", fill = "black")
    canvas_card.itemconfig(card_txt_word, text=current_card["French"], fill = "black")
    canvas_card.itemconfig(card_img, image=card_front)
    
    # Schedule to flip the card to show the English translation after 3 seconds
    flip_timer = window.after(3000, flip_card)

def flip_card():
    # Change the canvas to display the English translation and the back image
    canvas_card.itemconfig(card_txt_lang, text="English", fill="white")
    canvas_card.itemconfig(card_txt_word, text=current_card["English"], fill = "white")
    canvas_card.itemconfig(card_img, image=card_back)

def is_known():

    to_learn.remove(current_card)
    
    data = pd.DataFrame(to_learn)

    data.to_csv("./data./words_to_learn.csv", index=False)

    update_word()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flip timer (to flip the card every 3 seconds)
flip_timer = window.after(3000, flip_card)

#Canvas Card
canvas_card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# card_front and card_back images
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

# Create the initial canvas image with the card front
card_img = canvas_card.create_image(400, 263, image=card_front)

# Create text placeholders for language and word
card_txt_lang = canvas_card.create_text(400, 150, text="French", fill="black", font=("Arial", 30, "italic"))
card_txt_word = canvas_card.create_text(400, 263, text="", fill="black", font=("Arial", 50, "bold"))

# Buttons
right_img_btn = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img_btn, highlightthickness=0, background=BACKGROUND_COLOR, command=is_known)

wrong_img_btn = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img_btn, highlightthickness=0, background=BACKGROUND_COLOR, command=update_word)

# canvas grid layout
canvas_card.grid(column=0, row=0, columnspan=2)
wrong_btn.grid(column=0, row=1)
right_btn.grid(column=1, row=1)

# Start by showing a random word
update_word()

window.mainloop()
