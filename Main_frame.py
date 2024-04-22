from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from Frame_units import Frame_units
class Main_frame:
    def __init__(self, main):
        self.main = main
        self.main.geometry('825x600+100+50')
        self.main.wm_title('Converter')
        self.main.wm_resizable(0, 0)
        self.main.configure(fg_color='#e6ffe6')

        font1 = CTkFont('Monospace', 34, 'normal', underline=True, slant='italic')
        font2 = CTkFont('Monospace', 20, 'normal')
        font3 = CTkFont('Monospace', 16, 'normal')

        self.ttl = CTkLabel(main, text='Converter', font=font1, text_color='#404040')
        self.ttl.place(x=350, y=20)

        img = Image.open(".\images\mainframe_img.png")
        res = img.resize((550, 600), Image.FASTOCTREE)
        self.main_img = CTkLabel(main, text='', image=ImageTk.PhotoImage(res))
        self.main_img.place(x=15, y=100)

        img = Image.open(".\images\conversion.png")
        res = img.resize((90,60), Image.FASTOCTREE)
        conv_img1 = ImageTk.PhotoImage(res)
        self.btn1 = CTkButton(main, text=' Units', fg_color=main.cget('background'), font=font2, border_width=2, border_color='#000', border_spacing=3,
                         corner_radius=7, text_color='#000', image=conv_img1, hover_color='#c0f2c0', height=70, width=220, command=self.unit_page)
        self.btn1.place(x=580, y=110)

        img = Image.open(".\images\currency-conversion.png")
        res = img.resize((100,80), Image.FASTOCTREE)
        conv_img2 = ImageTk.PhotoImage(res)
        self.btn2 = CTkButton(main, text=' Currency', fg_color=main.cget('background'), font=font2, border_width=2, border_color='#000', border_spacing=3,
                         corner_radius=7, text_color='#000', image = conv_img2, hover_color='#c0f2c0', height=70, width=220)
        self.btn2.place(x=520, y=225)

        img = Image.open(".\images\live_rates.png")
        res = img.resize((90,70), Image.FASTOCTREE)
        conv_img3 = ImageTk.PhotoImage(res)
        self.btn3 = CTkButton(main, text=' Live rate', fg_color=main.cget('background'), font=font2, border_width=2, border_color='#000', border_spacing=3,
                         corner_radius=7, text_color='#000', image=conv_img3, hover_color='#c0f2c0', height=70, width=220)
        self.btn3.place(x=580, y=340)

        img = Image.open(".\images\employees.png")
        res = img.resize((90,70), Image.FASTOCTREE)
        conv_img4 = ImageTk.PhotoImage(res)
        self.btn4 = CTkButton(main, text=' About us', fg_color=main.cget('background'), font=font2, border_width=2, border_color='#000', border_spacing=3,
                         corner_radius=7, text_color='#000', image=conv_img4, hover_color='#c0f2c0', height=70, width=220)
        self.btn4.place(x=520, y=455)

    def unit_page(self):
        self.main.quit()


-------------------- ----------------------- ----------------------- ------------------------ ----------------------
if __name__ == "__main__":
    main = CTk()
    obj = Main_frame(main)
    main.mainloop()