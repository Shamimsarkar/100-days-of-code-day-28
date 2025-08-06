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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00.00")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        title_label.config(text="Break", fg=RED, background=YELLOW, font=(FONT_NAME, 35, "bold"))
    elif reps % 2 == 0:
        count_down(short_break)
        title_label.config(text="Break", fg=PINK, background=YELLOW, font=(FONT_NAME, 35, "bold"))
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN, background=YELLOW, font=(FONT_NAME, 35, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if  count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Game")
window.config(padx=100, pady=50,background=YELLOW)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 112,text="00.00", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=2, column=2)

title_label = Label(text="Timer", fg=GREEN, background=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(row=1, column=2)

start_button = Button(text="Start", highlightthickness=0,command=start_count)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command= reset)
reset_button.grid(row=3, column=3)

check_mark = Label( background=YELLOW, fg=GREEN)
check_mark.grid(row=4, column=2)



window.mainloop()