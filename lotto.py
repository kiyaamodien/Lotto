from tkinter import *
from random import sample
from tkinter import messagebox

root = Tk()
root.geometry("500x400")
root.config(bg="gold")
list1 = []
list2 = []
list3 = []

canvas = Canvas(root, width=500, height=400, bg="gold", highlightthickness=0)
canvas.place(x=0, y=100)
img = PhotoImage(file="lotto-G.png")
canvas.create_image(0, 0, anchor=NW, image=img)

label_fr1 = LabelFrame(root, text="Entry Numbers", bg="royalblue", pady=10)
label_fr1.pack(fill="both")


def funcname(num):
    if len(list1) < 6 and num not in list1:
        list1.append(int(num))
        user_entries1.config(text=list1)
    elif len(list1) == 6 and len(list2) < 6 and num not in list2:
        list2.append(int(num))
        user_entries2.config(text=list2)
    elif len(list2) == 6 and len(list1) == 6 and len(list3) < 6 and num not in list3:
        list3.append(int(num))
        user_entries3.config(text=list3)
    if len(list3) == 6:
        numbtn1.config(state=DISABLED)
        numbtn2.config(state=DISABLED)
        numbtn3.config(state=DISABLED)
        numbtn4.config(state=DISABLED)
        numbtn5.config(state=DISABLED)
        numbtn6.config(state=DISABLED)
        numbtn7.config(state=DISABLED)
        numbtn8.config(state=DISABLED)
        numbtn9.config(state=DISABLED)
        numbtn10.config(state=DISABLED)
        numbtn11.config(state=DISABLED)
        numbtn12.config(state=DISABLED)
        numbtn13.config(state=DISABLED)
        numbtn14.config(state=DISABLED)
        numbtn15.config(state=DISABLED)
        numbtn16.config(state=DISABLED)
        numbtn17.config(state=DISABLED)
        numbtn18.config(state=DISABLED)
        numbtn19.config(state=DISABLED)
        numbtn20.config(state=DISABLED)
        numbtn21.config(state=DISABLED)
        numbtn22.config(state=DISABLED)
        numbtn23.config(state=DISABLED)
        numbtn24.config(state=DISABLED)
        numbtn25.config(state=DISABLED)
        numbtn26.config(state=DISABLED)
        numbtn27.config(state=DISABLED)
        numbtn28.config(state=DISABLED)
        numbtn29.config(state=DISABLED)
        numbtn30.config(state=DISABLED)
        numbtn31.config(state=DISABLED)
        numbtn32.config(state=DISABLED)
        numbtn33.config(state=DISABLED)
        numbtn34.config(state=DISABLED)
        numbtn35.config(state=DISABLED)
        numbtn36.config(state=DISABLED)
        numbtn37.config(state=DISABLED)
        numbtn38.config(state=DISABLED)
        numbtn39.config(state=DISABLED)
        numbtn40.config(state=DISABLED)
        numbtn41.config(state=DISABLED)
        numbtn42.config(state=DISABLED)
        numbtn43.config(state=DISABLED)
        numbtn44.config(state=DISABLED)
        numbtn45.config(state=DISABLED)
        numbtn46.config(state=DISABLED)
        numbtn47.config(state=DISABLED)
        numbtn48.config(state=DISABLED)
        numbtn49.config(state=DISABLED)


# buttons
numbtn1 = Button(root, text=1, command=lambda: funcname(1))
numbtn1.place(x=30, y=20)
numbtn2 = Button(root, text=2, command=lambda: funcname(2))
numbtn2.place(x=70, y=20)
numbtn3 = Button(root, text=3, command=lambda: funcname(3))
numbtn3.place(x=110, y=20)
numbtn4 = Button(root, text=4, command=lambda: funcname(4))
numbtn4.place(x=150, y=20)
numbtn5 = Button(root, text=5, command=lambda: funcname(5))
numbtn5.place(x=190, y=20)
numbtn6 = Button(root, text=6, command=lambda: funcname(6))
numbtn6.place(x=230, y=20)
numbtn7 = Button(root, text=7, command=lambda: funcname(7))
numbtn7.place(x=270, y=20)
numbtn8 = Button(root, text=8, command=lambda: funcname(8))
numbtn8.place(x=310, y=20)
numbtn9 = Button(root, text=9, command=lambda: funcname(9))
numbtn9.place(x=350, y=20)
numbtn10 = Button(root, text=10, command=lambda: funcname(10))
numbtn10.place(x=30, y=60)
numbtn11 = Button(root, text=11, command=lambda: funcname(11))
numbtn11.place(x=70, y=60)
numbtn12 = Button(root, text=12, command=lambda: funcname(12))
numbtn12.place(x=110, y=60)
numbtn13 = Button(root, text=13, command=lambda: funcname(13))
numbtn13.place(x=150, y=60)
numbtn14 = Button(root, text=14, command=lambda: funcname(14))
numbtn14.place(x=190, y=60)
numbtn15 = Button(root, text=15, command=lambda: funcname(15))
numbtn15.place(x=230, y=60)
numbtn16 = Button(root, text=16, command=lambda: funcname(16))
numbtn16.place(x=270, y=60)
numbtn17 = Button(root, text=17, command=lambda: funcname(17))
numbtn17.place(x=310, y=60)
numbtn18 = Button(root, text=18, command=lambda: funcname(18))
numbtn18.place(x=350, y=60)
numbtn19 = Button(root, text=19, command=lambda: funcname(19))
numbtn19.place(x=30, y=100)
numbtn20 = Button(root, text=20, command=lambda: funcname(20))
numbtn20.place(x=70, y=100)
numbtn21 = Button(root, text=21, command=lambda: funcname(21))
numbtn21.place(x=110, y=100)
numbtn22 = Button(root, text=22, command=lambda: funcname(22))
numbtn22.place(x=150, y=100)
numbtn23 = Button(root, text=23, command=lambda: funcname(23))
numbtn23.place(x=190, y=100)
numbtn24 = Button(root, text=24, command=lambda: funcname(24))
numbtn24.place(x=230, y=100)
numbtn25 = Button(root, text=25, command=lambda: funcname(25))
numbtn25.place(x=270, y=100)
numbtn26 = Button(root, text=26, command=lambda: funcname(26))
numbtn26.place(x=310, y=100)
numbtn27 = Button(root, text=27, command=lambda: funcname(27))
numbtn27.place(x=350, y=100)
numbtn28 = Button(root, text=28, command=lambda: funcname(28))
numbtn28.place(x=30, y=140)
numbtn29 = Button(root, text=29, command=lambda: funcname(29))
numbtn29.place(x=70, y=140)
numbtn30 = Button(root, text=30, command=lambda: funcname(30))
numbtn30.place(x=110, y=140)
numbtn31 = Button(root, text=31, command=lambda: funcname(31))
numbtn31.place(x=150, y=140)
numbtn32 = Button(root, text=32, command=lambda: funcname(32))
numbtn32.place(x=190, y=140)
numbtn33 = Button(root, text=33, command=lambda: funcname(33))
numbtn33.place(x=230, y=140)
numbtn34 = Button(root, text=34, command=lambda: funcname(34))
numbtn34.place(x=270, y=140)
numbtn35 = Button(root, text=35, command=lambda: funcname(35))
numbtn35.place(x=310, y=140)
numbtn36 = Button(root, text=36, command=lambda: funcname(36))
numbtn36.place(x=350, y=140)
numbtn37 = Button(root, text=37, command=lambda: funcname(37))
numbtn37.place(x=30, y=180)
numbtn38 = Button(root, text=38, command=lambda: funcname(38))
numbtn38.place(x=70, y=180)
numbtn39 = Button(root, text=39, command=lambda: funcname(39))
numbtn39.place(x=110, y=180)
numbtn40 = Button(root, text=40, command=lambda: funcname(40))
numbtn40.place(x=150, y=180)
numbtn41 = Button(root, text=41, command=lambda: funcname(41))
numbtn41.place(x=190, y=180)
numbtn42 = Button(root, text=42, command=lambda: funcname(42))
numbtn42.place(x=230, y=180)
numbtn43 = Button(root, text=43, command=lambda: funcname(43))
numbtn43.place(x=270, y=180)
numbtn44 = Button(root, text=44, command=lambda: funcname(44))
numbtn44.place(x=310, y=180)
numbtn45 = Button(root, text=45, command=lambda: funcname(45))
numbtn45.place(x=350, y=180)
numbtn46 = Button(root, text=46, command=lambda: funcname(47))
numbtn46.place(x=30, y=220)
numbtn47 = Button(root, text=47, command=lambda: funcname(48))
numbtn47.place(x=70, y=220)
numbtn48 = Button(root, text=48, command=lambda: funcname(48))
numbtn48.place(x=110, y=220)
numbtn49 = Button(root, text=49, command=lambda: funcname(49))
numbtn49.place(x=150, y=220)
total = Label(root, text="")
total.place(x=20, y=540)

user_entries1 = Label(root, text='', bg='yellow', width=15, justify='center')
user_entries1.place(x=0, y=260)
user_entries2 = Label(root, text='', bg='yellow', width=15, justify='center')
user_entries2.place(x=0, y=310)
user_entries3 = Label(root, text='', bg='yellow', width=15, justify='center')
user_entries3.place(x=0, y=360)

def reset_list():
    list1.clear()
    list2.clear()
    list3.clear()
    user_entries1.config(text='')
    user_entries2.config(text='')
    user_entries3.config(text='')
    numbtn1.config(state=NORMAL)
    numbtn2.config(state=NORMAL)
    numbtn3.config(state=NORMAL)
    numbtn4.config(state=NORMAL)
    numbtn5.config(state=NORMAL)
    numbtn6.config(state=NORMAL)
    numbtn7.config(state=NORMAL)
    numbtn8.config(state=NORMAL)
    numbtn9.config(state=NORMAL)
    numbtn10.config(state=NORMAL)
    numbtn11.config(state=NORMAL)
    numbtn12.config(state=NORMAL)
    numbtn13.config(state=NORMAL)
    numbtn14.config(state=NORMAL)
    numbtn15.config(state=NORMAL)
    numbtn16.config(state=NORMAL)
    numbtn17.config(state=NORMAL)
    numbtn18.config(state=NORMAL)
    numbtn19.config(state=NORMAL)
    numbtn20.config(state=NORMAL)
    numbtn21.config(state=NORMAL)
    numbtn22.config(state=NORMAL)
    numbtn23.config(state=NORMAL)
    numbtn24.config(state=NORMAL)
    numbtn25.config(state=NORMAL)
    numbtn26.config(state=NORMAL)
    numbtn27.config(state=NORMAL)
    numbtn28.config(state=NORMAL)
    numbtn29.config(state=NORMAL)
    numbtn30.config(state=NORMAL)
    numbtn31.config(state=NORMAL)
    numbtn32.config(state=NORMAL)
    numbtn33.config(state=NORMAL)
    numbtn34.config(state=NORMAL)
    numbtn35.config(state=NORMAL)
    numbtn36.config(state=NORMAL)
    numbtn37.config(state=NORMAL)
    numbtn38.config(state=NORMAL)
    numbtn39.config(state=NORMAL)
    numbtn40.config(state=NORMAL)
    numbtn41.config(state=NORMAL)
    numbtn42.config(state=NORMAL)
    numbtn44.config(state=NORMAL)
    numbtn43.config(state=NORMAL)
    numbtn45.config(state=NORMAL)
    numbtn46.config(state=NORMAL)
    numbtn47.config(state=NORMAL)
    numbtn48.config(state=NORMAL)
    numbtn49.config(state=NORMAL)


def random_list():
    random_list = sample(range(1, 49), 6)
    random_list.sort()
    label_show.configure(text=random_list)

    counter = 0
    for x in range(0, 6):
        # import pdb;pdb.set_trace()
        if list1[x] == random_list[x]:
            counter = counter + 1
        if counter <= 1:
            messagebox.showinfo("Unlucky")
            break

        elif counter == 2:
            messagebox.showinfo("You won R20")
            break

        elif counter == 3:
            messagebox.showinfo("You won R100")
            break

        elif counter == 4:
            messagebox.showinfo("You won R2,384.00")
            break

        elif counter == 5:
            messagebox.showinfo("You won R2,384.00")
            break

        elif counter == 6:
            messagebox.showinfo("You won R10,000 000.00")
            break

    for numbers in range(0, 6):
        if list2[numbers] == random_list[numbers]:
            counter += 1
        if counter <= 1:
            messagebox.showinfo("Unlucky")
            break

        elif counter == 2:
            messagebox.showinfo("You won R20")
            break

        elif counter == 3:
            messagebox.showinfo("You won R100")
            break

        elif counter == 4:
            messagebox.showinfo("You won R2,384.00")
            break

        elif counter == 5:
            messagebox.showinfo("You won R2,384.00")
            break

        elif counter == 6:
            messagebox.showinfo("You won R10,000 000.00")
            break

    for numbers in range(0, 6):
        if list3[numbers] == random_list[numbers]:
            counter += 1
        if counter <= 1:
            messagebox.showinfo("Unlucky")
            break

        elif counter == 2:
            messagebox.showinfo("You won R20")
            break

        elif counter == 3:
            messagebox.showinfo("You won R100")
            break

        elif counter == 4:
            messagebox.showinfo("You won R2,384.00")
            break

        elif counter == 5:
            messagebox.showinfo("You won R2,384.00")
            break

        elif counter == 6:
            messagebox.showinfo("You won R10,000 000.00")
            break


click_btn = Button(root, text="Play", command=random_list)
click_btn.place(x=300, y=220)

click_btn.configure(command=random_list)

pa_btn = Button(root, text="Play again", command=reset_list)
pa_btn.place(x=300, y=250)


label_num = Label(root, text="Lotto Numbers!")
label_num.place(x=200, y=300)

label_show = Label(root)
label_show.place(x=320, y=300)


root.mainloop()
