from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
import tkinter.messagebox
import os
from tkcalendar import DateEntry
from ctypes import alignment
from datetime import date
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
def main():
    root=Tk()
    app=loginwindow(root)
    root.mainloop()
class profile:

    def __init__(self,root,email):
        self.email=email
        self.frame=Frame(root,bg="#FFFFF0")
        self.frame.place(x=300,y=0,width=1250,height=1000)
        upload_button=Button(self.frame,text="Upload Image",command=self.upload_image,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="#FFFFF0",bg="#6C3483")
        upload_button.place(x=400,y=200,width=140,height=35)

        profile=Label(self.frame,text="Profile",font=("times new roman",20,"bold"),fg="#4A235A",bg="#FFFFF0")
        profile.place(x=430,y=20)
        conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
        my_cur=conn.cursor()
        self.image1=ImageTk.PhotoImage(file=r"C:\Users\this pc\Downloads\se project\images\profile.jpg")
        query=("select image from images where Email=%s")
        values=(self.email,)
        my_cur.execute(query,values)
        r=my_cur.fetchone()
        if r!=None:
            frame1=Frame(self.frame)
            frame1.place(x=400,y=85,width=120,height=100)
            k=r[0]
            img2=Image.open(k)
            img2=img2.resize((120,100))
            self.image1=ImageTk.PhotoImage(img2)
            lblimg1=Label(self.frame,image=self.image1,borderwidth=0)
            lblimg1.place(x=400,y=85,width=120,height=100)   

        else:
            query=("insert into images values (%s,%s)")
            values=(0,self.email)
            my_cur.execute(query,values)
            frame1=Frame(self.frame)
            frame1.place(x=400,y=85,width=120,height=100)
            img2=Image.open(r"C:\Users\this pc\Downloads\se project\images\profile.jpg")
            img2=img2.resize((120,100))
            self.image1=ImageTk.PhotoImage(img2)
            lblimg1=Label(self.frame,image=self.image1,borderwidth=0)
            lblimg1.place(x=400,y=85,width=120,height=100)

        
        Firstname=Label(self.frame,text="First Name",font=("times new roman",15,"bold"),fg="#4A235A",bg="#FFFFF0")
        Firstname.place(x=200,y=260)

        my_cur.execute("select First_Name from register where Email=%s" ,(email,))
        self.firstname=my_cur.fetchone()
        self.Firstname1=Label(self.frame,text=self.firstname[0],font=("times new roman",15,"bold"),fg="#4A235A",bg="#FFFFF0")
        self.Firstname1.place(x=600,y=260)

        Lastname=Label(self.frame,text="Last Name",font=("times new roman",15,"bold"),fg="#4A235A",bg="#FFFFF0")
        Lastname.place(x=200,y=320)
        my_cur.execute("select Last_Name from register where Email=%s" ,(email,))
        self.lastname=my_cur.fetchone()

        self.lastname1=Label(self.frame,text=self.lastname[0],font=("times new roman",15,"bold"),fg="#4A235A",bg="#FFFFF0")
        self.lastname1.place(x=600,y=320)
        
        contact=Label(self.frame,text="Contact",font=("times new roman",15,"bold"),fg="#4A235A",bg="#FFFFF0")
        contact.place(x=200,y=380)
        my_cur.execute("select contact from register where Email=%s" ,(email,))
        self.Contact=my_cur.fetchone()
        self.contact1=Label(self.frame,text=self.Contact[0],font=("times new roman",15,"bold"),fg="#4A235A",bg="#FFFFF0")
        self.contact1.place(x=600,y=380)
        
        email1=Label(self.frame,text="Email",font=("times new roman",15,"bold"),fg="#4A235A",bg="#FFFFF0")
        email1.place(x=200,y=440)

        email2=Label(self.frame,text=email,font=("times new roman",15,"bold"),fg="#4A235A",bg="#FFFFF0")
        email2.place(x=600,y=440)

        editbutton=Button(self.frame,text="Edit",command = self.on_edit, font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="#FFFFF0",bg="#6C3483")
        editbutton.place(x=400,y=550,width=120,height=35) 
        conn.commit()
        conn.close()



    def on_edit(self):
        
        self.conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
        self.my_cur=self.conn.cursor(buffered=True)
        k1 = "First Name "
        k2 = "Last Name"
        k3 = "Contact"
        category, string, contact = customdialog9(self.frame, k1, k2, k3,self.email).show()
        self.Firstname1.config(text=category)
        self.lastname1.config(text=string)
        self.contact1.config(text=contact)
        
                
        
    def upload_image(self):
        global filename,img
        conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
        my_cur=conn.cursor()
        f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
        self.filename = filedialog.askopenfilename(filetypes=f_types,parent=self.frame)
        img = ImageTk.PhotoImage(file=self.filename)
        query=("update images set image=%s where Email=%s")
        values=(self.filename,self.email)
        my_cur.execute(query,values)
        query=("select image from images where Email=%s")
        values=(self.email,)
        my_cur.execute(query,values)
        r=my_cur.fetchone()
        if r==None:
            frame1=Frame(self.frame)
            frame1.place(x=400,y=85,width=120,height=100)
            img2=Image.open(r"C:\Users\this pc\Downloads\se project\images\login-icon.png")
            img2=img2.resize((120,100))
            self.image1=ImageTk.PhotoImage(img2)
            lblimg1=Label(self.frame,image=self.image1,borderwidth=0)
            lblimg1.place(x=400,y=85,width=120,height=100)
        else:
            frame1=Frame(self.frame)
            frame1.place(x=400,y=85,width=120,height=100)
            k=r[0]
            img2=Image.open(k)
            img2=img2.resize((120,100))
            self.image1=ImageTk.PhotoImage(img2)
            lblimg1=Label(self.frame,image=self.image1,borderwidth=0)
            lblimg1.place(x=400,y=85,width=120,height=100)
          
        conn.commit()
        conn.close()

class customdialog9(Toplevel):
    def __init__(self, parent, prompt, prompt1, prompt2,email):
        self.email=email
        Toplevel.__init__(self, parent)
        self.var = StringVar()
        self.var1 = StringVar()
        self.var2 = StringVar()
        conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
        my_cur=conn.cursor()   
        self.label = Label(self, text=prompt,font=("times new roman", 20),pady = 50)
        self.entry = Entry(self, textvariable=self.var,font=("times new roman", 15))
        self.label1 = Label(self, text=prompt1,font=("times new roman", 20),pady = 50)
        self.entry1 = Entry(self, textvariable=self.var1,font=("times new roman", 15))
        self.label2 = Label(self, text=prompt2,font=("times new roman", 20),pady = 50)
        self.entry2 = Entry(self, textvariable=self.var2,font=("times new roman", 15))
        self.ok_button = Button(self, text="OK", command=self.on_Ok , font=("times new roman",15,"bold"),relief=RIDGE,fg="#FFFFF0",bg="#6C3483")
        self.entry.bind("<Return>", self.on_Ok)
        
        my_cur.execute("select First_Name from register where Email=%s" ,(email,))
        self.firstname=my_cur.fetchone()
        self.entry.insert(10,self.firstname)
        my_cur.execute("select Last_Name from register where Email=%s" ,(email,))
        self.lastname=my_cur.fetchone()
        self.entry1.insert(10,self.lastname)
        my_cur.execute("select contact from register where Email=%s" ,(email,))
        self.Contact=my_cur.fetchone()
        self.entry2.insert(10,self.Contact)




        
        self.label.pack(side="top", fill="x",padx = 100)
        self.entry.pack(side="top", fill="x",padx=150)
        self.label1.pack(side="top", fill="x",padx = 100)
        self.entry1.pack(side="top", fill="x",padx=150)
        self.ok_button.pack(side="bottom",pady = 50)
        self.label2.pack(side="top", fill="x",padx = 100)
        self.entry2.pack(side="top", fill="x",padx=150)

        
        conn.commit()
        conn.close()
    def on_Ok(self, event=None):
        conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
        my_cur=conn.cursor()
        my_cur.execute("update register set First_Name=%s,Last_Name=%s,contact=%s where Email=%s" ,(self.entry.get(),self.entry1.get(),self.entry2.get(),self.email))        

        self.destroy()
        conn.commit()
        conn.close()

    def show(self):
        self.wm_deiconify()
        self.entry.focus_force()
        self.wait_window()
        return self.var.get(), self.var1.get(), self.var2.get()


class loginwindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")
        self.root.config(background = "#D8BFD8")
        frame=Frame(self.root,bg="#FFFFF0")
        frame.place(x=470,y=100,width=340,height=450)
        img1=Image.open(r"C:\Users\this pc\Downloads\se project\images\user.png")
        img1=img1.resize((100,100))
        self.image1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.image1,bg="#FFFFF0",borderwidth=0)
        lblimg1.place(x=600,y=120,width=100,height=100)
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="#6C3483",bg="#FFFFF0")
        username.place(x=115,y=155)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
    
        self.txtuser.place(x=30,y=180,width=270)
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="#6C3483",bg="#FFFFF0")
        password.place(x=115,y=225)        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show='*')
        self.txtpass.place(x=30,y=250,width=270)
        login_button=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="#FFFFF0",bg="#6C3483")
        login_button.place(x=110,y=300,width=120,height=35)
        register_button=Button(frame,text="Register",command=self.registerwindow,font=("times new roman",10,"bold"),borderwidth=0,fg="#6C3483",bg="#FFFFF0",activebackground="#FFFFF0",activeforeground="#6C3483")
        register_button.place(x=-7,y=360,width=160)
        register_button=Button(frame,text="Forgot Password ?",command=self.forgot_password,font=("times new roman",10,"bold"),borderwidth=0,fg="#6C3483",bg="#FFFFF0",activebackground="#FFFFF0",activeforeground="#6C3483")
        register_button.place(x=20,y=380,width=160)
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        elif self.txtuser.get()=="shravya" and self.txtpass.get()=="shravya":
            messagebox.showinfo("success","login successful")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
            my_cur=conn.cursor()
            my_cur.execute("select * from register where Email=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))
            r=my_cur.fetchone()
            if r==None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                self.func1()
        
            conn.commit()
            conn.close()
    def func1(self):
        self.neww1 = Toplevel()
        self.app2 = mainscreen(self.neww1,self.txtuser.get())
        self.neww1.mainloop()    
        
    def reset(self):
        if self.txt_q.get()=="Select":
            messagebox.showerror("Error","please select the question",parent=self.root2)
        elif self.txt_a.get()=="":
            messagebox.showerror("Error","please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","please enter the password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
            my_cur=conn.cursor()
            query=("select * from register where Email=%s and SecurityQ=%s and SecurityA=%s")
            value=(self.txtuser.get(),self.txt_q.get(),self.txt_a.get())
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where Email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cur.execute(query,value)
                messagebox.showinfo("success","password has be changed successfully",parent=self.root2)
                self.root2.destroy()
            conn.commit()
            conn.close()
            
            
        
    def forgot_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the email address")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
            my_cur=conn.cursor()
            query=("select * from register where Email=%s")
            value=(self.txtuser.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            if row==None:
                messagebox.showerror("Error","please enter valid email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x450+480+100")
                self.root2.config(background = "#FFFFF0")
                a=Label(self.root2,text="Forget password",font=("times new roman",20,"bold"),fg="#6C3483",bg="#FFFFF0")
                a.place(x=50,y=40)
                self.q=Label(self.root2,text="Select Security Question",font=("times new roman",20,"bold"),fg="#6C3483",bg="#FFFFF0")
                self.q.place(x=50,y=100)
                self.txt_q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.txt_q["values"]=("Select","Your favourite color","Your Pet name","Your school name")
                self.txt_q.place(x=50,y=135,width=270)
                self.txt_q.current(0)
                
                self.a=Label(self.root2,text="Security Answer",font=("times new roman",20,"bold"),fg="#6C3483",bg="#FFFFF0")
                self.a.place(x=50,y=170)
                self.txt_a=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_a.place(x=50,y=205,width=180)
                
                self.new_password=Label(self.root2,text="New Password",font=("times new roman",20,"bold"),fg="#6C3483",bg="#FFFFF0")
                self.new_password.place(x=50,y=240)
                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_password.place(x=50,y=275,width=180)
                btn=Button(self.root2,text="Reset",command=self.reset,font=("times new roman",15,"bold"),bg="#6C3483",fg="#FFFFF0")
                btn.place(x=150,y=350)
                

    
        




                
            
                
    def registerwindow(self):
        self.newwindow=Toplevel(self.root)
        self.app=register(self.newwindow)
        
        
            
class register:
    def __init__(self,root):
        self.root=root
        self.root.title("register")
        self.root.geometry("1500x800+0+0")
        self.root.config(background = "#D8BFD8")
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_password=StringVar()
        self.var_confirmpassword=StringVar()
        self.var_check=IntVar()  
        frame=Frame(self.root,bg="#FFFFF0")
        frame.place(x=240,y=70,width=800,height=500)
        
        register_lbl=Label(frame,text="Register",font=("times new roman",20,"bold"),fg="#6C3483",bg="#FFFFF0")
        register_lbl.place(x=350,y=20)
        
        Firstname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="#6C3483",bg="#FFFFF0")
        Firstname.place(x=115,y=100)
        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txt_fname.place(x=115,y=130,width=270)
        
        Lastname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="#6C3483",bg="#FFFFF0")
        Lastname.place(x=450,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=450,y=130,width=270)
        
        contactno=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="#6C3483",bg="#FFFFF0")
        contactno.place(x=115,y=170)
        self.txt_contactno=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contactno.place(x=115,y=200,width=270)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="#6C3483",bg="#FFFFF0")
        email.place(x=450,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=450,y=200,width=270)        


        q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="#6C3483",bg="#FFFFF0")
        q.place(x=115,y=230)
        self.txt_q=ttk.Combobox(frame,textvariable=self.var_securityq,font=("times new roman",15,"bold"),state="readonly")
        self.txt_q["values"]=("Select","Your favourite color","Your Pet name","Your school name")
        self.txt_q.place(x=115,y=260,width=270)
        self.txt_q.current(0)
        
        a=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="#6C3483",bg="#FFFFF0")
        a.place(x=450,y=230)
        self.txt_a=ttk.Entry(frame,textvariable=self.var_securitya,font=("times new roman",15,"bold"))
        self.txt_a.place(x=450,y=260,width=270)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="#6C3483",bg="#FFFFF0")
        password.place(x=115,y=290)
        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold"))
        self.txt_password.place(x=115,y=320,width=270)
        
        cpassword=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="#6C3483",bg="#FFFFF0")
        cpassword.place(x=450,y=290)
        self.txt_cpassword=ttk.Entry(frame,textvariable=self.var_confirmpassword,font=("times new roman",15,"bold"))
        self.txt_cpassword.place(x=450,y=320,width=270)

              
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms and Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0,fg="#6C3483",bg="#FFFFF0")
        checkbtn.place(x=115,y=380)
        
        register=Button(frame,text="Register",command=self.registerdata,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="#FFFFF0",bg="#6C3483")
        register.place(x=115,y=450,width=120,height=35)
        
        login_button=Button(frame,text="Login",command=self.return_login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="#FFFFF0",bg="#6C3483")
        login_button.place(x=450,y=450,width=120,height=35)
    
    def registerdata(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityq.get()=="Select" or self.var_lname.get()=="" :
            messagebox.showerror("Error","all fields required",parent=self.root)
        elif self.var_password.get()!= self.var_confirmpassword.get():
            messagebox.showerror("Error","Password and confirm Password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
            my_cur=conn.cursor()
            query=("select * from register where Email=%s")
            values=(self.var_email.get(),)
            my_cur.execute(query,values)
            r=my_cur.fetchone()
            if r!=None:
                messagebox.showerror("Error","user already exists",parent=self.root)
            else:
                img2=Image.open(r"C:\Users\this pc\Downloads\se project\images\profile.jpg")
                img2=img2.resize((120,100))
                self.image1=ImageTk.PhotoImage(img2)
                values=(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityq.get(),
                        self.var_securitya.get(),self.var_password.get())
                my_cur.execute("insert into register values (%s,%s,%s,%s,%s,%s,%s)",values)
                messagebox.showinfo("success","Register successful",parent=self.root)
            conn.commit()
            conn.close()
    def return_login(self):
        self.root.destroy()




class customdialog(Toplevel):
    def __init__(self, parent, prompt):
        Toplevel.__init__(self, parent)
        self.var = StringVar()

        self.label = Label(self, text=prompt,font=("times new roman", 20),pady = 50)
        self.entry = Entry(self, textvariable=self.var,font=("times new roman", 15))
        self.ok_button = Button(self, text="OK", command=self.on_Ok , font=("times new roman",15,"bold"),relief=RIDGE,fg="#FFFFF0",bg="#6C3483")

        self.label.pack(side="top", fill="x",padx = 100)
        self.entry.pack(side="top", fill="x",padx=150)
        self.ok_button.pack(side="bottom",pady = 50)

        self.entry.bind("<Return>", self.on_Ok)

    def on_Ok(self, event=None):
        self.destroy()

    def show(self):
        self.wm_deiconify()
        self.entry.focus_force()
        self.wait_window()
        return self.var.get()
class customdialog1(Toplevel):
    def __init__(self, parent, prompt, prompt1):
        Toplevel.__init__(self, parent)
        self.var = StringVar()
        self.var1 = StringVar()

        self.label = Label(self, text=prompt,font=("times new roman", 20),pady = 50)
        self.entry = Entry(self, textvariable=self.var,font=("times new roman", 15))
        self.label1 = Label(self, text=prompt1,font=("times new roman", 20),pady = 50)
        self.entry1 = Entry(self, textvariable=self.var1,font=("times new roman", 15))
        self.ok_button = Button(self, text="OK", command=self.on_Ok , font=("times new roman",15,"bold"),relief=RIDGE,fg="#FFFFF0",bg="#6C3483")

        self.label.pack(side="top", fill="x",padx = 100)
        self.entry.pack(side="top", fill="x",padx=150)
        self.label1.pack(side="top", fill="x",padx = 100)
        self.entry1.pack(side="top", fill="x",padx=150)
        self.ok_button.pack(side="bottom",pady = 50)

        self.entry.bind("<Return>", self.on_Ok)

    def on_Ok(self, event=None):
        self.destroy()

    def show(self):
        self.wm_deiconify()
        self.entry.focus_force()
        self.wait_window()
        return self.var.get(), self.var1.get()

class customdialog2(Toplevel):
    def __init__(self, parent, prompt, prompt1):
        Toplevel.__init__(self, parent)
        self.var = StringVar()
        self.var1 = StringVar()

        self.label = Label(self, text=prompt,font=("times new roman", 20),pady = 50)
        self.entry = Entry(self, textvariable=self.var,font=("times new roman", 15))
        self.label1 = Label(self, text=prompt1,font=("times new roman", 20),pady = 50)
        self.entry1 = Entry(self, textvariable=self.var1,font=("times new roman", 15))
        self.edit_button = Button(self, text="Edit", command=self.on_edit , font=("times new roman",15,"bold"),relief=RIDGE,fg="#FFFFF0",bg="#6C3483")

        self.label.pack(side="top", fill="x",padx = 100)
        self.entry.pack(side="top", fill="x",padx=150)
        self.label1.pack(side="top", fill="x",padx = 100)
        self.entry1.pack(side="top", fill="x",padx=150)
        self.edit_button.pack(side="bottom",pady = 50)

        self.entry.bind("<Return>", self.on_edit)

    def on_edit(self, event=None):
        self.destroy()

    def show(self):
        self.wm_deiconify()
        self.entry.focus_force()
        self.wait_window()
        return self.var.get(), self.var1.get()
class Setting:
    def __init__(self,root,email):
        self.root=Frame(root,bg="#FFFFF0")
        self.root.place(x=300,y=0,width=1250,height=1000)
        self.var_food=StringVar()
        self.var_bills=StringVar()
        self.var_clothes=StringVar()
        self.var_communications=StringVar()
        self.var_eatingout=StringVar()
        self.var_entertainment=StringVar()
        self.var_gifts=StringVar()
        self.var_health=StringVar()
        self.email=email
        frame=LabelFrame(self.root,bg="#D8BFD8")
        frame.place(x=40,y=70,width=300,height=525)
        frame1=LabelFrame(self.root,bg="#D8BFD8")
        frame1.place(x = 400, y = 200, width = 500, height = 270)
        self.conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
        self.my_cur=self.conn.cursor(buffered=True)
        trv = ttk.Treeview(frame1, selectmode ='browse')
        trv.grid(row=1,column=1,padx=20,pady=20)
        # number of columns
        trv["columns"] = ("1", "2", "3")
              
        # Defining heading
        trv['show'] = 'headings'
              
        # width of columns and alignment 
        trv.column("1", width = 60, anchor ='c')
        trv.column("2", width = 200, anchor ='c')
        trv.column("3", width = 200, anchor ='c')
              
        # Headings  
        # respective columns
        trv.heading("1", text ="S. No.")
        trv.heading("2", text ="Category")
        trv.heading("3", text ="Max Limit")
        query=("select * from settings where email=%s")
        values=(self.email,)
        self.my_cur.execute(query,values)
        r=self.my_cur.fetchall()
        for item in trv.get_children():
            trv.delete(item)
        if len(r)!=0:
            i = 1
            for res in r:
                trv.insert("", 'end',values=(i, res[0], res[1]))
                i+=1

        def on_Button(category):
                self.conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
                self.my_cur=self.conn.cursor(buffered=True)
                query=("select * from settings where categories=%s and email=%s")
                values=(category,self.email)
                self.my_cur.execute(query,values)
                r=self.my_cur.fetchall()
                
                if len(r)!=0:
                    tkinter.messagebox.showerror("Error","Maximum limit for this category is already entered.\n Please select any other category.",parent=self.root)
                else:
                    k = "Enter the max limit you want to spend on " +category
                    string = customdialog(root, k).show()
                    query=("insert into settings values(%s, %s, %s)")
                    values=(category, string, self.email)
                    self.my_cur.execute(query,values)
                    query=("select * from settings where email=%s")
                    values=(self.email,)
                    self.my_cur.execute(query,values)
                    r=self.my_cur.fetchall()
                    for item in trv.get_children():
                        trv.delete(item)
                    if len(r)!=0:
                        i = 1
                        for res in r:
                            trv.insert("", 'end',values=(i, res[0], res[1]))
                            i+=1
                    self.conn.commit()
                    self.conn.close()
        def on_Button1():
                self.conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
                self.my_cur=self.conn.cursor(buffered=True)
                k1 = "Enter the category "
                k2 = "Enter the max limit you want to spend "
                category, string = customdialog1(root, k1, k2).show()
                if category!=" " and string !="":
                    query=("insert into settings values(%s, %s, %s)")
                    values=(category, string, self.email)
                    self.my_cur.execute(query,values)
                    query=("select * from settings where email=%s")
                    values=(self.email,)
                    self.my_cur.execute(query,values)
                    r=self.my_cur.fetchall()
                    for item in trv.get_children():
                        trv.delete(item)
                    if len(r)!=0:
                        i = 1
                        for res in r:
                            trv.insert("", 'end',values=(i, res[0], res[1]))
                            i+=1
                    self.conn.commit()
                    self.conn.close()
                
        def on_Button2():
                self.conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
                self.my_cur=self.conn.cursor(buffered=True)
                k1 = "category you want to edit: "
                k2 = "Enter the max limit  "
                category, string = customdialog1(root, k1, k2).show()
                query=("select * from settings where email=%s")
                values=(self.email,)
                self.my_cur.execute(query,values)
                r=self.my_cur.fetchall()
                if len(r)==0:
                    query=("insert into settings values(%s, %s, %s)")
                    values=(category, string, self.email)
                    self.my_cur.execute(query,values)
                else:
                    query=("update settings set Maxlimit = %s where email = %s and categories = %s")
                    values=(string, self.email, category)
                    self.my_cur.execute(query,values)
                query=("select * from settings where email=%s")
                values=(self.email,)
                self.my_cur.execute(query,values)
                r=self.my_cur.fetchall()
                for item in trv.get_children():
                    trv.delete(item)
                if len(r)!=0:
                    i = 1
                    for res in r:
                        trv.insert("", 'end',values=(i, res[0], res[1]))
                        i+=1
                self.conn.commit()
                self.conn.close()
        cat_button=Button(frame,text="Food",font=("times new roman",15,"bold"),relief=RIDGE,fg="#6C3483",bg="#FFFFF0",command = lambda: on_Button("Food"))
        cat_button.place(x=65,y=80,width=160,height=35)
        cat_button1=Button(frame,text="Bills",font=("times new roman",15,"bold"),relief=RIDGE,fg="#6C3483",bg="#FFFFF0",command = lambda:  on_Button("Bills"))
        cat_button1.place(x=65,y=80,width=160,height=35)
        cat_button2=Button(frame,text="Clothes",font=("times new roman",15,"bold"),relief=RIDGE,fg="#6C3483",bg="#FFFFF0",command = lambda:  on_Button("Clothes"))
        cat_button2.place(x=65,y=380,width=160,height=35)
        cat_button3=Button(frame,text="Communications",font=("times new roman",15,"bold"),relief=RIDGE,fg="#6C3483",bg="#FFFFF0",command = lambda:  on_Button("Communications"))
        cat_button3.place(x=65,y=140,width=160,height=35)
        cat_button4=Button(frame,text="Eating out",font=("times new roman",15,"bold"),relief=RIDGE,fg="#6C3483",bg="#FFFFF0",command = lambda:  on_Button("Eating out"))
        cat_button4.place(x=65,y=200,width=160,height=35)
        cat_button5=Button(frame,text="Entertainment",font=("times new roman",15,"bold"),relief=RIDGE,fg="#6C3483",bg="#FFFFF0",command = lambda:  on_Button("Entertainment"))
        cat_button5.place(x=65,y=200,width=160,height=35)
        cat_button6=Button(frame,text="Gifts",font=("times new roman",15,"bold"),relief=RIDGE,fg="#6C3483",bg="#FFFFF0",command = lambda:  on_Button("Gifts"))
        cat_button6.place(x=65,y=320,width=160,height=35)
        cat_button7=Button(frame,text="Health",font=("times new roman",15,"bold"),relief=RIDGE,fg="#6C3483",bg="#FFFFF0",command = lambda:  on_Button("Health"))
        cat_button7.place(x=65,y=260,width=160,height=35)
        cat_edit=Button(frame,text="Other",font=("times new roman",15,"bold"),relief=RIDGE,fg="#6C3483",bg="#FFFFF0",command = on_Button1)
        cat_edit.place(x=65,y=450,width=160,height=35)
        cat_edit1=Button(root,text="edit",font=("times new roman",15,"bold"),relief=RIDGE,fg="#FFFFF0",bg="#6C3483",command=on_Button2)
        cat_edit1.place(x=680,y=600,width=160,height=35)



class Expenses:
    def __init__(self,root,mail):
        self.root=Frame(root,bg="#FFFFF0")
        self.root.place(x=300,y=0,width=1250,height=1000)
        self.var_title=StringVar()
        self.var_expense=StringVar()
        self.var_amount=StringVar()
        self.var_payment=StringVar()
        self.email=mail
        frame=LabelFrame(self.root,bg="#D8BFD8")
        frame.place(x=25,y=70,width=450,height=525)
        self.frame2=LabelFrame(self.root,bg="#D8BFD8")
        self.frame2.place(x=500,y=200,width=450,height=270)
        expenses1=Label(frame,text="Add Expense",font=("times new roman",20),fg="#4A235A",bg="#D8BFD8")
        expenses1.place(x=150,y=20)
        date=Label(frame,text="Date",font=("times new roman",15),fg="#4A235A",bg="#D8BFD8")
        date.place(x=60,y=145)
        self.cal = DateEntry(frame, width=40,locale='en_US', date_pattern='dd/mm/yyyy', 
        background='darkblue', foreground='white', borderwidth=2)
        self.cal.pack(padx=150, pady=150)
        self.type_expense=Label(frame,text="Expense Title",font=("times new roman",15),fg="#4A235A",bg="#D8BFD8")
        self.type_expense.place(x=60,y=205)
        self.title=ttk.Entry(frame,textvariable=self.var_title,font=("times new roman",15,"bold"))
        self.title.place(x=250,y=205,width=160)
        amount=Label(frame,text="Amount",font=("times new roman",15),fg="#4A235A",bg="#D8BFD8")
        amount.place(x=60,y=270)
        self.amount=ttk.Entry(frame,textvariable=self.var_amount,font=("times new roman",15,"bold"))
        self.amount.place(x=250,y=270,width=160)
        q=Label(frame,text="Payment methods",font=("times new roman",15),fg="#4A235A",bg="#D8BFD8")
        q.place(x=60,y=340)
        self.txt_q=ttk.Combobox(frame,textvariable=self.var_payment,font=("times new roman",15),state="readonly")
        self.txt_q["values"]=("Select","Net Banking","UPI","Cash","Debit/credit/ATM card")
        self.txt_q.place(x=250,y=340,width=160)
        self.txt_q.current(0)
        self.conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
        self.my_cur=self.conn.cursor(buffered=True)
        self.trv = ttk.Treeview(self.frame2, selectmode ='browse')
        self.trv.grid(row=1,column=1,padx=20,pady=20)
        # number of columns
        self.trv["columns"] = ("1", "2", "3","4","5")
              
        # Defining heading
        self.trv['show'] = 'headings'
              
        # width of columns and alignment 
        self.trv.column("1", width = 60, anchor ='c')
        self.trv.column("2", width = 85, anchor ='c')
        self.trv.column("3", width = 85, anchor ='c')
        self.trv.column("4", width = 85, anchor ='c')
        self.trv.column("5", width = 85, anchor ='c')             
        # Headings  
        # respective columns
        self.trv.heading("1", text ="S. No.")
        self.trv.heading("2", text ="Category")
        self.trv.heading("3", text ="Date")
        self.trv.heading("4", text ="payment_mode")
        self.trv.heading("5", text ="Amount")
        query=("select category,date,payment_mode,amount from totalexpense where email=%s")
        values=(self.email,)
        self.my_cur.execute(query,values)
        r=self.my_cur.fetchall()

        for item in self.trv.get_children():
            self.trv.delete(item)
        if len(r)!=0:
            i = 1
            for res in r:
                self.trv.insert("", 'end',values=(i, res[0], res[1],res[2],res[3]))
                i+=1
        Submitbutton=Button(frame,text="Add",command=self.Sub,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="#FFFFF0",bg="#6C3483")
        Submitbutton.place(x=170,y=440,width=120,height=35)
        
    def Sub(self):
        if self.var_title.get()=="" or self.var_payment.get()=="Select" or self.var_amount.get()=="":
            messagebox.showerror("Error","all fields required",parent=self.root)
        else:
            self.conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
            self.my_cur=self.conn.cursor(buffered=True)
            query=("insert into totalexpense values(%s, %s, %s,%s,%s)")
            values=(self.email,self.cal.get_date(),self.var_title.get(),self.var_payment.get(),self.var_amount.get())
            self.my_cur.execute(query,values)
            query=("select category,date,payment_mode,amount from totalexpense where email=%s")
            values=(self.email,)
            self.my_cur.execute(query,values)
            r=self.my_cur.fetchall()
            for item in self.trv.get_children():
                    self.trv.delete(item)
            if len(r)!=0:
                    i = 1
                    for res in r:
                        self.trv.insert("", 'end',values=(i, res[0], res[1],res[2],res[3]))
                        i+=1

            query=("select Maxlimit from settings where email=%s and categories=%s")
            values=(self.email,self.title.get())
            self.my_cur.execute(query,values)
            r=self.my_cur.fetchone()
            query=("select amount from totalexpense where email=%s and category=%s")
            values=(self.email,self.title.get())
            self.my_cur.execute(query,values)
            r1=self.my_cur.fetchall()
            
            sum=0
            for (i,) in r1:
                sum=sum+int(i)
            if int(r[0])-sum==100:
                messagebox.showerror("Error","you have almost reached your max limit",parent=self.root)
            if int(r[0])-sum<0:
                messagebox.showerror("Error","you have exceeded your max limit",parent=self.root)
            self.conn.commit()
            self.conn.close()            
class analysis:
    def __init__(self,root,email):
        self.root=Frame(root,bg="white")
        self.root.place(x=300,y=0,width=1250,height=1000)
        self.email=email
        self.frame = Frame(self.root,bg="white")
        self.frame.place(x = 0, y = 0, width = 1000, height = 700)
        self.startdate=StringVar()
        self.enddate=StringVar()
        date=Label(self.frame,text="Start date",font=("times new roman",20),bg="white")
        date.place(x=80,y=75)
        self.cal = DateEntry(self.frame, width=30,locale='en_US', date_pattern='yyyy/mm/dd', textvariable=self.startdate,
        background='darkblue', foreground='white', borderwidth=2)
        self.cal.place(x=230, y=80)
        date1=Label(self.frame,text="End date",font=("times new roman",20), bg="white")
        date1.place(x=550,y=75)
        self.cal1 = DateEntry(self.frame, width=30,locale='en_US', date_pattern='yyyy/mm/dd',textvariable=self.enddate ,
        background='darkblue', foreground='white', borderwidth=2)
        self.cal1.place(x=700, y=80)
        Submitbutton=Button(self.frame,text="Show Analysis",command=self.analysis,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="#FFFFF0",bg="#6C3483")
        Submitbutton.place(x=430,y=140,width=150,height=35)
    def create_charts(self,records):
        self.frame = Frame(self.root,bg="white" )
        self.frame.place(x = 50, y = 200, width = 920, height = 700)
        actualFigure = plt.figure(figsize = (5,4))
        actualFigure.suptitle("Expenses Stats", fontsize = 22)
        explode = list()
        labels2 = []
        pieSizes = []
        for i,j in records.items():
            labels2.append(i)
            pieSizes.append(j)
        labels2=list(set(labels2))
        for k in labels2:
            explode.append(0.05)
        pie= plt.pie(pieSizes, labels=labels2, explode = explode,autopct='%1.1f%%')

        canvas = FigureCanvasTkAgg(actualFigure, self.frame)
        canvas.get_tk_widget().pack()
    

    def analysis(self):
        self.conn=mysql.connector.connect(host="localhost",user="root",password="shravya0805",database="world")
        self.my_cur=self.conn.cursor(buffered=True)
        query=("select category,amount from totalexpense where email=%s and date between %s and %s ")
        values=(self.email,self.cal.get_date(),self.cal1.get_date())
        self.my_cur.execute(query,values)
        r=self.my_cur.fetchall()
        Output = {}
        for x, y in r:
            if x in Output:
                Output[x].append(int(y))
            else:
                Output[x] = [int(y)]
        records={}
        for x,y in Output.items():
            records[x]=sum(y)
        self.create_charts(records)
        self.conn.commit()
        self.conn.close()

        
class mainscreen:
    def __init__(self,root,email):
        self.root=root
        self.root.title("Expense Tracker")
        self.root.geometry("1500x800+0+0")
        self.email=email
        img1=Image.open(r"C:\Users\this pc\Downloads\se project\images\expense icon.png")
        img1=img1.resize((1050,700))
        self.image1=ImageTk.PhotoImage(img1)
        bg_label=Label(self.root,image=self.image1)
        bg_label.place(x=110,y=0,relwidth=1,relheight=1)
        frame=Frame(self.root,bg="#D8BFD8")
        frame.place(x=0,y=0,width=300,height=800)
        
        register_button1=Button(frame,text="PROFILE MANAGEMENT",command=self.p,font=("times new roman",12,"bold"),relief=RIDGE,borderwidth=4,fg="#6C3483",bg="#FFFFF0",activeforeground="white", activebackground = "#6C3483")
        register_button1.place(x=20,y=80,width=260,height=40)        

        register_button=Button(frame,text="EXPENSES MANAGEMENT",command=self.p2,font=("times new roman",12,"bold"),relief=RIDGE,borderwidth=4,fg="#6C3483",bg="#FFFFF0",activeforeground="white", activebackground = "#6C3483")
        register_button.place(x=20,y=160,width=260)

        register_button2=Button(frame,text="SETTINGS MANAGEMENT",command=self.p1, font=("times new roman",12,"bold"),relief=RIDGE,borderwidth=4,fg="#6C3483",bg="#FFFFF0",activeforeground="white", activebackground = "#6C3483")
        register_button2.place(x=20,y=240,width=260)
        register_button3=Button(frame,text="SHOW ANALYSIS",command=self.p3, font=("times new roman",12,"bold"),relief=RIDGE,borderwidth=4,fg="#6C3483",bg="#FFFFF0",activeforeground="white", activebackground = "#6C3483")
        register_button3.place(x=20,y=320,width=260)
        
        register_button4=Button(frame,text="LOG OUT",command=self.p4, font=("times new roman",12,"bold"),relief=RIDGE,borderwidth=4,fg="#6C3483",bg="#FFFFF0",activeforeground="white", activebackground = "#6C3483")
        register_button4.place(x=20,y=500,width=260)        
    def p(self):
        profile(self.root,self.email)
    def p1(self):
        Setting(self.root,self.email)
    def p2(self):
        Expenses(self.root,self.email)
    def p3(self):
        analysis(self.root,self.email)
    def p4(self):
        
        self.root.destroy()
        
if __name__=="__main__":
    main()

