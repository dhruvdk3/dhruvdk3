from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_entry.delete(0,END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []
    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letter + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(END,password)
    
# --------------------------- Find Password --------------------------------#
def find_password():
    website = websie_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message="No data Found")
            
# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_data():
    website = websie_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    
    new_data = {
        website:
            {
            "email":email,
            "password":password
            }
    }
    
    if len(websie_entry.get()) < 1 or len(user_entry.get()) < 1 or len(password_entry.get()) < 1:
        messagebox.showinfo(title="Oops", message="A field cann't be left empty.")
    
    else:
        is_ok = messagebox.askokcancel(title=websie_entry.get(), message=f"Details\nWebsite : {websie_entry.get()}\nUser/Email : {user_entry.get()}\nPasswprd : {password_entry.get()}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except :
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
                    websie_entry.delete(0,END)
                    password_entry.delete(0,END)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:        
                websie_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

websie_lable = Label(text="Website :")
user_lable = Label(text="Email/Username :")
password_lable = Label(text="Password :")
websie_lable.grid(row=1, column=0)
user_lable.grid(row=2, column=0)
password_lable.grid(row=3, column=0)

websie_entry = Entry(width=21)
websie_entry.focus()
user_entry = Entry(width=38)
user_entry.insert(END,"anemail@gmail.com")
password_entry = Entry(width=21)
websie_entry.grid(row=1, column=1, columnspan=1)
user_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)


add_button = Button(text="Add", width=36,command=get_data)
add_button.grid(row=4, column=1, columnspan=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1,column=2, columnspan=1)

canvas = Canvas(height=200, width=200)
x = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = x)
canvas.grid(row=0, column=1)
window.mainloop()