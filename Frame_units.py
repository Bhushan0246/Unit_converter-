from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tktooltip import ToolTip

class Frame_units:
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x650+100+50')
        self.root.wm_title('Categories')
        self.root.wm_resizable(0, 0)
        self.root.configure(fg_color='#e5f2ff')
        color_bg = root.cget('background')

        font1 = CTkFont('Monospace', 34, 'normal', underline=True, slant='italic')
        font2 = CTkFont('Monospace', 20, 'bold')
        font3 = CTkFont('Monospace', 16, 'normal', slant='italic')

        img = Image.open(".\images\img_units.png")
        res = img.resize((980, 760), Image.FASTOCTREE)
        self.main_img = CTkLabel(root, text='', image=ImageTk.PhotoImage(res))
        self.main_img.place(x=5, y=10)

        img = Image.open(".\images\previous.png")
        res = img.resize((32,30), Image.FASTOCTREE)
        conv_img_back = ImageTk.PhotoImage(res)
        self.back = CTkButton(root,text='', fg_color=color_bg, border_spacing=3, corner_radius=50, image=conv_img_back,
                         height=30, width=32, border_width=3, border_color='#88dd88')
        ToolTip(self.back, msg="Back to Home", delay=0.5, bg='#fff')
        self.back.configure(hover_color = color_bg)
        self.back.place(x=720, y=10)

        self.desp = CTkLabel(root, text = 'Choose a unit converting category', font=font3, text_color='#404040')
        self.desp.place(x=70, y=18)

        self.len = CTkButton(root, text='Length', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120, hover_color='#169c95')
        self.len.place(x=22, y=190)

        self.wht = CTkButton(root, text='Weight', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120)
        self.wht.place(x=210, y=190)

        self.area = CTkButton(root, text='Area', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120, hover_color='#169c95')
        self.area.place(x=395, y=190)

        self.time = CTkButton(root, text='Time', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120)
        self.time.place(x=20, y=360)

        self.vol = CTkButton(root, text='Volume', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120, hover_color='#169c95')
        self.vol.place(x=210, y=360)

        self.temp = CTkButton(root, text='Temperature', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120)
        self.temp.place(x=385, y=360)

        self.ang = CTkButton(root, text='Angle', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120, hover_color='#169c95')
        self.ang.place(x=20, y=525)

        self.prs = CTkButton(root, text='Pressure', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120)
        self.prs.place(x=210, y=525)


if __name__ == "__main__":
    root = CTk()
    frame = Frame_units(root)
    root.mainloop()
