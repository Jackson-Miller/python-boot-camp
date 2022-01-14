import requests
from tkinter import *


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
kanye_img = PhotoImage(file="./resources/kanye.png")
background_img = PhotoImage(file="./resources/background.png")
window.title("Kanye Says...")
window.config(padx=50, pady=50)
window.iconphoto(False, kanye_img)

canvas = Canvas(width=300, height=414)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 24, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_button = Button(image=kanye_img, relief="flat", highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


get_quote()
window.mainloop()