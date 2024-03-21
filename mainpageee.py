#mainpage
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import mysql.connector


root=Tk()
width1= root.winfo_screenwidth()               
height1= root.winfo_screenheight()
root.geometry("%dx%d" % (width1, height1))

def delete_pages():
    for frame in frame2.winfo_children():
        frame.destroy()
    

def hide_indicate():
    step1_indicate.config(bg='#83ebd3')
    step2_indicate.config(bg='#83ebd3')
    step3_indicate.config(bg='#83ebd3')

 
def indicate(lb):
    hide_indicate()
    lb.configure(bg='blue')
    delete_pages()
    

def homepage():
    delete_pages()
    def search_trip():
        query = search_entry.get()

    search_label = Label(frame2, text="Search Your Trip here:", bg='#a9e8c0', font=('Arial',16))
    search_label.pack(side=TOP, pady=10)

    search_frame = Frame(frame2)  
    search_frame.pack(side=TOP, pady=10)

    search_entry = Entry(search_frame, width=150)
    search_entry.pack(side=LEFT, padx=10)

    search_button = Button(search_frame, text="Search", command=search_trip)
    search_button.pack(side=LEFT, padx=10)

    offers_label = Label(frame2, text="Offers:", bg='#a9e8c0',font=('Arial', 16))
    offers_label.pack(side=TOP, pady=25)

    offers_text = Text(frame2, height=10, width=150)
    offers_text.pack(side=TOP, padx=10, pady=10)

    
    offers_text.insert(END, "1. 20% off on all bookings\n", ('offer',))
    offers_text.insert(END, "2. Free meal on selected routes\n", ('offer',))
    offers_text.insert(END, "3. Flat ₹500 discount on weekend trips\n", ('offer',))

    offers_text.tag_configure('offer', font=('Arial', 15), spacing1=10, spacing2=5, spacing3=10)

    def submit_review():
        review = review_text.get("1.0", END)
        rating = rating_scale.get()
        print("Submitted Review:", review)
        print("Rating:", rating)

        thanks_label = Label(frame2, text="Thanks for rating!", bg='#6AFB92', font=('Arial', 20))
        thanks_label.pack(side=TOP, pady=10)

        def remove_message():
            thanks_label.pack_forget()

        frame2.after(2000, remove_message) 

    reviews_label = Label(frame2, text="Customer Review:", bg='#a9e8c0', font=('Arial', 14))
    reviews_label.pack(side=TOP, pady=10)

    review_text = Text(frame2, height=5, width=110, font=('Arial', 16))
    review_text.pack(side=TOP, padx=10, pady=5)

    rating_label = Label(frame2, text="Rate This Trip:", bg='#a9e8c0', font=('Arial', 16))
    rating_label.pack(side=TOP, pady=5)

    rating_scale = Scale(frame2, from_=1, to=5, orient=HORIZONTAL, length=200)
    rating_scale.pack(side=TOP, pady=5)

    submit_button = Button(frame2, text="Submit Review", command=submit_review)
    submit_button.pack(side=TOP, pady=10)

    
def aboutpage():
    delete_pages()
    label=Label(frame2,text="this is the about page")
    label.pack(side=TOP)

def bookingpage():
    delete_pages()
    label=Label(frame2,text="this is the booking page page")
    label.pack(side=TOP)

def cancelpage():
    delete_pages()
    label=Label(frame2,text="this is the ticket cancel page")
    label.pack(side=TOP)
def feedpage():
    delete_pages()
    label=Label(frame2,text="this is the feed page")
    label.pack(side=TOP)

frame3=Frame(root)
frame1=Frame(root)
frame2=Frame(root)
frame3.config(width=width1,height=50,bg='#83ebd3')
frame2.config(width=1000, height=height1,bg='white')
frame1.config(width=1,height=height1,bg='#a9e8c0')


step1=Button(frame1,text="step1",font=('bold',12),command=  lambda: indicate(step1_indicate),height=2,width=20,bg='#45b592',fg='#ffffff', bd=0,activebackground='#347061',activeforeground='white')
step1.place(x=20,y=250)

step1_indicate=Label(frame1,text='',bg='#83ebd3')
step1_indicate.place(x=5,y=250,width=5,height=40)

step2=Button(frame1,text="contact",command=  lambda: indicate(step2_indicate),height=2,width=20,font=('Bold',12),bg='#45b592',fg='#ffffff',bd=0,activebackground='#347061',activeforeground='white')
step2.place(x=20,y=350)
step2_indicate=Label(frame1,text='',bg='#83ebd3')
step2_indicate.place(x=5,y=350,width=5,height=40)

step3=Button(frame1,text="about us",height=2,width=20,font=('Bold',12),command=  lambda: indicate(step3_indicate),bg='#45b592',fg='#ffffff',bd=0,activebackground='#347061',activeforeground='white')
step3.place(x=20,y=450)
step3_indicate=Label(frame1,text='',bg='#83ebd3')
step3_indicate.place(x=5,y=450,width=5,height=40)

label2=Label(frame2,text="this is window two")
label2.pack(pady=50,padx=20)

canvas=Canvas(frame1, height=150,width=160)
canvas.pack(pady=30)

img=PhotoImage(file='busicon2.png')
canvas.create_image(2,4,anchor=NW,image=img)

canvas1=Canvas(frame3,height=45,width=50)
canvas1.pack(padx=30,side=LEFT)
img1=PhotoImage(file='buslogo.png')
canvas1.create_image(1,1,anchor=NW,image=img1)


but3=Button(frame3,text="feedback",bg='#83ebd3',font=('Arial',15),bd=0,command=feedpage)
but3.pack(side=RIGHT,padx=40)

but4=Button(frame3,text="about us",bg='#83ebd3',font=('Arial',15),bd=0,command=aboutpage)
but4.pack(side=RIGHT,padx=40)




but7=Button(frame3,text="cancellation",bg='#83ebd3',font=('Arial',15),bd=0,command=cancelpage)
but7.pack(side=RIGHT,padx=40)
but6=Button(frame3,text="ticket booking",bg='#83ebd3',font=('Arial',15),bd=0,command=bookingpage)
but6.pack(side=RIGHT,padx=40)

but5=Button(frame3,text="home",bg='#83ebd3',font=('Arial',15),bd=0,command=homepage)
but5.pack(side=RIGHT,padx=40)



frame3.pack(fill=BOTH,expand=True,side=TOP)
frame3.pack_propagate(0)



frame1.pack(fill=BOTH,expand=True,side=LEFT)

frame1.pack_propagate(0)

frame2.pack(fill=BOTH,expand=True,side=LEFT)
frame2.pack_propagate(0)

