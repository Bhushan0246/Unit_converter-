from tkinter import Tk, ttk
from tkinter import *

from PIL import Image, ImageTk

import requests
import json

# colors
cor0 = "#FFFFFF"  # white
cor1 = "#333333"  # black
cor2 = "#ffff80"  # Top frame color

window = Tk()
window.geometry('620x750+420+20')
window.title('Converter')
window.configure(bg=cor0)
window.resizable(height=FALSE, width=FALSE)

# frames
top = Frame(window, width=700, height=65, bg=cor2)
top.grid(row=0, column=0)

main = Frame(window, width=700, height=690, bg=cor0)
main.grid(row=1, column=0)

top_2 = Frame(main, width=290, height=120,bg=cor0,highlightbackground="black", highlightthickness=2)

#top_2.grid(row=2, column=0)
top_2.place(x=155,y=400)


def convert():
    global result, disp1_label, disp2_label, value_disp
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    if currency_2 == 'USD':
        symbol = '$'
    elif currency_2 == 'INR':
        symbol = '₹'
    elif currency_2 == 'EUR':
        symbol = '€'
    elif currency_2 == 'BRL':
        symbol = 'R$'
    elif currency_2 == 'CAD':
        symbol = 'CA $'
    elif currency_2 == 'AUD':
        symbol = '$'
    elif currency_2 == 'GBP':
        symbol = '£'
    elif currency_2 == 'SGD':
        symbol = 'S$'
    elif currency_2 == 'NZD':
        symbol = '$'
    elif currency_2 == 'NPR':
        symbol = 'Rs'
    elif currency_2 == 'JPY':
        symbol = '¥'
    elif currency_2 == 'IDR':
        symbol = 'Rp'
    elif currency_2 == 'RUB':
        symbol = '₽'
    elif currency_2 == 'LKR':
        symbol = 'Rs'
    elif currency_2 == 'CNY':
        symbol = '¥'


    headers = {
        'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
        'x-rapidapi-key': "90c59d6c9fmsh4599f814e2ffc92p17fc6djsndeaa0265ac61"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + " {:,.3f}".format(converted_amount)

    result['text'] = formatted

    disp1_label['text'] = combo1.get()
    disp2_label['text'] = combo2.get()

    value_disp['text']=value.get()
    print(converted_amount, formatted)

#def display():




# top frame

# icon = Image.open('images/icon.png')
# icon = icon.resize((40, 40))
# icon = ImageTk.PhotoImage(icon)
# app_name = Label(top, image=icon, compound=LEFT, text="Currency Converter", height=5, padx=13, pady=30, anchor=CENTER,
#                font=('Arial 16 bold'), bg=cor2, fg=cor0)
# app_name.place(x=0, y=0)

# main frame
result = Label(top_2, text=" ", width=7, height=2, pady=0, relief="flat", anchor=CENTER, font=('Monospace 17 bold'), bg=cor0,fg=cor1)
result.place(x=180, y=55)

currency = ['CAD', 'BRL', 'EUR', 'INR', 'USD','AUD','GBP','SGD','NZD','NPR','JPY','IDR','RUB','LKR','CNY']

from_label = Label(main, text="From", width=16, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Monospace 12 bold'),
                   bg=cor0, fg=cor1)
from_label.place(x=160, y=190)
combo1 = ttk.Combobox(main, width=22, justify=CENTER, font=("Monospace 16 normal"))
combo1['values'] = (currency)
combo1.place(x=160, y=215)

image = Image.open(r"C:\Users\nidhi\Downloads\repeat_223109.png")
#Resize the Image
image = image.resize((32,32))
#Convert the image to PhotoImage
img= ImageTk.PhotoImage(image)

button_1 = Button(main,image=img, width=40, padx=5, height=35, bg=cor2, fg=cor1, font=("Monospace 14 bold"))
button_1.image = img
button_1.place(x=270, y=265)

to_label = Label(main, text="To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Monospace 12 bold'),
                 bg=cor0, fg=cor1)
to_label.place(x=160, y=300)
combo2 = ttk.Combobox(main, width=22, justify=CENTER, font=("Monospace 16 normal"))
combo2['values'] = (currency)
combo2.place(x=160, y=325)

entry_label = Label(main, text="Enter the value", width=18, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Monospace 12 bold'),
                 bg=cor0, fg=cor1)

entry_label.place(x=120, y=100)

value = Entry(main, width=16, justify=CENTER, font=("Monospace 18 bold"), relief=SOLID)
value.place(x=265, y=95)

value_disp=Label(top_2, text=" ", width=8, height=2, pady=0, relief="flat", anchor=CENTER, font=('Monospace 17 bold'), bg=cor0,
               fg=cor1)
value_disp.place(x=0, y=55)

Converter_label = Label(top, text="Currency Converter", width=18, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Monospace 21 normal'),
                 bg=cor2, fg=cor1)
Converter_label.place(x=185, y=18)

equal_label = Label(top_2, text="=", width=2, height=2, pady=0, relief="flat", anchor=CENTER, font=('Monospace 19 bold'), bg=cor0,
               fg=cor1)
equal_label.place(x=120, y=30)


disp1_label = Label(top_2, text=" ", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Monospace 14 normal'),
                   bg=cor0, fg=cor1)
disp1_label.place(x=40, y=16)


disp2_label = Label(top_2, text=" ", width=6, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Monospace 14 normal'),
                   bg=cor0, fg=cor1)
disp2_label.place(x=190, y=16)


button = Button(main, text="Convert", width=22, padx=5, height=1, bg=cor2, fg=cor1, font=("Monospace 14 bold"),
                command=convert)
button.place(x=158, y=550)

'''button_change = Button(main, width=22, padx=5, height=1, bg=cor2, fg=cor1, font=("Monospace 14 bold"),
                command=convert)
button_change.place(x=158, y=400)'''


'''back =Button(main, borderwidth=2, height=40, width=80, bg="#eef7f5", fg="black",activebackground="white")
back.place(x=850, y=30)'''

result.lift()
disp1_label.lift()
disp2_label.lift()
value_disp.lift()
equal_label.lift()

window.mainloop()
