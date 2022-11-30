import sys
from tkinter import messagebox

from tkinter import *
import time

b=sys.argv[1]
f1=open("otp.txt","r")
b1=f1.read()
f1.close()
#print(b,b1)
if b==b1:
    f = open("status.txt", "w")
    f.write("success")
    f.close()
    messagebox.showinfo("Congratulations", "Your OTP was verified Successfully!!\n You are successfully loggedin")
    
else:
    f = open("status.txt", "w")
    f.write("failure")
    f.close()
