import tkinter as tk
import time
from math import floor

PINK = "#F292B3"
NADESHIKO_PINK = "#DBA6B7"
SILVER_PINK = "#CFB0B9"
PALE_SILVER = "#C3BABA"
BLACK_COFFEE = "#32292F"
BG_COLOR = "#E5E5E5"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BEAK_MIN = 20
rounds = 0
clock = None


def start_timer():
    global rounds

    rounds += 1
    window.state = True

    # Long break given after the 4th round
    if rounds % 8 == 0:
        checkmark["text"] += "✔"
        ui_label.config(text="Break time")
        countdown(LONG_BEAK_MIN * 60)
    elif rounds % 2 == 0:
        checkmark["text"] += "✔"
        ui_label.config(text="Break time")
        countdown(SHORT_BREAK_MIN * 60)
    else:
        ui_label.config(text="Work time")
        countdown(WORK_MIN * 60)
    start_btn.config(command=start_btn_click)


def countdown(secs):
    mins = floor(secs / 60)
    seconds = secs % 60

    if secs == 0:
        start_timer()
    else:
        global clock
        timer = '{:02d}:{:02d}'.format(mins, seconds)
        canvas.itemconfig(timer_text, text=timer)
        clock = window.after(3, countdown,  secs - 1)


def start_btn_click():
    global clock
    if window.state:
        print("Turning off")
        window.state = False
    else:
        print("Turning on")
        window.state = True


def reset_btn_click():
    global clock
    global rounds
    window.after_cancel(clock)
    checkmark["text"] = ""
    canvas.itemconfig(timer_text, text="00:00")
    ui_label.config(text="Timer")
    start_btn.config(command=start_timer)
    rounds = 0


window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=25, bg=BG_COLOR)

# Background image
canvas = tk.Canvas(width=500, height=430, bg=BG_COLOR, highlightthickness=0)
canvas.grid(column=1, row=1)
background_img = tk.PhotoImage(file="material-background.png")
canvas.create_image(250, 215, image=background_img)

# Timer text
timer_text = canvas.create_text(250, 215, text="00:00", fill=BLACK_COFFEE, font=(FONT_NAME, 38, "bold"))

# Checkmark text
checkmark = tk.Label( bg=BG_COLOR, fg=BLACK_COFFEE, font=55)
checkmark.grid(column=1, row=4, pady=15)


show_completed = tk.Label(text="Completed cycles:", bg=BG_COLOR, fg=BLACK_COFFEE, font=(FONT_NAME, 15, "bold"))
show_completed.grid(column=1, row=3)

ui_label = tk.Label(text="Timer", bg=BG_COLOR, fg=BLACK_COFFEE, font=(FONT_NAME, 25, "bold"))
ui_label.grid(column=1, row=0)

start_btn = tk.Button(text="Start",
                      bg=NADESHIKO_PINK,
                      fg=BLACK_COFFEE,
                      font=(FONT_NAME, 20),
                      width=7,
                      borderwidth=5,
                      highlightthickness=0,
                      command=lambda: start_timer())
start_btn.grid(column=0, row=2, columnspan=1, pady=5)

reset_btn = tk.Button(text="Reset",
                      bg=NADESHIKO_PINK,
                      fg=BLACK_COFFEE,
                      font=(FONT_NAME, 20),
                      width=7,
                      borderwidth=5,
                      highlightthickness=0,
                      command=lambda: reset_btn_click())
reset_btn.grid(column=2, row=2, columnspan=1, pady=5)

window.mainloop()
