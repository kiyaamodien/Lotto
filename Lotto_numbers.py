from tkinter import *
from tkinter import messagebox
import datetime
import re

regex = '[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def confirm_details():
    age = datetime.datetime.today()
    try:
        for i in range(len(email.get())):
            if re.search(regex, email.get()):
                messagebox.showinfo("Status", "Valid Email")
                break

            else:
                messagebox.showerror("Error", "Invalid Email")
                break

        for x in range(int(id_number.get())):
            res = int(id_number.get()[0:2]) - int(age.strftime("%y"))
            if res >= 18:
                gamelog = open("Winnings.txt", "+w")
                gamelog.write("name: " + username.get() + "\nEmail: " + email.get() + "\nID number: " + id_number.get() + "\naddress:" + address.get())
                gamelog.close()
                messagebox.showinfo("Status", "You qualify to play")
                root.destroy()
                import lotto
            elif len(id_number.get()) != 13:
                messagebox.showerror("Error", "Not valid ID number")
                break
            else:
                messagebox.showerror("Error", "You are too young")
                break
    except ValueError:
        if id_number.get() != int:
            messagebox.showerror("Error", "the ID number must be an integer")


root = Tk()
root.title("Lotto Numbers")
root.geometry('400x300')
root.config(bg="royalblue")
canvas = Canvas(root, width=500, height=400, bg="gold", highlightthickness=0)
canvas.place(x=0, y=0)
img = PhotoImage(file="lotto-G.png")
img = img.subsample(1)
canvas.create_image(0, 0, anchor=NW, image=img)

username = Label(root, text="Please enter name")
username.place(x=10, y=50)
username = Entry(bg="white")
username.place(x=180, y=50)

id_number = Label(root, text="Please enter ID number")
id_number.place(x=10, y=80)
id_number = Entry(bg="white")
id_number.place(x=180, y=80)

address = Label(root, text="Please enter address")
address.place(x=10, y=110)
address = Entry(bg="white")
address.place(x=180, y=110)

email = Label(root, text="Please enter email")
email.place(x=10, y=140)
email = Entry(bg="white")
email.place(x=180, y=140)

label_register = Label(root, text="Register now", font="arial 20 bold")
label_register.place(x=100, y=12)

b1 = Button(root, text="Enter", command=confirm_details)
b1.place(x=50, y=180)


root.mainloop()
