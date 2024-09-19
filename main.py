from tkinter import *
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

canvas_card = Canvas(width=800, height=526, highlightthickness=0)
#card_front
card_front = PhotoImage(file="./images./card_front.png")
# #card_back
# card_back = PhotoImage(file="./images./card_back.png")
canvas_card.create_image(400, 263, image = card_front)
card_text = canvas_card.create_text(400,150, text="French", fill="black", font=("Arial", 30, "italic"))
card_text = canvas_card.create_text(400,263, text="Configurable", fill="black", font=("Arial", 50, "bold"))

canvas_right_btn = Canvas(width=100, height=100, highlightthickness=0)
right_btn = PhotoImage(file="./images./right.png")
canvas_wrong_btn = Canvas(width=100, height=100, highlightthickness=0)
wrong_btn = PhotoImage(file="./images./wrong.png")
canvas_right_btn.create_image(50, 50, image = right_btn)
canvas_wrong_btn.create_image(50, 50, image = wrong_btn)

canvas_card.grid(column=0, row=0, columnspan = 2)
canvas_wrong_btn.grid(column=0, row=1)
canvas_right_btn.grid(column=1, row=1)

window.mainloop()