import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(3, 6)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [letters[random.randint(0, len(letters) - 1)] for n in range(0, nr_letters)]
    password_numbers = [numbers[random.randint(0, len(numbers) - 1)] for n in range(0, nr_numbers)]
    password_symbols = [symbols[random.randint(0, len(symbols) - 1)] for n in range(0, nr_symbols)]

    password = password_letters + password_numbers + password_symbols
    random.shuffle(password)
    final_password = ''.join(password)

    password_entry.delete(0, END)
    password_entry.insert(END, string=final_password)
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(80, 100, image=logo)
canvas.grid(row=1, column=2)

# labels
website_label = Label(text='Website:', font=('Courier', 10))
website_label.grid(row=2, column=1)

email_label = Label(text='Email/Username:', font=('Courier', 10))
email_label.grid(row=3, column=1)

password_label = Label(text='Password:', font=('Courier', 10))
password_label.grid(row=4, column=1)

# entries

website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(row=2, column=2, columnspan=1)

email_entry = Entry(width=50)
email_entry.insert(END, string='')
email_entry.grid(row=3, column=2, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(row=4, column=2)


# functions

def search_data():
    website = website_entry.get()
    try:
        with open('data.json') as data:
            all_data = json.load(data)
            messagebox.showinfo(title=website, message=f'Your Password is: {all_data[website]["password"]}')
            pyperclip.copy(all_data[website]["password"])
    except KeyError:
        messagebox.showerror(title='Oops', message=f'No data for {website}')
    except FileNotFoundError:
        messagebox.showerror(title='Oops', message=f'No datafile found.')


def add_data():
    website = website_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()

    new_data = {website: {'email': email_username, 'password': password}}

    if website == '' or password == '' or email_username == '':
        messagebox.showerror(title='Invalid Details', message="You can't leave any of the fields empty.")

    else:
        save_conformation = messagebox.askokcancel(title='Confirm Details',
                                                   message=f'Website: {website} \n Password: {password} \n Save it?')

        if save_conformation:
            try:
                with open('data.json', 'r') as data:
                    all_data = json.load(data)
                    all_data.update(new_data)
            except FileNotFoundError:
                with open('data.json', 'w') as data:
                    json.dump(new_data, data, indent=2)
            else:
                with open('data.json', 'w') as data:
                    json.dump(all_data, data, indent=2)

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title='✔', message='Saved successfully.')


# Buttons

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=4, column=3)

add_button = Button(text='Add', command=add_data)
add_button.grid(row=5, column=2, columnspan=2)
add_button.config(width=40)

search_button = Button(text='Search', width=13, command=search_data)
search_button.grid(row=2, column=3)

window.mainloop()
