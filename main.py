from tkinter import *
from tkinter import messagebox
import random
import pyperclip


#_PASSWORD GENERATOR_#

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    for letter in range(0, random.randint(1, 10)):
        random1 = random.choice(letters)
        password_list += random1

    for number in range(0, random.randint(1, 5)):
        random2 = random.choice(numbers)
        password_list += random2

    for symbol in range(0, random.randint(1, 5)):
        random3 = random.choice(symbols)
        password_list += random3

    random.shuffle(password_list)
    s_password = "".join(password_list)
    password_entry.insert(0, s_password)
    pyperclip.copy(s_password)


#_PASSWORD SAVER_#

def save_password():
    website_name = website_entry.get()
    user_email = username_entry.get()
    user_password = password_entry.get()
    if len(user_password) == 0 or len(website_name) == 0:
        messagebox.showerror(title="something went wrong!", message="hey, you have left a box empty")
    else:
        is_right = messagebox.askokcancel(title=f"{website_name}",
                                          message=f"Email :{user_email} \n Password: {user_password} \n"
                                                  f"Do You wanna save this? ")
        if is_right:
            with open("password_manager.txt", "a") as file:
                file.write(f"({website_name} | {user_email} | {user_password}) \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


#_UI SETUP_#

window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=1)
#
website = Label(text="Website :", font=("Arial", 10, "bold"))
website.grid(column=0, row=2)

website_entry = Entry(width=39)
website_entry.focus()
website_entry.grid(column=1, row=2, columnspan=2)

username = Label(text="Email/Username :", font=("Arial", 10, "bold"))
username.grid(column=0, row=3)

username_entry = Entry(width=39)
username_entry.insert(0, "yourmail@gmail.com")
username_entry.grid(column=1, row=3, columnspan=2)

password = Label(text="Password :", font=("Arial", 10, "bold"))
password.grid(column=0, row=4)
#
password_entry = Entry(width=21)
password_entry.grid(column=1, row=4)

password_gen_button = Button(text="Generate Password", command=password_generator)
password_gen_button.grid(column=2, row=4)

add_password = Button(text="Add the Password", width=40, command=save_password)
add_password.grid(column=1, row=6, columnspan=2)

window.mainloop()
