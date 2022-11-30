import random
import time
from datetime import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from PIL import ImageTk, Image  # pip install pillow
from tkinter import PhotoImage
import tkinter.filedialog
import pandas as pd
import numpy as np
import re
import os
import math
import sys
import smtplib
import matplotlib.pyplot as plt
from uuid import uuid4
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import sqlite3

window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#=============================Window setting=========================================================

window.resizable(0, 0)  # Delete the restore button
window_height = 750
window_width = 1350

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

#==============================Database==============================================================
def connect_database():
    try:
        global conn
        global cursor
        #connect to database
        conn = sqlite3.connect('C:/Users/user/OneDrive/Documents/ALL2 Ver2/ALL2/money.db')
        #define cursor 
        cursor = conn.cursor()
    except:
        messagebox.showerror('Error', 'Cannot connect to database!')

connect_database()




#===========================Set Frame==================================================================

page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)
page4 = Frame(window)
page5 = Frame(window)
page6 = Frame(window)
page7 = Frame(window)
page8 = Frame(window)
page9 = Frame(window)
page10 = Frame(window)
page11 = Frame(window)
page12 = Frame(window)
page13 = Frame(window)
page14 = Frame(window)


for frame in(page1,page2,page3,page4,page5):
    frame.grid(row=0,column=0,sticky='nsew')



def show_frame(frame):
    frame.tkraise()

show_frame(page1)
#================================Login Page=======================================

page1.config()

uname_stvar = StringVar()
pwd_stvar = StringVar()




#===============================Function===========================================
def gotorg():
    show_frame(page2)

def login():
    Username = uname_stvar.get()
    Password = pwd_stvar.get()

    find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
    cursor.execute(find_user,[(uname_stvar.get()),(pwd_stvar.get())])

    result = cursor.fetchall()
                      

    if result:
        messagebox.showinfo('Login Status', 'You are successfully loged in ')

        calc_total_expenses()
        current_budget()
        display_trans_database()
        display_budget_database()
        display_credit_database()
        display_home_expense()
        display_home_savings()
        display_home_credit()

        show_frame(page4)
        


    elif Username == '' or Password == '' : 
        messagebox.showerror('Login Error','You are required to fill in all the fields.')
       
    else:
        messagebox.showerror('Login Error' , 'Wrong information')
        


        

            

#=============================Background============================================
bg1 = Image.open('Login_background.jpeg')
photo = ImageTk.PhotoImage(bg1)
bg1_panel = Label(page1, image=photo)
bg1_panel.image = photo
bg1_panel.pack(fill='both', expand='yes')
#===========================Login Frame===============
lgn_frame = Frame(page1, bg='white', width='450', height=630)  # Color and the size of the frame
lgn_frame.place(x=476, y=80)  # Placement of the frame

lgn_txt = 'Login'
lgn_heading = Label(lgn_frame, text=lgn_txt, font=('yu gothic ui', 25, 'bold'), bg='white', fg='blue')
lgn_heading.place(x=80, y=170 ,width=300, height=45)

lgn_txt2 = 'Sign in to your account'
lgn_heading2 = Label(lgn_frame, text=lgn_txt2, font=('yu gothic ui', 13, 'bold'), bg='white', fg='gray')
lgn_heading2.place(x=80, y=215 ,width=300, height=25)

 # ================= user Image =================
user_image = Image.open('Login_User.jpeg')
photo = ImageTk.PhotoImage(user_image)
user_image_label = Label(page1, image=photo, bg='white')
user_image_label.image = photo
user_image_label.place(x=630, y=100)

user_label = Label(lgn_frame, text='Sign In', bg='#040405', fg='white',
                           font=('yu gothic ui', 17, 'bold'))
user_label.place(x=676, y=190)



#=======================Username Icon=========================
uname_icon = Image.open('Login_username.jpeg')
photo = ImageTk.PhotoImage(uname_icon)
uname_icon_label = Label(page1, image=photo,bg='white')
uname_icon_label.image = photo
uname_icon_label.place(x=545, y=385)


# ================= Password =================
pwd_label = Label(page1, text='Password', bg='white', font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
pwd_label.place(x=551, y=440)

pwd_entry = Entry(page1, highlightthickness=0, relief=FLAT, bg='white', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'), show='*',textvariable=pwd_stvar)
pwd_entry.place(x=581, y=475, width=270)

pwd_line = Canvas(page1, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
pwd_line.place(x=551, y=499)

pwd_txt3 = 'Forgot my password. Click here to reset'
pwd_heading3 = Label(lgn_frame, text=pwd_txt3, font=('yu gothic ui', 11, 'bold'), bg='white', fg='gray')
pwd_heading3.place(x=71,y=430,width=310,height=30)



#=======================Password Icon=========================
pwd_icon = Image.open('Login_password.jpeg')
photo = ImageTk.PhotoImage(pwd_icon)
pwd_icon_label = Label(page1, image=photo,bg='white')
pwd_icon_label.image = photo
pwd_icon_label.place(x=540, y=465)

# ================= Login Button =================)

btn_login = Button(page1, text='LOGIN', font=('yu gothic ui', 13, 'bold'), width=26,height=2, bd=0,
                            bg='#61b4b4', cursor='hand2', activebackground='#0080b3', fg='white',command=login)
btn_login.place(x=568, y=560)

txt_register = 'Do not have an account? Register here.'
heading_txt_register = Label(lgn_frame, text=txt_register, font=('yu gothic ui', 11, 'bold'), bg='white', fg='gray')
heading_txt_register.place(x=71,y=550,width=310,height=30)

gotoregister = Button(page1, text='here', font=('yu gothic ui', 11, 'bold'), width=3,height=1, bd=0,bg='white',fg='blue',command=gotorg)
gotoregister.place(x=800, y=630)



#===================Register===============================================================================
page2.config()
  
Rgusername_strvar = StringVar()
crtpassword_strvar = StringVar()
confirmpassword_strvar = StringVar()

Rgusername = Rgusername_strvar.get()
crtpassword = crtpassword_strvar.get()
confirmpassword = confirmpassword_strvar.get()


#=========================================Function=====================================================
def backtolg():
    show_frame(page1)

def rginsertdata(): #add data to database
    confirmpassword = confirmpassword_strvar.get()
    Rgusername = Rgusername_strvar.get()
    crtpassword = crtpassword_strvar.get()

    check_counter =0
    warn=""

    if Rgusername_strvar.get() == "" or crtpassword_strvar.get() == "":
        warn= "Fill in the all component"
    else:
        check_counter +=1

    if confirmpassword_strvar.get()== "":
        warn= "Enter your password again"
    else:
        check_counter +=1

    if crtpassword_strvar.get() != confirmpassword_strvar.get():
        warn= "Password are not match"
    else:
        check_counter +=1

    if len(crtpassword_strvar.get() )< 8:
        warn="password are too short"
    else:
        check_counter +=1
        

    if check_counter == 4:
        try:
            conn.execute("INSERT INTO user (username, password) VALUES(?,?)",(Rgusername, crtpassword))
            conn.commit()
            tkinter.messagebox.showinfo("success")
        except Exception as ep:
            messagebox.showerror('',ep)
    else:
        messagebox.showerror('Error',warn)
    
    
    
#==================Register Bg============================================================
bg2 = Image.open('Login_background.jpeg')
photo = ImageTk.PhotoImage(bg2)
bg2_panel = Label(page2, image=photo)
bg2_panel.image = photo
bg2_panel.pack(fill='both', expand='yes')

#===========================Register Frame===============
Register_frame = Frame(page2, bg='white', width='450', height=630)  # Color and the size of the frame
Register_frame.place(x=476, y=80)  # Placement of the frame

Registertxt = 'Register'
Registerheading = Label(Register_frame, text=Registertxt, font=('yu gothic ui', 25, 'bold'), bg='white', fg='blue')
Registerheading.place(x=80, y=150 ,width=300, height=45)


# ================= Register Image =================
Register_image = Image.open('Register_image.jpeg')
photo = ImageTk.PhotoImage(Register_image)
Register_image_label = Label(page2, image=photo, bg='white')
Register_image_label.image = photo
Register_image_label.place(x=640, y=100)

user_label = Label(Register_frame, text='Sign In', bg='#040405', fg='white',
                           font=('yu gothic ui', 17, 'bold'))
user_label.place(x=676, y=190)

# ================= Username =================
Rgusername_label = Label(page2, text='Enter your email', bg='white',font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
Rgusername_label.place(x=551, y=305)

Rgusername_entry = Entry(page2, highlightthickness=0, relief=FLAT, bg='white', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'),textvariable=Rgusername_strvar)
Rgusername_entry.place(x=581, y=340, width=270)

Rgusername_line = Canvas(page2, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
Rgusername_line.place(x=551, y=364)

#===================Create Password================================================
crtpassword_label = Label(page2, text='Create a Password', bg='white', font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
crtpassword_label.place(x=551, y=385)

crtpassword_entry = Entry(page2, highlightthickness=0, relief=FLAT, bg='white', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'), show='*',textvariable=crtpassword_strvar)
crtpassword_entry.place(x=581, y=420, width=270)

crtpassword_line = Canvas(page2, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
crtpassword_line.place(x=551, y=444)

Registertxt3 = 'Password must be 8 characters in length'
Registerheading3 = Label(Register_frame, text=Registertxt3, font=('yu gothic ui', 8, 'bold'), bg='white', fg='gray')
Registerheading3.place(x=22,y=360,width=310,height=30)

#===================Confirm Password================================================================================
confirmpassword_label = Label(page2, text='Confirm your password', bg='white', font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
confirmpassword_label.place(x=551, y=474)

confirmpassword_entry = Entry(page2, highlightthickness=0, relief=FLAT, bg='white', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'), show='*',textvariable = confirmpassword_strvar)
confirmpassword_entry.place(x=581, y=506, width=270)

confirmpassword_line = Canvas(page2, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
confirmpassword_line.place(x=551, y=528)

#==========================check box =============================================================================

chk = tkinter.Checkbutton(page2, text='I agree with the terms and condition')
chk.place(x=551, y=550)

#==========================Register Button=========================================================================
registerbtn = Button(page2, text='Register', font=('yu gothic ui', 13, 'bold'), width=13,height=1, bd=0,
                            bg='#61b4b4', cursor='hand2', activebackground='#0080b3', fg='white',command=rginsertdata )
registerbtn.place(x=550, y=600)

cancelrgbtn = Button(page2, text='Cancel', font=('yu gothic ui', 13, 'bold'), width=13,height=1, bd=0,
                            bg='#61b4b4', cursor='hand2', activebackground='#0080b3', fg='white',command=backtolg )
cancelrgbtn.place(x=720, y=600)


#==============================page4=============================
page4.config()
bg4 = Image.open('Login_background.jpeg')
photo = ImageTk.PhotoImage(bg4)
bg4_panel = Label(page4, image=photo)
bg4_panel.image = photo
bg4_panel.pack(fill='both', expand='yes')



def verify():
    cmd = str(Emailotp.get())
    temp ='python sendmail.py'+' '+cmd
    os.system(temp)
    show_frame(page5)
    
    
Emailotp = StringVar()

#============================Verify Frame===========================================
emailverification_frame = Frame(page4, bg='white', width='450', height=630)  # Color and the size of the frame
emailverification_frame.place(x=476, y=80)  # Placement of the frame

emailverificationtxt = 'Verification'
emailverificationheading = Label(emailverification_frame, text=emailverificationtxt, font=('yu gothic ui', 25, 'bold'), bg='white', fg='blue')
emailverificationheading.place(x=80, y=150 ,width=300, height=45)


#================================Email Entry==============================================================
emailotp_label = Label(page4, text='Enter your Email', bg='white', font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
emailotp_label.place(x=551, y=474)

emailotp_entry = Entry(page4, highlightthickness=0, relief=FLAT, bg='white', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'), textvariable = Emailotp)
emailotp_entry.place(x=581, y=506, width=270)

emailotp_line = Canvas(page4, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
emailotp_line.place(x=551, y=528)

#===============================Submit Button=========================================================
emailotpbtn = Button(page4, text='Submit', font=('yu gothic ui', 13, 'bold'), width=13,height=1, bd=0,
                            bg='#61b4b4', cursor='hand2', activebackground='#0080b3', fg='white', command = verify )
emailotpbtn.place(x=550, y=600)
"xxzajgfjhbvazprk"


#==============================page5=============================
page5.config()
bg5 = Image.open('Login_background.jpeg')
photo = ImageTk.PhotoImage(bg5)
bg5_panel = Label(page5, image=photo)
bg5_panel.image = photo
bg5_panel.pack(fill='both', expand='yes')

count = 3  #global variable for count calculation. Initially there are 3 attempts. So I set as 3
def verifyotp():
    global count
    global Window
    end=time.time()          # timers ends when the user clicks verfiy
    t = format(end - start)  # calculate the difference between end and start timer
    print(float(t))          #  print the time in seconds
    if float(t) >= 120:      # Check it the user enters above 2 minutes. So i set as >=120
        messagebox.showinfo("Time out", "Session Expired ...Time out Please regenerate OTP")
    else:
        cmd1=str(otpnum.get())             # Get the entered OTP
        cmd='python verify.py '+cmd1  
        os.system(cmd)                # call the verify program
        ok='Invalid OTP: '+str((count-1))+' attempts remaining' 
        count=count-1
        f1=open("status.txt","r")
        bh=f1.read()

        if count>=1 and bh != "success":

            tkinter.messagebox.askretrycancel("Error", ok)
            f1.close()
        elif count == 0 and bh != "success":
            f=open("otp.txt","w")
            f.write("")
            f.close()
            messagebox.showinfo("Oooo","Your 3 attempts was over. Please regenerate OTP")
            f1.close()
            show_frame(page4)
        elif bh == "success":
            f1.close()
            show_frame(page3)
            
start=time.time()
otpnum = StringVar()
#============================OTPVerify Frame===========================================
otpverification_frame = Frame(page5, bg='white', width='450', height=630)  # Color and the size of the frame
otpverification_frame.place(x=476, y=80)  # Placement of the frame

otpverificationtxt = 'OtpVerification'
otpverificationheading = Label(otpverification_frame, text=otpverificationtxt, font=('yu gothic ui', 25, 'bold'), bg='white', fg='blue')
otpverificationheading.place(x=80, y=150 ,width=300, height=45)

#================================OTP Entry==============================================================
otpverification_label = Label(page5, text='Enter your Email', bg='white', font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
otpverification_label.place(x=551, y=474)

otpverification_entry = Entry(page5, highlightthickness=0, relief=FLAT, bg='white', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'), textvariable = otpnum)
otpverification_entry.place(x=581, y=506, width=270)

otpverification_line = Canvas(page5, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
otpverification_line.place(x=551, y=528)

otpverificationbtn = Button(page5, text='Submit', font=('yu gothic ui', 13, 'bold'), width=13,height=1, bd=0,
                            bg='#61b4b4', cursor='hand2', activebackground='#0080b3', fg='white', command = verifyotp )
otpverificationbtn.place(x=550, y=600)




#==============================page3=============================
page3.config(bg='#273648')



#=========================Calculator=============================
def open_calculator():
    global cal
    global open_calculator
    cal = Toplevel(window)

    cal.configure(background = 'white')
    cal.resizable(width=False, height=False)
    cal.geometry("480x568+450+90")

    class Calc():
        def __init__(self):
            self.total=0
            self.current=''
            self.input_value=True
            self.check_sum=False
            self.op=''
            self.result=False
     
        def numberEnter(self, num):
            self.result=False
            firstnum=txtDisplay.get()
            secondnum=str(num)
            if self.input_value:
                self.current = secondnum
                self.input_value=False
            else:
                if secondnum == '.':
                    if secondnum in firstnum:
                        return
                self.current = firstnum+secondnum
            self.display(self.current)
     
        def sum_of_total(self):
            self.result=True
            self.current=float(self.current)
            if self.check_sum==True:
                self.valid_function()
            else:
                self.total=float(txtDisplay.get())
     
        def display(self, value):
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, value)
     
        def valid_function(self):
            if self.op == "add":
                self.total += self.current
            if self.op == "sub":
                self.total -= self.current
            if self.op == "multi":
                self.total *= self.current
            if self.op == "divide":
                self.total /= self.current
            if self.op == "mod":
                self.total %= self.current
            self.input_value=True
            self.check_sum=False
            self.display(self.total)
     
        def operation(self, op):
            self.current = float(self.current)
            if self.check_sum:
                self.valid_function()
            elif not self.result:
                self.total=self.current
                self.input_value=True
            self.check_sum=True
            self.op=op
            self.result=False
     
        def Clear_Entry(self):
            self.result = False
            self.current = "0"
            self.display(0)
            self.input_value=True
     
        def All_Clear_Entry(self):
            self.Clear_Entry()
            self.total=0
     
        def mathPM(self):
            self.result = False
            self.current = -(float(txtDisplay.get()))
            self.display(self.current)
     
        def squared(self):
            self.result = False
            self.current = math.sqrt(float(txtDisplay.get()))
            self.display(self.current)


    added_value = Calc()
     
    txtDisplay = Entry(cal, font=('Helvetica',20,'bold'),
                       bg='black',fg='white',
                       bd=30,width=28,justify=RIGHT)
    txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
    txtDisplay.insert(0,"0")
     
    numberpad = "789456123"
    i=0
    btn = []
    for j in range(2,5):
        for k in range(3):
            btn.append(Button(cal, width=6, height=2,
                              bg='black',fg='white',
                              font=('Helvetica',20,'bold'),
                              bd=4,text=numberpad[i]))
            btn[i].grid(row=j, column= k, pady = 1)
            btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
            i+=1
           
    btnClear = Button(cal, text=chr(67),width=6,
                      height=2,bg='orange',
                      font=('Helvetica',20,'bold')
                      ,bd=4, command=added_value.Clear_Entry
                     ).grid(row=1, column= 0, pady = 1)
     
    btnAllClear = Button(cal, text=chr(67)+chr(69),
                         width=6, height=2,
                         bg='orange',
                         font=('Helvetica',20,'bold'),
                         bd=4,
                         command=added_value.All_Clear_Entry
                        ).grid(row=1, column= 1, pady = 1)
     
    btnsq = Button(cal, text="\u221A",width=6, height=2,
                   bg='orange', font=('Helvetica',
                                           20,'bold'),
                   bd=4,command=added_value.squared
                  ).grid(row=1, column= 2, pady = 1)
     
    btnAdd = Button(cal, text="+",width=6, height=2,
                    bg='orange',
                    font=('Helvetica',20,'bold'),
                    bd=4,command=lambda:added_value.operation("add")
                    ).grid(row=1, column= 3, pady = 1)
     
    btnSub = Button(cal, text="-",width=6,
                    height=2,bg='orange',
                    font=('Helvetica',20,'bold'),
                    bd=4,command=lambda:added_value.operation("sub")
                    ).grid(row=2, column= 3, pady = 1)
     
    btnMul = Button(cal, text="x",width=6,
                    height=2,bg='orange',
                    font=('Helvetica',20,'bold'),
                    bd=4,command=lambda:added_value.operation("multi")
                    ).grid(row=3, column= 3, pady = 1)
     
    btnDiv = Button(cal, text="/",width=6,
                    height=2,bg='orange',
                    font=('Helvetica',20,'bold'),
                    bd=4,command=lambda:added_value.operation("divide")
                    ).grid(row=4, column= 3, pady = 1)
     
    btnZero = Button(cal, text="0",width=6,
                     height=2,bg='black',fg='white',
                     font=('Helvetica',20,'bold'),
                     bd=4,command=lambda:added_value.numberEnter(0)
                     ).grid(row=5, column= 0, pady = 1)
     
    btnDot = Button(cal, text=".",width=6,
                    height=2,bg='orange',
                    font=('Helvetica',20,'bold'),
                    bd=4,command=lambda:added_value.numberEnter(".")
                    ).grid(row=5, column= 1, pady = 1)
    btnPM = Button(cal, text=chr(177),width=6,
                   height=2,bg='orange', font=('Helvetica',20,'bold'),
                   bd=4,command=added_value.mathPM
                  ).grid(row=5, column= 2, pady = 1)
     
    btnEquals = Button(cal, text="=",width=6,
                       height=2,bg='orange',
                       font=('Helvetica',20,'bold'),
                       bd=4,command=added_value.sum_of_total
                      ).grid(row=5, column= 3, pady = 1)
     
    lblDisplay = Label(cal, text = "Scientific Calculator",
                       font=('Helvetica',30,'bold'),
                       bg='black',fg='white',justify=CENTER)
     
    lblDisplay.grid(row=0, column= 4,columnspan=4)
     
    def iExit():
        iExit = messagebox.askyesno("Scientific Calculator",
                                            "Do you want to exit ?")
        if iExit>0:
            cal.destroy()
            return
     
     
    def Standard():
        cal.resizable(width=False, height=False)
        cal.geometry("480x568+0+0")
     
    menubar = Menu(cal)
     
    # ManuBar 1 :
    filemenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'File', menu = filemenu)
    filemenu.add_command(label = "Standard", command = Standard)
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command = iExit)
     
    # ManuBar 2 :
    editmenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Edit', menu = editmenu)
    editmenu.add_command(label = "Cut")
    editmenu.add_command(label = "Copy")
    editmenu.add_separator()
    editmenu.add_command(label = "Paste")
    

    cal.config(menu=menubar)
     
    cal.mainloop()

#==============================All Transaction page=======================================

def calc_total_expenses():
    uname = uname_stvar.get()
    today = datetime.now()
    
    cursor.execute("SELECT SUM(expense) FROM transac WHERE username = ? and date LIKE ? and date LIKE ?", ( uname, str(today.month)+'%','%'+str(today.strftime("%y"))))#select data in database
    data = cursor.fetchone()
    all_trans_total_expense.config(text = data)

def list_TOF():
    global TOF_list
    
    uname = uname_stvar.get()
    connect_database()
    TOF_data = cursor.execute("SELECT TOF FROM budget WHERE username = ?",(uname,))
    TOF_list = [x for x, in TOF_data]
    AddTransTOF_combobox = ttk.Combobox(AddTransBgFrame, font=(20), width = 20, textvariable = add_TOF_strvar, values= TOF_list, state='readonly')
    AddTransTOF_combobox.place(x = 290, y = 55)
    EditTransTOF_combobox = ttk.Combobox(EditTransBgFrame, font=(20), width = 20, textvariable = edit_TOF_strvar, values=TOF_list, state='readonly')
    EditTransTOF_combobox.place(x = 290, y = 55)


#function to display transaction data from database in all transaction page
def display_trans_database():
    uname = uname_stvar.get()
    #delete inventory list
    AllTransTree.delete(*AllTransTree.get_children()) #delete treeview
    
    connect_database()#connect to database
    cursor.execute("SELECT ID, date, method, type, description, income, expense, savings FROM transac WHERE username =  ? ORDER BY date DESC",(uname,))#select data in database
    data = cursor.fetchall()#fetch data from database

    # Add our data to the screen
    count = 0
    for records in data:
        if count % 2 == 0:
            AllTransTree.insert('', END, values= records, tags = ('evenrow',))
        else:
            AllTransTree.insert('', END, values= records, tags =('oddrow',))
        count +=1
            

    # Commit changes
    conn.commit()



#function to delete transaction records
def remove_trans():
    #validate inventory is selected
    if not AllTransTree.selection():
        messagebox.showerror("Error", "Please select an item to delete")
        
    else:
    	# Add a little message box for fun
        response = messagebox.askyesno("Delete", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")

	#Add logic for message box
        if response == 1:
		# Designate selections
                x = AllTransTree.selection()

		# Create List of ID's
                ids_to_delete = []
		
		# Add selections to ids_to_delete list
                for record in x:
                    ids_to_delete.append(AllTransTree.item(record, 'values')[0])

                #connect to database
                connect_database()
		

		# Delete Everything From The Table
                cursor.executemany("DELETE FROM transac WHERE ID = ?", [(a,) for a in ids_to_delete])


		# Reset List
                ids_to_delete = []


		# Commit changes
                conn.commit()


                #display new database values
                display_trans_database()

                #display new total expense
                calc_total_expenses()

                #display new budget spent 
                current_budget()
                
		#display delete status
                messagebox.showinfo('Status' , 'You have successfully deleted the items!')


#function to reset fields in add transaction page                
def reset_add_trans_fields():
    for i in ['add_TOF_strvar', 'add_desc_strvar', 'add_amount_strvar', 'add_method_strvar', 'add_date_strvar']:
        exec(f"{i}.set('')")#set fields in Add Transaction page to empty
    add_income_intvar.set(0)#set quantity field in Add Transaction page to empty
    add_expense_intvar.set(0)#set minimum quantity field in Add Transaction page to empty
    add_savings_intvar.set(0)
    calc_total_expenses()
    
def open_add_trans():
    show_frame(AddTransFrame)
    list_TOF()
    
#function to add transaction to database
def add_trans():
    #get input from entry in Add Transaction page
    ID = str(uuid4())
    TOF = add_TOF_strvar.get()
    desc = add_desc_strvar.get()
    amt = add_amount_strvar.get()
    method = add_method_strvar.get()
    trans_date = add_date_strvar.get()
    income = add_income_intvar.get()
    expense = add_expense_intvar.get()
    uname = uname_stvar.get()
    savings = add_savings_intvar.get()


    #def format for transaction date
    format = '%m/%d/%y'
    #define true boolean
    res = True
    #validate all entries are filled in Add Transaction page :)
    if not TOF or not desc or not amt or not method or not trans_date:
            messagebox.showerror('Error', "Please fill in all the fields!")    
    else:
        try:
            #validate amount is integer
            float(amt)
        except ValueError:
            messagebox.showerror('Error', "Please insert the Amount in number form")
        else:
            try:
                #validate transaction date is in correct format
                res = bool(datetime.strptime(trans_date, format))
            except ValueError:
                messagebox.showerror('Error', "Please insert date in MM/DD/YY format or choose the date from the calendar")
                        
            else:
                #validate income or expense
                if income == 0 and expense == 0 and savings ==0:
                    messagebox.showerror('Error', "Please choose one checkbox!")    
                elif income==1 and expense ==1 and savings == 1:
                    messagebox.showerror('Error', "Please choose only one checkbox!")
                elif income ==1 and expense == 1:
                    messagebox.showerror('Error', "Please choose only one checkbox!")
                elif income ==1 and savings ==1:
                    messagebox.showerror('Error', "Please choose only one checkbox!")
                elif expense == 1 and savings ==1:
                    messagebox.showerror('Error', "Please choose only one checkbox!")
                    
                else:
                    if income == 1:

                        connect_database()#connect to database
                        conn.execute("""INSERT INTO transac (ID, date, type,
                                                method, description, income, expense,savings,username)
                                                VALUES(?,?,?,?,?,?,'-','-',?)""",
                                                (ID, trans_date, TOF, method, desc, amt,uname))#insert data into transac table in database
                        conn.commit()#commit changes to database
                        display_trans_database()#display the new list of transactions
                        reset_add_trans_fields()#set fields in add transactions to empty
                        calc_total_expenses()
                        current_budget()
                        display_budget_database()
                        messagebox.showinfo('Record added', "Record was successfully added")
                                
                    elif expense ==1:
                        connect_database()#connect to database
                        conn.execute("""INSERT INTO transac (ID, date, type,
                                                method, description, income, expense, savings, username)
                                                VALUES(?,?,?,?,?,'-',?,'-',?)""",
                                                (ID, trans_date, TOF, method, desc, amt, uname))#insert data into transac table in database
                        conn.commit()#commit changes to database
                        display_trans_database()#display the new list of transactions
                        reset_add_trans_fields()#set fields in add transaction to empty
                        current_budget()
                        calc_total_expenses()
                        display_budget_database()
                        messagebox.showinfo('Record added', "Record was successfully added")
                    else:
                        connect_database()#connect to database
                        conn.execute("""INSERT INTO transac (ID, date, type,
                                                method, description, income, expense, savings, username)
                                                VALUES(?,?,?,?,?,'-','-',?,?)""",
                                                (ID, trans_date, TOF, method, desc, amt, uname))#insert data into transac table in database
                        conn.commit()#commit changes to database
                        display_trans_database()#display the new list of transactions
                        reset_add_trans_fields()#set fields in add transaction to empty
                        calc_total_expenses()
                        current_budget()
                        display_budget_database()
                        messagebox.showinfo('Record added', "Record was successfully added")


#function to close add transaction page 
def close_add_trans():
    answer = messagebox.askyesno(title='Confirmation',
                          message='Are you sure that you want to return to All Transaction page?  The entries made will be cleared.')
    if answer:
        reset_add_trans_fields()#set fields in Add Transaction page to empty
        show_frame(transFrame)#close add transaction page
    


#convert input to string for add_trans function
add_TOF_strvar = tk.StringVar()
add_desc_strvar= tk.StringVar()
add_amount_strvar = tk.StringVar()
add_method_strvar = tk.StringVar()
add_date_strvar = tk.StringVar()
add_income_intvar = tk.IntVar()
add_expense_intvar = tk.IntVar()
add_savings_intvar = tk.IntVar()


def open_edit_trans():
    selected = AllTransTree.focus()#select transaction
    values = AllTransTree.item(selected)#get value in selection
    selection = values["values"]#set values in selection
    list_TOF()
    if not AllTransTree.selection():
        messagebox.showerror("Error", "Please select an transaction to edit")
    elif selection[5] != '-':
        list_TOF()
        #set field in edit transaction page according to selected value
        edit_ID_strvar.set(selection[0])
        edit_date_strvar.set(selection[1])
        edit_method_strvar.set (selection [2])
        connect_database()#connect to database
        cursor.execute('SELECT TOF FROM budget WHERE TOF LIKE ?', (str(selection [3]),))#get TOF ID
        TOF_strvar = cursor.fetchall()#fetch data from database
        edit_TOF_strvar.set (selection [3])
        edit_desc_strvar.set (selection [4])
        edit_income_intvar.set (1)
        edit_expense_intvar.set (0)
        edit_amount_strvar.set (selection[5])
        edit_savings_intvar.set (0)
        show_frame(EditTransFrame)
        
    elif selection [6] != '-':        
        #set field in edit transaction page according to selected value
        edit_ID_strvar.set(selection[0])
        edit_date_strvar.set(selection[1])
        edit_method_strvar.set (selection [2])
        connect_database()#connect to database
        cursor.execute('SELECT TOF FROM budget WHERE TOF LIKE ?', (str(selection [3]),))#get TOF ID
        TOF_strvar = cursor.fetchall()#fetch data from database
        edit_TOF_strvar.set (selection [3])
        edit_desc_strvar.set (selection [4])
        edit_income_intvar.set (0)
        edit_expense_intvar.set (1)
        edit_amount_strvar.set (selection[6])
        edit_savings_intvar.set (0)
        show_frame(EditTransFrame)
    else:
        #set field in edit transaction page according to selected value
        edit_ID_strvar.set(selection[0])
        edit_date_strvar.set(selection[1])
        edit_method_strvar.set (selection [2])
        connect_database()#connect to database
        cursor.execute('SELECT TOF FROM budget WHERE TOF LIKE ?', (str(selection [3]),))#get TOF ID
        TOF_strvar = cursor.fetchall()#fetch data from database
        edit_TOF_strvar.set (selection [3])
        edit_desc_strvar.set (selection [4])
        edit_income_intvar.set (0)
        edit_expense_intvar.set (0)
        edit_amount_strvar.set (selection[7])
        edit_savings_intvar.set (1)
        show_frame(EditTransFrame)

def edit_trans():
    #get input from entry in Add Transaction page
    ID = edit_ID_strvar.get()
    TOF = edit_TOF_strvar.get()
    desc = edit_desc_strvar.get()
    amt = edit_amount_strvar.get()
    method = edit_method_strvar.get()
    trans_date = edit_date_strvar.get()
    income = edit_income_intvar.get()
    expense = edit_expense_intvar.get()
    savings = edit_savings_intvar.get()


    #def format for transaction date
    format = '%m/%d/%y'
    #define true boolean
    res = True
    #validate all entries are filled in Add Transaction page :)
    if not TOF or not desc or not amt or not method or not trans_date:
            messagebox.showerror('Error', "Please fill in all the fields!")    
    else:
        try:
            #validate amount is integer
            float(amt)
        except ValueError:
            messagebox.showerror('Error', "Please insert the Amount in number form")
        else:
            try:
                #validate transaction date is in correct format
                res = bool(datetime.strptime(trans_date, format))
            except ValueError:
                messagebox.showerror('Error', "Please insert date in MM/DD/YY format or choose the date from the calendar")
                        
            else:
                #validate income or expense
                if income == 0 and expense == 0 and savings ==0:
                    messagebox.showerror('Error', "Please choose one checkbox!")    
                elif income==1 and expense ==1 and savings == 1:
                    messagebox.showerror('Error', "Please choose only one checkbox!")
                elif income ==1 and expense == 1:
                    messagebox.showerror('Error', "Please choose only one checkbox!")
                elif income ==1 and savings ==1:
                    messagebox.showerror('Error', "Please choose only one checkbox!")
                elif expense == 1 and savings ==1:
                    messagebox.showerror('Error', "Please choose only one checkbox!")
                    
                else:
                    if income == 1:

                        connect_database()#connect to database
                        conn.execute("""UPDATE transac SET date = ?, type=?,
                                                method =? , description=?, income=?, expense='-',savings ='-'
                                                WHERE ID = ?""",
                                                (trans_date, TOF, method, desc, amt, ID))#insert data into transac table in database
                        conn.commit()#commit changes to database
                        messagebox.showinfo('Record added', "Record was successfully added")
                        display_trans_database()#display the new list of transactions
                        calc_total_expenses()
                        current_budget()
                        display_budget_database()
                        show_frame(transFrame)
                                
                    elif expense ==1:
                        connect_database()#connect to database
                        conn.execute("""UPDATE transac SET date = ?, type=?,
                                                method=?, description=?, income='-', expense = ?, savings = '-'
                                                WHERE ID =?""",
                                                (trans_date, TOF, method, desc, amt, ID))#insert data into transac table in database
                        conn.commit()#commit changes to database
                        messagebox.showinfo('Record added', "Record was successfully added")
                        display_trans_database()#display the new list of transactions
                        calc_total_expenses()
                        current_budget()
                        display_budget_database()
                        show_frame(transFrame)
                    else:
                        connect_database()#connect to database
                        conn.execute("""UPDATE transac SET date = ?, type=?,
                                                method=?, description=?, income='-', expense = '-', savings = ?
                                                WHERE ID =?""",
                                                (trans_date, TOF, method, desc, amt, ID))#insert data into transac table in database
                        conn.commit()#commit changes to database
                        messagebox.showinfo('Record added', "Record was successfully added")
                        display_trans_database()#display the new list of transactions
                        calc_total_expenses()
                        current_budget()
                        display_budget_database()
                        show_frame(transFrame)

def close_edit_trans():
    answer = messagebox.askyesno(title='Confirmation',
                          message='Are you sure that you want to return to All Transaction page? Any changes made will not be saved.')
    if answer:
        show_frame(transFrame)#close edit transaction page
        
    
#convert input to string for edit_trans function
edit_ID_strvar = tk.StringVar()
edit_TOF_strvar = tk.StringVar()
edit_desc_strvar= tk.StringVar()
edit_amount_strvar = tk.StringVar()
edit_method_strvar = tk.StringVar()
edit_date_strvar = tk.StringVar()
edit_income_intvar = tk.IntVar()
edit_expense_intvar = tk.IntVar()
edit_savings_intvar = tk.IntVar()


#============================Add Transaction Page UI=================================
AddTransFrame = Frame(page3, bg='#212429', highlightbackground='#212429', highlightthickness=1)
AddTransFrame.place(x=150,y=20, height=715, width = 1200)

AddTransBottomFrame = Frame(AddTransFrame, bg = '#2A2E31')
AddTransBottomFrame.place(x=40,y=50, height=640, width = 1115)

AddTransTopLabel = Label(AddTransBottomFrame, text='Add Transaction', font=('Arial', 40,'italic'), fg='white', bg='#2A2E31')
AddTransTopLabel.place(x=30, y=20)

AddTransBackButton = Button(AddTransBottomFrame, text= "Back", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = close_add_trans)
AddTransBackButton.place(x=1010, y=40)

AddTransBgFrame =  Frame(AddTransBottomFrame, bg = '#525557')
AddTransBgFrame.place(x=30,y=98, height=515, width = 1050)

AddTransTOF_label = Label (AddTransBgFrame, text='Type of transaction:', font=('Arial',20,'italic'), fg='white', bg='#525557')
AddTransTOF_label.place(x=30, y=50)



AddTransDesc_label = Label (AddTransBgFrame, text='Description:', font=('Arial',20,'italic'), fg='white', bg='#525557')
AddTransDesc_label.place(x=30, y=130)


AddTransDesc_entry = Entry(AddTransBgFrame, font=(20), width = 20, textvariable = add_desc_strvar)
AddTransDesc_entry.place(x = 290, y = 135)

AddTransIncome_label = Label (AddTransBgFrame, text=' Income          ', font=('Arial',20,'italic'), fg='white', bg='#988E8E')
AddTransIncome_label.place(x=30, y=220)


AddTransIncome_checkbutton = Checkbutton(AddTransBgFrame, bg='#988E8E', variable = add_income_intvar).place(x=175, y=225)

AddTransExpense_label = Label (AddTransBgFrame, text=' Expense        ', font=('Arial',20,'italic'), fg='white', bg='#988E8E')
AddTransExpense_label.place(x=250, y=220)

AddTransExpense_checkbutton = Checkbutton(AddTransBgFrame, bg='#988E8E', variable = add_expense_intvar).place(x=400, y=225)

AddTransSavings_label = Label (AddTransBgFrame, text=' Savings       ', font=('Arial',20,'italic'), fg='white', bg='#988E8E')
AddTransSavings_label.place(x=470, y=220)

AddTransSavings_checkbutton = Checkbutton(AddTransBgFrame, bg='#988E8E', variable = add_savings_intvar).place(x=605, y=225)


AddTransAmount_label = Label (AddTransBgFrame, text='Amount:', font=('Arial',20,'italic'), fg='white', bg='#525557')
AddTransAmount_label.place(x=30, y=300)

AddTransAmount_entry = Entry(AddTransBgFrame, font=(20), width = 20, textvariable = add_amount_strvar)
AddTransAmount_entry.place(x = 290, y = 305)

AddTransMethod_label = Label (AddTransBgFrame, text='Method:', font=('Arial',20,'italic'), fg='white', bg='#525557')
AddTransMethod_label.place(x=30, y=380)

AddTransMethod_entry = Entry(AddTransBgFrame, font=(20), width = 20, textvariable = add_method_strvar)
AddTransMethod_entry.place(x = 290, y = 385)

AddTransDate_label = Label(AddTransBgFrame, text='Date:', font=('Arial',20,'italic'), fg='white', bg='#525557')
AddTransDate_label.place(x=550, y=50)

AddTransEnter_button = Button(AddTransBgFrame, text= "Enter", font=('Inter', 16, 'italic'), fg='white', bg = '#988E8E', padx = 15, command = add_trans)
AddTransEnter_button.place(x=480, y=440)

#=============================Edit Transaction Page UI=========================================

EditTransFrame = Frame(page3, bg='#212429', highlightbackground='#212429', highlightthickness=1)
EditTransFrame.place(x=150,y=20, height=715, width = 1200)

EditTransBottomFrame = Frame(EditTransFrame, bg = '#2A2E31')
EditTransBottomFrame.place(x=40,y=50, height=640, width = 1115)

EditTransTopLabel = Label(EditTransBottomFrame, text='Edit Transaction', font=('Arial', 40,'italic'), fg='white', bg='#2A2E31')
EditTransTopLabel.place(x=30, y=20)

EditTransBackButton = Button(EditTransBottomFrame, text= "Back", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = close_edit_trans)
EditTransBackButton.place(x=1010, y=40)

EditTransBgFrame =  Frame(EditTransBottomFrame, bg = '#525557')
EditTransBgFrame.place(x=30,y=98, height=515, width = 1050)

EditTransTOF_label = Label (EditTransBgFrame, text='Type of transaction:', font=('Arial',20,'italic'), fg='white', bg='#525557')
EditTransTOF_label.place(x=30, y=50)



EditTransDesc_label = Label (EditTransBgFrame, text='Description:', font=('Arial',20,'italic'), fg='white', bg='#525557')
EditTransDesc_label.place(x=30, y=130)


EditTransDesc_entry = Entry(EditTransBgFrame, font=(20), width = 20, textvariable = edit_desc_strvar)
EditTransDesc_entry.place(x = 290, y = 135)

EditTransIncome_label = Label (EditTransBgFrame, text=' Income          ', font=('Arial',20,'italic'), fg='white', bg='#988E8E')
EditTransIncome_label.place(x=30, y=220)


EditTransIncome_checkbutton = Checkbutton(EditTransBgFrame, bg='#988E8E', variable = edit_income_intvar).place(x=175, y=225)

EditTransExpense_label = Label (EditTransBgFrame, text=' Expense        ', font=('Arial',20,'italic'), fg='white', bg='#988E8E')
EditTransExpense_label.place(x=250, y=220)

EditTransExpense_checkbutton = Checkbutton(EditTransBgFrame, bg='#988E8E', variable = edit_expense_intvar).place(x=400, y=225)

EditTransSavings_label = Label (EditTransBgFrame, text=' Savings       ', font=('Arial',20,'italic'), fg='white', bg='#988E8E')
EditTransSavings_label.place(x=470, y=220)

EditTransSavings_checkbutton = Checkbutton(EditTransBgFrame, bg='#988E8E', variable = edit_savings_intvar).place(x=605, y=225)


EditTransAmount_label = Label (EditTransBgFrame, text='Amount:', font=('Arial',20,'italic'), fg='white', bg='#525557')
EditTransAmount_label.place(x=30, y=300)

EditTransAmount_entry = Entry(EditTransBgFrame, font=(20), width = 20, textvariable = edit_amount_strvar)
EditTransAmount_entry.place(x = 290, y = 305)

EditTransMethod_label = Label (EditTransBgFrame, text='Method:', font=('Arial',20,'italic'), fg='white', bg='#525557')
EditTransMethod_label.place(x=30, y=380)

EditTransMethod_entry = Entry(EditTransBgFrame, font=(20), width = 20, textvariable = edit_method_strvar)
EditTransMethod_entry.place(x = 290, y = 385)

EditTransDate_label = Label(EditTransBgFrame, text='Date:', font=('Arial',20,'italic'), fg='white', bg='#525557')
EditTransDate_label.place(x=550, y=50)

EditTransEnter_button = Button(EditTransBgFrame, text= "Enter", font=('Inter', 16, 'italic'), fg='white', bg = '#988E8E', padx = 15, command = edit_trans)
EditTransEnter_button.place(x=480, y=440)

EditID_entry = Entry(EditTransBgFrame, font=(20), width = 20, textvariable = edit_ID_strvar)
EditID_entry.place(x = 600, y = 440)



# Add Calendar in Add Transaction page
#get calendar date 
def grad_date():
    Add_trans_get_date_entry.delete(0,END)
    Add_trans_get_date_entry.insert(0, Add_trans_cal.get_date())
    
Add_trans_cal = Calendar(AddTransBgFrame, selectmode = 'day', year = 2022, month = 10, day = 30)
Add_trans_cal.place(x = 700, y = 60)



Add_trans_cal_button = Button(AddTransBgFrame, text = "Get Date",font=('Inter', 12, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = grad_date).place(x = 780, y = 265)
 

Add_trans_get_date_entry = Entry(AddTransBgFrame, font=(15), width = 15, textvariable = add_date_strvar)
Add_trans_get_date_entry.place(x = 740, y = 320)




# Add Calendar in Edit Transaction page
#get calendar date 
def edit_grad_date():
    Edit_trans_get_date_entry.delete(0,END)
    Edit_trans_get_date_entry.insert(0, Edit_trans_cal.get_date())
    
Edit_trans_cal = Calendar(EditTransBgFrame, selectmode = 'day', year = 2022, month = 10, day = 30)
Edit_trans_cal.place(x = 700, y = 60)



Edit_trans_cal_button = Button(EditTransBgFrame, text = "Get Date",font=('Inter', 12, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = edit_grad_date).place(x = 780, y = 265)
 

Edit_trans_get_date_entry = Entry(EditTransBgFrame, font=(15), width = 15, textvariable = edit_date_strvar)
Edit_trans_get_date_entry.place(x = 740, y = 320)


#============================ All Transaction Page===============================
transFrame = Frame(page3, bg='#212429', highlightbackground='#212429', highlightthickness=1)
transFrame.place(x=150,y=20, height=715, width = 1200)

def search_trans():
    uname = uname_stvar.get()
    connect_database()
    find = search_trans_strvar.get()
    if not find:
        messagebox.showerror('Error', 'Please fill in the search field')
    else:
        cursor.execute("""SELECT ID, date, method, type, description, income, expense FROM transac
                            WHERE type LIKE ? and username = ? ORDER BY date DESC""", ('%'+find+'%', uname,))#select data from database
        data = cursor.fetchall()#fetch data selected
        if len(data) !=0:#validate record existence
            AllTransTree.delete(*AllTransTree.get_children())
            count = 0
            for records in data:
                if count % 2 == 0:
                    AllTransTree.insert('', END, values= records, tags = ('evenrow',))
                else:
                    AllTransTree.insert('', END, values= records, tags =('oddrow',))
                count +=1
                        
                conn.commit()#commit changes
        else:
            messagebox.showerror('Error', 'Record is not found')
            
def reset_trans():
    display_trans_database()
    for i in ['search_trans_strvar']:
        exec(f"{i}.set('')")#clear search field

search_trans_strvar = tk.StringVar()

TransTopLabel = Label(transFrame, text='All Transaction', font=('Arial', 40,'italic'), fg='white', bg='#212429')
TransTopLabel.place(x=40, y=15)

TransBottomFrame = Frame(transFrame, bg = '#2A2E31')
TransBottomFrame.place(x=40,y=85, height=600, width = 1115)

TransBottomLabel = Label(TransBottomFrame, text="Search for Type of Transaction", font=('Arial', 15,'italic'), fg='white', bg = '#2A2E31')
TransBottomLabel.place(x=15, y=10)

TransSearchEntry = Entry(TransBottomFrame, font = 15, text = 'Search', textvariable = search_trans_strvar)
TransSearchEntry.place(x=19, y=53)

SearchTransButton = Button(TransBottomFrame, text= "Search", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = search_trans)
SearchTransButton.place(x=260, y=50)

AddTransButton = Button(TransBottomFrame, text= "Add", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = open_add_trans)
AddTransButton.place(x=885, y=50)

EditTransButton = Button(TransBottomFrame, text= "Edit", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = open_edit_trans)
EditTransButton.place(x= 1030, y=50 )

DeleteTransButton = Button(TransBottomFrame, text= "Delete", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = remove_trans)
DeleteTransButton.place(x= 948, y=50)

ResetTransButton = Button(TransBottomFrame, text= "Reset", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = reset_trans)
ResetTransButton.place(x=350, y=50)

all_trans_total_expense = Label(transFrame, font=('Arial', 15,'italic'), fg='white', bg = '#212429')
all_trans_total_expense.place(x=985, y=40)
all_trans_total_expense_label = Label(transFrame, font=('Arial', 15,'italic'),text = 'Total Expenses for Current Month: RM', fg='white', bg = '#212429')
all_trans_total_expense_label.place(x=650, y=40)

calc_total_expenses()



#find treeview
#all transaction treeview
#Add some style:
style = ttk.Style()

style.theme_use("clam")

style.configure("style1.Treeview",
                    background="#6C6C6C",
                    foreground="white",
                    rowheight=30,
                    fieldbackground="silver")
style.configure("Treeview.Heading", background = "#2A2E31", foreground = 'White', rowheight=30)
style.configure("Budget.Treeview",
                    background="#6C6C6C",
                    foreground="white",
                    rowheight=65,
                    fieldbackground='#2A2E31',
                    font = ('None', 20))
style.configure("Credit.Treeview",
                    background="#6C6C6C",
                    foreground="white",
                    rowheight=80,
                    fieldbackground='silver',
                    font = ('None', 18))


style.configure("HomeP.Treeview",
                    background="#33373A",
                    foreground="white",
                    rowheight=80,
                    fieldbackground='#33373A',
                    font = ('None', 18))





#configure transaction treeview
AllTransTree = ttk.Treeview(TransBottomFrame, selectmode="extended", show='headings',
                    columns = ('ID', 'Date', 'Method', 'Type', 'Desc', 'Income', 'Expense', 'Savings'), style = "style1.Treeview")
AllTransTree.place(x = 15, y = 95, relwidth=0.97, relheight=0.82)



# Create striped row tags
AllTransTree.tag_configure('oddrow', background="#6C6C6C")
AllTransTree.tag_configure('evenrow', background="#8D8D8D")


#configure horizontal and vertical scrollbar for treeview
x_scroller= Scrollbar(AllTransTree, orient = HORIZONTAL, command =AllTransTree.xview)
y_scroller= Scrollbar(AllTransTree, orient = VERTICAL, command =AllTransTree.yview)
x_scroller.pack(side= BOTTOM, fill=X)
y_scroller.pack(side= RIGHT, fill=Y)
AllTransTree.config(yscrollcommand=y_scroller.set, xscrollcommand=x_scroller.set)

#set heading name for treeview column
AllTransTree.heading('ID', text = 'ID', anchor=CENTER)
AllTransTree.heading('Date', text = 'Date', anchor=CENTER)
AllTransTree.heading('Method', text = 'Method', anchor=CENTER)
AllTransTree.heading('Type', text = 'Type of Transaction', anchor=CENTER)
AllTransTree.heading('Desc', text = 'Description', anchor=CENTER)
AllTransTree.heading('Income', text = 'Income(RM)', anchor=CENTER)
AllTransTree.heading('Expense', text = 'Expense(RM)', anchor=CENTER)
AllTransTree.heading('Savings', text = 'Savings(RM)', anchor=CENTER)

AllTransTree.column("ID", anchor=CENTER, width=100)
AllTransTree.column("Date", anchor=CENTER, width=100)
AllTransTree.column("Method", anchor=CENTER, width=100)
AllTransTree.column("Type", anchor=CENTER, width=150)
AllTransTree.column("Desc", anchor=CENTER, width=150)
AllTransTree.column("Income", anchor=CENTER, width=100)
AllTransTree.column("Expense", anchor=CENTER, width=100)
AllTransTree.column("Savings", anchor=CENTER, width=100)

 



#================================Show Add and Edit Budget Page Function===================================
def open_add_budget():
    show_frame(AddBudgetFrame)

def open_edit_budget():
    selected = BudgetTree.focus()
    values = BudgetTree.item(selected)
    selection = values["values"]
    if not BudgetTree.selection():
        messagebox.showerror("Error", "Please select a budget or saving to edit")
    else:
        if selection[1] =='savings':
            edit_saving_amt_strvar.set(selection[6])
            edit_saving_TOF_strvar.set(selection[1])
            show_frame(EditSavingFrame)
        
        else:
            TOF = selection[1]
            edit_budget_amt_strvar.set(selection[6])
            edit_budget_TOF_strvar.set(selection[1])
            show_frame(EditBudgetFrame)

    
#set variables to string
add_budget_TOF_strvar = tk.StringVar()
add_budget_target_strvar= tk.StringVar()
edit_budget_TOF_strvar = tk.StringVar()
edit_budget_amt_strvar = tk.StringVar()
edit_saving_amt_strvar = tk.StringVar()
edit_saving_TOF_strvar= tk.StringVar()


#function to display transaction data from database in all transaction page
def display_budget_database():
    current_budget()
    uname = uname_stvar.get()
    #delete inventory list
    BudgetTree.delete(*BudgetTree.get_children()) #delete treeview
    
    connect_database()#connect to database
    cursor.execute("SELECT TOF, current_amt, budget_set FROM budget WHERE username =  ? ",(uname,))#select data in database
    data1 = cursor.fetchall()#fetch data from database


    # Add our data to the screen
    count = 0

    for records in data1:
        if int(records[1])>int(records[2]) and str(records[0]) == 'savings':
            BudgetTree.insert('', END, values= ('',records[0],'RM',records[1],'of','RM',records[2],), tags = ('saving',))
        elif int(records[1])>int(records[2]):
            BudgetTree.insert('', END, values= ('',records[0],'RM',records[1],'of','RM',records[2],), tags = ('exceed',))
        elif int(records[1])== int(records[2]):
            BudgetTree.insert('', END, values= ('',records[0],'RM',records[1],'of','RM',records[2],), tags = ('equal',))

        elif count % 2 == 0:
            BudgetTree.insert('', END, values= ('',records[0],'RM',records[1],'of','RM',records[2],), tags = ('evenrow',))
        else:
            BudgetTree.insert('', END, values= ('',records[0],'RM',records[1],'of','RM',records[2],), tags =('oddrow',))
        count +=1


            

    # Commit changes
    conn.commit()

def current_budget():
    uname = uname_stvar.get()
    today = datetime.now()
    connect_database()#connect to database
    cursor.execute ("SELECT TOF FROM budget WHERE username =?",(uname,))
    data = cursor.fetchall()
    for TOF in data:
        data2 = TOF[0]
        print(str(today.month)+'____'+ str(today.strftime("%y")))
        cursor.execute("SELECT SUM(expense) FROM transac WHERE type =? and date LIKE ? and username =?",(data2, str(today.month)+'____'+ str(today.strftime("%y")),uname,))
        total_string = str(cursor.fetchone()).strip("(,)")
        if total_string == 'None':
            conn.execute("UPDATE budget SET current_amt =? WHERE TOF =? and username = ?", (0, data2 ,uname,))#select data in database
            conn.commit()
            
        else:
            total_float = float(total_string)
            conn.execute("UPDATE budget SET current_amt =? WHERE TOF =? and username = ?", (total_float, data2 ,uname,))#select data in database
            conn.commit()
    cursor.execute ("SELECT SUM(savings) FROM transac WHERE date LIKE ?  and username =?",(str(today.month)+'____'+str(today.strftime("%y")),uname,))
    saving_string = str(cursor.fetchone()).strip("(,)")
    saving_float = float(saving_string)
    conn.execute("UPDATE budget set current_amt = ? WHERE TOF = 'savings' and username =?",(saving_float, uname,))
    conn.commit()


def add_budget():
    #get input from entry in Add Transaction page
    TOF = add_budget_TOF_strvar.get()
    target = add_budget_target_strvar.get()
    uname= uname_stvar.get()
    
    if not TOF or not target:
            messagebox.showerror('Error', "Please fill in all the fields!")    
    else:
        try:
            #validate amount is integer
            float(target)
        except ValueError:
            messagebox.showerror('Error', "Please insert the Budget Limit in number form")
        else:
            connect_database()
            cursor.execute("SELECT TOF from budget WHERE TOF =? and username =?",(TOF, uname,))
            find = cursor.fetchall()
            if len(find)!= 0:
                messagebox.showerror('Error','Type of Transaction already exists')
            else:
                connect_database()#connect to database
                conn.execute("""INSERT INTO budget (TOF, budget_set, username, current_amt)
                                VALUES(?,?,?,0)""",
                                (TOF, target,uname))#insert data into transac table in database
                conn.commit()#commit changes to database
                messagebox.showinfo('Record added', "Record was successfully added")
                display_budget_database()#display the new list of transactions
                reset_add_budget_fields()
                show_frame(budgetFrame)

def reset_add_budget_fields():
    for i in ['add_budget_TOF_strvar']:
        exec(f"{i}.set('')")#set fields in Add Budget page to empty
    add_budget_target_strvar.set(0)#set quantity field in Add Budget page to empty)
                               
                   
def close_add_budget():
    answer = messagebox.askyesno(title='Confirmation',
                          message='Are you sure that you want to return to Budget and Savings page? Any changes made will not be saved.')
    if answer:
        reset_add_budget_fields()
        show_frame(budgetFrame)#close edit transaction page
        
def close_edit_budget():
    answer = messagebox.askyesno(title='Confirmation',
                          message='Are you sure that you want to return to Budget and Savings page? Any changes made will not be saved.')
    if answer:
        show_frame(budgetFrame)#close edit transaction page


def edit_budget():
    TOF = edit_budget_TOF_strvar.get()
    target = edit_budget_amt_strvar.get()
    uname= uname_stvar.get()
    if not target:
            messagebox.showerror('Error', "Please fill in all the fields!")    
    else:
        try:
            #validate amount is integer
            float(target)
        except ValueError:
            messagebox.showerror('Error', "Please insert the Budget Limit in number form")
        else:
            connect_database()
            cursor.execute("UPDATE budget SET budget_set =? WHERE TOF =? and username =?",(target, TOF, uname,))
            conn.commit()#commit changes to database
            messagebox.showinfo('Record added', "Record was successfully edited")
            display_budget_database()#display the new list of transactions
            show_frame(budgetFrame)

def edit_saving():
    TOF = edit_saving_TOF_strvar.get()
    target = edit_saving_amt_strvar.get()
    uname= uname_stvar.get()
    if not target:
            messagebox.showerror('Error', "Please fill in all the fields!")    
    else:
        try:
            #validate amount is integer
            float(target)
        except ValueError:
            messagebox.showerror('Error', "Please insert the Saving Target in number form")
        else:
            connect_database()
            cursor.execute("UPDATE budget SET budget_set =? WHERE TOF =? and username =?",(target, TOF, uname,))
            conn.commit()#commit changes to database
            messagebox.showinfo('Record added', "Record was successfully edited")
            display_budget_database()#display the new list of transactions
            show_frame(budgetFrame)

def remove_budget():
    uname = uname_stvar.get()
    selected = BudgetTree.focus()
    values = BudgetTree.item(selected)
    selection = values["values"]
    if not BudgetTree.selection():
        messagebox.showerror("Error", "Please select an item to delete")
    elif selection[1] == 'savings':
        messagebox.showerror("Error", "savings cannot be deleted")
        
    else:
    	# Add a little message box for fun
        response = messagebox.askyesno("Delete", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")

	#Add logic for message box
        if response == 1:
		# Designate selections
                x = BudgetTree.selection()
                
                # Create List of ID's
                ids_to_delete = []

                # Add selections to ids_to_delete list
                for record in x:
                    ids_to_delete.append(BudgetTree.item(record, 'values')[1])
                if 'savings' in ids_to_delete:
                    messagebox.showerror("Error", "savings cannot be deleted")
                else:  

                    #connect to database
                    connect_database()
                    

                    # Delete Everything From The Table
                    cursor.executemany("DELETE FROM budget WHERE TOF = ? and username = ?", [(a,uname,) for a in ids_to_delete])


                    # Reset List
                    ids_to_delete = []


                    # Commit changes
                    conn.commit()

                    display_budget_database()

                


#============================Budget Page=================================
budgetFrame = Frame(page3, bg='#212429', highlightbackground='#212429', highlightthickness=1)
budgetFrame.place(x=150,y=20, height=715, width = 1200)

BudgetTopLabel = Label(budgetFrame, text='Budget & Savings', font=('Arial', 40,'italic'), fg='white', bg='#212429')
BudgetTopLabel.place(x=40, y=20)

BudgetBottomFrame = Frame(budgetFrame, bg = '#2A2E31')
BudgetBottomFrame.place(x=40,y=100, height=580, width = 1115)


AddBudgetButton = Button(budgetFrame, text= "Add", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = open_add_budget)
AddBudgetButton.place(x=885, y=40)

EditBudgetButton = Button(budgetFrame, text= "Edit", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = open_edit_budget)
EditBudgetButton.place(x= 1030, y=40 )

DeleteBudgetButton = Button(budgetFrame, text= "Delete", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = remove_budget)
DeleteBudgetButton.place(x= 948, y=40)



    
#configure budget treeview
BudgetTree = ttk.Treeview(BudgetBottomFrame, selectmode="extended",show ='',
                    columns = ('space','type', 'rm1','curr', 'of','rm2', 'budget'),style = "Budget.Treeview")
BudgetTree.place(x = 50, y = 50, relwidth=0.9, relheight=0.9)

# Create striped row tags
BudgetTree.tag_configure('oddrow', background="#54585B")
BudgetTree.tag_configure('evenrow', background="#64686B")
BudgetTree.tag_configure('exceed', background="#800000")
BudgetTree.tag_configure('equal', background="#FEBE00")
BudgetTree.tag_configure('saving', background="#4C9A2A")  


#configure horizontal and vertical scrollbar for treeview
budget_y_scroller= Scrollbar(BudgetTree, orient = VERTICAL, command =BudgetTree.yview)
budget_y_scroller.pack(side= RIGHT, fill=Y)
BudgetTree.config(yscrollcommand=budget_y_scroller.set)
BudgetTree.column("space", anchor='w', width=50)
BudgetTree.column("type", anchor='w', width=300)
BudgetTree.column("rm1", anchor= CENTER, width=70)
BudgetTree.column("curr", anchor='w', width=100)
BudgetTree.column("of", anchor=CENTER, width=50)
BudgetTree.column("rm2", anchor='e', width=70)
BudgetTree.column("budget", anchor='w', width=200)


#============================Add Budget Page=================================

AddBudgetFrame = Frame(page3, bg='#212429', highlightbackground='#212429', highlightthickness=1)
AddBudgetFrame.place(x=150,y=20, height=715, width = 1200)

AddBudgetBottomFrame = Frame(AddBudgetFrame, bg = '#2A2E31')
AddBudgetBottomFrame.place(x=40,y=130, height=530, width = 1115)

AddBudgetTopLabel = Label(AddBudgetFrame, text='Add Budget', font=('Arial', 40,'italic'), fg='white', bg='#212429')
AddBudgetTopLabel.place(x=50, y=30)

AddBudgetBackButton = Button(AddBudgetFrame, text= "Back", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = close_add_budget)
AddBudgetBackButton.place(x=1020, y=50)


AddBudgetTOFLabel = Label(AddBudgetBottomFrame, text='Type of Transaction : ', font=('Arial', 28,'italic'), fg='white', bg='#2A2E31')
AddBudgetTOFLabel.place(x=200, y=120)

AddBudgetTOF_entry = Entry(AddBudgetBottomFrame, font=(25), width = 25, textvariable = add_budget_TOF_strvar)
AddBudgetTOF_entry.place(x = 590, y = 130)


AddBudgetTargetLabel = Label(AddBudgetBottomFrame, text='Budget Limit (RM)  : ', font=('Arial', 28,'italic'), fg='white', bg='#2A2E31')
AddBudgetTargetLabel.place(x=200, y=220)


AddBudgetTarget_entry = Entry(AddBudgetBottomFrame, font=(25), width = 25, textvariable = add_budget_target_strvar)
AddBudgetTarget_entry.place(x = 590, y = 230)



AddBudgetAddButton = Button(AddBudgetBottomFrame, text= "Add", font=('Inter', 20, 'italic'), fg='white', bg = '#988E8E', padx = 20, pady = 0, command = add_budget)
AddBudgetAddButton.place(x=500, y=380)

#============================Edit Budget Page=================================

EditBudgetFrame = Frame(page3, bg='#212429', highlightbackground='#212429', highlightthickness=1)
EditBudgetFrame.place(x=150,y=20, height=715, width = 1200)

EditBudgetBottomFrame = Frame(EditBudgetFrame, bg = '#2A2E31')
EditBudgetBottomFrame.place(x=40,y=130, height=530, width = 1115)

EditBudgetTopLabel = Label(EditBudgetFrame, text='Edit Budget', font=('Arial', 40,'italic'), fg='white', bg='#212429')
EditBudgetTopLabel.place(x=50, y=30)

EditBudgetBackButton = Button(EditBudgetFrame, text= "Back", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = close_edit_budget)
EditBudgetBackButton.place(x=1020, y=50)


EditBudgetTOFLabel = Label(EditBudgetBottomFrame, text='Type of Transaction : ', font=('Arial', 28,'italic'), fg='white', bg='#2A2E31')
EditBudgetTOFLabel.place(x=200, y=120)

EditBudgetTOF_entry = Entry(EditBudgetBottomFrame, font = 25, textvariable= edit_budget_TOF_strvar, state = 'disabled' )
EditBudgetTOF_entry.place(x = 590, y = 130)


EditBudgetTargetLabel = Label(EditBudgetBottomFrame, text='Budget Target(RM)  : ', font=('Arial', 28,'italic'), fg='white', bg='#2A2E31')
EditBudgetTargetLabel.place(x=200, y=220)


EditBudgetTarget_entry = Entry(EditBudgetBottomFrame, font=(30), width = 25, textvariable = edit_budget_amt_strvar)
EditBudgetTarget_entry.place(x = 590, y = 230)



EditBudgetAddButton = Button(EditBudgetBottomFrame, text= "Save", font=('Inter', 20, 'italic'), fg='white', bg = '#988E8E', padx = 20, pady = 0, command = edit_budget)
EditBudgetAddButton.place(x=500, y=380)

#============================Edit Saving Page=================================

EditSavingFrame = Frame(page3, bg='#212429', highlightbackground='#212429', highlightthickness=1)
EditSavingFrame.place(x=150,y=20, height=715, width = 1200)

EditSavingBottomFrame = Frame(EditSavingFrame, bg = '#2A2E31')
EditSavingBottomFrame.place(x=40,y=130, height=530, width = 1115)

EditSavingTopLabel = Label(EditSavingFrame, text='Edit Savings', font=('Arial', 40,'italic'), fg='white', bg='#212429')
EditSavingTopLabel.place(x=50, y=30)

EditSavingBackButton = Button(EditSavingFrame, text= "Back", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = close_edit_budget)
EditSavingBackButton.place(x=1020, y=50)


EditSavingTOFLabel = Label(EditSavingBottomFrame, text='Type of Transaction  : ', font=('Arial', 28,'italic'), fg='white', bg='#2A2E31')
EditSavingTOFLabel.place(x=200, y=120)

EditSavingTOF_entry = Entry(EditSavingBottomFrame, font=25, textvariable = edit_saving_TOF_strvar, state= 'disabled')
EditSavingTOF_entry.place(x = 590, y = 130)


EditSavingTargetLabel = Label(EditSavingBottomFrame, text='Savings Target(RM) : ', font=('Arial', 28,'italic'), fg='white', bg='#2A2E31')
EditSavingTargetLabel.place(x=200, y=220) 


EditSavingTarget_entry = Entry(EditSavingBottomFrame, font=(30), width = 25, textvariable = edit_saving_amt_strvar)
EditSavingTarget_entry.place(x = 590, y = 230)



EditSavingsAddButton = Button(EditSavingBottomFrame, text= "Save", font=('Inter', 20, 'italic'), fg='white', bg = '#988E8E', padx = 20, pady = 0, command =edit_saving)
EditSavingsAddButton.place(x=500, y=380)
#=========Open add and edit credit page====================

add_credit_name_strvar = tk.StringVar()
add_credit_amt_strvar = tk.StringVar()
add_credit_due_strvar = tk.StringVar()
add_credit_limit_strvar = tk.StringVar()

edit_credit_name_strvar = tk.StringVar()
edit_credit_amt_strvar = tk.StringVar()
edit_credit_due_strvar = tk.StringVar()
edit_credit_limit_strvar = tk.StringVar()





def open_add_credit():
    show_frame(AddCreditFrame)

def open_edit_credit():
    selected = CreditDueTree.focus()
    values = CreditDueTree.item(selected)
    selection = values["values"]
    if not CreditDueTree.selection():
        messagebox.showerror("Error", "Please select a budget or saving to edit")
    else:
        edit_credit_name_strvar.set(selection[0])
        edit_credit_amt_strvar.set(selection[1])
        edit_credit_limit_strvar.set(selection[2])
        edit_credit_due_strvar.set(selection[3])
        show_frame(EditCreditFrame)
        

with Image.open("Blue_Square.png") as photo_b:
    blu_pic = ImageTk.PhotoImage(photo_b)
with Image.open("yellow_square.png") as photo_y:
    ylw_pic = ImageTk.PhotoImage(photo_y)
with Image.open("red_square.png") as photo_r:
    red_pic = ImageTk.PhotoImage(photo_r)
with Image.open("black_square.png") as photo_blk:
    blk_pic = ImageTk.PhotoImage(photo_blk)
with Image.open("purple_square.png") as photo_pur:
    pur_pic = ImageTk.PhotoImage(photo_pur)
    
with Image.open("black_red_even.PNG") as photo_blre:
    blre_pic = ImageTk.PhotoImage(photo_blre)
with Image.open("purple_red_even.JPG") as photo_pre:
    pre_pic = ImageTk.PhotoImage(photo_pre)
with Image.open("blue_red_even.JPG") as photo_bre:
    bre_pic = ImageTk.PhotoImage(photo_bre)
with Image.open("black_yellow_even.PNG") as photo_blye:
    blye_pic = ImageTk.PhotoImage(photo_blye)
with Image.open("purple_yellow_even.PNG") as photo_pye:
    pye_pic = ImageTk.PhotoImage(photo_pye)
with Image.open("blue_yellow_even.PNG") as photo_bye:
    bye_pic = ImageTk.PhotoImage(photo_bye)
    
with Image.open("black_red_odd.JPG") as photo_blro:
    blro_pic = ImageTk.PhotoImage(photo_blro)
with Image.open("purple_red_odd.png") as photo_pro:
    pro_pic = ImageTk.PhotoImage(photo_pro)
with Image.open("blue_red_odd.JPG") as photo_bro:
    bro_pic = ImageTk.PhotoImage(photo_bro)
with Image.open("black_yellow_odd.JPG") as photo_blyo:
    blyo_pic = ImageTk.PhotoImage(photo_blyo)
with Image.open("purple_yellow_odd.JPG") as photo_pyo:
    pyo_pic = ImageTk.PhotoImage(photo_pyo)
with Image.open("blue_yellow_odd.JPG") as photo_byo:
    byo_pic = ImageTk.PhotoImage(photo_byo)
    


def display_credit_database():

    uname = uname_stvar.get()
    today = datetime.today()
    today_date = today.strftime('%m/%d/%y')
    today_format = datetime.strptime(today_date,'%m/%d/%y')

    


    #delete inventory list
    CreditDueTree.delete(*CreditDueTree.get_children()) #delete treeview
    
    connect_database()#connect to database
    cursor.execute("SELECT card_name, amt_used, credit_limit ,due_date FROM credit_due WHERE username =  ? ",(uname,))#select data in database
    data1 = cursor.fetchall()#fetch data from database
    

    # Add our data to the screen
    count = 0

    for records in data1:
        CreditDueTree.image = (blre_pic, pre_pic, blro_pic,blk_pic,bre_pic,red_pic,blye_pic,pye_pic,bye_pic,ylw_pic,pur_pic,blu_pic,pro_pic,bro_pic,blyo_pic,pyo_pic,byo_pic)
        percent = float(records[1])/float(records[2])
        due_format = datetime.strptime(records[3], '%m/%d/%y')
        diff = due_format - today_format

        
        if count % 2 == 0:
            if diff.days <1 :
                if percent >= 0.8:
                    CreditDueTree.insert('', END, values= (records), image =(blre_pic), tags = ('evenrow',))
                    
                elif percent >=0.5:
                    CreditDueTree.insert('', END, values= (records), image =(pre_pic), tags = ('evenrow',))

                elif percent >=0.3:
                    CreditDueTree.insert('', END, values= (records), image =(bre_pic), tags = ('evenrow',))

                else:
                    CreditDueTree.insert('', END, values= (records), image =(red_pic), tags = ('evenrow',))

            elif diff.days<6:
                if percent>=0.8:
                    CreditDueTree.insert('', END, values= (records), image =(blye_pic), tags = ('evenrow',))

                    
                elif percent >=0.5:
                    CreditDueTree.insert('', END, values= (records), image =(pye_pic), tags = ('evenrow',))
                    
                elif percent >=0.3:
                    CreditDueTree.insert('', END, values= (records), image =(bye_pic), tags = ('evenrow',))

                else:
                    CreditDueTree.insert('', END, values= (records), image =(ylw_pic), tags = ('evenrow',))


            elif percent>0.8:
                CreditDueTree.insert('', END, values= (records), image =(blk_pic), tags = ('evenrow',))

            elif percent>0.5:
                CreditDueTree.insert('', END, values= (records), image =(pur_pic), tags = ('evenrow',))

            elif percent>0.3:
                CreditDueTree.insert('', END, values= (records), image =(blu_pic), tags = ('evenrow',))


            else:
                CreditDueTree.insert('', END, values= (records), tags = ('evenrow',))
        else:
            if diff.days < 1 :
                if percent>=0.8:
                    CreditDueTree.insert('', END, values= (records), image =(blro_pic), tags = ('oddrow',))

                elif percent >=0.5:
                    CreditDueTree.insert('', END, values= (records), image =(pro_pic), tags = ('oddrow',))

                elif percent >=0.3:
                    CreditDueTree.insert('', END, values= (records), image =(bro_pic), tags = ('oddrow',))

                else:
                    CreditDueTree.insert('', END, values= (records), image =(red_pic), tags = ('oddrow',))
            elif diff.days <6:
                if percent>=0.8:
                    CreditDueTree.insert('', END, values= (records), image =(blyo_pic), tags = ('oddrow',))

                    
                elif percent >=0.5:
                    CreditDueTree.insert('', END, values= (records), image =(pyo_pic), tags = ('oddrow',))

                    
                elif percent >=0.3:
                    CreditDueTree.insert('', END, values= (records), image =(byo_pic), tags = ('oddrow',))

                else:
                    CreditDueTree.insert('', END, values= (records), image =(ylw_pic), tags = ('oddrow',))


            elif percent>=0.8:

                CreditDueTree.insert('', END, values= (records), image =(blk_pic), tags = ('oddrow',))

            elif percent>=0.5:

                CreditDueTree.insert('', END, values= (records), image =(pur_pic), tags = ('oddrow',))

            elif percent>=0.3:
                CreditDueTree.insert('', END, values= (records), image =(blu_pic), tags = ('oddrow',))

            else:
                CreditDueTree.insert('', END, values= (records), tags =('oddrow',))
        count +=1


#function to reset fields in add transaction page                
def reset_add_credit_fields():
    for i in ['add_credit_name_strvar', 'add_credit_due_strvar','add_credit_limit_strvar','add_credit_amt_strvar']:
        exec(f"{i}.set('')")#set fields in Add Transaction page to empty

        
def add_credit():
    card_name = add_credit_name_strvar.get()
    credit_limit = add_credit_limit_strvar.get()
    credit_due = add_credit_due_strvar.get()
    credit_amt = add_credit_amt_strvar.get()
    uname = uname_stvar.get()
    format = '%m/%d/%y'
    if not card_name or not credit_limit or not credit_due or not credit_amt:
        messagebox.showerror('Error', "Please fill in all the fields!")    
    else:
        try:
            float(credit_limit)
        except ValueError:
            messagebox.showerror('Error', "Please insert the Credit Limit in number form")
        else:
            try:
                float(credit_amt)
            except ValueError:
                messagebox.showerror('Error', "Please insert the Amount Spent in number form")
            else:
                try:
                    res = bool(datetime.strptime(credit_due,format))
                except ValueError:
                    messagebox.showerror('Error', "Please insert date in MM/DD/YY format or choose the date from the calendar")
                else:                
                    connect_database()
                    cursor.execute("SELECT card_name from credit_due WHERE card_name =? and username =?",(card_name, uname,))
                    find = cursor.fetchall()
                    if len(find)!= 0:
                        messagebox.showerror('Error','Card already exists in the system')
                    else:
                        connect_database()
                        conn.execute("""INSERT INTO credit_due (card_name, credit_limit, username, due_date,amt_used)
                                VALUES(?,?,?,?,?)""",
                                (card_name, credit_limit,uname,credit_due, credit_amt))#insert data into transac table in database
                        conn.commit()
                        display_credit_database()
                        reset_add_credit_fields()
                        show_frame(CreditFrame)
                    
def edit_credit():
    card_name = edit_credit_name_strvar.get()
    credit_limit = edit_credit_limit_strvar.get()
    credit_due = edit_credit_due_strvar.get()
    credit_amt = edit_credit_amt_strvar.get()
    uname = uname_stvar.get()
    format = '%m/%d/%y'
    if not card_name or not credit_limit or not credit_due or not credit_amt:
        messagebox.showerror('Error', "Please fill in all the fields!")    
    else:
        try:
            float(credit_limit)
        except ValueError:
            messagebox.showerror('Error', "Please insert the Credit Limit in number form")
        else:
            try:
                float(credit_amt)
            except ValueError:
                messagebox.showerror('Error', "Please insert the Amount Spent in number form")
            else:
                try:
                    res = bool(datetime.strptime(credit_due,format))
                except ValueError:
                    messagebox.showerror('Error', "Please insert date in MM/DD/YY format or choose the date from the calendar")
                else:                
                    connect_database()
                    conn.execute("""UPDATE credit_due SET credit_limit =?, due_date =?, amt_used =?
                                    WHERE card_name = ? and username =?""",(credit_limit, credit_due,credit_amt, card_name, uname,))
                    conn.commit()
                    display_credit_database()
                    show_frame(CreditFrame)

def remove_credit():
    uname = uname_stvar.get()
    #validate inventory is selected
    if not CreditDueTree.selection():
        messagebox.showerror("Error", "Please select an item to delete")
        
    else:
    	# Add a little message box for fun
        response = messagebox.askyesno("Delete", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")

	#Add logic for message box
        if response == 1:
		# Designate selections
                x = CreditDueTree.selection()

		# Create List of ID's
                ids_to_delete = []
		
		# Add selections to ids_to_delete list
                for record in x:
                    ids_to_delete.append(CreditDueTree.item(record, 'values')[0])

                #connect to database
                connect_database()
		

		# Delete Everything From The Table
                cursor.executemany("DELETE FROM credit_due WHERE card_name = ? and username = ?", [(a,uname,) for a in ids_to_delete])
		# Reset List
                ids_to_delete = []


		# Commit changes
                conn.commit()


                #display new database values
                display_credit_database()

		#display delete status
                messagebox.showinfo('Status' , 'You have successfully deleted the items!')

def close_add_credit():
    answer = messagebox.askyesno(title='Confirmation',
                          message='Are you sure that you want to return to Credit Due Date page?  The entries made will be cleared.')
    if answer:
        reset_add_credit_fields()#set fields in Add Transaction page to empty
        show_frame(CreditFrame)#close add transaction page
        
def close_edit_credit():
    answer = messagebox.askyesno(title='Confirmation',
                          message='Are you sure that you want to return to All Transaction page? Any changes made will not be saved.')
    if answer:
        show_frame(CreditFrame)#close edit transaction page







#===================================Credit Card Due Date Page======================================

CreditFrame = Frame(page3, bg='#212429', highlightbackground='#212429', highlightthickness=1)
CreditFrame.place(x=150,y=20, height=715, width = 1200)


CreditTopLabel = Label(CreditFrame, text='Credit Card Due Date', font=('Arial', 40,'italic'), fg='white', bg='#212429')
CreditTopLabel.place(x=40, y=15)

CreditBottomFrame = Frame(CreditFrame, bg = '#2A2E31')
CreditBottomFrame.place(x=40,y=95, height=585, width = 1115)


AddCreditButton = Button(CreditFrame, text= "Add", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = open_add_credit)
AddCreditButton.place(x=925, y=30)

EditCreditButton = Button(CreditFrame, text= "Edit", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = open_edit_credit)
EditCreditButton.place(x= 1070, y=30 )

DeleteCreditButton = Button(CreditFrame, text= "Delete", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = remove_credit)
DeleteCreditButton.place(x= 988, y=30)

blck_square_label = Label(CreditBottomFrame, image=blk_pic, bg = '#2A2E31')
blck_square_label.image= blk_pic
blck_square_label.place(x=570, y=555)

blck_desc_label = Label(CreditBottomFrame, text = 'Amount spent is greater or equal to 80% of credit limit', bg = '#2A2E31', fg = 'white', font =('Inter', 11, 'italic') )
blck_desc_label.place(x=615, y=555)

pur_square_label = Label(CreditBottomFrame, image=pur_pic, bg = '#2A2E31')
pur_square_label.image= pur_pic
pur_square_label.place(x=570, y=515)

pur_desc_label = Label(CreditBottomFrame, text = 'Amount spent is greater or equal to 50% of credit limit', bg = '#2A2E31', fg = 'white', font =('Inter', 11, 'italic') )
pur_desc_label.place(x=615, y=515)

blu_square_label = Label(CreditBottomFrame, image=blu_pic, bg = '#2A2E31')
blu_square_label.image= blu_pic
blu_square_label.place(x=570, y=475)

blu_desc_label = Label(CreditBottomFrame, text = 'Amount spent is greater or equal to 30% of credit limit', bg = '#2A2E31', fg = 'white', font =('Inter', 11, 'italic') )
blu_desc_label.place(x=615, y=475)

red_square_label = Label(CreditBottomFrame, image=red_pic, bg = '#2A2E31')
red_square_label.image= red_pic
red_square_label.place(x=50, y=515)

red_desc_label = Label(CreditBottomFrame, text = 'Credit due date has passed, please pay your credits ASAP', bg = '#2A2E31', fg = 'white', font =('Inter', 11, 'italic') )
red_desc_label.place(x=95, y=515)

ylw_square_label = Label(CreditBottomFrame, image=ylw_pic, bg = '#2A2E31')
ylw_square_label.image= ylw_pic
ylw_square_label.place(x=50, y=475)

ylw_desc_label = Label(CreditBottomFrame, text = 'Credit due date is in 5 days or less, please pay your credits', bg = '#2A2E31', fg = 'white', font =('Inter', 11, 'italic') )
ylw_desc_label.place(x=95, y=475)


#credit card due date treeview
#configure credit due treeview
CreditDueTree = ttk.Treeview(CreditBottomFrame, selectmode="extended",
                    columns = ('name', 'curr', 'set', 'due'), style = "Credit.Treeview")
CreditDueTree.place(x = 30, y = 20, relwidth=0.95, relheight=0.75)



# Create striped row tags
CreditDueTree.tag_configure('oddrow', background="#54585b")
CreditDueTree.tag_configure('evenrow', background="#747a7d")


#configure horizontal and vertical scrollbar for treeview
credit_x_scroller= Scrollbar(CreditDueTree, orient = HORIZONTAL, command =CreditDueTree.xview)
credit_y_scroller= Scrollbar(CreditDueTree, orient = VERTICAL, command =CreditDueTree.yview)
credit_x_scroller.pack(side= BOTTOM, fill=X)
credit_y_scroller.pack(side= RIGHT, fill=Y)
CreditDueTree.config(yscrollcommand=credit_y_scroller.set, xscrollcommand=credit_x_scroller.set)

#set heading name for treeview column
CreditDueTree.heading('name', text = 'Card Name', anchor=CENTER)
CreditDueTree.heading('curr', text = 'Current Amount', anchor=CENTER)
CreditDueTree.heading('set', text = 'Amount Set', anchor=CENTER)
CreditDueTree.heading('due', text = 'Due Date', anchor=CENTER)
##CreditDueTree.heading('status', text = 'Status', anchor=CENTER)

CreditDueTree.column("#0", anchor='e', width=100)
CreditDueTree.column("name", anchor=CENTER, width=100)
CreditDueTree.column("curr", anchor=CENTER, width=100)
CreditDueTree.column("set", anchor=CENTER, width=100)
CreditDueTree.column("due", anchor=CENTER, width=150)
##CreditDueTree.column("status", anchor=CENTER, width=150)


#===================================Add Credit Card Due Date Page======================================

AddCreditFrame = Frame(page3, bg='#212429', highlightbackground='#212429', highlightthickness=1)
AddCreditFrame.place(x=150,y=20, height=715, width = 1200)

AddCreditBottomFrame = Frame(AddCreditFrame, bg = '#2A2E31')
AddCreditBottomFrame.place(x=40,y=50, height=640, width = 1115)

AddCreditTopLabel = Label(AddCreditBottomFrame, text='Add Credit Card Details', font=('Arial', 40,'italic'), fg='white', bg='#2A2E31')
AddCreditTopLabel.place(x=30, y=20)

AddCreditBackButton = Button(AddCreditBottomFrame, text= "Back", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = close_add_credit)
AddCreditBackButton.place(x=1010, y=40)

AddCreditBgFrame =  Frame(AddCreditBottomFrame, bg = '#525557')
AddCreditBgFrame.place(x=30,y=98, height=515, width = 1050)

AddCreditName_label = Label (AddCreditBgFrame, text='Name               :', font=('Arial',25,'italic'), fg='white', bg='#525557')
AddCreditName_label.place(x=50, y=60)

AddCreditName_entry = Entry(AddCreditBgFrame, font=(25), width = 20, textvariable = add_credit_name_strvar)
AddCreditName_entry.place(x = 320, y = 65)

AddCreditAmount_label = Label (AddCreditBgFrame, text='Current \n            Amount used   :', font=('Arial',25,'italic'), fg='white', bg='#525557')
AddCreditAmount_label.place(x=-55, y=160)

AddCreditAmount_entry = Entry(AddCreditBgFrame, font=(25), width = 20, textvariable = add_credit_amt_strvar)
AddCreditAmount_entry.place(x = 320, y = 180)

AddCreditLimit_label = Label (AddCreditBgFrame, text='Credit Limit       :', font=('Arial',25,'italic'), fg='white', bg='#525557')
AddCreditLimit_label.place(x=50, y=310)

AddCreditLimit_entry = Entry(AddCreditBgFrame, font=(25), width = 20, textvariable = add_credit_limit_strvar)
AddCreditLimit_entry.place(x = 320, y = 315)

AddCreditDate_label = Label(AddCreditBgFrame, text='Date:', font=('Arial',25,'italic'), fg='white', bg='#525557')
AddCreditDate_label.place(x=600, y=60)

AddCreditEnter_button = Button(AddCreditBgFrame, text= "Enter", font=('Inter', 16, 'italic'), fg='white', bg = '#988E8E', padx = 15, command = add_credit)
AddCreditEnter_button.place(x=480, y=400)


# Add Calendar in Add Credit Card page
#get calendar date 
def add_credit_grad_date():
    Add_credit_get_date_entry.delete(0,END)
    Add_credit_get_date_entry.insert(0, Add_credit_cal.get_date())
    
Add_credit_cal = Calendar(AddCreditBgFrame, selectmode = 'day', year = 2022, month = 10, day = 30)
Add_credit_cal.place(x = 720, y = 60)



Add_credit_cal_button = Button(AddCreditBgFrame, text = "Get Date",font=('Inter', 12, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = add_credit_grad_date).place(x = 800, y = 265)
 

Add_credit_get_date_entry = Entry(AddCreditBgFrame, font=(15), width = 15, textvariable = add_credit_due_strvar)
Add_credit_get_date_entry.place(x = 760, y = 315)



#===================================Edit Credit Card Due Date Page======================================

EditCreditFrame = Frame(page3, bg='#212429', highlightbackground='#212429', highlightthickness=1)
EditCreditFrame.place(x=150,y=20, height=715, width = 1200)

EditCreditBottomFrame = Frame(EditCreditFrame, bg = '#2A2E31')
EditCreditBottomFrame.place(x=40,y=50, height=640, width = 1115)

EditCreditTopLabel = Label(EditCreditBottomFrame, text='Edit Credit Card Details', font=('Arial', 40,'italic'), fg='white', bg='#2A2E31')
EditCreditTopLabel.place(x=30, y=20)

EditCreditBackButton = Button(EditCreditBottomFrame, text= "Back", font=('Inter', 13, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = close_edit_credit)
EditCreditBackButton.place(x=1010, y=40)

EditCreditBgFrame =  Frame(EditCreditBottomFrame, bg = '#525557')
EditCreditBgFrame.place(x=30,y=98, height=515, width = 1050)

EditCreditName_label = Label (EditCreditBgFrame, text='Name               :', font=('Arial',25,'italic'), fg='white', bg='#525557')
EditCreditName_label.place(x=50, y=60)

EditCreditName_entry = Entry(EditCreditBgFrame, font=(25), width = 20, textvariable = edit_credit_name_strvar, state = 'disabled' )
EditCreditName_entry.place(x = 320, y = 65)

EditCreditAmount_label = Label (EditCreditBgFrame, text='Current \n            Amount used   :', font=('Arial',25,'italic'), fg='white', bg='#525557')
EditCreditAmount_label.place(x=-55, y=160)

EditCreditAmount_entry = Entry(EditCreditBgFrame, font=(25), width = 20, textvariable = edit_credit_amt_strvar)
EditCreditAmount_entry.place(x = 320, y = 180)

EditCreditLimit_label = Label (EditCreditBgFrame, text='Credit Limit       :', font=('Arial',25,'italic'), fg='white', bg='#525557')
EditCreditLimit_label.place(x=50, y=310)

EditCreditLimit_entry = Entry(EditCreditBgFrame, font=(25), width = 20, textvariable = edit_credit_limit_strvar)
EditCreditLimit_entry.place(x = 320, y = 315)

EditCreditDate_label = Label(EditCreditBgFrame, text='Date:', font=('Arial',25,'italic'), fg='white', bg='#525557')
EditCreditDate_label.place(x=600, y=60)

EditCreditEnter_button = Button(EditCreditBgFrame, text= "Enter", font=('Inter', 16, 'italic'), fg='white', bg = '#988E8E', padx = 15, command = edit_credit)
EditCreditEnter_button.place(x=480, y=400)


# Add Calendar in Add Credit Card page
#get calendar date 
def edit_credit_grad_date():
    Edit_credit_get_date_entry.delete(0,END)
    Edit_credit_get_date_entry.insert(0, Edit_credit_cal.get_date())
    
Edit_credit_cal = Calendar(EditCreditBgFrame, selectmode = 'day', year = 2022, month = 10, day = 30)
Edit_credit_cal.place(x = 720, y = 60)



Edit_credit_cal_button = Button(EditCreditBgFrame, text = "Get Date",font=('Inter', 12, 'italic'), fg='white', bg = '#988E8E', padx = 10, command = edit_credit_grad_date).place(x = 800, y = 265)
 

Edit_credit_get_date_entry = Entry(EditCreditBgFrame, font=(15), width = 15, textvariable = edit_credit_due_strvar)
Edit_credit_get_date_entry.place(x = 760, y = 315)






#================================Home Page===================================

def display_home_expense():
    uname = uname_stvar.get()
    #delete inventory list
    HomeBudgetTree.delete(*HomeBudgetTree.get_children()) #delete treeview
    
    connect_database()#connect to database
    cursor.execute("SELECT TOF, current_amt FROM budget WHERE username =  ? and TOF != 'savings' ORDER BY current_amt DESC  ",(uname,))#select data in database
    data = cursor.fetchall()#fetch data from database

    # Add our data to the screen
    count = 0


    for records in data:
        if count<4:
            HomeBudgetTree.insert('', END, values= ('', records[0],records[1],))
            
        count +=1

    # Commit changes
    conn.commit()
    

def display_home_savings():
    uname = uname_stvar.get()
    #delete inventory list
    HomeSavingsTree.delete(*HomeSavingsTree.get_children()) #delete treeview
    
    connect_database()#connect to database
    cursor.execute("SELECT TOF, current_amt FROM budget WHERE username =  ? and TOF = 'savings'",(uname,))#select data in database
    data = cursor.fetchall()#fetch data from database

    for records in data:
        HomeSavingsTree.insert('', END, values= ('', records[0],records[1],))


    # Commit changes
    conn.commit()


def display_home_credit():
    uname = uname_stvar.get()
    today = datetime.today()
    today_date = today.strftime('%m/%d/%y')
    today_format = datetime.strptime(today_date,'%m/%d/%y')
    
    #delete inventory list    
    HomeCreditTree.delete(*HomeCreditTree.get_children()) #delete treeview
    
    connect_database()#connect to database
    cursor.execute("SELECT card_name, due_date FROM credit_due WHERE username =  ?",(uname,))#select data in database
    data = cursor.fetchall()#fetch data from database
    for records in data:
        due_format = datetime.strptime(records[1], '%m/%d/%y')
        diff = due_format - today_format
        if diff.days <0 or diff.days<6:
            HomeCreditTree.insert('', END, values= ('', records[0],records[1],))


    # Commit changes
    conn.commit()




# ================= Username =================
uname_label = Label(page1, text='Username', bg='white',font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
uname_label.place(x=551, y=350)

uname_entry = Entry(page1, highlightthickness=0, relief=FLAT, bg='white', fg='#6b6a69',font=('yu gothic ui', 13, 'bold'),textvariable= uname_stvar)
uname_entry.place(x=581, y=385, width=270)

uname_line = Canvas(page1, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
uname_line.place(x=551, y=409)

#========================Home Frame==============================
HomeFrame = Frame(page3, bg='#212429', highlightbackground='#212429', highlightthickness=1)
HomeFrame.place(x=150,y=20, height=715, width = 1390)


HomeTopFrame=Frame(HomeFrame, bg='#212429', highlightbackground='#212429', highlightthickness=1)
HomeTopFrame.place(x=0,y=0, height=100,width = 1550)

HomeBottomFrame=Frame(HomeFrame, bg='#212429', highlightbackground='#212429', highlightthickness=1)
HomeBottomFrame.place(x=0,y=100, height=800, width = 1390)



#Display "Home Page"
HomeTopLabel = Label(HomeTopFrame, text='Home', font=('Arial', 40,'italic'), fg='white', bg='#212429')
HomeTopLabel.place(x=40, y=30)

HomeExpenseFrame = Frame(HomeBottomFrame, bg='#2A2E31').place(x=35,y=10, width = 322, height = 80)
HomeExpenseLabel= Label( HomeBottomFrame, text = ' Expense        RM', fg='white', bg='#2A2E31', font = ('Inter', 23)).place(x = 35, y = 20)


HomeSavingsFrame = Frame(HomeBottomFrame, bg='#2A2E31').place(x=400,y=10, width = 322, height = 80)
HomeSavingsLabel= Label( HomeBottomFrame, text = '   Savings       RM', fg='white', bg='#2A2E31', font = ('Inter', 23)).place(x = 400, y = 20)


HomeCreditFrame = Frame(HomeBottomFrame, bg='#2A2E31').place(x=768,y=10, width = 322, height = 80)
HomeCreditLabel= Label( HomeBottomFrame, text = '   Credit Card       Date', fg='white', bg='#2A2E31', font = ('Inter', 23)).place(x = 768, y = 20)



#home page expense treeview
#configure treeview
HomeBudgetTree = ttk.Treeview(HomeBottomFrame, selectmode="none",show ='',
                    columns = ('space','expense', 'amount'), style = "HomeP.Treeview")
HomeBudgetTree.place(x = 35, y = 80, relwidth=0.23, relheight=0.33)



#set heading name for treeview column
HomeBudgetTree.heading('space', text = '', anchor=CENTER)
HomeBudgetTree.heading('expense', text = 'Expenses', anchor=CENTER)
HomeBudgetTree.heading('amount', text = 'RM', anchor=CENTER)

HomeBudgetTree.column("space", anchor='w', width=20)
HomeBudgetTree.column("expense", anchor='w', width=150)
HomeBudgetTree.column("amount", anchor='w', width=100)




#home page savings treeview
#configure treeview
HomeSavingsTree = ttk.Treeview(HomeBottomFrame, selectmode="none",show ='',
                    columns = ('space','savings', 'amount'), style = "HomeP.Treeview")
HomeSavingsTree.place(x = 400, y = 80, relwidth=0.23, relheight=0.12)



#set heading name for treeview column
HomeSavingsTree.heading('space', text = '', anchor=CENTER)
HomeSavingsTree.heading('savings', text = 'savings', anchor=CENTER)
HomeSavingsTree.heading('amount', text = 'amount', anchor=CENTER)

HomeSavingsTree.column("space", anchor='w', width=20)
HomeSavingsTree.column("savings", anchor='w', width=150)
HomeSavingsTree.column("amount", anchor='w', width=100)





#home page expense treeview
#configure treeview
HomeCreditTree = ttk.Treeview(HomeBottomFrame, selectmode="none",show ='',
                    columns = ('space','credit', 'due'), style = "HomeP.Treeview")
HomeCreditTree.place(x = 768, y = 80, relwidth=0.23, relheight=0.33)



#set heading name for treeview column
HomeCreditTree.heading('space', text = '', anchor=CENTER)
HomeCreditTree.heading('credit', text = 'credit', anchor=CENTER)
HomeCreditTree.heading('due', text = 'Due', anchor=CENTER)

HomeCreditTree.column("space", anchor='w', width=20)
HomeCreditTree.column("credit", anchor='w', width=150)
HomeCreditTree.column("due", anchor='w', width=100)

def display_IncomeGraph():
    cursor.execute('SELECT date,income FROM transac WHERE income between "1" AND "10000000" ')
    expenses_data = cursor.fetchall()
    
    if get_year_strvar.get == '' :
        messagebox.showerror('Error','Please enter the year')
    
    elif get_category_strvar.get() =='':
        messagebox.showerror('Error','Please select one options')
    else:
        if get_category_strvar.get() =='Monthly':
            for item in ReportBottomFrame.winfo_children():
                    item.destroy()

            #convert the string to int 
            converted_year= int(get_year_strvar.get())
            df = pd.DataFrame(expenses_data,columns=['Date','Amount'])
            df['Date']=pd.to_datetime(df['Date'])
            year = df[df.Date.dt.year == converted_year]
            print(year)
                
            data= year.groupby(year['Date'].dt.strftime('%B'))['Amount'].sum().sort_values()
                
            df1 = pd.DataFrame(data,columns=['Amount'])
            cats = ['January', 'Febuary', 'March', 'April','May','June', 'July', 'August','September', 'October', 'November', 'December']
            df1 = df1.reindex(cats)

            print(df1)
            
            fig =Figure(figsize=(5,5))
            fig.set_facecolor('dimgray')
            ax = fig.add_subplot(111)
            ax.set_facecolor('dimgray')
            
            df1.plot(kind='bar',legend=True,ax=ax,color='lime',title='Monthly Income Report')
            
        
            chart = FigureCanvasTkAgg(fig,ReportBottomFrame)
            chart.get_tk_widget().place(relx=0.01,rely=0.05)
            for label in ax.get_xticklabels():
                label.set(rotation=30, horizontalalignment='right')

            
            tree = ttk.Treeview(ReportBottomFrame, height=100, selectmode=BROWSE,
                                        columns=('Month', 'Total'))

            X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
            Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
            X_scroller.pack(side=BOTTOM, fill=X)
            Y_scroller.pack(side=RIGHT, fill=Y)
            tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
            tree.heading('Month', text='Month', anchor=CENTER)
            tree.heading('Total', text='Total', anchor=CENTER)

            tree.column('#0', width=0, stretch=NO,anchor=CENTER)
            tree.column('#1', width=275, stretch=NO,anchor=CENTER)
            tree.column('#2', width=275, stretch=NO,anchor=CENTER)
            tree.place(relx=0.5,rely=0.05, relwidth=1, relheight=0.9)

            table_data = list(df1.itertuples(name=None))
            for record in table_data:
                tree.insert('',END,values=record)

        elif get_category_strvar.get()=='Yearly':
            for item in ReportBottomFrame.winfo_children():
                    item.destroy()
            df1 = pd.DataFrame(expenses_data,columns=['Year','Amount'])
            df1['Year']=pd.to_datetime(df1['Year'])
            
            data= df1.groupby(df1['Year'].dt.strftime('%Y'))['Amount'].sum().sort_values()
            df1= pd.DataFrame(data,columns=['Amount'])
            print(df1)
            #print(df)
            fig =Figure(figsize=(5,5))
            fig.set_facecolor('dimgray')
            ax = fig.add_subplot(111)
            ax.set_facecolor('dimgray')
            
            df1.plot(kind='bar',legend=True,ax=ax,color='lime',title='Yearly Income Report')
            
        
            chart = FigureCanvasTkAgg(fig,ReportBottomFrame)
            chart.get_tk_widget().place(relx=0.01,rely=0.05)
            for label in ax.get_xticklabels():
                label.set(rotation=30, horizontalalignment='right')

            
            tree = ttk.Treeview(ReportBottomFrame, height=100, selectmode=BROWSE,
                                        columns=('Year','Total'))

            X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
            Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
            X_scroller.pack(side=BOTTOM, fill=X)
            Y_scroller.pack(side=RIGHT, fill=Y)
            tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
            tree.heading('Year', text='Year', anchor=CENTER)
            tree.heading('Total', text='Total', anchor=CENTER)

            tree.column('#0', width=0, stretch=NO,anchor=CENTER)
            tree.column('#1', width=275, stretch=NO,anchor=CENTER)
            tree.column('#2', width=275, stretch=NO,anchor=CENTER)
            
            tree.place(relx=0.5,rely=0.05, relwidth=0.7, relheight=0.9)

            table_data = list(df1.itertuples(name=None))
            for record in table_data:
                tree.insert('',END,values=record)

def display_ExpensesGraph():
    cursor.execute('SELECT date,expense FROM transac WHERE expense between "1" AND "10000000"')
    expenses_data = cursor.fetchall()
    
    
    if get_year_strvar.get() == "":
        messagebox.showerror('Error','Please enter the year')

    elif get_category_strvar.get() =='':
        messagebox.showerror('Error','Please select one options')

    else:

        if get_category_strvar.get() =='Monthly' :
            for item in ReportBottomFrame.winfo_children():
                    item.destroy()
            #convert the string to int 
            converted_year= int(get_year_strvar.get())
            df = pd.DataFrame(expenses_data,columns=['Date','Amount'])
            df['Date']=pd.to_datetime(df['Date'])
            year = df[df.Date.dt.year == converted_year]
            print(year)
            
            data= year.groupby(year['Date'].dt.strftime('%B'))['Amount'].sum().sort_values()
            
            df1 = pd.DataFrame(data,columns=['Amount'])
            cats = ['January', 'Febuary', 'March', 'April','May','June', 'July', 'August','September', 'October', 'November', 'December']
            df1 = df1.reindex(cats)

            print(df1)
            
            fig =Figure(figsize=(5,5))
            fig.set_facecolor('dimgray')
            ax = fig.add_subplot(111)
            ax.set_facecolor('dimgray')
            
            df1.plot(kind='bar',legend=True,ax=ax,color='red',title='Monthly Expenses Report')
            
        
            chart = FigureCanvasTkAgg(fig,ReportBottomFrame)
            chart.get_tk_widget().place(relx=0.01,rely=0.05)
            for label in ax.get_xticklabels():
                label.set(rotation=30, horizontalalignment='right')

            
            tree = ttk.Treeview(ReportBottomFrame, height=100, selectmode=BROWSE,
                                        columns=('Month', 'Total' ))

            X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
            Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
            X_scroller.pack(side=BOTTOM, fill=X)
            Y_scroller.pack(side=RIGHT, fill=Y)
            tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
            tree.heading('Month', text='Month', anchor=CENTER)
            tree.heading('Total', text='Total', anchor=CENTER)

            tree.column('#0', width=0, stretch=NO,anchor=CENTER)
            tree.column('#1', width=275, stretch=NO,anchor=CENTER)
            tree.column('#2', width=275, stretch=NO,anchor=CENTER)
            tree.place(relx=0.5,rely=0.05, relwidth=1, relheight=0.9)

            table_data = list(df1.itertuples(name=None))
            for record in table_data:
                tree.insert('',END,values=record)

        elif get_category_strvar.get()=='Yearly':
            for item in ReportBottomFrame.winfo_children():
                    item.destroy()
            df1 = pd.DataFrame(expenses_data,columns=['Year','Amount'])
            df1['Year']=pd.to_datetime(df1['Year'])
            
            data= df1.groupby(df1['Year'].dt.strftime('%Y'))['Amount'].sum().sort_values()
            df1= pd.DataFrame(data,columns=['Amount'])
            print(df1)
            #print(df)
            fig =Figure(figsize=(5,5))
            fig.set_facecolor('dimgray')
            ax = fig.add_subplot(111)
            ax.set_facecolor('dimgray')
            
            df1.plot(kind='bar',legend=True,ax=ax,color='red',title='Yearly Expenses Report')
            
        
            chart = FigureCanvasTkAgg(fig,ReportBottomFrame)
            chart.get_tk_widget().place(relx=0.01,rely=0.05)
            for label in ax.get_xticklabels():
                label.set(rotation=30, horizontalalignment='right')

            
            tree = ttk.Treeview(ReportBottomFrame, height=100, selectmode=BROWSE,
                                        columns=('Year','Total'))

            X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
            Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
            X_scroller.pack(side=BOTTOM, fill=X)
            Y_scroller.pack(side=RIGHT, fill=Y)
            tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
            tree.heading('Year', text='Year', anchor=CENTER)
            tree.heading('Total', text='Total', anchor=CENTER)

            tree.column('#0', width=0, stretch=NO,anchor=CENTER)
            tree.column('#1', width=275, stretch=NO,anchor=CENTER)
            tree.column('#2', width=275, stretch=NO,anchor=CENTER)
            
            tree.place(relx=0.5,rely=0.05, relwidth=0.7, relheight=0.9)

            table_data = list(df1.itertuples(name=None))
            for record in table_data:
                tree.insert('',END,values=record)

        
  
get_category_strvar =StringVar()
get_year_strvar =StringVar()
reportFrame = Frame(page3,bg='#212429', highlightbackground='#212429', highlightthickness=1)
reportFrame.place(x=150,y=20, height=715, width = 1200)

ReportTopLabel = Label(reportFrame,text='Reports',font=('Inter', 23),fg='#FFFFFF',bg='#212429').place(x=40,y=15)

ReportBottomFrame = Frame(reportFrame ,bg = '#2A2E31')
ReportBottomFrame.place(x=40,y=95, height=585, width = 1115)

IncomeBtn = Button(reportFrame,text="Income",bg='#212429',width=10,command=display_IncomeGraph).place(x=400,y=20)
ExpensesBtn = Button(reportFrame,text="Expenses",bg='#212429',width=10,command=display_ExpensesGraph).place(x=550,y=20)

value =['Monthly','Yearly']
ttk.Combobox(reportFrame,values=value,textvariable=get_category_strvar,width=10,state='readonly').place(x=700,y=20)
Entry(reportFrame,width=10,textvariable=get_year_strvar,relief=FLAT).place(x=850,y=20)


# ========== Create side menu bar ==========

min_w = 70  # Minimum width of the frame
max_w = 145  # Maximum width of the frame
cur_width = min_w  # Increasing width of the frame

        
        

#placing frame for menu bar
menuFrame = Frame(page3, bg='#2b2e33', width=160, height=715,highlightbackground='black', highlightthickness=1)
menuFrame.place(x=0, y=20)


# Defining the buttons for menu bar in Home page

home_b = Button(menuFrame, text="Home" , bg='#2b2e33', relief='flat',fg='white',font=('yu gothic ui', 13, 'bold'),activebackground='#74bc94', command = lambda:show_frame(HomeFrame))
budget_b = Button(menuFrame,text="Budget" , bg='#2b2e33', relief='flat',fg='white',font=('yu gothic ui', 13, 'bold'),activebackground='#74bc94', command = lambda:show_frame(budgetFrame))
scheduler_b = Button(menuFrame, text="Scheduler" ,  bg='#2b2e33', relief='flat',fg='white',font=('yu gothic ui', 13, 'bold'),activebackground='#74bc94')
reports_b = Button(menuFrame, text="Reports" , bg='#2b2e33', relief='flat',fg='white',font=('yu gothic ui', 13, 'bold'),activebackground='#74bc94',command= lambda:show_frame(reportFrame))
alltransaction_b = Button(menuFrame, text="All Transaction" ,  bg='#2b2e33', relief='flat',fg='white',font=('yu gothic ui', 13, 'bold'),activebackground='#74bc94', command = lambda:show_frame(transFrame))
calculator_b = Button(menuFrame, text="Calculator" , bg='#2b2e33', relief='flat',fg='white',font=('yu gothic ui', 13, 'bold'),activebackground='#74bc94', command = open_calculator)
investment_b = Button(menuFrame, text="Credit Card \n Due Date" , bg='#2b2e33', relief='flat',fg='white',font=('yu gothic ui', 13, 'bold'),activebackground='#74bc94', command = lambda: show_frame(CreditFrame))
help_b = Button(menuFrame, text="Help" , bg='#2b2e33', relief='flat',fg='white',font=('yu gothic ui', 13, 'bold'),activebackground='#74bc94')
logout_b = Button(menuFrame, text="Log Out" , bg='#2b2e33', relief='flat',fg='white',font=('yu gothic ui', 13, 'bold'),activebackground='#74bc94')



# Placing buttons in menu bar Home Page

home_b.place(x=25, y=40, width = 110)
budget_b.place(x=25, y=100, width = 110)
scheduler_b.place(x=25, y=160, width = 110)
reports_b.place(x=25, y=220, width = 110)
alltransaction_b.place(x=25, y=280, width = 110)
calculator_b.place(x=25, y=340, width = 110)
investment_b.place(x=25, y=400, width = 110)
help_b.place(x=25, y=460, width = 110)
logout_b.place(x=25, y=520, width = 110)



# So that Frame does not depend on the widgets inside the frame
menuFrame.grid_propagate(False)




window.mainloop()

