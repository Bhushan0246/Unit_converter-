'''from customtkinter import *
from PIL import Image
from tktooltip import ToolTip
from tkinter import *
import requests
import json'''
import json
import requests
from customtkinter import *
from tkinter import *

def liveRates():
    def get_live_rates():
        url = "https://live-metal-prices.p.rapidapi.com/v1/latest/XAU,XAG,PA,PL,GBP,EUR/INR"
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
            pound_price = float(rates['GBP'])
            euro_price = float(rates['EUR'])

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
            text_area.insert(END, f"Gold Price (XAU): {gold_price} ({profit_loss_percentage['XAU']:.2f}%) (24H)\n")
            text_area.insert(END, f"Silver Price (XAG): {silver_price} ({profit_loss_percentage['XAG']:.2f}%) (24H)\n")
            text_area.insert(END, f"Platinum Price (PA): {platinum_price} ({profit_loss_percentage['PA']:.2f}%) (24H)\n")
            text_area.insert(END, f"Palladium Price (PL): {palladium_price} ( {profit_loss_percentage['PL']:.2f}%) (24H)\n")
            text_area.insert(END, f"GBP to INR Exchange Rate: {pound_price}\n")
            text_area.insert(END, f"EUR to INR Exchange Rate: {euro_price}\n")
            text_area.config(state='disabled')
        else:
            text_area.config(state='normal')
            text_area.delete('1.0', END)
            text_area.insert(END, "Failed to retrieve data from API")
            text_area.config(state='disabled')

        #refreshes the rate after every 5 seconds
        master.after(500000000, display_rates)

    master = CTk()
    master.title("Live Rates")
    master.geometry("1000x700+400+60")
    master.wm_resizable(0, 0)
    master.configure(fg_color='#fff')
    color_bg = master.cget('background')

    custom_font = ("Arial", 14)

    text_area = Text(master, wrap='word', height=120, width=300, bg='white', fg='black', insertbackground='white',font=custom_font)
    text_area.pack(pady=0)
    text_area.config(state='disabled')


    display_rates()

    master.mainloop()

liveRates()
