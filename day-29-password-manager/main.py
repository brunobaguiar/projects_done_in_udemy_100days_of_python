from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ------------------------------ PASSWORD SEARCH -------------------------------- #
def find_passord():
    try:
        with open("data.json", mode="r") as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Empty Database", message=f"There is no passwords stored yet.")
    else:
        check_website = (website_entry.get()).title()
        if check_website == "":
            messagebox.showwarning(title="Oops", message=f"Please don't leave fields empty")
        elif check_website in data:
            email = data[check_website]['email']
            password = data[check_website]['password']
            messagebox.showwarning(title=check_website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title=check_website, message=f"No details for the website {check_website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = randint(8, 10)
    # nr_symbols = randint(2, 4)
    # nr_numbers = randint(2, 4)

    # password_list = []

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_website = (website_entry.get()).title()
    new_email = email_username_entry.get()
    new_password = password_entry.get()
    new_data = {
        new_website: {
            "email": new_email,
            "password": new_password
        }
    }

    if new_website == "" or new_password == "":
        messagebox.showwarning(title="Oops", message=f"Please don't leave fields empty")
    else:
        is_ok = messagebox.askokcancel(title=new_website, message=f"These are details entered: \nEmail: {new_email} "f"\nPassword: {new_password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    #Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    #Saving updated data
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", mode="w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, 'end')
                email_username_entry.delete(0, 'end')
                email_username_entry.insert(0, 'your@gmail.com')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:", bg="white", font=("Arial", 10, "normal"))
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:", bg="white", font=("Arial", 10, "normal"))
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3)

# Buttons

generate_password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky=W)

add_button = Button(text="Add", highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)
add_button.config(width=43)

search_button = Button(text="Search", highlightthickness=0, command=find_passord)
search_button.grid(row=1, column=2, sticky=W)
search_button.config(width=14)

# Entry

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
website_entry.config(width=32)
website_entry.focus()

email_username_entry = Entry()
email_username_entry.grid(column=1, row=2, columnspan=2, sticky=W)
email_username_entry.config(width=51)
email_username_entry.insert(0, "your@gmail.com")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky=W)
password_entry.config(width=32)


window.mainloop()
