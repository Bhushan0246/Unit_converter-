from customtkinter import *
from PIL import Image, ImageTk
from tkinter import Canvas
import mysql.connector
import Categories

def openHistory():
    def go_back():
        root.destroy()
        Categories.category()

    root = CTk()
    root.geometry('850x610+100+50')
    root.wm_title('History')
    root.wm_resizable(0, 0)
    root.configure(fg_color='#fff')
    color_bg = root.cget('background')

    font1 = CTkFont('Monospace', 34, 'normal', underline=False, slant='italic')
    font2 = CTkFont('Monospace', 19, 'normal')
    font3 = CTkFont('Monospace', 16, 'normal', slant='italic')

    img = CTkImage(light_image = Image.open(".\images\history_img.png"), size=(240,525))
    main_img = CTkLabel(root, text='', image=img)
    main_img.place(x=608, y=10)

    title = CTkLabel(root, text=' History ', font=font1, text_color='#78ba80')
    title.place(x=235, y=15)

    back_btn = CTkButton(root, text='Back', width=220, height=30, corner_radius=5, border_width=2, border_color='#95C89B', bg_color=color_bg, fg_color=color_bg, text_color='#95C89B',
                                  font=font2, hover_color=color_bg, state=NORMAL, command=go_back)
    back_btn.place(x=612, y=550)

    heading = " Date-Time\tFrom \t  To\t    Value \t          Result"
    sbfrm = CTkScrollableFrame(root, width=570, height=460, corner_radius=8, border_width=1, bg_color='#C3E4C0', fg_color='#C3E4C0', scrollbar_fg_color='#C3E4C0', scrollbar_button_color='#ddeedf',
                                        scrollbar_button_hover_color='#DBF9DF', orientation="vertical", label_text=heading, label_font=font2, label_anchor="sw", label_text_color='#263238',
                               label_fg_color='#C3E4C0')
    sbfrm.place(x=2, y=70)

    #   Database connection and fetching goes here
    try:
        mydb = mysql.connector.connect(host='localhost', user='root', password='mysql@123456', database='converter')
        mycur = mydb.cursor()
        query = "SELECT * FROM unit_history"
        mycur.execute(query)
        ndata = mycur.fetchall()
        mycur.execute("SELECT * FROM unit_history")
        i = 0
    #   Heading buttons for data entries
        for student in mycur:
            for j in range(len(student)):
                e = CTkButton(sbfrm, width=100, height=20, text_color='#263238', font=font3, border_width=1, border_color='#C3E4C0', fg_color=color_bg, state=NORMAL, hover=False)
                e.configure(text=student[j])
                if (j == 0):
                    e.configure(width=160)
                    e.grid(row=(i+1), column=j)
                else:
                    e.grid(row=(i+1), column=j)
            i = i + 1
    except:
        print('Database Error!')

    root.mainloop()
