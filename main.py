from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    data = {
        website: {
            "email": email,
            "password": password
        }
    }

    messagebox.askquestion(title="Confirmation",
                           message=f"website = {website}\nemail = {email}\npassword = {password}\n Is this OK?")
    try:
        with open("data.json", "r") as data_file:
            # json.dump(data, data_file, indent=4)
            # reading old data
            load = json.load(data_file)

        with open("data.json", "a") as data_file:
            json.dump(data, data_file, indent=4)

    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    else:
        data.update(data)

        with open("data.json", "w") as data_file:
            # saving updated data
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------- SEARCH -----------------------#
def search():
    web_name = website_entry.get()
    data = json.loads(open("data.json").read())

    email = data[web_name]["email"]
    password = data[web_name]["password"]

    messagebox.showinfo(message=f"Email: {email}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=lock)
canvas.grid(column=1, row=0)

# --- WEBSITE ----

website_label = Label(text="Website: ", font=("Arial", 8, "normal"))
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

# --- USERNAME ---

username_label = Label(text="Email/Username:", font=("Arial", 8, "normal"))
username_label.grid(column=0, row=2)
username_entry = Entry(width=35)
username_entry.insert("0", "anas@gmail.com")
username_entry.grid(column=1, row=2, columnspan=1)

# --- PASSWORD ---

password_label = Label(text="Password: ", font=("Arial", 8, "normal"))
password_label.grid(row=3, column=0)
password_entry = Entry()
password_entry.grid(column=1, row=3, columnspan=1)

generate_password = Button(text="Generate password", command=generate_password)
generate_password.grid(column=2, row=3)

search = Button(text="Search", command=search)
search.grid(column=2, row=1)

add = Button(text="Add", width=36, command=add)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
