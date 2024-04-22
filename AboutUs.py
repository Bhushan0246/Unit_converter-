import tkinter
from tkinter import *
from PIL import Image, ImageTk

main = Tk()
#main.configure(highlightthickness=2,highlightcolor="#000000",bg="#fff")
main.configure(bg="#fff")
main.geometry("1000x760+350+20")
main.resizable(0, 0)
main.wm_title("About Us")
img = PhotoImage(file='C:\\Users\\nidhi\\Desktop\\nidhi\\nidhi python\\AboutUsIcon.png')
main.iconphoto(False, img)

font1 = ("Monospace", 22, "bold")
font2 = ("Monospace", 14, "normal")
font3 = ("Monospace", 13)

l1 = Label(main, text='About Us', font=font1, fg="black", bg="white")
l1.place(x=430, y=15)

l2 = Label(main, text="Welcome to our Unit and Currency Converter GUI project!", font=font2, fg="black", bg="white")
l2.place(x=30, y=70)

s1 = "Our converter handles both unit and currency conversions smoothly, serving as a versatile tool for various needs. "
s2 = "With our   converter, switching between different measurement units like length, weight,volume, and   temperature is effortless."
s3 = s1 + s2

l3 = Label(main, text=s3, font=font3, fg="black", bg="#eef7f5", justify=LEFT, wraplength=930)
l3.place(x=30, y=105)

l4 = Label(main, text="Our Aim : Simplifying Conversions.", font=font2, fg="black", bg="white", justify=LEFT)
l4.place(x=30, y=170)

s4 = " We are committed, to developing a user tool for effortless unit and currency conversions. Our main goal is to offer an experience, for all users prioritizing accuracy and simplicity."
s5 = "\nWe also offer real time currency exchange rates making sure you stay updated with the information whenever you need it. Whether you're arranging a journey or handling transactions our tool has got you covered."
s6 = " In the end our goal is to simplify unit and currency conversions so users can concentrate on their tasks without having to deal with math."
s7 = s4 + s5 + s6

l5 = Label(main, text=s7, font=font3, fg="black", bg="#eef7f5", justify=LEFT, wraplength=910)
l5.place(x=30, y=205)
l6 = Label(main, text="Our Team :", font=font2, fg="black", bg="white", justify=LEFT)
l6.place(x=25, y=325)

s8 = "Our team is dedicated to providing a top notch converter that fulfills the needs of our users. We focus on simplicity, precision\n and dependability in crafting and refining our product to guarantee an user experience."
s9 = " Our focus is, on developing a user tool that simplifies conversions while gaining hands on experience through our project."
s10 = s8 + s9

l7 = Label(main, text=s10, font=font3, fg="black", bg="#eef7f5", justify=LEFT, wraplength=920)
l7.place(x=25, y=355)
l8 = Label(main, text="Developers :", font=font2, fg="black", bg="white", justify=LEFT)
l8.place(x=25, y=430)

s11 = "Bhushan Harode & Nidhi Sikarwar\n"
s12 = "Bachelor of Science (Computer Science,Electronics,Mathematics)\n"
s13 = "School of Electronics, DAVV (Indore)"
s15 = s11 + s12 + s13

l9 = Label(main, text=s15, font=font3, fg="black", bg="#eef7f5", justify=LEFT)
l9.place(x=25, y=460)

l10 = Label(main, text="Guided By:", font=font2, fg="black", bg="white", justify=LEFT)
l10.place(x=25, y=540)
l11 = Label(main, text="Ms. Kirti Panwar Bhati \nAssistant Professor, School of Electronics, DAVV (Indore)", font=font3, fg="black", bg="#eef7f5",
            justify=LEFT)

l11.place(x=25, y=570)
l12 = Label(main, text="Contact Us :", font=font2, fg="black", bg="white", justify=LEFT)
l12.place(x=25, y=620)

s11 = "We love hearing from you! If you have any questions, suggestions, or just want to say hello, feel free to contact us or\n drop us a mail."
s12 = "Thankyou for being part of this Converter community!"
s13 = s11 + s12

l13 = Label(main, text=s13, font=font3, fg="black", bg="#eef7f5", justify=LEFT)
l13.place(x=25, y=650)
l14 = Label(main, text="Nidhisikarwar24@gmail.com, \t github.com/Nidhisikarwar", font=font3, fg="black", bg="#eef7f5", justify=LEFT)
l14.place(x=25, y=700)
l16 = Label(main, text="Bhushanharode0246@gmail.com, \t github.com/Bhushan0246", font=font3, fg="black", bg="#eef7f5", justify=LEFT)
l16.place(x=25, y=725)


'''btnphoto = Image.open("C:\\Users\\nidhi\\Downloads\\arrow (1).png")
res = btnphoto.resize((20, 70), Image.FASTOCTREE)
res_photo = ImageTk.PhotoImage(res)'''

back = tkinter.Button(main, text="Back",font=("Monospace", 14, "bold"), borderwidth=0, height=0, width=6, bg="#eef7f5", fg="black", activebackground="white")
back.place(x=850, y=30)

'''btnphoto = PhotoImage(file = "C:\\Users\\nidhi\\Downloads\\arrow.png")
res=btnphoto.resize((size:40,80),Image.FASTOCTREE)
res_photo=ImageTk.PhotoImage(res)

back = tkinter.Button(main, text="",image=btnphoto, borderwidth=2, height=40, width=80, bg="#eef7f5", fg="black",activebackground="white")
back.place(x=850, y=30)'''

main.mainloop()
