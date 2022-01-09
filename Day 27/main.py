import tkinter as tk


def on_click():
    miles = int(user_input.get())
    km = miles * 1.609
    output_label.config(text=km)


window = tk.Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

user_input = tk.Entry(width=7)
user_input.grid(column=1, row=0)

input_label = tk.Label(text="Miles")
input_label.grid(column=2, row=0)

conversion_text = tk.Label(text="is equal to")
conversion_text.grid(column=0, row=1)

output_label = tk.Label(text="0")
output_label.grid(column=1, row=1)

output_unit = tk.Label(text="Km")
output_unit.grid(column=2, row=1)

button = tk.Button(text="Calculate", command=on_click)
button.grid(column=1, row=2)


window.mainloop()
