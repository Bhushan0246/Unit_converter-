from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
from tktooltip import ToolTip
from Main_window import Main_frame

class About:
    def __init__(self, main):
        self.main = main
        self.main.configure(bg="#fff")
        self.main.wm_geometry("950x760+100+20")
        self.main.resizable(0, 0)
        self.main.wm_title("About Us")
        # img = PhotoImage(file='C:\\Users\\nidhi\\Desktop\\nidhi\\nidhi python\\AboutUsIcon.png')
        # main.iconphoto(False, img)

        font1 = ("Monospace", 22, "bold")
        font2 = ("Monospace", 14, "normal")
        font3 = ("Monospace", 13)

        self.l1 = Label(main, text='About Us', font=font1, fg="black", bg="white")
        self.l1.place(x=430, y=15)

        self.l2 = Label(main, text="Welcome to our Unit and Currency Converter GUI project!", font=font2, fg="black", bg="white")
        self.l2.place(x=30, y=70)

        s1 = "Our converter handles both unit and currency conversions smoothly, serving as a versatile tool for various needs. "
        s2 = "With our   converter, switching between different measurement units like length, weight,volume, and   temperature is effortless."
        s3 = s1 + s2

        self.l3 = Label(main, text=s3, font=font3, fg="black", bg="#ebf9eb", justify=LEFT, wraplength=930)
        self.l3.place(x=30, y=105)

        self.l4 = Label(main, text="Our Aim : Simplifying Conversions.", font=font2, fg="black", bg="white", justify=LEFT)
        self.l4.place(x=30, y=170)

        s4 = " We are committed, to developing a user tool for effortless unit and currency conversions. Our main goal is to offer an experience, for all users prioritizing accuracy and simplicity."
        s5 = "\nWe also offer real time currency exchange rates making sure you stay updated with the information whenever you need it. Whether you're arranging a journey or handling transactions our tool has got you covered."
        s6 = " In the end our goal is to simplify unit and currency conversions so users can concentrate on their tasks without having to deal with math."
        s7 = s4 + s5 + s6

        self.l5 = Label(main, text=s7, font=font3, fg="black", bg="#ebf9eb", justify=LEFT, wraplength=910)
        self.l5.place(x=30, y=205)
        self.l6 = Label(main, text="Our Team :", font=font2, fg="black", bg="white", justify=LEFT)
        self.l6.place(x=25, y=325)

        s8 = "Our team is dedicated to providing a top notch converter that fulfills the needs of our users. We focus on simplicity, precision\n and dependability in crafting and refining our product to guarantee an user experience."
        s9 = " Our focus is, on developing a user tool that simplifies conversions while gaining hands on experience through our project."
        s10 = s8 + s9

        self.l7 = Label(main, text=s10, font=font3, fg="black", bg="#ebf9eb", justify=LEFT, wraplength=920)
        self.l7.place(x=25, y=355)
        self.l8 = Label(main, text="Developers :", font=font2, fg="black", bg="white", justify=LEFT)
        self.l8.place(x=25, y=430)

        s11 = "Bhushan Harode & Nidhi Sikarwar\n"
        s12 = "Bachelor of Science (Computer Science,Electronics,Mathematics)\n"
        s13 = "School of Electronics, DAVV (Indore)"
        s15 = s11 + s12 + s13

        self.l9 = Label(main, text=s15, font=font3, fg="black", bg="#ebf9eb", justify=LEFT)
        self.l9.place(x=25, y=460)

        self.l10 = Label(main, text="Guided By:", font=font2, fg="black", bg="white", justify=LEFT)
        self. l10.place(x=25, y=540)
        self.l11 = Label(main, text="Ms. Kirti Panwar Bhati \nAssistant Professor, School of Electronics, DAVV (Indore)", font=font3, fg="black", bg="#ebf9eb",
                    justify=LEFT)

        self.l11.place(x=25, y=570)
        self.l12 = Label(main, text="Contact Us :", font=font2, fg="black", bg="white", justify=LEFT)
        self.l12.place(x=25, y=620)

        s11 = "We love hearing from you! If you have any questions, suggestions, or just want to say hello, feel free to contact us or\n drop us a mail."
        s12 = "Thankyou for being part of this Converter community!"
        s13 = s11 + s12

        self.l13 = Label(main, text=s13, font=font3, fg="black", bg="#ebf9eb", justify=LEFT)
        self.l13.place(x=25, y=650)
        self.l14 = Label(main, text="Nidhisikarwar24@gmail.com, \t github.com/Nidhisikarwar", font=font3, fg="black", bg="#ebf9eb", justify=LEFT)
        self.l14.place(x=25, y=700)
        self.l16 = Label(main, text="Bhushanharode0246@gmail.com, \t github.com/Bhushan0246", font=font3, fg="black", bg="#ebf9eb", justify=LEFT)
        self.l16.place(x=25, y=725)

        img = Image.open(".\images\previous.png")
        res = img.resize((25,22), Image.FASTOCTREE)
        conv_img_back = ImageTk.PhotoImage(res)
        self.back = CTkButton(main,text='', fg_color='#fff', border_spacing=3, corner_radius=50, image=conv_img_back,
                         height=28, width=30, border_width=2, border_color='#88dd88', command=self.backhome)
        ToolTip(self.back, msg="Back to Home", delay=0.5, bg='#fff')
        self.back.configure(hover_color = '#fff')
        self.back.place(x=690, y=10)

    def backhome(self):
        root = self.main
        root.destroy()
        temp = CTk()
        new_win = Main_frame(temp)
        temp.mainloop()

main = Tk()
win = About(main)
main.mainloop()
