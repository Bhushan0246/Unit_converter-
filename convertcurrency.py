from customtkinter import *
from CTkMessagebox import *
from PIL import Image
from tktooltip import ToolTip
import mysql.connector
from requests import *
from json import *
import curr_history
import Main_window
from datetime import datetime

def currency():
        def history_cur():
            master.destroy()
            curr_history.historyCurr()

        def go_home():
            master.destroy()
            temp = CTk()
            new_win = Main_window.Main_frame(temp)
            temp.mainloop()

        def trace_to(choice):
            lbl_curr_to.configure(text=choice)
        def trace_from(choice):
            lbl_curr_from.configure(text=choice)

        def swap_curr():
            currency_1 = combo_from.get()
            combo_from.set(combo_to.get())
            combo_to.set(currency_1)
            trace_to(combo_to.get())
            trace_from(combo_from.get())

        def action():
            global result, lbl_curr_from, lbl_curr_to, value_disp
            url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
            currency_1 = combo_from.get()
            currency_2 = combo_to.get()
            amount = inp_val.get()

            if currency_2 == 'USD':
                symbol = '$'
            elif currency_2 == 'INR':
                symbol = '₹'
            elif currency_2 == 'EUR':
                symbol = '€'
            elif currency_2 == 'BRL':
                symbol = 'R $'
            elif currency_2 == 'CAD':
                symbol = 'CA $'
            elif currency_2 == 'AUD':
                symbol = '$'
            elif currency_2 == 'GBP':
                symbol = '£'
            elif currency_2 == 'SGD':
                symbol = 'S $'
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

            querystring = {"from": currency_1, "to": currency_2, "amount": amount}
            headers = {
                'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
                'x-rapidapi-key': "90c59d6c9fmsh4599f814e2ffc92p17fc6djsndeaa0265ac61"
            }
            response = request("GET", url, headers=headers, params=querystring)
            data = loads(response.text)
            converted_amount = data["result"]["convertedAmount"]
            formatted = symbol + " {:,.3f}".format(converted_amount)

            lbl_curr_from.configure(text=currency_1)
            lbl_curr_to.configure(text=currency_2)
            value_disp.configure(text=amount)
            result.configure(text=formatted)

            # Defining writeHistory function to write tuples in database for history
            def writeHistory():
                stamp = datetime.now().strftime("%X, " + "%x")
                new_result = formatted[2:]
                try:
                    mydb = mysql.connector.connect(host='localhost', user='root', password='mysql@123456', database='converter')
                    mycur = mydb.cursor()
                    query = "INSERT INTO curr_history(on_date, from_curr, to_curr, from_value, into_value) VALUES (%s,%s,%s,%s,%s)"
                    qvalue = ( stamp,currency_1, currency_2, amount, new_result)
                    mycur.execute(query, qvalue)
                    mydb.commit()
                except:
                    CTkMessagebox(master, title='Error', message="Action can't be registered into history!",
                                  icon='cancel', border_width=2, fg_color=color_bg, bg_color=color_bg,
                                  text_color='#263238', corner_radius=10, fade_in_duration=1, sound=True)
            # Call to the writeHistory function
            writeHistory()

        master = CTk()
        master.title("Currency Converter")
        master.geometry("620x700+400+20")
        master.wm_resizable(0, 0)
        master.configure(fg_color='#fff')
        color_bg = master.cget('background')

        font1 = CTkFont('Monospace', 32, 'normal', underline=False, slant='italic')
        font2 = CTkFont('Monospace', 18, 'bold', slant='italic')
        font3 = CTkFont('Monospace', 18, 'bold')

        head = CTkFrame(master, width=620, height=70, bg_color='#ffa480', fg_color='#ffa480').pack()
        title = CTkLabel(head, text='Currency Converter', bg_color='#ffa480', fg_color='#ffa480', font=font1, text_color='#34444c').place(x=175, y=15)

        amount = DoubleVar()
        currency_1 = StringVar(value='CAD')
        currency_2 = StringVar(value='BRL')

        rupee = CTkImage(Image.open('./images/cur_rupee.png'), size=(80, 70))
        CTkLabel(master, text='', fg_color="transparent", bg_color="transparent", image=rupee).place(x=10, y=120)
        dollar = CTkImage(Image.open('./images/cur_dollar.png'), size=(80, 70))
        CTkLabel(master, text='', fg_color="transparent", bg_color="transparent", image=dollar).place(x=475, y=310)
        JPY = CTkImage(Image.open('./images/cur_JPY.png'), size=(100, 85))
        CTkLabel(master, text='', fg_color="transparent", bg_color="transparent", image=JPY).place(x=180, y=490)
        cent = CTkImage(Image.open('./images/cur_cent.png'), size=(100, 85))
        CTkLabel(master, text='', fg_color="transparent", bg_color="transparent", image=cent).place(x=500, y=100)
        euro = CTkImage(Image.open('./images/cur_euro.png'), size=(80, 70))
        CTkLabel(master, text='', fg_color="transparent", bg_color="transparent", image=euro).place(x=30, y=580)
        plant = CTkImage(Image.open('./images/Plants.png'), size=(210, 305))
        CTkLabel(master, text='', fg_color="transparent", bg_color="transparent", image=plant).place(x=410, y=400)


        lbl_val=CTkLabel(master, text='Enter the value', text_color='#263238', fg_color=color_bg, font=font2).place(x=120, y=100)
        inp_val=CTkEntry(master, width=210, height=25, corner_radius=4,border_width=2, border_color='#ff9166', bg_color=color_bg, fg_color=color_bg,
                         text_color='#263238', state=NORMAL, font=font2, textvariable=amount)
        inp_val.place(x=270, y=100)

        curr = ['CAD', 'BRL', 'EUR', 'INR', 'USD','AUD','GBP','SGD','NZD','NPR','JPY','IDR','RUB','LKR','CNY']

        lbl_from = CTkLabel(master, text='From', text_color='#263238', fg_color=color_bg, font=font2).place(x=120, y=180)
        combo_from = CTkComboBox(master,width=260, height=25, corner_radius=4,border_width=2, border_color='#ff9166', bg_color=color_bg, fg_color=color_bg,
                               button_color='#ff9166', button_hover_color='#ffc8b3', dropdown_hover_color='#ffc8b3', dropdown_fg_color=color_bg, dropdown_text_color='#263238',
                               text_color='#263238', font=font2, dropdown_font=font3, values=curr, state=NORMAL, justify="center", variable=currency_1, command=trace_from)
        combo_from.place(x=230, y=180)

        img = CTkImage(Image.open('./images/swap.png'), size=(30,28))
        swap_btn = CTkButton(master, text='',width=60, height=28,image=img, corner_radius=4, border_width=2, border_color='#ff9166', fg_color=color_bg, state=NORMAL, command=swap_curr)
        ToolTip(swap_btn, msg="Swap Currency", delay=0.3, bg='#fff')
        swap_btn.configure(hover_color='#ffc8b3')
        swap_btn.place(x=320,y=230)

        lbl_to = CTkLabel(master, text='Into', text_color='#263238', fg_color=color_bg, font=font2).place(x=120,y=300)
        combo_to = CTkComboBox(master, width=260, height=25, corner_radius=4, border_width=2, border_color='#ff9166',
                                 bg_color=color_bg, fg_color=color_bg, button_color='#ff9166', button_hover_color='#ffc8b3',
                                 dropdown_hover_color='#ffc8b3', dropdown_fg_color=color_bg, dropdown_text_color='#263238',
                                 text_color='#263238', font=font2, dropdown_font=font3, values=curr, state=NORMAL,justify="center", variable=currency_2, command=trace_to)
        combo_to.place(x=230, y=300)

        result_frm = CTkFrame(master, width=350, height=120, bg_color=color_bg, fg_color=color_bg, border_width=3, border_color='#ff9166', corner_radius=4).place(x=130, y=380)
        global lbl_curr_from, lbl_curr_to
        lbl_equal = CTkLabel(result_frm, text='=', font=font1, fg_color=color_bg, text_color='#263238')
        lbl_equal.place(x=300, y=420)

        lbl_curr_from = CTkLabel(result_frm, text='', fg_color=color_bg, text_color='#263238', font=font2)
        lbl_curr_from.place(x=180, y=400)
        lbl_curr_to = CTkLabel(result_frm, text='', fg_color=color_bg, text_color='#263238', font=font2)
        lbl_curr_to.place(x=380, y=400)

        global value_disp, result
        value_disp=CTkLabel(result_frm, text='', width=130,  fg_color=color_bg, bg_color=color_bg, text_color='#263238', font=font2)
        value_disp.place(x=150, y=450)
        result = CTkLabel(result_frm, text='', width=135, fg_color=color_bg, bg_color=color_bg, text_color='#263238', font=font2)
        result.place(x=330, y=450)

        hst_btn = CTkButton(master, text='History', width=100, height=25, font=font3, text_color='#263238', corner_radius=4,
                             border_width=2, border_color='#ff9166', border_spacing=10, bg_color=color_bg,
                             fg_color=color_bg, hover_color='#ffc8b3', command=history_cur).place(x=130, y=580)

        conv_btn = CTkButton(master, text='Convert', width=100, height=25, font=font3, text_color='#263238', corner_radius=4,
                             border_width=2, border_color='#ff9166', border_spacing=10, bg_color=color_bg, fg_color=color_bg,
                             hover_color='#ffc8b3', command=action).place(x=260, y=580)

        back_btn = CTkButton(master, text='Back', width=100, height=25, font=font3, text_color='#263238', corner_radius=4,
                             border_width=2, border_color='#ff9166', border_spacing=10, bg_color='transparent',
                             fg_color='transparent', hover_color='#ffc8b3', command=go_home).place(x=390, y=580)

        result.lift()
        lbl_curr_from.lift()
        lbl_curr_to.lift()
        value_disp.lift()
        lbl_equal.lift()

        master.mainloop()
