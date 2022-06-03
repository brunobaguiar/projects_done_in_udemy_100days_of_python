from tkinter import *
from tkinter import messagebox


TIMER = 5  # Time in seconds until app ends the typing
timer = None


# ---------------------------- MONITOR TYPING --------------------------- #
def key_press(event):
    window.after_cancel(timer)
    count_down(TIMER)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    timer_text.delete("1.0", "1.5")
    timer_text.insert(INSERT, f"{count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        end_game()


def end_game():
    content = text.get("1.0", "end")
    text.delete("1.0", "end")
    print(content)
    messagebox.showinfo(title="You didn't type for too long", message=f"Your text: {content}")
    window.quit()


# GUI Interface
window = Tk()
window.title("Write fast or loose everything")
window.config(padx=50, pady=50, bg="black")

# Timer
Label(text="TIMER:").grid(column=0, row=0)
timer_text = Text(window, bg="#212121", height=1, width=3, foreground="white")
timer_text.grid(column=1, row=0)

# User text box for typing
text = Text(window, bg="#212121", height=10, width=60, foreground="white", insertbackground='white')
text.grid(column=0, row=1, columnspan=20, pady=20)
text.focus_set()

# Capture pressed keys in real time
window.bind('<Key>', key_press)

count_down(TIMER)

window.mainloop()
