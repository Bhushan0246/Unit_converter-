from customtkinter import *
from customtkinter import CTkComboBox
from PIL import Image
from tkinter import Canvas
import mysql.connector
import convertcurrency

def historyCurr():
    def back_curr():
        root.destroy()
        convertcurrency.currency()

    root = CTk()
    root.geometry('850x610+100+50')
    root.wm_title('Currency History')
    root.wm_resizable(0, 0)
    root.configure(fg_color='#FEF6FF')
    color_bg = root.cget('background')

    font1 = CTkFont('Monospace', 34, 'normal', underline=False, slant='italic')
    font2 = CTkFont('Monospace', 19, 'normal')
    font3 = CTkFont('Monospace', 16, 'normal', slant='italic')

    img = CTkImage(light_image=Image.open(".\images\history_curr.png"), size=(170, 540))
    main_img = CTkLabel(root, text='', image=img)
    main_img.place(x=650, y=30)

    title = CTkLabel(root, text='History', font=font1, text_color='#636C5E')
    title.place(x=235, y=15)

    back_btn = CTkButton(root, text='Back', width=200, height=30, corner_radius=5, border_width=2,
                         border_color='#636C5E', bg_color=color_bg, fg_color=color_bg, text_color='#636C5E',
                         font=font2, hover_color=color_bg, state=NORMAL, command=back_curr)
    back_btn.place(x=630, y=570)

    heading = " Date-Time\tFrom \t    Into\t    Value \t          Result"
    sbfrm = CTkScrollableFrame(root, width=595, height=460, corner_radius=8, border_width=1, bg_color='#FDF2FF',
                               fg_color='#FDF2FF', scrollbar_fg_color='#FDF2FF', scrollbar_button_color='#ddeedf',
                               scrollbar_button_hover_color='#ddeedf', orientation="vertical", label_text=heading,
                               label_font=font2, label_anchor="sw", label_text_color='#636C5E',
                               label_fg_color='#FDF2FF')
    sbfrm.place(x=2, y=70)

    #   Database connection and fetching goes here
    try:
        mydb = mysql.connector.connect(host='localhost', user='root', password='mysql@123456', database='converter')
        mycur = mydb.cursor()
        query = "SELECT * FROM curr_history"
        mycur.execute(query)
        ndata = mycur.fetchall()
        mycur.execute(query)
        i = 0
        #   Heading buttons for data entries
        for student in mycur:
            for j in range(len(student)):
                e = CTkButton(sbfrm, width=100, height=20, text_color='#263238', font=font3, border_width=1,
                              border_color='#C3E4C0', fg_color=color_bg, state=NORMAL, hover=False)
                e.configure(text=student[j])
                if (j==0 or j==4):
                    e.configure(width=160)
                    e.grid(row=(i + 1), column=j)
                else:
                    e.grid(row=(i + 1), column=j)
            i = i + 1
    except:
        print('Database Error!')

    root.mainloop()
