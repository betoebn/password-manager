from tkinter import *
from tkinter import messagebox
import random
import json


# ----------------------------    SEARCH BUTTON   ------------------------------- #


def search():
    website = website_entry.get().lower()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Please enter a website first")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']}\n "
                                                            f"Password: {data[website]['password']}")
        else:
            messagebox.showerror(title="ERROR", message=f"There's no password associated with {website}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random_password = password_letters + password_symbols + password_numbers

    random.shuffle(random_password)
    password_ready = ''.join(map(str, random_password))

    password_entry.delete(0, 'end')
    password_entry.insert(END, string=password_ready)
    password_entry.clipboard_clear()
    password_entry.clipboard_append(password_ready)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get().lower()
    email = email_entry.get().lower()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="You left some fields blank")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}"
                                                              f"\n Password: {password}\n Is it ok to save?", )
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=51)
website_entry.insert(END, string="Please enter Website")
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=51)
email_entry.insert(END, string="rtb65.rb@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=33)
password_entry.insert(END, string="Please enter Password")
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", width=14, command=password_generator)
generate_password_button.grid(column=2, row=3)

search_button = Button(text="Search Password", width=14, command=search)
search_button.grid(column=2, row=1)

add_password_button = Button(text="Add Password", width=40, command=save)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
