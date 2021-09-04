# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:22:04 2020

@author: tomin
"""

from math import cos,sin,radians,atan,sqrt,degrees
from numpy import array,linalg
from tkinter import Tk,Label,Entry,Button,Label,IntVar,Radiobutton,END,Text,WORD
class force():
   def __init__(self):
      self.f=0.0
      self.a=0.0
      self.positive_xFlag=1
      self.positive_yFlag=1
      self.setdir(1)
      self.d=1
     
   def define(self,a,m,d):
       self.f=m
       self.a=a
       if d==0:
           self.a=self.a+180 if self.a <= 180 else self.a-180
           self.setdir(d)
   
   def setdir(self,d):
       if d == 1:
          self.dir="away from point of action"
       else:
          self.dir="towards the point of action"
          self.d=0

def resultantCalc(F,n):
    Fx=0
    Fy=0
    
    for i in range(n):
        Fx+=F[i].f * cos(radians(F[i].a))
        Fy+=F[i].f * sin(radians(F[i].a))
       
    R = force()
    if Fx<0:
        R.positive_xFlag=0
        Fx= -Fx
    if Fy<0:
        R.positive_yFlag=0
        Fy= -Fy
    R.f=sqrt(pow(Fx,2)+pow(Fy,2))
    if (Fx == 0):
        Fx = 0.000000000001
    R.a=degrees(atan(Fy/Fx))
    if R.positive_xFlag==0 and R.positive_yFlag==1:
        R.a=180.0-R.a
    elif R.positive_xFlag==0 and R.positive_yFlag==0:
        R.a=180.0+R.a
    elif R.positive_xFlag==1 and R.positive_yFlag==0:
        R.a=360.0-R.a

    if R.a==360.0:
       R.a=0.0
    R.a=round(R.a,2)
    R.f=round(R.f,2)
    
    return R

def equilibriumCheck():
    UB.place_forget()
    L1.place_forget()
    RB.place_forget()
    EB.place_forget()
    Output.place_forget()
    L = Label(w,text="Enter the number of forces :",fg="darkcyan",font="impact 20",bg="powder blue")
    L.place(x=150,y=200)
    enter = Entry(w,fg="darkcyan",font="impact 20",bd=8)
    enter.place(x=500,y=200,width=100)
    def submit():
        n=int(enter.get())
        enter.destroy()
        L.destroy()
        SB.destroy()
        forceDefiner(n,2)
        
    SB = Button(w,text="Submit",bg="palegreen",fg="green",font="times 18",command= submit,bd=8 )
    SB.place(x=250,y=300,width=100)
    CANCEL.place(x=370,y=300,width=100)
   
def Resultant():
    UB.place_forget()
    L1.place_forget()
    RB.place_forget()
    EB.place_forget()
    Output.place_forget()
    L = Label(w,text="Enter the number of forces :",fg="darkcyan",font="impact 20",bg="powder blue")
    L.place(x=150,y=200)
    enter = Entry(fg="darkcyan",font="impact 20",bd=8)
    enter.place(x=500,y=200,width=100)
    def submit():
        n=int(enter.get())
        enter.destroy()
        L.destroy()
        SB.destroy()
        forceDefiner(n,1)
   
    SB = Button(w,text="Next",bg="palegreen",font="times 18",command= submit,bd=8)
    SB.place(x=250,y=300,width=100)
    CANCEL.place(x=370,y=300,width=100)

def forceDefiner(n,val,i=0,FORCE=[],un=0):
    
    label1 = Label(w,text="Inclination :",fg="darkgreen",font="times 18",bg="powder blue")
    label2 = Label(w,text="Magnitude :",fg="darkgreen",font="times 18",bg="powder blue")
    label3 = Label(w,text="Enter the details of force No. {}".format(i+1),fg="darkcyan",font="impact 18",bg="powder blue")
    angle = Entry(w,fg="green",font="impact 18",bd=8)
    magnitude = Entry(w,fg="green",font="impact 18",bd=8)
    dir_val=IntVar()
    dir_val.set(1)
    radio1 = Radiobutton(w,text="Force acting away from point of action",bg="powder blue",value=1,variable=dir_val,fg="darkgreen",font="times 14")
    radio2 = Radiobutton(w,text="Force acting towards point of action",bg="powder blue",value=0,variable=dir_val,fg="darkgreen",font="times 14")
    Output.delete(0.0,END)
    Output.place(x=0,y=500,width=800,height=140)
    Output.config(fg="darkgreen",font="impact 16")
    Output.insert(END,"Instructions\n")
    Output.config(fg="darkgreen",font="times 15")
    Output.insert(END,"1.All the forces(magnitude) should be in same unit(Newton)\n2.The inclination is the angle measured in degree between the positive x-axis and force in anti-clockwise direction " )
    label3.place(x=200,y=100)
    label1.place(x=150,y=300)
    label2.place(x=150,y=200)
    angle.place(x=300,y=300,width=100)
    magnitude.place(x=300,y=200,width=100)
    radio1.place(x=450,y=200)
    radio2.place(x=450,y=250)
          
        
    s = Button(w,text="Next ",bg="palegreen",fg="black",font="times 18",command=lambda:m(n),bd=8)
    s.place(x=250,y=400,width=100)
    CANCEL.place(x=370,y=400,width=100,height=58)
    if n-i<=0:
        output_scr(force(),0)
        label1.destroy()
        label2.destroy()
        label3.destroy()
        angle.destroy()
        magnitude.destroy()
        s.destroy()
        radio1.destroy()
        radio2.destroy()
        Output.config(fg="darkgreen",font="ariel 20")
        
    def m(n):
            nonlocal i,FORCE
            
            if i<n-1 :
                FORCE.append(force())
                m=float(magnitude.get())
                a=float(angle.get())
                d=dir_val.get()
                FORCE[i].define(a,m,d)
                i+=1
                label3.config(text="Enter the details of force No. {}".format(i+1),bg="powder blue")
                dir_val.set(1)
                angle.delete("0",END)
                magnitude.delete("0",END)
                
            else:
                FORCE.append(force())
                m=float(magnitude.get())
                a=float(angle.get())
                d=dir_val.get()
                FORCE[i].define(a,m,d)
                label1.destroy()
                label2.destroy()
                label3.destroy()
                angle.destroy()
                magnitude.destroy()
                s.destroy()
                radio1.destroy()
                radio2.destroy()
                Output.place_forget()
                Output.config(fg="darkcyan",font="arielt 20")
                if un !=1:
                    R=resultantCalc(FORCE,n)
                    output_scr(R,val)
                else:
                    output_scr(FORCE,val,n)
              
def output_scr(F=0,i=-1,n=0):
    UB.place(x=300,y=350,width=200,height=75)
    L1.place(x=150,y=50)
    RB.place(x=300,y=150,width=200,height=75)
    EB.place(x=300,y=250,width=200,height=75)
    Output.delete(0.0,END)
    Output.place(x=0,y=450,width=800,height=190)
    CANCEL.place_forget()
    if i == -1:
        Output.config(font="ariel 20 bold")
        Output.insert(END,"Output:")
    elif i == 0:
        Output.insert(END,"Invalid Number of forces") 
    elif i == 1:
        if F.f!=0:
            Output.insert(END,"Output\nMagnitude of Resultant force = {} N with inclination of = {} degres\nThe force is acting {}".format(F.f,F.a,F.dir))
            Output.config(fg="darkgreen",font="ariel 15")
        else:
            Output.insert(END,"Output\nThe system is already in equilibrium the Resultant force is a null force")
            Output.config(fg="darkgreen",font="ariel 18")
            
    elif i == 2:
        if F.f==0:
            Output.insert(END,"Output\nThe provided system is in equilibrium")
            Output.config(fg="darkgreen",font="ariel 15")
        else:
            Output.insert(END,"Output\nThe provided system is not in equilibrium")
            Output.config(fg="darkgreen",font="ariel 15")
    elif i == 3:
        if F.f!=0:
            F.setdir(1) if F.d !=1 else F.setdir(0)
            Output.insert(END,"Output\nMagnitude of unknown force = {} N with inclination of = {} degres\nThe force is acting {}".format(F.f,F.a,F.dir))
            Output.config(fg="darkgreen",font="ariel 15")
        else:
            Output.config(fg="darkgreen",font="ariel 18")
            Output.insert(END,"Output\nThe system is already in equilibrium the unknown force is a null force")
        if not(F.f==0):
            if F.a >=180:
                F.a=F.a-180
            else :
                F.a=F.a+180
            F.setdir(1) if F.d != 1 else F.setdir(0)
            Output.insert(END,"\nOr\nMagnitude of unknown force = {} N with inclination of = {} degres\nThe force is acting {}".format(F.f,F.a,F.dir))
            Output.config(fg="darkgreen",font="ariel 15")
   
    elif i == 4:
        Fx=0
        Fy=0
        for i in range(2,n):
            
            
            Fx-=F[i].f * cos(radians(F[i].a))
            Fy-=F[i].f * sin(radians(F[i].a))
        x1=cos(radians(F[0].a))
        x2=cos(radians(F[1].a))        
        y1=sin(radians(F[0].a))        
        y2=sin(radians(F[1].a))
       
        A=array([[x1,x2],[y1,y2]])
        B=array([Fx,Fy])
        X=linalg.solve(A,B)
        d1="away from point of action"
        d2="away from point of action"
        m1=round(X[0],2)
        m2=round(X[1],2)
        if m1<=0:
            m1=-m1
            d1="towards point of action"
        if m2<=0:
            m2=-m2
            d2="towards point of action"
        Output.config(fg="darkcyan",font="ariel 16")
        if m1!=0:
            Output.insert(END,"Output\nMangnitude of the unknown force with inclination {} degres is {} N and acting {}\n".format(F[0].a,m1,d1))
        else:
            Output.insert(END,"Output\nThe system is already in equilibrium without the unknown force with inclination {} degree\n".format(F[0].a)) 
        if m2!=0:
            Output.insert(END,"Mangnitude of the unknown force with inclination {} degree is {} N and acting {}\n".format(F[1].a,m2,d2))
        else:
            Output.insert(END,"The system is already in equilibrium without the unknown force with inclination {} degres\n ".format(F[1].a))
       
def unknown_force():
    def one():
        label.destroy()
        button1.destroy()
        button2.destroy()
        L = Label(w,text="Enter the total number of forces ",fg="darkcyan",font="impact 20",bg="powder blue")
        L.place(x=150,y=200)
        enter = Entry(fg="darkcyan",font="impact 20",bd=8)
        enter.place(x=550,y=200,width=100)
        def submit():
            n=int(enter.get())-1
            enter.destroy()
            L.destroy()
            SB.destroy()
            forceDefiner(n,3)
        SB = Button(w,text="Submit",bg="palegreen",fg="black",font="times 18",command= submit,bd=8)
        SB.place(x=280,y=300,width=100)
        CANCEL.place(x=400,y=300,width=100)
   
    def two():
        label.destroy()
        button1.destroy()
        button2.destroy()
        F=[force(),force()]
        L = Label(w,text="Enter the total number of forces ",fg="darkcyan",font="impact 20",bg="powder blue")
        label1 = Label(w,text="First Force's      :",fg="green",font="times 18",bg="powder blue")
        label2 = Label(w,text="Second Force's  :",fg="green",font="times 18",bg="powder blue")
        label3 = Label(w,text="Enter corresponding inclination of unknown forces",fg="darkcyan",font="impact 18",bg="powder blue")
        enter = Entry(w,fg="darkcyan",font="impact 20",bd=8)
        first_angle = Entry(fg="green",font="impact 18",bd=8)
        second_angle = Entry(fg="green",font="impact 18",bd=8)
        Output.delete(0.0,END)
        Output.config(fg="darkgreen",font="impact 16")
        Output.insert(END,"Instructions\n")
        Output.config(fg="darkgreen",font="times 15")
        Output.insert(END,"The inclination is the angle measured in degree between the  positive x-axis and force in anti-clockwise direction" )
        Output.place(x=0,y=500,width=800,height=140)
        first_angle.place(x=450,y=250,width=100)
        second_angle.place(x=450,y=300,width=100)
        label3.place(x=150,y=200)
        label1.place(x=250,y=250)
        label2.place(x=250,y=310)
        L.place(x=150,y=100)
        enter.place(x=550,y=100,width=100)
        def submit():
            n=int(enter.get())
            F[0].a=float(first_angle.get())
            F[1].a=float(second_angle.get())
            label1.destroy()
            label2.destroy()
            label3.destroy()
            first_angle.destroy()
            second_angle.destroy()
            enter.destroy()
            L.destroy()
            SB.destroy()
            forceDefiner(n,4,2,F,1)
        
        SB = Button(w,text="Submit",bg="palegreen",fg="black",font="times 18",command= submit,bd=8)
        SB.place(x=280,y=400,width=100)
        CANCEL.place(x=400,y=400,width=100)
        
      
    UB.place_forget()
    L1.place_forget()
    RB.place_forget()
    EB.place_forget()
    Output.place_forget()
    label = Label(w,text="Choose the number of unknown force ",fg="darkcyan",bg="powder blue",font="impact 20 bold")
    button1 = Button(w,text="1",bg="palegreen",fg="green",font="impact 22 bold",command= one,bd=8)
    button2 = Button(w,text="2",bg="palegreen",fg="green",font="impact 22 bold",command= two,bd=8)
    label.place(x=150,y=100)
    button1.place(x=150,y=300,width=150,height=75)
    button2.place(x=500,y=300,width=150,height=75)
    CANCEL.place(x=350,y=400,width=100)

def cancel():
    widget_list = w.winfo_children()
    for item in widget_list :
        if item.winfo_children() :
            widget_list.extend(item.winfo_children())
    for item in widget_list:
        item.place_forget()
    output_scr()
    
w=Tk()
w.title("Force Calculator v1.2.0.1")
        
w.iconbitmap("icon.ico")
w.minsize(800,640)
w.maxsize(800,640)
L1 = Label(w,text="what service you want",fg="darkcyan",bg="powder blue",font="impact 36 bold",)
RB = Button(w,text="Calculate\nResultant",bg="palegreen",fg="darkgreen",font="times 14 ",command=Resultant,bd=8)
EB = Button(w,text="Check\nEquillibrium",bg="palegreen",fg="darkgreen",font="times 14 ",command=equilibriumCheck,bd=8)
UB = Button(w,text="Find unknown\nforce",bg="palegreen",fg="darkgreen",font="times 14 ",command=unknown_force,bd=8)
CANCEL =Button(w,bg="orange red",text="Cancel",font="times 18",command=cancel,bd=8)
Output = Text(w,wrap= WORD,fg="darkgreen",font="ariel 20 bold",borderwidth=18)
UB.place(x=300,y=350,width=200,height=75)
L1.place(x=150,y=50)
RB.place(x=300,y=150,width=200,height=75)
EB.place(x=300,y=250,width=200,height=75)
Output.place(x=0,y=450,width=800,height=190)
Output.insert(END,'Output Box: ')
w.config(bg="powder blue")
w.mainloop()




















