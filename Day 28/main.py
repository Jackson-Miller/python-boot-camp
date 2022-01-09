from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
timer_round = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer_round
    timer_round = 0
    window.after_cancel(timer)
    title_header.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    round_tracker.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global timer_round
    timer_round += 1
    if timer_round % 8 == 0:
        minutes = LONG_BREAK_MIN
        title_header.config(text="Break", fg=RED)
    elif timer_round % 2 == 0:
        minutes = SHORT_BREAK_MIN
        title_header.config(text="Break", fg=PINK)
    else:
        minutes = WORK_MIN
        title_header.config(text="Work", fg=GREEN)
    countdown(minutes * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    message = f"{count_min:02}:{count_sec:02}"
    canvas.itemconfig(timer_text, text=message)
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(timer_round/2)):
            marks += CHECK_MARK
        round_tracker.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
tomato_img = PhotoImage(file="tomato.png")
window.iconphoto(False, tomato_img)
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(False, False)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

title_header = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
title_header.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

round_tracker = Label(bg=YELLOW, fg=GREEN)
round_tracker.grid(column=1, row=3)

window.mainloop()
