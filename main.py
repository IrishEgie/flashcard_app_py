from tkinter import *
from tkinter import messagebox
import pandas as pd
import random as rd
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CSV FETCH ------------------------------- #
def fetch_fr_word():
    # Load the CSV data into a DataFrame
    df = pd.read_csv('./data/french_words.csv')
    
    # Fetch the "French" column from the DataFrame
    french_words = df["French"].tolist()
    
    # Select a random word from the French words list
    random_word = rd.choice(french_words)
    
    return random_word

def update_word():
    # Get a random French word
    random_word = fetch_fr_word()
    
    # Update the canvas text with the random word
    canvas_card.itemconfig(card_txt_word, text=random_word)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

#Canvas Card
canvas_card = Canvas(width=800, height=526, highlightthickness=0,bg=BACKGROUND_COLOR)
#card_front
card_front = PhotoImage(file="./images./card_front.png")
# #card_back
# card_back = PhotoImage(file="./images./card_back.png")


# Canvas Buttons
canvas_right_btn = Canvas(width=100, height=100, bg=BACKGROUND_COLOR)
right_btn = PhotoImage(file="./images./right.png")
canvas_wrong_btn = Canvas(width=100, height=100, bg=BACKGROUND_COLOR)
wrong_btn = PhotoImage(file="./images./wrong.png")
canvas_right_btn.create_image(50, 50, image = right_btn)
canvas_wrong_btn.create_image(50, 50, image = wrong_btn)

# Bind the canvas_right_btn to call the csv_read function on click
canvas_right_btn.bind("<Button-1>", lambda event: update_word())
canvas_wrong_btn.bind("<Button-1>", lambda event: update_word())

canvas_card.create_image(400, 263, image = card_front)
card_txt_lang = canvas_card.create_text(400,150, text="French", fill="black", font=("Arial", 30, "italic"))
card_txt_word = canvas_card.create_text(400,263, text=f"", fill="black", font=("Arial", 50, "bold"))


# canvas grid layout
canvas_card.grid(column=0, row=0, columnspan = 2)
canvas_wrong_btn.grid(column=0, row=1)
canvas_right_btn.grid(column=1, row=1)

update_word()

window.mainloop()