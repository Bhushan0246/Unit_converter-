from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import Categories
import AboutUs
import convertcurrency

class Main_frame:
    def unit_page(self):
        self.main.destroy()
        Categories.category()

    def about_page(self):
        self.main.destroy()
        AboutUs.about()

    def curr_page(self):
        self.main.destroy()
        convertcurrency.currency()

    def __init__(self, main):
        self.main = main
        self.main.geometry('825x600+100+50')
        self.main.wm_title('Live Rates')
        self.main.wm_resizable(0, 0)
        self.main.configure(fg_color='#e6ffe6')

        font1 = CTkFont('Monospace', 34, 'normal', underline=True, slant='italic')
        font2 = CTkFont('Monospace', 20, 'normal')
        font3 = CTkFont('Monospace', 16, 'normal')

        self.ttl = CTkLabel(main, text='Live Rates', font=font1, text_color='#404040')
        self.ttl.place(x=350, y=20)

        img = CTkImage(light_image=Image.open("D:\PD\GUI\images\mainframe_img.png"), size=(480,500))
        self.main_img = CTkLabel(main, text='', image=img)
        self.main_img.place(x=15, y=100)

        conv_img1 = CTkImage(light_image = Image.open("D:\PD\GUI\images\conversion.png"), size=(90,60))
        self.btn1 = CTkButton(main, text=' Units', fg_color=main.cget('background'), font=font2, border_width=2, border_color='#000', border_spacing=3,
                         corner_radius=7, text_color='#000', image=conv_img1, hover_color='#c0f2c0', height=70, width=220, command=self.unit_page)
        self.btn1.place(x=580, y=110)

        conv_img2 = CTkImage(light_image=Image.open("D:\PD\GUI\images\currency-conversion.png"), size=(100, 80))
        self.btn2 = CTkButton(main, text=' Currency', fg_color=main.cget('background'), font=font2, border_width=2, border_color='#000', border_spacing=3,
                         corner_radius=7, text_color='#000', image = conv_img2, hover_color='#c0f2c0', height=70, width=220, command=self.curr_page)
        self.btn2.place(x=520, y=225)

        conv_img3 = CTkImage(light_image = Image.open("D:\PD\GUI\images\live_rates.png"), size=(90,70))
        self.btn3 = CTkButton(main, text=' Live rate', fg_color=main.cget('background'), font=font2, border_width=2, border_color='#000', border_spacing=3,
                         corner_radius=7, text_color='#000', image=conv_img3, hover_color='#c0f2c0', height=70, width=220)
        self.btn3.place(x=580, y=340)

        conv_img4 = CTkImage(light_image=Image.open("D:\PD\GUI\images\employees.png"), size=(90,70))
        self.btn4 = CTkButton(main, text=' About us', fg_color=main.cget('background'), font=font2, border_width=2, border_color='#000', border_spacing=3,
                         corner_radius=7, text_color='#000', image=conv_img4, hover_color='#c0f2c0', height=70, width=220, command=self.about_page)
        self.btn4.place(x=520, y=455)


#-------------------- ----------------------- ----------------------- ------------------------ ----------------------
if __name__ == "__main__":
    main = CTk()
    obj = Main_frame(main)
    main.mainloop()
