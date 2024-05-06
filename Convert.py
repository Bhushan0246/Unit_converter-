from customtkinter import *
from CTkMessagebox import *
from PIL import Image
from tkinter import Canvas
from tktooltip import ToolTip
import mysql.connector
import Categories
from datetime import datetime

def convert_unit(con_unit):
    def back_page():
        master.destroy()
        Categories.category()

    def swap_unit():
        var2 = from_list.get()
        from_list.set(to_list.get())
        to_list.set(var2)

    def action():
        var1 = val_inp.get()
        var2 = from_list.get()
        var3 = to_list.get()

        if con_unit == 'Temperature':
            if var2 == 'Celsius':   # from celsius
                converted = float(var1)
                if var3 == 'Kelvin':
                    converted = float(var1) + 273.15
                elif var3 == 'Fahrenheit':
                    converted = (float(var1) * 1.8) + 32
                elif var3 == 'Rankine':
                    converted = float(var1) * 1.8 + 493.47
            elif var2 == 'Kelvin':  # from Kelvin
                converted = float(var1)
                if var3 == 'Celsius':
                    converted = float(var1) - 273.15
                elif var3 == 'Fahrenheit':
                    converted = (float(var1)-273.15) * 1.8 + 32
                elif var3 == 'Rankine':
                    converted = float(var1) * 1.8
            elif var2 == 'Fahrenheit':  # from Fahrenheit
                converted = float(var1)
                if var3 == 'Celsius':
                    converted = (float(var1)-32) * 0.555
                elif var3 == 'Kelvin':
                    converted = (float(var1)-32) * 0.555 + 273.15
                elif var3 == 'Rankine':
                    converted = float(var1) + 459.67
            else:                       # from Rankine
                converted = float(var1)
                if var3 == 'Celsius':
                    converted = (float(var1)-491.67) * 0.555
                elif var3 == 'Fahrenheit':
                    converted = (float(var1) - 459.67)
                elif var3 == 'Kelvin':
                    converted = (float(var1) * 0.555)

        # converting units other than temperatures
        else:
            std = float(var1) / conv_factor[var2]
            converted = std * conv_factor[var3]

        #   Round off to 8 decimal places and display result
        rounded = round(converted, 8)
        val_out.configure(text=rounded)

        # quries to write tuples in database for history
        stamp = datetime.now().strftime("%X, " + "%x")
        try:
            mydb = mysql.connector.connect(host='localhost', user='root', password='mysql@123456', database='converter')
            mycur = mydb.cursor()
            query = "INSERT INTO unit_history(on_date, from_unit, to_unit, from_value, to_value) VALUES (%s,%s,%s,%s,%s)"
            qvalue = (stamp, var2, var3, var1, rounded)
            mycur.execute(query, qvalue)
            mydb.commit()
        except:
            CTkMessagebox(master, title='Error', message="Action can't be registered into history!",
                              icon='cancel', border_width=2, fg_color=color_bg, bg_color=color_bg,
                              text_color='#263238', corner_radius=10, fade_in_duration=1, sound=True)

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
    temp_factor={}
    conv_factor={}
    if (con_unit == 'Length'):
        conv_units= ['Meter', 'Kilometer', 'Millimeter', 'Foot', 'Centimeter', 'Inch', 'Yard', 'Mile', 'Micrometer']
        conv_factor={'Meter':1, 'Kilometer': 0.001, 'Millimeter':1000, 'Foot':3.281, 'Centimeter':100, 'Inch':39.37,
                     'Yard':1.094, 'Mile':0.00062137}
    elif (con_unit == 'Weight'):
        conv_units = ['Kilogram', 'Gram', 'Milligram', 'Tonne', 'Megatonne', 'Pound', 'Ounce']
        conv_factor={'Kilogram':1, 'Gram':1000, 'Milligram':1000000, 'Tonne':0.001, 'Pound':2.20462, 'Ounce':35.2739}
    elif (con_unit == 'Area'):
        conv_units = ['Sq. Kilometer', 'Sq. Meter', 'Sq. Mile', 'Sq. Foot', 'Sq. Inch', 'Sq Hectare']
        conv_factor={'Sq. Kilometer':1, 'Sq. Meter':1000000, 'Sq. Mile':0.38610, 'Sq. Foot':10763910, 'Sq. Inch':1550003100, 'Sq Hectare':100}
    elif (con_unit == 'Volume'):
        conv_units = ['Litre', 'Millilitre', 'Gallon', 'Cubic Metre', 'Cubic Foot', 'Cubic Inch', 'Cubic Centimeter']
        conv_factor={'Litre':1, 'Millilitre':1000, 'Gallon':0.21997, 'Cubic Metre':0.001, 'Cubic Foot':0.035315, 'Cubic Inch':61.0237, 'Cubic Centimeter':1000}
    elif (con_unit == 'Temperature'):
        conv_units = ['Celsius', 'Kelvin', 'Fahrenheit', 'Rankine']
    elif (con_unit == 'Angle'):
        conv_units =['Radian', 'Degree', 'Arcseconds', 'Minute of arc']
        conv_factor={'Radian':1, 'Degree':57.296, 'Arcseconds':206264.806, 'Minute of arc':10313.2}
    elif (con_unit == 'Time'):
        conv_units = ['Day', 'Decade', 'Year', 'Month', 'Week', 'Hour', 'Minute', 'Second', 'Millisecond']
        conv_factor={'Day':1, 'Decade':0.000273973, 'Year':0.00273973, 'Month':0.0328767, 'Week':0.142857, 'Hour':24, 'Minute':1440, 'Second':86400, 'Millisecond':86400000}
    elif (con_unit == 'Pressure'):
        conv_units = ['Pascal', 'Bar', 'Torr', 'Atmosphere']
        conv_factor = {'Pascal':1, 'Bar':0.00001, 'Torr':0.00750062, 'Atmosphere':0.0000098692}
    else :
        conv_units =[' - - -']

    from_list = CTkComboBox(master, width = 220, height=35,corner_radius = 4, border_width = 3, border_color='#C4E848', fg_color = color_bg, bg_color = color_bg, button_hover_color='#EBFFA5',
                            button_color='#C4E848',dropdown_fg_color=color_bg, dropdown_hover_color='#EBFFA5', dropdown_text_color='#263238', dropdown_font=font3,
                            font=font3,text_color='#263238', state=NORMAL, values=conv_units, variable=var2)
    from_list.place(x = 580, y = 120)

    img = CTkImage(Image.open('.\images\swap.png'), size=(30, 20))
    swap_btn = CTkButton(master, text='', width=30, height=20, image=img, corner_radius=4, border_width=3,
                         border_color='#C4E848', fg_color=color_bg, state=NORMAL, command=swap_unit)
    ToolTip(swap_btn, msg="Swap unit", delay=0.3, bg='#fff')
    swap_btn.configure(hover_color='#EBFFA5')
    swap_btn.place(x=650, y=170)

    to_label = CTkLabel(master, text='To', font=font2, text_color='#263238')
    to_label.place(x=500, y=220)
    # command='', variable=''  in combobox
    to_list = CTkComboBox(master, width = 220, height=35,corner_radius = 4, border_width = 3, border_color='#C4E848', fg_color = color_bg, bg_color = color_bg, button_hover_color='#EBFFA5',
                          button_color='#C4E848',dropdown_fg_color=color_bg, dropdown_hover_color='#EBFFA5', dropdown_text_color='#263238', dropdown_font=font3,
                          font=font3,text_color='#263238', state=NORMAL, values=conv_units, variable=var3)
    to_list.place(x=580, y=220)

    val_lbl = CTkLabel(master, text="Value", font=font2, text_color='#263238')
    val_lbl.place(x=500, y=280)

    val_inp = CTkEntry(master, width=220, height=35, corner_radius=4, border_width=3, border_color='#C4E848', placeholder_text=' - - -' ,font=font3, state=NORMAL,
                       bg_color=color_bg, fg_color=color_bg, textvariable=var1, text_color='#263238')
    val_inp.place(x=580, y=280)

    val_out_lbl = CTkLabel(master, text="Result", font=font2, text_color='#263238')
    val_out_lbl.place(x=500, y=340)

    val_frame = CTkFrame(master, width=220, height=35,corner_radius=4, border_width=3, border_color='#C4E848', bg_color=color_bg, fg_color=color_bg)
    val_frame.place(x=580, y=340)
    val_out = CTkLabel(master, text='', width=210, font=font3, bg_color="transparent", fg_color="transparent", text_color='#263238',)
    val_out.place(x=583, y=343)

    con_btn = CTkButton(master, text='Convert', width=250, height=30, corner_radius=5, border_width=3, border_color='#C4E848', bg_color=color_bg, fg_color=color_bg, text_color='#263238',
                        font=font2, hover_color='#EBFFA5', state=NORMAL, command=action)
    con_btn.place(x=520, y=450)

    back_btn = CTkButton(master, text='Back', width=250, height=30, corner_radius=5, border_width=3, border_color='#C4E848', bg_color=color_bg, fg_color=color_bg, text_color='#263238',
                         font=font2, hover_color='#EBFFA5', state=NORMAL, command=back_page)
    back_btn.place(x=520, y=500)

    master.mainloop()
