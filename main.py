import tkinter.font
from tkinter import *
from PIL import ImageTk, Image

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#393E46"
WHITE = "#ffffff"
FONT_NAME = "FangSong"
THINK_sec = 15
SPEAK_sec_1 = 45
SPEAK_sec_2 = 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    prepare_time_label.config(text="  Preparation Time: 00 seconds")
    record_time_label.config(text = f"  Record Time: 00 seconds")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM 1 ------------------------------- #
def start_timer1():
    global reps
    if reps == 0:
        count_down1(THINK_sec, 't')
        reps += 1
    elif reps == 1:
        count_down1(SPEAK_sec_1, 's')
        reps += 1
    else:
        reset_timer()

# ---------------------------- COUNTDOWN MECHANISM 1 ------------------------------- #
def count_down1(count,think_or_speak):
    global timer

    if count == 0:
        count = "00"
    elif count < 10:
        count = f"0{count}"

    if think_or_speak == 't':
        prepare_time_label.config(text = f"  Preparation Time: {count} seconds")
    elif think_or_speak == 's':
        record_time_label.config(text = f"  Record Time: {count} seconds")
    count = int(count)
    if count > 0:
        timer = window.after(1000, count_down1, count-1, think_or_speak)
    else:
        start_timer1()

# ---------------------------- TIMER MECHANISM 2 ------------------------------- #
def start_timer2():
    global reps
    if reps == 0:
        count_down2(THINK_sec,'t')
        reps += 1
    elif reps == 1:
        count_down2(SPEAK_sec_2,'s')
        reps += 1
    else:
        reset_timer()

# ---------------------------- COUNTDOWN MECHANISM 2 ------------------------------- #
def count_down2(count,think_or_speak):
    global timer

    if count == 0:
        count = "00"
    elif count < 10:
        count = f"0{count}"

    if think_or_speak == 't':
        prepare_time_label.config(text = f"  Preparation Time: {count} seconds")
    elif think_or_speak == 's':
        record_time_label.config(text = f"  Record Time: {count} seconds")
    count = int(count)
    if count > 0:
        timer = window.after(1000, count_down2, count-1, think_or_speak)
    else:
        start_timer2()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("TOEFL Speaking Alarm")
window.config(padx=100, pady=50, bg=YELLOW)

# open image
my_pic = Image.open("Images/head.png")
# resize image
resized = my_pic.resize((248, 231), Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)
# put image into label
my_label = Label(window, image=new_pic, pady=5, bg=YELLOW)
my_label.grid(column=0, row=0, columnspan=3)

label_font = tkinter.font.Font(family=FONT_NAME)
prepare_time_label = Label(text="  Preparation Time: 00 seconds", font=label_font, fg=WHITE, bg=BLACK, width=26, height=1,
                           anchor='w')
prepare_time_label.grid(column=0, row=1, columnspan=3, padx=1, pady=1)

record_time_label = Label(text="  Record Time: 00 seconds", font=label_font, fg=WHITE, bg=BLACK, width=26, height=1,
                          anchor='w')
record_time_label.grid(column=0, row=2, columnspan=3)

start1 = Button(text="Independent Task", bg=YELLOW, highlightbackground=YELLOW,
               command=start_timer1)
start1.grid(column=0, row=3)

start2 = Button(text="Integrated Task", bg=YELLOW, highlightbackground=YELLOW,
               command=start_timer2)
start2.grid(column=1, row=3)

reset = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW,
               command=reset_timer)
reset.grid(column=2, row=3)

window.mainloop()
