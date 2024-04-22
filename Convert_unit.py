from customtkinter import *
from PIL import Image, ImageTk
from tkinter import Canvas

class Convert_unit:
    def __init__(self, master, con_unit):
        self.master = master
        self.master.title("Conversion Window")
        self.master.geometry("850x600+100+50")
        self.master.wm_resizable(0, 0)
        self.master.configure(fg_color='#fff')
        color_bg = root.cget('background')

        font1 = CTkFont('Monospace', 34, 'normal', underline=True, slant='italic')
        font2 = CTkFont('Monospace', 20, 'normal')
        font3 = CTkFont('Monospace', 16, 'normal', slant='italic')

        img = Image.open(".\images\convert_img.png")
        res = img.resize((500, 750), Image.FASTOCTREE)
        main_img = CTkLabel(master, text='', image=ImageTk.PhotoImage(res))
        main_img.place(x=15, y=0)

        self.line1 = Canvas(master, width=2, height=710)
        self.line1.create_line(2, 0, 2, 750, fill='#263238', width=3, dash=(254,254))
        self.line1.place(x=540, y=10)

        self.label = CTkLabel(master, text="Converting " + con_unit, font = font1, text_color = '#263238')
        self.label.place(x=500,y = 10)

        self.from_label = CTkLabel(master, text = 'From', font = font2, text_color = '#263238')
        self.from_label.place(x = 500, y = 120)

        self.from_list = CTkComboBox(master, width = 200, corner_radius = 4, border_width = 3, border_color='#C4E848', fg_color = color_bg, bg_color = color_bg, button_hover_color='#EBFFA5',
                                     button_color='#C4E848',dropdown_fg_color=color_bg, dropdown_hover_color='#EBFFA5', dropdown_text_color='#263238', dropdown_font=font3, text_color='#263238', state=NORMAL)
        self.from_list.place(x = 580, y = 120)

        self.to_label = CTkLabel(master, text='To', font=font2, text_color='#263238')
        self.to_label.place(x=500, y=180)
        # value='', command='', variable=''  in combobox
        self.to_list = CTkComboBox(master, width = 200, corner_radius = 4, border_width = 3, border_color='#C4E848', fg_color = color_bg, bg_color = color_bg, button_hover_color='#EBFFA5',
                                     button_color='#C4E848',dropdown_fg_color=color_bg, dropdown_hover_color='#EBFFA5', dropdown_text_color='#263238', dropdown_font=font3, text_color='#263238', state=NORMAL)
        self.to_list.place(x=580, y=180)

        self.val_lbl = CTkLabel(master, text="Value", font=font2, text_color='#263238')
        self.val_lbl.place(x=500, y=240)

        self.val_inp = CTkEntry(master, width=200, corner_radius=4, border_width=3, border_color='#C4E848', placeholder_text='' ,font=font3, state=NORMAL, bg_color=color_bg, fg_color=color_bg)
        self.val_inp.place(x=580, y=240)

        self.val_out_lbl = CTkLabel(master, text="Result", font=font2, text_color='#263238')
        self.val_out_lbl.place(x=500, y=300)

        self.val_out = CTkEntry(master, width=200, corner_radius=4, border_width=3, border_color='#C4E848', font=font3, state=DISABLED, bg_color=color_bg, fg_color=color_bg,
                                text_color='#263238')
        self.val_out.place(x=580, y=300)

        self.con_btn = CTkButton(master, text='Convert', width=250, height=30, corner_radius=5, border_width=3, border_color='#C4E848', bg_color=color_bg, fg_color=color_bg, text_color='#263238',
                                 font=font2, hover_color=color_bg, state=NORMAL)
        self.con_btn.place(x=520, y=400)

        def back():
            master.destroy()
            import frame_units

        self.con_btn = CTkButton(master, text='Back', width=250, height=30, corner_radius=5, border_width=3, border_color='#C4E848', bg_color=color_bg, fg_color=color_bg, text_color='#263238',
                                 font=font2, hover_color=color_bg, state=NORMAL, command=self.back)
        self.con_btn.place(x=520, y=450)

    def back(self):
        self.master.destroy()
        
master = CTk()
my_frame = Convert_unit(master, 'category')
master.mainloop()