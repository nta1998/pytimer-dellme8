
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
REPS = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def re():
    global REPS
    window.after_cancel(my_timer)
    screen.itemconfig(timer, text="00:00")
    titel.config(text="Timer")
    check_marks.config(text="")
    REPS = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def stimer():
    global REPS
    REPS +=1
    work_cec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if REPS % 2 != 0:
        titel.config(text="work",fg=GREEN)
        s = work_cec
    elif REPS == 8:
        titel.config(text="Break",fg=RED)
        s = long_break
    else:
        titel.config(text="Break",fg=PINK)
        s = short_break
        
    count_down(s)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    screen.itemconfig(timer,text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000,count_down,count -1)
    else:
        stimer()
        mark = ""
        for _ in range(math.floor(REPS/2)):
            mark += "✔"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("timer")
window.config(padx=100,pady=50,bg =YELLOW)
window.minsize(width=476,height=300)


screen = Canvas(width=200, height= 224,bg=YELLOW,highlightthickness=0)

tomato = PhotoImage(file="tomato.png")
screen.create_image(100,112,image=tomato)

timer = screen.create_text(102,125,text= "00:00",fill="white",font=(FONT_NAME,35,"bold"))
screen.grid(column=2,row=2)

titel = Label(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
titel.grid(column=2,row=1)

start = Button(text="start",command=stimer)
start.grid(column=1,row=3)

re = Button(text="reset",command=re)
re.grid(column=3,row=3)

check_marks = Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column= 2,row=4)





window.mainloop()