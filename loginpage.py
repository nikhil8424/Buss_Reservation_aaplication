from tkinter import *
import tkinter.messagebox as messagebox
from PIL import Image,ImageTk
import mysql.connector
from tkinter import ttk
import re



class BasePage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
    def toggle_password_visibility(self, entry):
        current_show_state = entry["show"]
        if current_show_state == "*":
            entry["show"] = ""
        else:
            entry["show"] = "*"

    def fetch_user_data(self, username):
        print("forget")
        try:
            # Connect to the database
            db_connection = mysql.connector.connect(
                host='localhost', password='gargi*1995', user='root', database='project'
            )
            cursor = db_connection.cursor()

            # Execute SQL query to fetch user data
            sql = "SELECT * FROM login WHERE username = %s"
            cursor.execute(sql, (username,))
            user_data = cursor.fetchone()

            # Close cursor and connection
            cursor.close()
            db_connection.close()

            return user_data

        except mysql.connector.Error as error:
            print("Error while connecting to MySQL", error)
            return None

class SignPage(BasePage):
    def __init__(self,parent,controller):
        super().__init__(parent, controller)
        self.passcpy=StringVar()
        self.name1=StringVar()
        self.email1=StringVar()
        self.password=StringVar()
        self.mobile=StringVar()
        self.question=StringVar()
        self.answer=StringVar()
        self.check=IntVar()
        self.frame2 = Frame(self, bg='yellow', height=700)
        
       
        
        a=True
        b=True
        Frame.__init__(self,parent)
        self.frame2=Frame(self,bg='#9df2de',width=300)

        self.frame1=Frame(self,width=200,height=700)
        
        title=Label(self.frame2,text="Create New Account",fg='#f75e11',bg='#9df2de',font=('Times New Roman', 40))
        title.place(x=170,y=100)
   
    
        efn=Label(self.frame2,text='Username: ',bg='#9df2de',font=('Times New Roman', 20))
        efn.place(x=150,y=250)
        fn=Entry(self.frame2,textvariable=self.name1,width=30,font=('Times New Roman', 14))
        fn.place(x=300,y=250)
        

        email=Label(self.frame2,text='Email: ',bg='#9df2de' ,font=('Times New Roman', 20))
        email.place(x=150,y=300)
    
        eemail=Entry(self.frame2,textvariable=self.email1,width=30,font=('Times New Roman', 14))
        eemail.place(x=300,y=300)


    
        fp=Label(self.frame2,text='Password: ',bg='#9df2de' ,font=('Times New Roman', 20))
        fp.place(x=150,y=350)

        self.efp=Entry(self.frame2,textvariable=self.password,show='*',width=30,font=('Times New Roman', 14))
        self.efp.place(x=300,y=350)
        self.show_password_button = Button(self, text="👁", bg='#9df2de',bd=1, command=lambda: self.toggle_password_visibility(self.efp))
        self.show_password_button.place(x=580, y=350)


        fm=Label(self.frame2,text='Mobile: ',bg='#9df2de' ,font=('Times New Roman', 20))
        fm.place(x=150,y=400)

        efm=Entry(self.frame2,textvariable=self.mobile,width=30,font=('Times New Roman', 14))
        efm.place(x=300,y=400)


        quest_label=Label(self.frame2,text='',width=10)
        questchoosen = ttk.Combobox(self.frame2,width = 20, textvariable =self.question,state='readonly') 
  
  
        questchoosen['values'] = ('--select security question--','name of mother:', 'name of first pet',\
                                  'date of birth - DDMMYY','nickname') 
    
        questchoosen.place(x=150,y=450)
        self.question.set('select question')
   

        ans=Entry(self.frame2,bd=1,textvariable=self.answer,width=30,font=('Times New Roman', 14))
        ans.place(x=300,y=450)


        c1=Checkbutton(self.frame2,text="Accept Terms and Condition",font=('Times New Roman', 20),bg='#9df2de',\
                       variable=self.check,height=2,bd=3,width=40)
        c1.place(x=120,y=490)
        
        #signup=Button(frame2,text='Sign Up',width=20,font=('bold',20),command=lambda:validform).place(x=450 , y=600)
        signup=Button(self.frame2, text='Sign Up', width=30, font=('bold',20),bg='#f75e11',activebackground='#b04713',\
                      activeforeground ='#facd96',cursor='hand2', command=self.validform)
        signup.place(x=150, y=600)
        self.pack()
        self.image = Image.open("busback.png")
        
        
        # Get the size of frame2
        frame_width = 750
        frame_height = 900
       
        self.image = self.image.resize((frame_width, frame_height))
        
        # Convert the image to PhotoImage
        self.img = ImageTk.PhotoImage(self.image)
  
        self.canvas=Canvas(self.frame1, height=1000,width=690)
        self.canvas.place(x=0,y=0)

        self.canvas.create_image(0,0,anchor=NW,image=self.img)
        self.canvas.create_text(250, 50, anchor=NW, text="New Here?", fill="white", font=('Times New Roman', 40, "bold"))
        self.canvas.create_text(100, 150, anchor=NW, text="sign up and discover a great amount of new offers on\n        \
                bus bookings!",fill="white", font=('Times New Roman', 19))
        self.rect_element=self.canvas.create_rectangle(260, 650, 550, 720,outline="#000", fill="#60cef0")
        self.canvas.create_text(350, 659, anchor=NW, text="Login",fill="white", font=('Times New Roman', 32))
        self.canvas.tag_bind(self.rect_element, '<Button-1>',self.show_login)
        self.frame2.pack(side=LEFT, fill=BOTH, expand=True)
        self.frame1.pack(side=RIGHT, fill=BOTH, expand=True)
        

    def show_login(self,event):
        self.name1.set("")
        self.email1.set("")
        self.password.set("")
        self.mobile.set("")
        self.check.set(0)
        self.question.set('select question')
        self.answer.set("")
        self.controller.show_login_page()
            
    def validform(self):
         name = self.name1.get()
         email = self.email1.get()
         password = self.password.get()
         mobile = self.mobile.get()
         question = self.question.get()
         answer = self.answer.get()
         check = self.check.get()

        # Perform validation
         errors = []

        # Check if all fields are filled
         if not all([name, email, password, mobile, question, answer]):
             errors.append("All fields are required")
         if name=='':
             errors.append("Please enter username")
         

        # Validate email format
         if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
             errors.append("Invalid email format")

        # Validate password complexity
         if len(password) < 5:
             errors.append("Password should be at least 5 characters long")
         elif not any(c.isupper() for c in password) or not any(c.isdigit() for c in password):
             errors.append("Password should contain at least one uppercase letter and one digit")

        # Validate mobile number format
         if not re.match(r'^\d{10}$', mobile):
             errors.append("Invalid mobile number format")
         if answer=='':
             errors.append("Please enter security answer")
         if question=='select question':
             errors.append("Please select security question")

        # Check if terms and conditions are accepted
         if not check:
             errors.append("Please accept terms and conditions")
         try:
            # Connect to MySQL database
            db_connection = mysql.connector.connect(
                host='localhost', password='gargi*1995', user='root', database='project'
            )
            cursor = db_connection.cursor()

            # Execute SQL query to check if username already exists
            sql = "SELECT * FROM login WHERE username = %s"
            val = (name,)
            cursor.execute(sql, val)
            result = cursor.fetchone()

            if result:
                errors.append("Username already exists")

            # Close connection
            cursor.close()
            db_connection.close()

         except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
         if not errors:
            try:
                # Connect to MySQL database
                db_connection = mysql.connector.connect(
                    host='localhost',password='gargi*1995',user='root',database='project'
                )
                cursor = db_connection.cursor()

                # Execute SQL query to insert data
                sql = "INSERT INTO login (username, password,email, question,answer,phonno) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (name, password,email,question, answer,mobile)
                cursor.execute(sql, val)

                # Commit changes and close connection
                db_connection.commit()
                cursor.close()
                db_connection.close()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        # Display errors or success message
         if errors:
             messagebox.showerror("Validation Error", "\n".join(errors))
         else:
             messagebox.showinfo("Success", "Form validated successfully. You can proceed.")
             
             self.name1.set=""
             self.email1.set=""
             self.password.set=""
             self.mobile.set=""
             self.question.set('select question')
             self.answer.set=""
             self.check.set=0
             self.controller.show_login_page()
             
             

    

class LoginPage(BasePage):
    
    def __init__(self,parent,controller):
        super().__init__(parent, controller)
        Frame.__init__(self,parent)
       
        self.username = StringVar()
        self.password = StringVar()
        

        self.frame2=Frame(self,bg='#9df2de',width=400)

        self.frame1=Frame(self,width=200,height=700)
        
        title=Label(self.frame2,text="Login into Blue Bus!",fg='#f75e11',bg='#9df2de',font=('Times New Roman', 40))
        title.place(x=170,y=100)
        
        efn=Label(self.frame2,text='Username: ',fg='#f75e11',bg='#9df2de',font=('Times New Roman', 22))
        efn.place(x=150,y=250)
        fn=Entry(self.frame2,textvariable=self.username,width=50,font=('Times New Roman', 19))
        fn.place(x=150,y=300)
        
        fp=Label(self.frame2,text='Password: ',fg='#f75e11',bg='#9df2de',font=('Times New Roman', 22))
        fp.place(x=150,y=400)
        efp=Entry(self.frame2,textvariable=self.password,show='*',width=50,font=('Times New Roman', 19))
        efp.place(x=150,y=450)
        
        show_password_button = Button(self.frame2, text="👁",command=lambda: self.toggle_password_visibility(efp))
        show_password_button.place(x=780, y=450)

        forget=Button(self.frame2,text='Forget Password?',bg='#9df2de',font=('Times New Roman', 12,"bold"),activebackground='#1e9694',command=self.controller.show_forget_page)
        forget.place(x=150,y=650)
    
        login_button = Button(self.frame2, text='Login', width=30, font=('bold',20),bg='#f75e11',activebackground='#b04713',\
                      activeforeground ='#facd96',cursor='hand2',command=self.login)
        login_button.place(x=150, y=550)
        self.image = Image.open("busback.png")
        
        
        # Get the size of frame2
        frame_width = 750
        frame_height = 900
       
        self.image = self.image.resize((frame_width, frame_height))
    
        # Convert the image to PhotoImage
        self.img = ImageTk.PhotoImage(self.image)
  
        self.canvas=Canvas(self.frame1, height=900,width=690)
        self.canvas.place(x=0,y=0)
        self.canvas.create_image(0,0,anchor=NW,image=self.img)
        self.canvas.create_text(150, 50, anchor=NW, text="Welcome Back!", fill="white", font=('Times New Roman', 40, "bold"))
        self.canvas.create_text(70, 150, anchor=NW, text="To keep connected with us and to take advantage of the \n         \
exciting offers login in to your account",fill="white", font=('Times New Roman', 17))
        self.rect_element=self.canvas.create_rectangle(100, 650, 500, 720,outline="#000", fill="#60cef0")
        self.canvas.create_text(215, 658, anchor=NW, text="Sign Up",fill="white", font=('Times New Roman', 32))
        self.canvas.tag_bind(self.rect_element, '<Button-1>',self.show_sign_page)
        self.frame1.pack(side=LEFT, fill=BOTH, expand=True)
        self.frame2.pack(side=LEFT, fill=BOTH, expand=True)
    def show_sign_page(self,event):
        self.controller.show_sign_page()


    def login(self):
        username = self.username.get()
        password = self.password.get()
        if username=='' or password=='':
            messagebox.showerror("input values", "enter username and password")
        else:
            self. authenticate_user(username, password)

            
    def authenticate_user(self,username, password):
               user_data = self.fetch_user_data(username)
               if user_data[1] and user_data[2] == password:  # Assuming password is stored in the third column
                      print("Authentication successful!")
                      self.controller.show_mainpage()
            # Proceed with login
               else:
                    messagebox.showerror("Authentication failed"," Invalid username or password.")
                    confirm = messagebox.askyesno("User Not Found", "User not found. Do you want to Sign Up?")
                    if confirm:
                        self.controller.show_sign_page()
                    else:
                        self.username.set("")
                        self.password.set("")

        
class ForgetPassPage(BasePage):
     def __init__(self,parent,controller):
        super().__init__(parent, controller)
        Frame.__init__(self,parent)
        
        self.name2=StringVar()
        self.question=StringVar()
        self.answer=StringVar()
        self.password=StringVar()
        self.confirm_password=StringVar()
        self.image2 =PhotoImage(file='arrow.png')
        self.frame1=Frame(self,width=100,height=700)

        self.frame2=Frame(self,bg='#9df2de',width=400,height=700)
        


        reset=Label(self.frame2,text='Reset Password',bg='#ff6721',fg='white',height=3,width=65,font=(40))
        reset.place(x=100,y=100)

        efn=Label(self.frame2,text='Username: ',bg='#9df2de',font=('Times New Roman', 20))
        efn.place(x=190,y=250)
        fn=Entry(self.frame2,textvariable=self.name2,width=37,font=('Times New Roman', 14))
        fn.place(x=390,y=250)
       

        quest_label=Label(self.frame2,text='',width=10,bg='#9df2de')
        questchoosen = ttk.Combobox(self.frame2,width = 27, textvariable =self.question) 
  

        questchoosen['values'] = ('--select security question--','name of mother:', 'name of first pet','date of birth - DDMMYY','nickname') 
    
        questchoosen.place(x=190,y=320)
        questchoosen.current(0)
   

        ans=Entry(self.frame2,width=37,bd=1,textvariable=self.answer,font=('Times New Roman', 14))
        ans.place(x=390,y=320)
   

        new_pass=Label(self.frame2,text='New Password',bg='#9df2de',font=('Times New Roman', 20))
        new_pass.place(x=190,y=370)

   
        new_entry=Entry(self.frame2,width=60,show='*',textvariable=self.password,font=('Times New Roman', 14))
        new_entry.place(x=190,y=420)

    
        con_pass=Label(self.frame2,text='confirm Password',bg='#9df2de',font=('Times New Roman', 20))
        con_pass.place(x=190,y=470)

        con_entry=Entry(self.frame2,width=60,show='*',textvariable=self.confirm_password,font=('Times New Roman', 14))
        con_entry.place(x=190,y=520)
        
        
        change=Button(self.frame2,text='Change',command=self.forget,bg='#ff6721',fg='white',height=1,width=25,font=(35))
        change.place(x=320,y=620)

        quitbt=Button(self.frame2,image=self.image2,bd=0,command=self.controller.show_login_page)
        quitbt.place(x=40,y=650)

        self.image = Image.open("lock.png")
        
        
        # Get the size of frame2
        frame_width = 750
        frame_height = 900
       
        self.image = self.image.resize((frame_width, frame_height))
        
        # Convert the image to PhotoImage
        self.img = ImageTk.PhotoImage(self.image)
  
        self.canvas=Canvas(self.frame1, height=900,width=690)
        self.canvas.place(x=0,y=0)

        self.canvas.create_image(0,0,anchor=NW,image=self.img)
##        self.canvas.create_text(250, 50, anchor=NW, text="New Here?", fill="white", font=("Arial", 40, "bold"))
##        self.canvas.create_text(150, 150, anchor=NW, text="sign up and discover a great amount of new offers on bus bookings!",\
##                                fill="white", font=("Arial", 12))
        self.frame1.pack(side=LEFT, fill=BOTH, expand=True)
        self.frame2.pack(side=LEFT, fill=BOTH, expand=True)
        

    
     def forget(self):
        error=[]
        username = self.name2.get()
        question1 = self.question.get()
        answer1 = self.answer.get()
        password = self.password.get()
        new_password = self.confirm_password.get()

        print('no')
        if username == '' or answer1 == '' or question1 == '--select security question--'or password=='' or new_password=='':
            error.append("All Field Required")
        elif password!=new_password:
            error.append("passwords not matching")
        # Validate password complexity
        if len(password) < 5:
             error.append("Password should be at least 5 characters long")
        elif not any(c.isupper() for c in password) or not any(c.isdigit() for c in password):
             error.append("Password should contain at least one uppercase letter and one digit")
        if error:
            messagebox.showerror('errors','\n'.join(error))
        else:
            self.authenticate_user_answer(username, question1, answer1,new_password)
        
##
     def authenticate_user_answer(self, username, security_question, answer,new_password):
        user_data = self.fetch_user_data(username)
        if user_data[1]and user_data[4] == security_question and user_data[5] == answer:  
            print("Security question answer authenticated!")
            try:
                db_connection = mysql.connector.connect(
                    host='localhost', password='gargi*1995', user='root', database='project'
                )
                cursor = db_connection.cursor()
                
                # Update the password in the database
                sql = "UPDATE login SET password = %s WHERE username = %s"
                cursor.execute(sql, (new_password, username))
                db_connection.commit()
                
                messagebox.showinfo("Success", "Password updated successfully")
                
                
                # Close cursor and connection
                cursor.close()
                db_connection.close()
                self.controller.show_login_page()
            except mysql.connector.Error as error:
                print("Error while connecting to MySQL", error)
                messagebox.showerror("Error", "Failed to update password")
        else:
            print("Authentication failed. Invalid security question or answer.")
            messagebox.showerror("Authentication failed", "Invalid information.")
    

     


class Application(Tk):
    def __init__(self,*args, **kwargs):

        Tk.__init__(self,*args,**kwargs)
        window=Frame(self)
        window.pack()
        self.geometry("8000x6000")
        window.grid_rowconfigure(0,minsize=7000)
        window.grid_columnconfigure(0,minsize=8000)
        self.sign_page = SignPage(self, self)
        self.login_page = LoginPage(self, self)
       
        self.forgetpassword_page = ForgetPassPage(self, self)

        self.show_sign_page()

    def show_sign_page(self):
        self.login_page.pack_forget()  # Hide LoginPage if visible
        self.sign_page.pack(fill=BOTH, expand=True)

    def show_login_page(self):
        self.forgetpassword_page.pack_forget()
        self.sign_page.pack_forget()  # Hide SignPage if visible
        self.login_page.pack(fill=BOTH, expand=True)

    def show_mainpage(self):
        self.destroy()
        import mainpage
    def show_forget_page(self):
        self.login_page.pack_forget()
        self.forgetpassword_page.pack_forget()
        self.forgetpassword_page.pack(fill=BOTH, expand=True)


if __name__ == "__main__":
    app = Application()
    app.mainloop()






















            
        
