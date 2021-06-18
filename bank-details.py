from tkinter import *
from tkinter import ttk
import requests
import smtplib

root = Tk()
root.title("Banking Details")
root.geometry("400x650")
root.config(bg="gold")

response = requests.get("https://v6.exchangerate-api.com/v6/c3572485401443ca9efc76d2/latest/ZAR")
responsej = response.json()

rates = responsej['conversion_rates']

account_holder = Label(root, text="Account holder name", bg="gold")
account_holder.place(x=10, y=50)
account_holder = Entry(bg="white")
account_holder.place(x=180, y=50)

branch_code = Label(root, text="Branch code", bg="gold")
branch_code.place(x=10, y=80)
branch_code = Entry(bg="white")
branch_code.place(x=180, y=80)

bank_account_number = Label(root, text="Account number", bg="gold")
bank_account_number.place(x=10, y=110)
bank_account_number = Entry(bg="white")
bank_account_number.place(x=180, y=110)

banks = Label(root, text="Choose you bank", bg="gold")
banks.place(x=10, y=140)

combo_b = ttk.Combobox(root, values=[
                                    "FNB",
                                    "ABSA",
                                    "Nedbank",
                                    "Standard Bank"])


combo_b.place(x=180, y=140)
combo_b.set("Bank")


def convert():
    num = float(amount_entry.get())
    print(responsej['conversion_rates'][t1.get(ACTIVE)])
    ans = num*responsej['conversion_rates'][t1.get(ACTIVE)]
    amount_label['text'] = "Converted Amount :"+str(round(ans,2))+t1.get(ACTIVE)


# Creating an Amount label
amount_label = Label(root, text="Amount", fg='black', bg='gold')
amount_label.place(x=175, y=230)

# Creating a from currency label
from_currency = Label(root, text="Convert to preferred currency", fg='black', bg='gold')
from_currency.place(x=10, y=200)


#Creating label for To
to_currency = Label(root, text="To")
to_currency.place(x=160, y=290)

#Creating label
amount_label = Label(root, text="Converted Amount:", fg='black', bg='gold')
amount_label.place(x=10, y=550)

#Creating listbox different currencies
t1 = Listbox(root, width=10)
for i in rates.keys():
    t1.insert(END, str(i))
t1.place(x=160, y=310)


#Convert button
cvert_btn = Button(root, text="Convert", command=convert)
cvert_btn.place(x=160, y=500)

#Amount that is being entered
amount_entry = Entry(root)
amount_entry.place(x=120, y=250)


def sendemail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    sender_email_id = 'kiyaamlotto@gmail.com'
    receiver_email_id = ['jeandreross@gmail.com', 'abdullah.isaacs@gmail.com', 'jessenterblanche@gmail.com']
    password = 'kiyaamodienlotto'

    s.starttls()

    s.login(sender_email_id, password)

    message = "Hi there, hope you are doing well\n"
    message = message + "How was your task yesterday"

    s.sendmail(sender_email_id, receiver_email_id, message)

    s.quit()


claimbtn = Button(root, text="claim")
claimbtn.place(x=170, y=600)


root.mainloop()

