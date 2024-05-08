from customtkinter import *
from PIL import Image
from tktooltip import ToolTip
from datetime import datetime
from tkinter import Canvas
from Shadow import *

def golive():
    def update_time():
        currernt_time = datetime.now().strftime('%H:%M:%S , %d %B %Y')
        time_lbl.configure(text=currernt_time, bg_color='#008080')
        root.after(1000, update_time)

    def get_live_rates():
        url = "https://live-metal-prices.p.rapidapi.com/v1/latest/XAU,XAG,PA,PL,INR"
        headers = {
            "X-RapidAPI-Key": "be0a6559b1msh266f58ebb076fc1p154ef8jsn295e92744e6f",
            "X-RapidAPI-Host": "live-metal-prices.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        print(response.text)  # Print response text
        if response.status_code == 200:
            data = json.loads(response.text)
            metal_prices = {}
            for metal, rate in data["rates"].items():
                metal_prices[metal] = rate
            return metal_prices
        else:
            return None

    def display_rates():
        # Define buying prices
        buying_prices = {
            'XAU': 194129.452393,  # Buying price for gold
            'XAG': 2285.461696,   # Buying price for silver
            'PA': 80342.497425,   # Buying price for platinum
            'PL': 81960.585182    # Buying price for palladium
        }

        rates = get_live_rates()
        if rates:
            gold_price = float(rates['XAU'])
            silver_price = float(rates['XAG'])
            platinum_price = float(rates['PA'])
            palladium_price = float(rates['PL'])

            # Calculate profit or loss as percentage
            profit_loss_percentage = {
                'XAU': ((gold_price - buying_prices['XAU']) / buying_prices['XAU']) * 100,
                'XAG': ((silver_price - buying_prices['XAG']) / buying_prices['XAG']) * 100,
                'PA': ((platinum_price - buying_prices['PA']) / buying_prices['PA']) * 100,
                'PL': ((palladium_price - buying_prices['PL']) / buying_prices['PL']) * 100
            }

            # Display metal prices and profit/loss percentage
            text_area.config(state='normal')
            text_area.delete('1.0', END)
            text_area.insert(END, f"Gold Price (XAU): {gold_price:.2f} ({profit_loss_percentage['XAU']:.2f}%) (24H)\n")
            text_area.insert(END, f"Silver Price (XAG): {silver_price:.2f} ({profit_loss_percentage['XAG']:.2f}%) (24H)\n")
            text_area.insert(END, f"Platinum Price (XPT): {platinum_price:.2f} ({profit_loss_percentage['PA']:.2f}%) (24H)\n")
            text_area.insert(END, f"Palladium Price (PL): {palladium_price:.2f} ( {profit_loss_percentage['PL']:.2f}%) (24H)\n")
            text_area.config(state='disabled')
        else:
            text_area.config(state='normal')
            text_area.delete('1.0', END)
            text_area.insert(END, "Failed to retrieve data from API")
            text_area.config(state='disabled')

        #refreshes the rate after every 5 seconds
        root.after((1000*120), display_rates)

    root = CTk()
    root.title("Live Rates")
    root.geometry("820x780+100+10")
    root.wm_resizable(0, 0)
    root.configure(fg_color='#F8F8FF')
    color_bg = root.cget('background')

    font1 = CTkFont('serif', 32, 'bold', underline=True, slant='italic')
    font2 = CTkFont('serif', 20, 'bold')
    font3 = CTkFont('serif', 19, 'normal', slant='italic')
    font4 = CTkFont('serif', 18, 'bold', 'italic')
    font5 = CTkFont('serif', 19, 'normal', slant='italic')

    header = CTkFrame(root, width=820, height=50, fg_color='#008080', corner_radius=0)
    header.pack()
    CTkLabel(header, text='Live Rates', fg_color='#008080', text_color='#FFFFF0', font=font1).place(x=15, y=8)

    india = CTkImage(light_image=Image.open("./images/india.png"), size=(50,40))
    india = CTkLabel(header, text='', fg_color='#008080', bg_color='#008080', image=india)
    india.place(x=520,y=8)
    ToolTip(india, msg="INDIA (IST)", delay=0.2)
    time_lbl = CTkLabel(header,text='', font=font2, fg_color='#008080', text_color='#FFFFF0')
    time_lbl.place(x=580, y=12)
    update_time()

    conv_img_back = CTkImage(light_image=Image.open("D:\PD\GUI\images\previous.png"), size=(32, 30))
    back = CTkButton(root, text='', fg_color=color_bg, border_spacing=3, corner_radius=50, image=conv_img_back,
                     height=30, width=32, border_width=2, border_color='#88dd88', command=backmain)
    ToolTip(back, msg="Back to Home", delay=0.5, bg='#fff')
    back.configure(hover_color=color_bg)
    back.place(x=720, y=10)

    # main content of the window describing the window containg image and a descriptive string
    str1 = "With this Real-time Metal price tracker, instantly access the live prices for some precious metals. It's a go to tool for instant updates on metal prices. \n\tStay ahead of market trends and make smart decisions with our last 24 hours profit and loss tracking feature."
    main_img = CTkImage(light_image=Image.open("./images/live_img.png"), size=(340,370))
    CTkLabel(root, text='', fg_color='transparent', image=main_img).place(x=470, y=50)

    detail = CTkTextbox(root, text_color="#333", font=font5, fg_color=color_bg, bg_color=color_bg, width=440, height=255, activate_scrollbars= False)
    detail.place(x=10, y=100)
    detail.insert("0.0", str1)
    detail.configure(wrap = 'word', state='disabled', spacing1 = 10, spacing2 = 12, spacing3 =5, exportselection=False)
    Shadow(detail, color='#404040', size=8, offset_x=8, offset_y= 8)
    # end main_content frame


    sub_content = CTkScrollableFrame(root, width=800, height=320, corner_radius=8, bg_color=color_bg, fg_color='#f2f2f2',border_width=2, border_color='#b3b3b3',
                                     scrollbar_fg_color='#f2f2f2', scrollbar_button_color='#30819c', scrollbar_button_hover_color='#30819c', orientation='horizontal')
    sub_content.place(x=0,y=430)
    CTkLabel(root, text='Metal Rates', fg_color=color_bg, font=font4, text_color='#263238', width=115, height=15).place(x=20, y=415)
    frm_color = sub_content.cget('fg_color')

    # Gold sub-frame
    XAU = CTkFrame(sub_content, width=250, height=300, border_width=3, corner_radius=5, fg_color='#f2f2f2', border_color='#F49C00')
    XAU.grid(row=0, column=0)
    CTkLabel(XAU, text='', fg_color=frm_color, image=CTkImage(light_image=Image.open("./images/gold.png"), size=(140,130))).place(x=60, y=10)
    CTkLabel(XAU, text='24 Carat Gold\t(XAU)', font=font5, fg_color = frm_color, width=240, text_color='#003B3B').place(x=5,y= 160)
    gold_rate = CTkLabel(XAU, text='', font=font5, fg_color=frm_color, width=240, text_color='#003B3B')
    gold_rate.place(x=5,y=210)
    gold_pl = CTkLabel(XAU, text='', font=font5, fg_color=frm_color, width=240)
    gold_pl.place(x=5,y=255)

    CTkFrame(sub_content, width=45, height=300, fg_color=frm_color).grid(row=0, column=1)

    # Silver sub-frame
    XAG = CTkFrame(sub_content, width=250, height=300, border_width=3, corner_radius=5, fg_color='#f2f2f2',
                   border_color='#F84E32')
    XAG.grid(row=0, column=2)
    CTkLabel(XAG, text='', fg_color=frm_color,
             image=CTkImage(light_image=Image.open("./images/silver.png"), size=(135, 120))).place(x=60, y=10)
    CTkLabel(XAG, text='Silver \t (XAG)', font=font5, fg_color=frm_color, width=240, text_color='#003B3B').place(x=5, y=160)
    silver_rate = CTkLabel(XAG, text='25.21  INR', font=font5, fg_color=frm_color, width=240, text_color='#003B3B')
    silver_rate.place(x=5, y=210)
    silver_pl = CTkLabel(XAG, text='8%\t(24 h)', font=font5, fg_color=frm_color, width=240, text_color='#003B3B')
    silver_pl.place(x=5, y=255)

    CTkFrame(sub_content, width=45, height=300, fg_color=frm_color).grid(row=0, column=3)

    # platinum sub-frame
    XPT = CTkFrame(sub_content, width=250, height=300, border_width=3, corner_radius=5, fg_color='#f2f2f2',
                   border_color='#F49C00')
    XPT.grid(row=0, column=4)
    CTkLabel(XPT, text='', fg_color=frm_color,
             image=CTkImage(light_image=Image.open("./images/platinum.png"), size=(135, 120))).place(x=60, y=10)
    CTkLabel(XPT, text='Platinum \t (XPT)', font=font5, fg_color=frm_color, width=240, text_color='#003B3B').place(x=5,
                                                                                                                 y=160)
    XPT_rate = CTkLabel(XPT, text='12225.21  INR', font=font5, fg_color=frm_color, width=240, text_color='#003B3B')
    XPT_rate.place(x=5, y=210)
    XPT_pl = CTkLabel(XPT, text='-2%\t(24 h)', font=font5, fg_color=frm_color, width=240, text_color='#003B3B')
    XPT_pl.place(x=5, y=255)

    CTkFrame(sub_content, width=45, height=300, fg_color=frm_color).grid(row=0, column=5)

    # palladium sub-frame
    XPD = CTkFrame(sub_content, width=250, height=300, border_width=3, corner_radius=5, fg_color='#f2f2f2',
                   border_color='#F84E32')
    XPD.grid(row=0, column=6)
    CTkLabel(XPD, text='', fg_color=frm_color,
             image=CTkImage(light_image=Image.open("./images/palladium.png"), size=(135, 120))).place(x=60, y=10)
    CTkLabel(XPD, text='Palladium \t (XPD)', font=font5, fg_color=frm_color, width=240, text_color='#003B3B').place(x=5,
                                                                                                                   y=160)
    XPD_rate = CTkLabel(XPD, text='897.77  INR', font=font5, fg_color=frm_color, width=240, text_color='#003B3B')
    XPD_rate.place(x=5, y=210)
    XPD_pl = CTkLabel(XPD, text='0%\t(24 h)', font=font5, fg_color=frm_color, width=240, text_color='#003B3B')
    XPD_pl.place(x=5, y=255)
    # name, rate, p&L, photo

    root.mainloop()


golive()
