# import requests
# from tkinter import *
#
# #URL
# response=requests.get("https://v6.exchangerate-api.com/v6/c3572485401443ca9efc76d2/latest/ZAR")
# responsej = response.json()
#
# rates=responsej['conversion_rates']
#
# #GUI
# root = Tk()
# root.title("Convertor")
# root.geometry("500x500")
#
# #function to convert currencies
# def convert():
#     num = float(amount_entry.get())
#     print(responsej['conversion_rates'][t1.get(ACTIVE)])
#     ans = num*responsej['conversion_rates'][t1.get(ACTIVE)]
#     amount_label['text'] = "Converted Amount :"+str(round(ans,2))+t1.get(ACTIVE)
#
# #exit function
# def exit():
#     root.destroy()
#
# # Creating head Label
# head_label = Label (root, text='CURRENCY CONVERTOR', fg='black',bg="red")
# head_label.pack()
#
# # Creating an Amount label
# amount_label = Label(root, text="Amount", fg='black',bg='dark green')
# amount_label.place(x=10, y=120)
#
# # Creating a from currency label
# from_currency=Label(root, text="From Currency", fg='black', bg='dark green')
# from_currency.place(x=10, y=105)
#
# # Creating a label for US Dollar
# from_currency=Label(root, text="Us Dollar",fg='black', bg='dark green')
# from_currency.place(x=10, y=120)
#
# #Creating label for To
# to_currency=Label(root, text="To")
# to_currency.place(x=10, y=160)
#
# #Creating label
# amount_label = Label(root, text="Converted Amount:", fg='black', bg='dark green')
# amount_label.place(x=10, y=400)
#
# #Creating listbox different currencies
# t1 = Listbox(root, width=10)
# for i in rates.keys():
#     t1.insert(END, str(i))
# t1.place(x=10, y=180)
#
#
# #Convert button
# cvert_btn = Button(root, text="Convert", command=convert)
# cvert_btn.pack(side=TOP)
#
# #Exit button
# ext_btn = Button(root, text="Exit", command=exit)
# ext_btn.pack(side=BOTTOM)
#
# #Amount that is being displayed
# amount_entry=Entry(root)
# amount_entry.pack()
# root.mainloop()
#


print("Hello.My name is jesse")