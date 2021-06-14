from tkinter import *
from tkinter import messagebox
import datetime


def confirm_details():
    age=datetime.datetime.today()
    try:
        for x in range(int(id_number.get())):
            res = int(id_number.get()[0:2]) - int(age.strftime("%y"))
            if res >= 18:
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
root.geometry('400x400')
root.config(bg="royalblue")


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

b1 = Button(root, text="Enter", command=confirm_details)
b1.place(x=50, y=160)


root.mainloop()
