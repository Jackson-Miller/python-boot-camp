import os
import random
import string
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_input.delete(0, END)
    length = int(pass_len.get())
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))
    pass_input.insert(0, ''.join(random.choice(chars) for i in range(length)))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_account():
    # Check if any files are blank
    if len(web_input.get()) == 0 or len(user_input.get()) == 0 or len(pass_input.get()) == 0:
        messagebox.showerror(title="Oops", message="Please fill in all fields.")
    else:
        # Prompt user to confirm changes
        accept = messagebox.askokcancel(title="Are you sure?", message="Are you sure you want to save the account details?")
        if accept:
            # Write the data to file
            with open("data.txt", mode="a") as file:
                file.write(f"{web_input.get()} | {user_input.get()} | {pass_input.get()}\n")
            # Set the password to clipboard
            window.clipboard_clear()
            window.clipboard_append(pass_input.get())
            # Clear the form for the user to add another account
            web_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
logo_img = PhotoImage(file="logo.png")
window.iconphoto(False, logo_img)
window.config(padx=50, pady=50)
window.resizable(False, False)


canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website section
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
web_input = Entry(width=50)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

# Username section
user_label = Label(text="Username:")
user_label.grid(column=0, row=2)
user_input = Entry(width=50)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(END, string="user@email.com")

# Password section
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)
pass_input = Entry(width=50)
pass_input.grid(column=1, row=3, columnspan=2)
pass_input.insert(END, string="Click 'Generate Password' or type the password here")
pass_len_label = Label(text="Password length:")
pass_len_label.grid(column=0, row=4)
pass_len = Spinbox(from_=8, to=100, width=30)
pass_len.grid(column=1, row=4)
pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=2, row=4)
submit_button = Button(width=43, text="Add", command=add_account)
submit_button.grid(column=1, row=5, columnspan=2)


window.mainloop()
