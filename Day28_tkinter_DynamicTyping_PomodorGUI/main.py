import math
from tkinter import *
marks = ""
timer = None
session = 0

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FFEBEB"
RED = "#e7305b"
GREEN = "#5D9C59"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=PINK)

# creating canvas in window to paste a picture and write over it
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)  # Height and width of tomato image

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)  # image lai canvas ko center ma lyauna lai thyakkai half half value
# deko taki origin tya hos
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


def reset():
    global session
    window.after_cancel(timer)
    title_label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    check_mark_label.config(text="")
    session = 0




def count_down(count):
    """
    This function uses 'after()' method of TK() class that helps to call a function after given amount of time ,we can
    also pass arguments to the function
    Args: time to countdown as argument and countdown is made upto 0
    Returns:each countdown number
    """
    global marks
    global timer

    count_min = math.floor(
        count / 60)  # count is given in seconds so converting it into minute in nearest lower integer
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # here 1000 millisecond means count_down will be called after
        # each second so we are passing count value in seconds
    else:
        # when count becomes 0, one session is completed so we are again calling start timer which will increase
        # value of session and select which session suits new value
        global session
        if session % 2 != 0:
            marks += "☑"
            check_mark_label.config(text=marks)
        start_timer()


def start_timer():  # we need to give method name without paranthesis  in command argument of button to prevent function
    # call but we need to pass argument in count down method so this method will be called
    global session
    session += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if session % 2 != 0:  # 1st,3rd,5th,7th session
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    elif session == 8:  # 8th session represents completion of 1 pomodoro round
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    else:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=RED)


# labels and buttons

title_label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=PINK)
title_label.grid(row=0, column=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=1)

check_mark_label = Label(text="", font="bold", fg=GREEN, bg=PINK)
check_mark_label.grid(row=3, column=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(row=3, column=3)





window.mainloop()
