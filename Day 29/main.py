import os
import json
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
    site = web_input.get()
    username = user_input.get()
    sec = pass_input.get()
    new_data = {
        site: {
            "username": username,
            "password": sec
        }
    }

    # Check if any files are blank
    if len(site) == 0 or len(username) == 0 or len(sec) == 0:
        messagebox.showerror(title="Oops", message="Please fill in all fields.")
    else:
        # Write the data to file
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except IOError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            # Set the password to clipboard
            window.clipboard_clear()
            window.clipboard_append(sec)
            # Clear the form for the user to add another account
            web_input.delete(0, END)
            pass_input.delete(0, END)


# -------------------------- Search SETUP ----------------------------- #
def search_data():
    site = web_input.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except IOError:
        messagebox.showwarning(title="Warning", message="No passwords exist!  Please add sites before searching.")
    else:
        if site in data:
            email = data[site]["username"]
            sec = data[site]["password"]
            messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {sec}")
        else:
            messagebox.showwarning(title="Warning", message=f"No details stored for {site}.")


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
web_input = Entry(width=32)
web_input.grid(column=1, row=1)
web_input.focus()

# Search section
search_button = Button(width=14, text="Search", command=search_data)
search_button.grid(column=2, row=1)

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
pass_len = Spinbox(from_=12, to=100, width=30)
pass_len.grid(column=1, row=4)
pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=2, row=4)
submit_button = Button(width=43, text="Add", command=add_account)
submit_button.grid(column=1, row=5, columnspan=2)


window.mainloop()
