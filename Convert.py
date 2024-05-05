from customtkinter import *
from PIL import Image
from tkinter import Canvas
from tktooltip import ToolTip
import Categories

def convert_unit(con_unit):
        def back_page():
            master.destroy()
            Categories.category()

        def action():
                var1 = val_inp.get()
                var2 = from_list.get()
                var3 = to_list.get()

        master = CTk()
        master.title("Conversion Window")
        master.geometry("850x610+100+50")
        master.wm_resizable(0, 0)
        master.configure(fg_color='#fff')
        color_bg = master.cget('background')

        font1 = CTkFont('Monospace', 34, 'normal', underline=False, slant='italic')
        font2 = CTkFont('Monospace', 20, 'normal')
        font3 = CTkFont('Monospace', 18, 'normal', slant='italic')

        root_img = CTkImage(light_image = Image.open("./images/mg_units.png"), size=(400, 600))
        main_img = CTkLabel(master, text='', image=root_img)
        main_img.place(x=15, y=2)

        line1 = Canvas(master, width=2, height=720, highlightbackground=color_bg)
        line1.create_line(2, 0, 2, 750, fill='#263238', width=3, dash=(254,254))
        line1.place(x=540, y=10)

        label = CTkLabel(master, text="Converting "+con_unit, font = font1, text_color = '#34444c', width=415, height=60, fg_color='#C4E848')
        label.place(x=435,y = 8)

        from_label = CTkLabel(master, text = 'From', font = font2, text_color = '#263238')
        from_label.place(x = 500, y = 120)

        var1 = IntVar()
        var2 = StringVar(value='- -- -- -')
        var3 = StringVar(value='- -- -- -')
        # Adding units for respective category in Combobox
        conv_units = []
        if (con_unit == 'Length'):
                conv_units=['Kilometer (km)', 'Meter (m)', 'Millimeter (mm)', 'Foot (ft)', 'Centimeter (cm)', 'Inch (in)', 'Yard (yd)', 'Mile (mile)', 'Micrometer (micron)']
        elif (con_unit == 'Weight'):
                conv_units = ['Kilogram (kg)', 'Gram (g)', 'Milligram (mg)', 'Tonne (t)', 'Megatonne (Mg)', 'Pound (Ibs)']
        elif (con_unit == 'Area'):
                conv_units = ['Sq. Meter', 'Sq. Kilometer', 'Sq. Mile', 'Sq. Foot', 'Sq. Inch', 'Sq Hectare']
        elif (con_unit == 'Volume'):
                conv_units = ['Litre (l)', 'Millilitre (ml)', 'Gallon ()', 'Cubic Metre', 'Cubic Foot', 'Cubic Inch', 'Cubic Centimeter']
        elif (con_unit == 'Temperature'):
                conv_units = ['Celsius (C)', 'Kelvin (K)', 'Fahrenheit (F)', 'Rankine (Ra)']
        elif (con_unit == 'Angle'):
                conv_units =['Radian', 'Degree', 'Seconds', 'Minutes']
        elif (con_unit == 'Time'):
                conv_units = ['Century', 'Decade', 'Year', 'Month', 'Week', 'Day', 'Hour', 'Minute', 'Second', 'Millisecond']
        elif (con_unit == 'Pressure'):
                conv_units = ['Bar', 'Pascal', 'Torr', 'Atmosphere']
        else :
                conv_units =['- - -']

        from_list = CTkComboBox(master, width = 200, corner_radius = 4, border_width = 3, border_color='#C4E848', fg_color = color_bg, bg_color = color_bg, button_hover_color='#EBFFA5',
                                     button_color='#C4E848',dropdown_fg_color=color_bg, dropdown_hover_color='#EBFFA5', dropdown_text_color='#263238', dropdown_font=font3,
                                text_color='#263238', state=NORMAL, values=conv_units, variable=var2)
        from_list.place(x = 580, y = 120)

        img = CTkImage(Image.open('.\images\swap.png'), size=(30, 20))
        swap_btn = CTkButton(master, text='', width=30, height=20, image=img, corner_radius=4, border_width=3,
                             border_color='#C4E848', fg_color=color_bg, state=NORMAL)
        ToolTip(swap_btn, msg="Swap unit", delay=0.3, bg='#fff')
        swap_btn.configure(hover_color='#EBFFA5')
        swap_btn.place(x=650, y=170)

        to_label = CTkLabel(master, text='To', font=font2, text_color='#263238')
        to_label.place(x=500, y=220)
        # command='', variable=''  in combobox
        to_list = CTkComboBox(master, width = 200, corner_radius = 4, border_width = 3, border_color='#C4E848', fg_color = color_bg, bg_color = color_bg, button_hover_color='#EBFFA5',
                                     button_color='#C4E848',dropdown_fg_color=color_bg, dropdown_hover_color='#EBFFA5', dropdown_text_color='#263238', dropdown_font=font3,
                              text_color='#263238', state=NORMAL, values=conv_units, variable=var3)
        to_list.place(x=580, y=220)

        val_lbl = CTkLabel(master, text="Value", font=font2, text_color='#263238')
        val_lbl.place(x=500, y=280)

        val_inp = CTkEntry(master, width=200, corner_radius=4, border_width=3, border_color='#C4E848', placeholder_text='- - -' ,font=font3, state=NORMAL,
                           bg_color=color_bg, fg_color=color_bg, textvariable=var1)
        val_inp.place(x=580, y=280)

        val_out_lbl = CTkLabel(master, text="Result", font=font2, text_color='#263238')
        val_out_lbl.place(x=500, y=340)

        val_out = CTkEntry(master,width=200, corner_radius=4, border_width=3, border_color='#C4E848', font=font3, state=DISABLED, bg_color=color_bg, fg_color=color_bg,
                                text_color='#263238')
        val_out.place(x=580, y=340)

        con_btn = CTkButton(master, text='Convert', width=250, height=30, corner_radius=5, border_width=3, border_color='#C4E848', bg_color=color_bg, fg_color=color_bg, text_color='#263238',
                                 font=font2, hover_color='#EBFFA5', state=NORMAL, command=action)
        con_btn.place(x=520, y=450)

        back_btn = CTkButton(master, text='Back', width=250, height=30, corner_radius=5, border_width=3, border_color='#C4E848', bg_color=color_bg, fg_color=color_bg, text_color='#263238',
                                 font=font2, hover_color='#EBFFA5', state=NORMAL, command=back_page)
        back_btn.place(x=520, y=500)

        master.mainloop()
