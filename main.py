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
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec  = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        title_label.config(text="break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        title_label.config(text="break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="work", fg=GREEN)

def countdown(count):
    minus = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minus}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomatoImg)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

st_button = Button(text="Start", command=start_timer)
st_button.grid(column=0,row=2)
rst_button = Button(text="Reset", command=reset_timer)
rst_button.grid(column=2,row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1,row=3)




window.mainloop()