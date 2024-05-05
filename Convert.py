from customtkinter import *
from PIL import Image
from tkinter import Canvas
import Categories

def convert_unit(con_unit):
        def back_page():
            master.destroy()
            Categories.category()

        master = CTk()
        master.title("Conversion Window")
        master.geometry("850x610+100+50")
        master.wm_resizable(0, 0)
        master.configure(fg_color='#fff')
        color_bg = master.cget('background')

        font1 = CTkFont('Monospace', 34, 'normal', underline=False, slant='italic')
        font2 = CTkFont('Monospace', 20, 'normal')
        font3 = CTkFont('Monospace', 16, 'normal', slant='italic')

        root_img = CTkImage(light_image = Image.open("./images/mg_units.png"), size=(400, 600))
        main_img = CTkLabel(master, text='', image=root_img)
        main_img.place(x=15, y=2)

        line1 = Canvas(master, width=2, height=720, highlightbackground=color_bg)
        line1.create_line(2, 0, 2, 750, fill='#263238', width=3, dash=(254,254))
        line1.place(x=540, y=10)

        label = CTkLabel(master, text="Converting " +con_unit, font = font1, text_color = '#34444c', width=415, height=60, fg_color='#C4E848')
        label.place(x=435,y = 8)

        from_label = CTkLabel(master, text = 'From', font = font2, text_color = '#263238')
        from_label.place(x = 500, y = 120)

        from_list = CTkComboBox(master, width = 200, corner_radius = 4, border_width = 3, border_color='#C4E848', fg_color = color_bg, bg_color = color_bg, button_hover_color='#EBFFA5',
                                     button_color='#C4E848',dropdown_fg_color=color_bg, dropdown_hover_color='#EBFFA5', dropdown_text_color='#263238', dropdown_font=font3, text_color='#263238', state=NORMAL)
        from_list.place(x = 580, y = 120)

        to_label = CTkLabel(master, text='To', font=font2, text_color='#263238')
        to_label.place(x=500, y=180)
        # value='', command='', variable=''  in combobox
        to_list = CTkComboBox(master, width = 200, corner_radius = 4, border_width = 3, border_color='#C4E848', fg_color = color_bg, bg_color = color_bg, button_hover_color='#EBFFA5',
                                     button_color='#C4E848',dropdown_fg_color=color_bg, dropdown_hover_color='#EBFFA5', dropdown_text_color='#263238', dropdown_font=font3, text_color='#263238', state=NORMAL)
        to_list.place(x=580, y=180)

        val_lbl = CTkLabel(master, text="Value", font=font2, text_color='#263238')
        val_lbl.place(x=500, y=240)

        val_inp = CTkEntry(master, width=200, corner_radius=4, border_width=3, border_color='#C4E848', placeholder_text='' ,font=font3, state=NORMAL, bg_color=color_bg, fg_color=color_bg)
        val_inp.place(x=580, y=240)

        val_out_lbl = CTkLabel(master, text="Result", font=font2, text_color='#263238')
        val_out_lbl.place(x=500, y=300)

        val_out = CTkEntry(master, width=200, corner_radius=4, border_width=3, border_color='#C4E848', font=font3, state=DISABLED, bg_color=color_bg, fg_color=color_bg,
                                text_color='#263238')
        val_out.place(x=580, y=300)

        con_btn = CTkButton(master, text='Convert', width=250, height=30, corner_radius=5, border_width=3, border_color='#C4E848', bg_color=color_bg, fg_color=color_bg, text_color='#263238',
                                 font=font2, hover_color=color_bg, state=NORMAL)
        con_btn.place(x=520, y=450)

        back_btn = CTkButton(master, text='Back', width=250, height=30, corner_radius=5, border_width=3, border_color='#C4E848', bg_color=color_bg, fg_color=color_bg, text_color='#263238',
                                 font=font2, hover_color=color_bg, state=NORMAL, command=back_page)
        back_btn.place(x=520, y=500)

        master.mainloop()

