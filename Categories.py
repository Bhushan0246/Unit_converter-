from tkinter import *
from customtkinter import *
from PIL import Image
from tktooltip import ToolTip
import Main_window
import Convert
import History_frm

def category():

        def backmain():
            root.destroy()
            temp = CTk()
            new_win = Main_window.Main_frame(temp)
            temp.mainloop()

        def length():
            root.destroy()
            Convert.convert_unit('Length')
        def weight():
            root.destroy()
            Convert.convert_unit('Weight')
        def area():
            root.destroy()
            Convert.convert_unit('Area')
        def time():
            root.destroy()
            Convert.convert_unit('Length')
        def volume():
            root.destroy()
            Convert.convert_unit('Volume')
        def temperature():
            root.destroy()
            Convert.convert_unit('Temperature')
        def angle():
            root.destroy()
            Convert.convert_unit('Angle')
        def pressure():
            root.destroy()
            Convert.convert_unit('Pressure')
        def history_page():
            root.destroy()
            History_frm.openHistory()


        root = CTk()
        root.geometry('800x650+100+50')
        root.wm_title('Categories')
        root.wm_resizable(0, 0)
        root.configure(fg_color='#e5f2ff')
        color_bg = root.cget('background')

        font1 = CTkFont('Monospace', 34, 'normal', underline=True, slant='italic')
        font2 = CTkFont('Monospace', 20, 'bold')
        font3 = CTkFont('Monospace', 16, 'normal', slant='italic')

        img_main = CTkImage(light_image=Image.open("D:\PD\GUI\images\img_units.png"), size=(780,620))
        main_img = CTkLabel(root, text='', image=img_main)
        main_img.place(x=5, y=10)

        conv_img_back = CTkImage(light_image=Image.open("D:\PD\GUI\images\previous.png"), size = (32,30))
        back = CTkButton(root,text='', fg_color=color_bg, border_spacing=3, corner_radius=50, image=conv_img_back,
                         height=30, width=32, border_width=2, border_color='#88dd88', command=backmain)
        ToolTip(back, msg="Back to Home", delay=0.5, bg='#fff')
        back.configure(hover_color = color_bg)
        back.place(x=720, y=10)

        desp = CTkLabel(root, text = 'Choose a unit converting category', font=font3, text_color='#404040')
        desp.place(x=70, y=18)

        len = CTkButton(root, text='Length', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3, corner_radius=10,
                             height=30, width=120, hover_color='#169c95', command=length)
        len.place(x=22, y=190)

        wht = CTkButton(root, text='Weight', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120, command=weight)
        wht.place(x=210, y=190)

        ara = CTkButton(root, text='Area', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120, hover_color='#169c95', command=area)
        ara.place(x=395, y=190)

        tim = CTkButton(root, text='Time', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120, command=time)
        tim.place(x=20, y=365)

        vol = CTkButton(root, text='Volume', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120, hover_color='#169c95', command=volume)
        vol.place(x=210, y=365)

        temp = CTkButton(root, text='Temperature', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3, corner_radius=10, height=30, width=120, command=temperature)
        temp.place(x=385, y=365)

        ang = CTkButton(root, text='Angle', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120, hover_color='#169c95', command=angle)
        ang.place(x=20, y=535)

        prs = CTkButton(root, text='Pressure', fg_color = color_bg, font=font2, text_color= '#DD8487', border_spacing=3,
                         corner_radius=10, height=30, width=120, command=pressure)
        prs.place(x=210, y=535)

        his = CTkButton(root, text='History', fg_color=color_bg, font=font2, text_color='#DD8487', border_spacing=3,
                        corner_radius=10, height=30, width=120, hover_color='#169c95', command=history_page)
        his.place(x=395, y=535)

        root.mainloop()
