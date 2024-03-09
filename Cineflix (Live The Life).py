#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Complete Code = FRONTEND + BACKEND


import tkinter as tk
from tkinter import *
from tkinter import Label, Frame, Button
from tkinter import ttk
import webbrowser
import mysql.connector
import random

class Cinema:
    
    
    def __init__(self):
        self.root = root
        self.root.title("Cineflix")
        self.root.geometry("1280x720")

        frame = tk.Frame(self.root, borderwidth=12, relief=tk.RIDGE, bg="white")
        frame.place(width=1280, height=720)

        lb1Member = tk.Label(frame, font=("arial", 40, "bold"), text="Cineflix", bg="white",fg="black")
        lb1Member.place(x=390,y=15,width=500,height=65)

        lb1Member = tk.Label(frame, font=("lucida handwriting", 14), text="LIVE the LIFE", bg="white",fg="black")
        lb1Member.place(x=390,y=80,width=500,height=30)

        lb1Member = tk.Label(frame, font=("arial", 14, "bold"), text="Select The City:", bg="white")
        lb1Member.place(x=565, y=300)

        options = ["Ahmedabad", "Delhi", "Jaipur", "Mumbai", "Pune"]
        dropdown_var = tk.StringVar(root)
        dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=options)
        dropdown.place(x=580, y=340)

        
        def on_select(event):
            selected_city = dropdown_var.get()
            if selected_city in options:
                self.main_window(selected_city)
            else:
                show_label.config(text="Currently not availiable in your city",bg="light grey")
        button = tk.Button(root, text="Proceed", command=lambda: on_select(None))
        button.place(x=620, y=380)        

### --------------------------------------------------Main WIndow-------------------------------------------------------------
### --------------------------------------------------------------------------------------------------------------------------

    def main_window(self, selected_city):
        self.root1=tk.Tk()
        self.root1.geometry("1280x720+0+0")
        self.root1.title("Cineflix")
        self.root1.configure(bg="powder blue")
        lbltitle=Label(self.root1,text="Cineflix",bg="white",fg="blue",bd=10,relief=RAISED,font=("times new roman",25,"bold"))
        lbltitle.place(x=5,y=10,width=200,height=50)

        framebutton=Frame(self.root1,bd=0,relief=RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=210,y=10,width=1320,height=50)

        
        btnHome=Button(framebutton,text="HOME",font=("Times new roman",20,"bold"),fg="blue",width=13,bg="powder blue",command=self.home)
        btnHome.place(x=0,y=0,width=115,height=50)
        btnHome.configure(highlightcolor="black",borderwidth=0,relief="solid")

        
        btnOrdSn=Button(framebutton,text="CINEMA",font=("Times new roman",20,"bold"),fg="blue",width=13,bg="powder blue",command=self.cinema)
        btnOrdSn.place(x=128,y=0,width=120,height=50)
        btnOrdSn.configure(highlightcolor="black",borderwidth=0,relief="solid")

        
        btnMS=Button(framebutton,text="SCHEDULES",font=("Times new roman",20,"bold"),fg="blue",width=13,bg="powder blue",command=self.schedule)
        btnMS.place(x=275,y=0,width=170,height=50)
        btnMS.configure(highlightcolor="black",borderwidth=0,relief="solid")
        
        
        btnQ=Button(framebutton,text="ADVERTISE",font=("Times new roman",20,"bold"),fg="blue",width=13,bg="powder blue",command=self.advertise)
        btnQ.place(x=465,y=0,width=175,height=50)
        btnQ.configure(highlightcolor="black",borderwidth=0,relief="solid")
        
        btnQW=Button(framebutton,text="SUPPORT",font=("Times new roman",20,"bold"),fg="blue",width=13,bg="powder blue",command=self.support)
        btnQW.place(x=640,y=0,width=175,height=50)
        btnQW.configure(highlightcolor="black",borderwidth=0,relief="solid")

        
        btnQB=Button(framebutton,text="ABOUT US",font=("Times new roman",20,"bold"),fg="blue",width=13,bg="powder blue",command=self.about)
        btnQB.place(x=820,y=0,width=175,height=50)
        btnQB.configure(highlightcolor="black",borderwidth=0,relief="solid")

        
        
        framebutton2=Frame(self.root1,bd=0,relief=RIDGE,padx=20,bg="powder blue")
        framebutton2.place(x=0,y=70,width=1550,height=40)

        
        btnNSM=Button(framebutton2,text="Now Showing Movies",font=("Times new roman",15),fg="red",width=20,bg="white",command=self.now_showing_movies)
        btnNSM.place(x=60,y=0,height=30,width=200)
        btnNSM.configure(highlightcolor="black",borderwidth=2,relief="solid")

        
        btnCSM=Button(framebutton2,text="Coming Soon Movies",font=("Times new roman",15),fg="red",width=20,bg="white",command=self.coming_soon_movies)
        btnCSM.place(x=300,y=0,height=30,width=200)
        btnCSM.configure(highlightcolor="black",borderwidth=2,relief="solid")

        
        
        frameMovies=Frame(self.root1,bd=0,relief=RIDGE,padx=20,bg="powder blue")
        frameMovies.place(x=0,y=110,width=1550,height=650)

        
        lblMovies1=Label(frameMovies,text="Fighter",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies1.place(x=60,y=0,width=200,height=190)
        lblMovies1.config(highlightbackground="red")
        def show_info1(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies1.config(text=f"Action\n\n02h 47min\n\nUA",font=("Times new roman",23))

        lblMovies1.bind("<Enter>", show_info1)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies1.bind("<Leave>", lambda event: lblMovies1.config(text="Fighter",font=("Times new roman",35)))

        btnM1B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov1)
        btnM1B.place(x=60,y=195,height=30,width=200)
        btnM1B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM1B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer1)
        btnM1B.place(x=60,y=225,height=30,width=200)
        btnM1B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies2=Label(frameMovies,text="Teri Baaton\nMein Aisa\nUljha\nDiya",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",25))
        lblMovies2.place(x=366,y=0,width=200,height=190)
        def show_info2(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies2.config(text=f"Comedy\n\n02h 23min\n\nUA",font=("Times new roman",23))

        lblMovies2.bind("<Enter>", show_info2)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies2.bind("<Leave>", lambda event: lblMovies2.config(text="Teri Baaton\nMein Aisa\nUljha\nDiya",font=("Times new roman",25)))

        btnM2B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov2)
        btnM2B.place(x=366,y=195,height=30,width=200)
        btnM2B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM2B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer2)
        btnM2B.place(x=366,y=225,height=30,width=200)
        btnM2B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies3=Label(frameMovies,text="Hanuman",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies3.place(x=672,y=0,width=200,height=190)
        def show_info3(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies3.config(text=f"Action\n\n02h 38min\n\nUA",font=("Times new roman",23))

        lblMovies3.bind("<Enter>", show_info3)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies3.bind("<Leave>", lambda event: lblMovies3.config(text="Hanuman",font=("Times new roman",35)))

        btnM3B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov3)
        btnM3B.place(x=672,y=195,height=30,width=200)
        btnM3B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM3B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer3)
        btnM3B.place(x=672,y=225,height=30,width=200)
        btnM3B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies4=Label(frameMovies,text="Argylle",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies4.place(x=978,y=0,width=200,height=190)
        def show_info4(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies4.config(text=f"Action,Comedy\n\n02h 19min\n\nUA",font=("Times new roman",20))

        lblMovies4.bind("<Enter>", show_info4)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies4.bind("<Leave>", lambda event: lblMovies4.config(text="Argylle",font=("Times new roman",35)))

        btnM4B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov4)
        btnM4B.place(x=978,y=195,height=30,width=200)
        btnM4B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM4B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer4)
        btnM4B.place(x=978,y=225,height=30,width=200)
        btnM4B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies5=Label(frameMovies,text="12th Fail",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies5.place(x=60,y=275,width=200,height=190)
        def show_info5(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies5.config(text=f"Drama\n\n02h 27min\n\nU",font=("Times new roman",23))

        lblMovies5.bind("<Enter>", show_info5)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies5.bind("<Leave>", lambda event: lblMovies5.config(text="12th Fail",font=("Times new roman",35)))

        btnM5B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov5)
        btnM5B.place(x=60,y=470,height=30,width=200)
        btnM5B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM5B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer5)
        btnM5B.place(x=60,y=500,height=30,width=200)
        btnM5B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies6=Label(frameMovies,text="Main\nAtal\nHoon",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies6.place(x=366,y=275,width=200,height=190)
        def show_info6(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies6.config(text=f"Biography\n\n02h 19min\n\nUA",font=("Times new roman",23))

        lblMovies6.bind("<Enter>", show_info6)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies6.bind("<Leave>", lambda event: lblMovies6.config(text="Main\nAtal\nHoon",font=("Times new roman",35)))

        btnM6B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov6)
        btnM6B.place(x=366,y=470,height=30,width=200)
        btnM6B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM6B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer6)
        btnM6B.place(x=366,y=500,height=30,width=200)
        btnM6B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies7=Label(frameMovies,text="Dunki",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies7.place(x=672,y=275,width=200,height=190)
        def show_info7(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies7.config(text=f"Comedy,Drama\n\n02h 41min\n\nUA",font=("Times new roman",20))

        lblMovies7.bind("<Enter>", show_info7)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies7.bind("<Leave>", lambda event: lblMovies7.config(text="Dunki",font=("Times new roman",35)))

        btnM7B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov7)
        btnM7B.place(x=672,y=470,height=30,width=200)
        btnM7B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM7B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer7)
        btnM7B.place(x=672,y=500,height=30,width=200)
        btnM7B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies8=Label(frameMovies,text="Warning\n2",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies8.place(x=978,y=275,width=200,height=190)
        def show_info8(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies8.config(text=f"Action,Crime\n\n02h 07min\n\nA",font=("Times new roman",23))

        lblMovies8.bind("<Enter>", show_info8)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies8.bind("<Leave>", lambda event: lblMovies8.config(text="Warning\n2",font=("Times new roman",35)))

        btnM8B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov8)
        btnM8B.place(x=978,y=470,height=30,width=200)
        btnM8B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM8B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer8)
        btnM8B.place(x=978,y=500,height=30,width=200)
        btnM8B.configure(highlightcolor="white",borderwidth=2,relief="solid")
    
    
### ---------------------------------------------Now Showing Movies Page------------------------------------------------------
### --------------------------------------------------------------------------------------------------------------------------    
    
    def now_showing_movies(self):
        
        frameMovies=Frame(self.root1,bd=0,relief=RIDGE,padx=20,bg="powder blue")
        frameMovies.place(x=0,y=110,width=1550,height=650)

        
        lblMovies1=Label(frameMovies,text="Fighter",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies1.place(x=60,y=0,width=200,height=190)
        lblMovies1.config(highlightbackground="red")
        def show_info1(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies1.config(text=f"Action\n\n02h 47min\n\nUA",font=("Times new roman",23))

        lblMovies1.bind("<Enter>", show_info1)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies1.bind("<Leave>", lambda event: lblMovies1.config(text="Fighter",font=("Times new roman",35)))

        btnM1B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov1)
        btnM1B.place(x=60,y=195,height=30,width=200)
        btnM1B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM1B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer1)
        btnM1B.place(x=60,y=225,height=30,width=200)
        btnM1B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies2=Label(frameMovies,text="Teri Baaton\nMein Aisa\nUljha\nDiya",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",25))
        lblMovies2.place(x=366,y=0,width=200,height=190)
        def show_info2(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies2.config(text=f"Comedy\n\n02h 23min\n\nUA",font=("Times new roman",23))

        lblMovies2.bind("<Enter>", show_info2)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies2.bind("<Leave>", lambda event: lblMovies2.config(text="Teri Baaton\nMein Aisa\nUljha\nDiya",font=("Times new roman",25)))

        btnM2B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov2)
        btnM2B.place(x=366,y=195,height=30,width=200)
        btnM2B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM2B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer2)
        btnM2B.place(x=366,y=225,height=30,width=200)
        btnM2B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies3=Label(frameMovies,text="Hanuman",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies3.place(x=672,y=0,width=200,height=190)
        def show_info3(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies3.config(text=f"Action\n\n02h 38min\n\nUA",font=("Times new roman",23))

        lblMovies3.bind("<Enter>", show_info3)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies3.bind("<Leave>", lambda event: lblMovies3.config(text="Hanuman",font=("Times new roman",35)))

        btnM3B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov3)
        btnM3B.place(x=672,y=195,height=30,width=200)
        btnM3B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM3B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer3)
        btnM3B.place(x=672,y=225,height=30,width=200)
        btnM3B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies4=Label(frameMovies,text="Argylle",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies4.place(x=978,y=0,width=200,height=190)
        def show_info4(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies4.config(text=f"Action,Comedy\n\n02h 19min\n\nUA",font=("Times new roman",20))

        lblMovies4.bind("<Enter>", show_info4)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies4.bind("<Leave>", lambda event: lblMovies4.config(text="Argylle",font=("Times new roman",35)))

        btnM4B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov4)
        btnM4B.place(x=978,y=195,height=30,width=200)
        btnM4B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM4B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer4)
        btnM4B.place(x=978,y=225,height=30,width=200)
        btnM4B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies5=Label(frameMovies,text="12th Fail",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies5.place(x=60,y=275,width=200,height=190)
        def show_info5(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies5.config(text=f"Drama\n\n02h 27min\n\nU",font=("Times new roman",23))

        lblMovies5.bind("<Enter>", show_info5)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies5.bind("<Leave>", lambda event: lblMovies5.config(text="12th Fail",font=("Times new roman",35)))

        btnM5B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov5)
        btnM5B.place(x=60,y=470,height=30,width=200)
        btnM5B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM5B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer5)
        btnM5B.place(x=60,y=500,height=30,width=200)
        btnM5B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies6=Label(frameMovies,text="Main\nAtal\nHoon",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies6.place(x=366,y=275,width=200,height=190)
        def show_info6(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies6.config(text=f"Biography\n\n02h 19min\n\nUA",font=("Times new roman",23))

        lblMovies6.bind("<Enter>", show_info6)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies6.bind("<Leave>", lambda event: lblMovies6.config(text="Main\nAtal\nHoon",font=("Times new roman",35)))

        btnM6B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov6)
        btnM6B.place(x=366,y=470,height=30,width=200)
        btnM6B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM6B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer6)
        btnM6B.place(x=366,y=500,height=30,width=200)
        btnM6B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies7=Label(frameMovies,text="Dunki",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies7.place(x=672,y=275,width=200,height=190)
        def show_info7(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies7.config(text=f"Comedy,Drama\n\n02h 41min\n\nUA",font=("Times new roman",20))

        lblMovies7.bind("<Enter>", show_info7)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies7.bind("<Leave>", lambda event: lblMovies7.config(text="Dunki",font=("Times new roman",35)))

        btnM7B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov7)
        btnM7B.place(x=672,y=470,height=30,width=200)
        btnM7B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM7B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer7)
        btnM7B.place(x=672,y=500,height=30,width=200)
        btnM7B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies8=Label(frameMovies,text="Warning\n2",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies8.place(x=978,y=275,width=200,height=190)
        def show_info8(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies8.config(text=f"Action,Crime\n\n02h 07min\n\nA",font=("Times new roman",23))

        lblMovies8.bind("<Enter>", show_info8)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies8.bind("<Leave>", lambda event: lblMovies8.config(text="Warning\n2",font=("Times new roman",35)))

        btnM8B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov8)
        btnM8B.place(x=978,y=470,height=30,width=200)
        btnM8B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM8B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer8)
        btnM8B.place(x=978,y=500,height=30,width=200)
        btnM8B.configure(highlightcolor="white",borderwidth=2,relief="solid")
    

# ----------------------------------------------- Book now window ------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------

    def booknow(self,url,url1):

        def paytm():
            webbrowser.open(url)
            button1.config(bg="blue",fg="white")
            button2.config(bg="white",fg="red")

        def bookmyshow():
            webbrowser.open(url1)
            button1.config(bg="white",fg="blue")
            button2.config(bg="red",fg="white")
        def change_color_enter(event):
            event.widget.config(bg="blue",fg="white")  # Change color to lightblue when cursor enters

        def change_color_leave(event):
            event.widget.config(bg="white",fg="blue")  # Change color to default when cursor leaves

        def change_color_enter1(event):
            event.widget.config(bg="red",fg="white")  # Change color to lightblue when cursor enters

        def change_color_leave1(event):
            event.widget.config(bg="white",fg="red")  # Change color to default when cursor leaves

        self.root2 = tk.Tk()
        self.root2.geometry("420x200+0+0")
        self.root2.title("Cineflix Book Now")

        lbltitle = tk.Label(self.root2, text="Proceed With:", fg="blue", font=("times new roman", 18, "bold"))
        lbltitle.place(x=100, y=10, width=200, height=50)

        button1 = tk.Button(self.root2, text="Paytm", font=("Times new roman", 19, "bold"), fg="blue", width=13, bg="white", command=paytm)
        button1.place(x=20, y=90, width=180, height=50)
        button1.bind("<Enter>", change_color_enter)  # Bind event when cursor enters button
        button1.bind("<Leave>", change_color_leave)  # Bind event when cursor leaves button

        button2 = tk.Button(self.root2, text="BookMyShow", font=("Times new roman", 19, "bold"), fg="red", width=13, bg="white", command=bookmyshow)
        button2.place(x=220, y=90, width=180, height=50)
        button2.bind("<Enter>", change_color_enter1)  # Bind event when cursor enters button
        button2.bind("<Leave>", change_color_leave1)  # Bind event when cursor leaves button
    
    def mov1(self):
        url="https://paytm.com/movies/fighter-movie-detail-145127?frmtid=3ih1_rihf"
        url1="https://in.bookmyshow.com/movies/fighter/ET00304730"
        self.booknow(url,url1)
    def mov2(self):
        url="https://paytm.com/movies/teri-baaton-mein-aisa-uljha-jiya-movie-detail-169320?frmtid=hr8b6uvmc"
        url1="https://in.bookmyshow.com/jaipur/movies/teri-baaton-mein-aisa-uljha-jiya/ET00383266"
        self.booknow(url,url1)
        
    def mov3(self):
        url="https://paytm.com/movies/hanuman-movie-detail-153751?frmtid=stsfadazo"
        url1="https://in.bookmyshow.com/national-capital-region-ncr/movies/hanuman/ET00311673"
        self.booknow(url,url1)
        
    def mov4(self):
        url="https://paytm.com/movies/argylle-movie-detail-166927?frmtid=dcnbr2can3"
        url1="https://in.bookmyshow.com/national-capital-region-ncr/movies/argylle/ET00371535"
        self.booknow(url,url1)
        
    def mov5(self):
        url="https://paytm.com/movies/12th-fail-movie-detail-165204?frmtid=rngxeqsox"
        url1="https://in.bookmyshow.com/national-capital-region-ncr/movies/12th-fail/ET00363787"
        self.booknow(url,url1)
        
    def mov6(self):
        url="https://paytm.com/movies/main-atal-hoon-movie-detail-158906?frmtid=cbyuchdk4"
        url1="https://in.bookmyshow.com/national-capital-region-ncr/movies/main-atal-hoon/ET00348408"
        self.booknow(url,url1)
        
    def mov7(self):
        url="https://paytm.com/movies/dunki-movie-detail-153868?frmtid=oy5j~os4h5"
        url1="https://in.bookmyshow.com/national-capital-region-ncr/movies/dunki/ET00326964"
        self.booknow(url,url1)
        
    def mov8(self):
        url="https://paytm.com/movies/warning-2-movie-detail-146793?frmtid=jw63bdhre"
        url1="https://in.bookmyshow.com/national-capital-region-ncr/movies/warning-2/ET00379967"
        self.booknow(url1)

# ----------------------------------------------- Movie Trailers ------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------
    
    def show_trailer(self,url2):
        webbrowser.open(url2)
        
    def Trailer1(self):
        url2="https://www.youtube.com/watch?v=X6cnfMOVHMU"
        self.show_trailer(url2)
    def Trailer2(self):
        url2="https://www.youtube.com/watch?v=w_N6d4ec79c"
        self.show_trailer(url2)
        
    def Trailer3(self):
        url2="https://www.youtube.com/watch?v=BsgtYM157K8"
        self.show_trailer(url2)
        
    def Trailer4(self):
        url2="https://www.youtube.com/watch?v=7mgu9mNZ8Hk"
        self.show_trailer(url2)
        
    def Trailer5(self):
        url2="https://www.youtube.com/watch?v=KjbtuqENvVE"
        self.show_trailer(url2)
        
    def Trailer6(self):
        url2="https://www.youtube.com/watch?v=D8ytz6RxuS4"
        self.show_trailer(url2)
        
    def Trailer7(self):
        url2="https://www.youtube.com/watch?v=Zd69FfhBmSc"
        self.show_trailer(url2)
        
    def Trailer8(self):
        url2="https://www.youtube.com/watch?v=0Q_v2Vs24sQ"
        self.show_trailer(url2)
    
### ---------------------------------------------Coming Soon Movies Page------------------------------------------------------
### --------------------------------------------------------------------------------------------------------------------------     
    
    def coming_soon_movies(self):

        frameMovies=Frame(self.root1,bd=0,relief=RIDGE,padx=20,bg="powder blue")
        frameMovies.place(x=0,y=110,width=1550,height=650)

        lblMovies1=Label(frameMovies,text="Article 370",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",30))
        lblMovies1.place(x=60,y=0,width=200,height=190)
        lblMovies1.config(highlightbackground="red")
        def show_info1(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies1.config(text=f"Article 370\n\nPolitical,\nDrama",font=("Times new roman",23))

        lblMovies1.bind("<Enter>", show_info1)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies1.bind("<Leave>", lambda event: lblMovies1.config(text="Article 370",font=("Times new roman",30)))

        btnM1B=Button(frameMovies,text="Release Date-\n30 Aug 24",font=("Times new roman",15),fg="red",width=17,bg="white")
        btnM1B.place(x=60,y=195,height=50,width=200)
        btnM1B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM1B=Button(frameMovies,text="Set Alert",font=("Times new roman",15),fg="red",width=17,bg="white",command=lambda: self.change_value(1))
        btnM1B.place(x=60,y=245,height=50,width=200)
        btnM1B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies2=Label(frameMovies,text="Vedaa",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies2.place(x=366,y=0,width=200,height=190)
        def show_info2(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies2.config(text=f"Vedaa\n\nAction,\nDrama",font=("Times new roman",25))

        lblMovies2.bind("<Enter>", show_info2)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies2.bind("<Leave>", lambda event: lblMovies2.config(text="Vedaa",font=("Times new roman",33)))

        btnM2B=Button(frameMovies,text="Release Date-\n12 July 24",font=("Times new roman",15),fg="red",width=17,bg="white")
        btnM2B.place(x=366,y=195,height=50,width=200)
        btnM2B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM2B=Button(frameMovies,text="Set Alert",font=("Times new roman",15),fg="red",width=17,bg="white",command=lambda: self.change_value(2))
        btnM2B.place(x=366,y=245,height=50,width=200)
        btnM2B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies3=Label(frameMovies,text="Pushpa 2\nRule",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",30))
        lblMovies3.place(x=672,y=0,width=200,height=190)
        def show_info3(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies3.config(text=f"Pushpa 2:\n Rule\n\nAction",font=("Times new roman",25))

        lblMovies3.bind("<Enter>", show_info3)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies3.bind("<Leave>", lambda event: lblMovies3.config(text="Pushpa 2\nRule",font=("Times new roman",28)))

        btnM3B=Button(frameMovies,text="Release Date-\n15 Aug 24",font=("Times new roman",15),fg="red",width=17,bg="white")
        btnM3B.place(x=672,y=195,height=50,width=200)
        btnM3B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM3B=Button(frameMovies,text="Set Alert",font=("Times new roman",15),fg="red",width=17,bg="white",command=lambda: self.change_value(3))
        btnM3B.place(x=672,y=245,height=50,width=200)
        btnM3B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies4=Label(frameMovies,text="Stree 2",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",28))
        lblMovies4.place(x=978,y=0,width=200,height=190)
        def show_info4(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies4.config(text=f"Stree 2\n\nComedy,\nHorror",font=("Times new roman",23))

        lblMovies4.bind("<Enter>", show_info4)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies4.bind("<Leave>", lambda event: lblMovies4.config(text="Stree 2",font=("Times new roman",28)))

        btnM4B=Button(frameMovies,text="Release Date-\n7 May 27",font=("Times new roman",15),fg="red",width=17,bg="white")
        btnM4B.place(x=978,y=195,height=50,width=200)
        btnM4B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM4B=Button(frameMovies,text="Set Alert",font=("Times new roman",15),fg="red",width=17,bg="white",command=lambda: self.change_value(4))
        btnM4B.place(x=978,y=245,height=50,width=200)
        btnM4B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        
        
### ---------------------------------------------------Set Alert Window-------------------------------------------------------
### ---------------------------------------------------Set Alert Window-------------------------------------------------------

    def alert(self):
        self.root4=Tk()
        self.root4.geometry("680x520")
        self.root4.title("Cineflix Set Alert")

        lb1Member = tk.Label(self.root4,font=("arial", 20, "bold"), text="Type your e-mail:")
        lb1Member.place(x=220, y=200)

        self.txtEmail = tk.Entry(self.root4,font=("arial", 10, "bold"))
        self.txtEmail.place(x=240, y=240, height=25, width=200)

        button = tk.Button(self.root4, text="Proceed", command=self.alert_input)
        button.place(x=300, y=280, height=25, width=60)

        self.result_label = tk.Label(self.root4, font=("arial", 12))
        self.result_label.place(x=230, y=380)

    def alert_input(self):
        self.email_entry = self.txtEmail.get()

        h, j, d = 0, 0, 0
        if len(self.email_entry) >= 9:
            if self.email_entry[0].isalpha():
                if ("@" in self.email_entry) and (self.email_entry.count("@") == 1) and (self.email_entry[-10] == "@"):
                    if ("gmail.com" in self.email_entry) and (self.email_entry[-4] == "."):
                        for k in self.email_entry:
                            if k == k.isspace():
                                h = 1
                            elif k.isalpha():
                                if k == k.upper():
                                    j = 1
                            elif k.isdigit():
                                continue
                            elif k == "_" or k == "." or k == "@":
                                continue
                            else:
                                d = 1
                        if h == 1 or j == 1 or d == 1:
                            self.result_label.config(text="Email entered was incorrect")
                        else:
                            self.result_label.config(text="You will get notified by email when \nthe booking will open")
                            insert_query="Insert into alert(e_mail_id,Movie) values (%s,%s)"
                            vals=[self.email_entry,self.movie]
                            self.my_cursor.execute(insert_query,vals)
                            self.conn.commit()
                    else:
                        self.result_label.config(text="Email entered was incorrect")
                else:
                    self.result_label.config(text="Email entered was incorrect")
            else:
                self.result_label.config(text="Email entered was incorrect")
        else:
            self.result_label.config(text="Email entered was incorrect")

    def change_value(self,button_value):
        self.movie="0"
        if button_value == 1:
            self.movie="Article 370"
            self.alert()
        elif button_value == 2:
            self.movie="Vedaa"
            self.alert()
        elif button_value == 3:
            self.movie="Pushpa 2: Rule"
            self.alert()
        else:
            self.movie="Stree 2"
            self.alert()

                
### ------------------------------------------------------Home Page-----------------------------------------------------------
### -------------------------------------------------------------------------------------------------------------------------- 
    
    def home(self):
        
        framebutton2=Frame(self.root1,bd=0,relief=RIDGE,padx=20,bg="powder blue")
        framebutton2.place(x=0,y=70,width=1550,height=40)

        
        btnNSM=Button(framebutton2,text="Now Showing Movies",font=("Times new roman",15),fg="red",width=20,bg="white",command=self.home)
        btnNSM.place(x=60,y=0,height=30,width=200)
        btnNSM.configure(highlightcolor="black",borderwidth=2,relief="solid")

        
        btnCSM=Button(framebutton2,text="Coming Soon Movies",font=("Times new roman",15),fg="red",width=20,bg="white",command=self.coming_soon_movies)
        btnCSM.place(x=300,y=0,height=30,width=200)
        btnCSM.configure(highlightcolor="black",borderwidth=2,relief="solid")

        
        
        frameMovies=Frame(self.root1,bd=0,relief=RIDGE,padx=20,bg="powder blue")
        frameMovies.place(x=0,y=110,width=1550,height=650)

        
        lblMovies1=Label(frameMovies,text="Fighter",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies1.place(x=60,y=0,width=200,height=190)
        lblMovies1.config(highlightbackground="red")
        def show_info1(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies1.config(text=f"Action\n\n02h 47min\n\nUA",font=("Times new roman",23))

        lblMovies1.bind("<Enter>", show_info1)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies1.bind("<Leave>", lambda event: lblMovies1.config(text="Fighter",font=("Times new roman",35)))

        btnM1B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov1)
        btnM1B.place(x=60,y=195,height=30,width=200)
        btnM1B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM1B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer1)
        btnM1B.place(x=60,y=225,height=30,width=200)
        btnM1B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies2=Label(frameMovies,text="Teri Baaton\nMein Aisa\nUljha\nDiya",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",25))
        lblMovies2.place(x=366,y=0,width=200,height=190)
        def show_info2(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies2.config(text=f"Comedy\n\n02h 23min\n\nUA",font=("Times new roman",23))

        lblMovies2.bind("<Enter>", show_info2)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies2.bind("<Leave>", lambda event: lblMovies2.config(text="Teri Baaton\nMein Aisa\nUljha\nDiya",font=("Times new roman",25)))

        btnM2B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov2)
        btnM2B.place(x=366,y=195,height=30,width=200)
        btnM2B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM2B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer2)
        btnM2B.place(x=366,y=225,height=30,width=200)
        btnM2B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies3=Label(frameMovies,text="Hanuman",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies3.place(x=672,y=0,width=200,height=190)
        def show_info3(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies3.config(text=f"Action\n\n02h 38min\n\nUA",font=("Times new roman",23))

        lblMovies3.bind("<Enter>", show_info3)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies3.bind("<Leave>", lambda event: lblMovies3.config(text="Hanuman",font=("Times new roman",35)))

        btnM3B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov3)
        btnM3B.place(x=672,y=195,height=30,width=200)
        btnM3B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM3B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer3)
        btnM3B.place(x=672,y=225,height=30,width=200)
        btnM3B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies4=Label(frameMovies,text="Argylle",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies4.place(x=978,y=0,width=200,height=190)
        def show_info4(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies4.config(text=f"Action,Comedy\n\n02h 19min\n\nUA",font=("Times new roman",20))

        lblMovies4.bind("<Enter>", show_info4)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies4.bind("<Leave>", lambda event: lblMovies4.config(text="Argylle",font=("Times new roman",35)))

        btnM4B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov4)
        btnM4B.place(x=978,y=195,height=30,width=200)
        btnM4B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM4B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer4)
        btnM4B.place(x=978,y=225,height=30,width=200)
        btnM4B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies5=Label(frameMovies,text="12th Fail",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies5.place(x=60,y=275,width=200,height=190)
        def show_info5(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies5.config(text=f"Drama\n\n02h 27min\n\nU",font=("Times new roman",23))

        lblMovies5.bind("<Enter>", show_info5)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies5.bind("<Leave>", lambda event: lblMovies5.config(text="12th Fail",font=("Times new roman",35)))

        btnM5B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov5)
        btnM5B.place(x=60,y=470,height=30,width=200)
        btnM5B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM5B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer5)
        btnM5B.place(x=60,y=500,height=30,width=200)
        btnM5B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies6=Label(frameMovies,text="Main\nAtal\nHoon",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies6.place(x=366,y=275,width=200,height=190)
        def show_info6(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies6.config(text=f"Biography\n\n02h 19min\n\nUA",font=("Times new roman",23))

        lblMovies6.bind("<Enter>", show_info6)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies6.bind("<Leave>", lambda event: lblMovies6.config(text="Main\nAtal\nHoon",font=("Times new roman",35)))

        btnM6B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov6)
        btnM6B.place(x=366,y=470,height=30,width=200)
        btnM6B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM6B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer6)
        btnM6B.place(x=366,y=500,height=30,width=200)
        btnM6B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies7=Label(frameMovies,text="Dunki",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies7.place(x=672,y=275,width=200,height=190)
        def show_info7(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies7.config(text=f"Comedy,Drama\n\n02h 41min\n\nUA",font=("Times new roman",20))

        lblMovies7.bind("<Enter>", show_info7)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies7.bind("<Leave>", lambda event: lblMovies7.config(text="Dunki",font=("Times new roman",35)))

        btnM7B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov7)
        btnM7B.place(x=672,y=470,height=30,width=200)
        btnM7B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM7B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer7)
        btnM7B.place(x=672,y=500,height=30,width=200)
        btnM7B.configure(highlightcolor="white",borderwidth=2,relief="solid")

        lblMovies8=Label(frameMovies,text="Warning\n2",bg="black",fg="yellow",bd=10,relief="raised",font=("times new roman",35))
        lblMovies8.place(x=978,y=275,width=200,height=190)
        def show_info8(event):
            x, y = event.x, event.y  # Label ke andar cursor ki position le lo
            lblMovies8.config(text=f"Action,Crime\n\n02h 07min\n\nA",font=("Times new roman",23))

        lblMovies8.bind("<Enter>", show_info8)  # Jab cursor label ke upar le jaata hai to show_info() function trigger hota hai
        lblMovies8.bind("<Leave>", lambda event: lblMovies8.config(text="Warning\n2",font=("Times new roman",35)))

        btnM8B=Button(frameMovies,text="Book Now",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.mov8)
        btnM8B.place(x=978,y=470,height=30,width=200)
        btnM8B.configure(highlightcolor="white",borderwidth=2,relief="solid")
        btnM8B=Button(frameMovies,text="Show Trailer",font=("Times new roman",15),fg="red",width=17,bg="white",command=self.Trailer8)
        btnM8B.place(x=978,y=500,height=30,width=200)
        btnM8B.configure(highlightcolor="white",borderwidth=2,relief="solid")

# ----------------------------------------------- Cinema Locations Page --------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------

    def cinema(self):
        def Ahemdabad():
            frameLocations=Frame(self.root1,bd=2,relief=SOLID,padx=20,bg="powder blue")
            frameLocations.place(x=202,y=120,width=1078,height=600)

            scrollbar=Scrollbar(frameLocations,orient=VERTICAL)
            scrollbar.pack(side=RIGHT,fill=Y)

            textarea=Text(frameLocations,height=600,width=1078,yscrollcommand=scrollbar.set)
            textarea.config(bg="powder blue",bd=0)
            textarea.pack()

            scrollbar.config(command=textarea.yview)

            textarea.insert(END,"\nCineflix Himalaya Mall, Ahmedabad\n","resize1")
            textarea.insert(END,"\nPVR Cineflix Limited.,Himalaya Mall 3rd floor, Himalaya Mall,\nDrive In Road, Gurukul,Ahmedabad, Gujarat-\n380052","resize2")
            textarea.insert(END,"\n\nPhone No.- 8080211111","resize3")
            textarea.tag_config("resize1",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize2",font=("times new roman",13,"bold"))
            textarea.tag_config("resize3",font=("times new roman",13,"bold"))

            textarea.config(state=DISABLED,bg="powder blue",bd=0)

            btn1.config(text="Ahemdabad >>>")
            btn2.config(text="Jaipur")
            btn3.config(text="Banglore")
            btn4.config(text="Delhi")
            btn5.config(text="Mumbai")

        def Jaipur():
            frameLocations=Frame(self.root1,bd=2,relief=SOLID,padx=20,bg="powder blue")
            frameLocations.place(x=202,y=120,width=1078,height=600)

            scrollbar=Scrollbar(frameLocations,orient=VERTICAL)
            scrollbar.pack(side=RIGHT,fill=Y)

            textarea=Text(frameLocations,height=600,width=1078,yscrollcommand=scrollbar.set)
            textarea.pack()

            scrollbar.config(command=textarea.yview)

            textarea.insert(END,"\n1. Cineflix Amrapali Circle,Vaishali Nagar","resize1")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 2nd Floor, Vaibhav Cinemultiplex,\nAmrapali Circle, Vaishali Nagar,Jaipur - 302021\nRajasthan","resize2")
            textarea.insert(END,"\n\nPhone No.- 9772178681","resize3")
            textarea.tag_config("resize1",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize2",font=("times new roman",13,"bold"))
            textarea.tag_config("resize3",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n2. Cineflix City Plaza Mall, Bani Park","resize4")
            textarea.insert(END,"\n\nPVR Cineflix Limited., Space Cinema, City Plaza Mall,\nJhotwara Road, Banipark, Jaipur - 302016, Rajasthan","resize5")
            textarea.insert(END,"\n\nPhone No.- 8976759132","resize6")
            textarea.tag_config("resize4",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize5",font=("times new roman",13,"bold"))
            textarea.tag_config("resize6",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n3. Cineflix Crystal Palm,C Scheme","resize7")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 4th Floor, Crystal Palm Mall, Sardar\nPatel Marg, C-Scheme, Jaipur - 302001, Rajasthan","resize8")
            textarea.insert(END,"\n\nPhone No.- 9772178683","resize9")
            textarea.tag_config("resize7",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize8",font=("times new roman",13,"bold"))
            textarea.tag_config("resize9",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n4. Cineflix Elements Mall,Ajmer Road","resize10")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 3rd Floor, Elements Mall, DCM Area,\nAjmer Road, Jaipur - 302021, Rajasthan","resize11")
            textarea.insert(END,"\n\nPhone No.- 8976759133","resize12")
            textarea.tag_config("resize10",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize11",font=("times new roman",13,"bold"))
            textarea.tag_config("resize12",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n5. Cineflix G.T Central, Malviya Nagar","resize13")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 4th Floor, GT Central Mall, Indira\nPalace, Malviya Nagar, Jaipur - 302017, Rajasthan","resize14")
            textarea.insert(END,"\n\nPhone No.- 9783729999","resize15")
            textarea.tag_config("resize13",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize14",font=("times new roman",13,"bold"))
            textarea.tag_config("resize15",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n6. Cineflix JTM Mall, Malviya Nagar","resize16")
            textarea.insert(END,"\n\nPVR Cineflix Limited., JTM MALL Model Town, Malviya\nNagar,Jaipur - 302017, Rajasthan","resize17")
            textarea.insert(END,"\n\nPhone No.- 8976759121","resize18")
            textarea.tag_config("resize16",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize17",font=("times new roman",13,"bold"))
            textarea.tag_config("resize18",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n7. Cineflix Pink Square Mall,Raja Park","resize19")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 4th Floor, Pink Square Mall, Govind\nMarg, Rajapark,Jaipur - 302004, Rajasthan","resize20")
            textarea.insert(END,"\n\nPhone No.- 9772178684","resize21")
            textarea.tag_config("resize19",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize20",font=("times new roman",13,"bold"))
            textarea.tag_config("resize21",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n8. Cineflix Sunny Trade Center","resize22")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 3rd Floor, Sunny Trade Center, New\nAatish Market, Mansarovar,Jaipur - 302020, Rajasthan,","resize23")
            textarea.insert(END,"\n\nPhone No.- 8976759128\n\n\n\n\n","resize24")
            textarea.tag_config("resize22",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize23",font=("times new roman",13,"bold"))
            textarea.tag_config("resize24",font=("times new roman",13,"bold"))

            textarea.config(state=DISABLED,bg="powder blue",bd=0)
            
            textarea.config(state=DISABLED,bg="powder blue",bd=0)
            btn1.config(text="Ahemdabad")
            btn2.config(text="Jaipur >>>")
            btn3.config(text="Banglore")
            btn4.config(text="Delhi")
            btn5.config(text="Mumbai")

        def Banglore():
            frameLocations=Frame(self.root1,bd=2,relief=SOLID,padx=20,bg="powder blue")
            frameLocations.place(x=202,y=120,width=1078,height=600)

            scrollbar=Scrollbar(frameLocations,orient=VERTICAL)
            scrollbar.pack(side=RIGHT,fill=Y)

            textarea=Text(frameLocations,height=600,width=1078,yscrollcommand=scrollbar.set)
            textarea.config(bg="powder blue",bd=0)
            textarea.pack()

            scrollbar.config(command=textarea.yview)

            textarea.insert(END,"\n1. Cineflix Brookefield Mall, Brookefield","resize1")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 4th Floor, Brookefield Mall,\nKundalahalli Main Road, Bengaluru - 560037,\nKarnataka","resize2")
            textarea.insert(END,"\n\nPhone No.- 9538275333","resize3")
            textarea.tag_config("resize1",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize2",font=("times new roman",13,"bold"))
            textarea.tag_config("resize3",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n2. Cineflix Central, Mantri Junction, JP Nagar","resize4")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 5th Floor, Central Mantri Junction,\n45th Cross, J.P. Nagar 2nd Phase,Bengaluru - 560069,\nKarnataka","resize5")
            textarea.insert(END,"\n\nPhone No.- 7899729014","resize6")
            textarea.tag_config("resize4",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize5",font=("times new roman",13,"bold"))
            textarea.tag_config("resize6",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n3. Cineflix Galleria Mall,Yelahanka","resize7")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 2nd Floor, Galleria Mall, Bellary Road,\nYelahanka, Bengaluru - 560064,\nKarnataka","resize8")
            textarea.insert(END,"\n\nPhone No.- 7829082626","resize9")
            textarea.tag_config("resize7",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize8",font=("times new roman",13,"bold"))
            textarea.tag_config("resize9",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n4. Cineflix Garuda Mall, Magrath Road","resize10")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 4th Floor, Garuda Mall, Magrath Road,\nBengaluru - 560025, Karnataka","resize11")
            textarea.insert(END,"\n\nPhone No.- 7899729011","resize12")
            textarea.tag_config("resize10",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize11",font=("times new roman",13,"bold"))
            textarea.tag_config("resize12",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n5. Cineflix Garuda Yelahanka","resize13")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 4th Floor, Garuda Yelahanka, 1st A\nMain Road, Yelahanka New Town, Bengaluru - 560064,\nKarnataka","resize14")
            textarea.insert(END,"\n\nPhone No.- 7829755657","resize15")
            textarea.tag_config("resize13",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize14",font=("times new roman",13,"bold"))
            textarea.tag_config("resize15",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n6. Cineflix Lido Mall, Ulsoor","resize16")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 2nd Floor, Lido Mall, Swamy\nVivekananda Road, Ulsoor, Bengaluru - 560008,\nKarnataka","resize17")
            textarea.insert(END,"\n\nPhone No.- 7899729015","resize18")
            textarea.tag_config("resize16",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize17",font=("times new roman",13,"bold"))
            textarea.tag_config("resize18",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n7. Cineflix Mantri Square, Malleshwarama","resize19")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 3rd Floor, Mantri Square, No. 1,\nSampige Road, Malleshwaram, Bengaluru - 560003,\nKarnataka","resize20")
            textarea.insert(END,"\n\nPhone No.- 9538271333","resize21")
            textarea.tag_config("resize19",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize20",font=("times new roman",13,"bold"))
            textarea.tag_config("resize21",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n8. Cineflix Nexus Whitefield","resize22")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 2nd Floor, Nexus Whitefield,\nWhitefield Main Road,Bengaluru - 560066, Karnataka","resize23")
            textarea.insert(END,"\n\nPhone No.- 9513915333","resize24")
            textarea.tag_config("resize22",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize23",font=("times new roman",13,"bold"))
            textarea.tag_config("resize24",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n9. Cineflix SBR Horizon, Seegehalli","resize25")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 2nd Floor, SBR Horizon Mall,\nSeegehalli,Bengaluru - 560067, Karnataka","resize26")
            textarea.insert(END,"\n\nPhone No.- 9538276333","resize27")
            textarea.tag_config("resize25",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize26",font=("times new roman",13,"bold"))
            textarea.tag_config("resize27",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n10. Cineflix Shree Garuda Swagath Mall, Jayanagar","resize28")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 4th Floor, Shree Garuda Swagath\nMall, Tilak Nagar Main Road, Jayanagar, Bengaluru -\n560041, Karnataka","resize29")
            textarea.insert(END,"\n\nPhone No.- 7899729012\n\n\n\n\n","resize30")
            textarea.tag_config("resize28",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize29",font=("times new roman",13,"bold"))
            textarea.tag_config("resize30",font=("times new roman",13,"bold"))
            textarea.config(state=DISABLED,bg="powder blue",bd=0)
            # lbltitle=Label(frameLocations,text=">>>     Cineflix Himalaya Mall, Ahmedabad",bg="powder blue",fg="blue",bd=0,relief=RAISED,font=("times new roman",15,"bold"))
            # lbltitle.place(x=-20,y=0,width=350,height=50)

            btn1.config(text="Ahemdabad")
            btn2.config(text="Jaipur")
            btn3.config(text="Banglore >>>")
            btn4.config(text="Delhi")
            btn5.config(text="Mumbai")

        def Delhi():
            frameLocations=Frame(self.root1,bd=2,relief=SOLID,padx=20,bg="powder blue")
            frameLocations.place(x=202,y=120,width=1078,height=600)

            scrollbar=Scrollbar(frameLocations,orient=VERTICAL)
            scrollbar.pack(side=RIGHT,fill=Y)

            textarea=Text(frameLocations,height=600,width=1078,yscrollcommand=scrollbar.set)
            textarea.pack()

            scrollbar.config(command=textarea.yview)

            textarea.insert(END,"\n1. Cineflix Eros One","resize1")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 1st Floor, Eros Cinema Building,\nJungpura Extension, New Delhi - 110014","resize2")
            textarea.insert(END,"\n\nPhone No.- 9818188748","resize3")
            textarea.tag_config("resize1",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize2",font=("times new roman",13,"bold"))
            textarea.tag_config("resize3",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n2. Cineflix IMAX Paras, Nehru Place","resize4")
            textarea.insert(END,"\n\nPVR Cineflix Limited.,Delhi Paras Paras Cinema\nBuilding,Nehru Place, New Delhi 110019","resize5")
            textarea.insert(END,"\n\nPhone No.- 7899729014","resize6")
            textarea.tag_config("resize4",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize5",font=("times new roman",13,"bold"))
            textarea.tag_config("resize6",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n3. Cineflix Insignia At Epicuria,Nehru Place","resize7")
            textarea.insert(END,"\n\nPVR Cineflix Limited., Lower Ground Floor, Epicuria, TDI\nSouth Bridge, Nehru Place Metro Station, PD Area,\nNehru Place, New Delhi - 110019","resize8")
            textarea.insert(END,"\n\nPhone No.- 7836030000","resize9")
            textarea.tag_config("resize7",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize8",font=("times new roman",13,"bold"))
            textarea.tag_config("resize9",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n4. Cineflix Insignia At RCube Monad Mall","resize10")
            textarea.insert(END,"\n\nPVR Cineflix Limited.,RCube Monad Mall, Shivaji Place\nDistrict Centre,Rajouri Garden,New Delhi – 110027.","resize11")
            textarea.insert(END,"\n\nPhone No.- 7899729011","resize12")
            textarea.tag_config("resize10",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize11",font=("times new roman",13,"bold"))
            textarea.tag_config("resize12",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n5. Cineflix Janak Place","resize13")
            textarea.insert(END,"\n\nPVR Cineflix Limited., Plot No. 19, Janak Place, Distt.\nCenter, Janak Puri, New Delhi - 110058","resize14")
            textarea.insert(END,"\n\nPhone No.- 8976759123","resize15")
            textarea.tag_config("resize13",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize14",font=("times new roman",13,"bold"))
            textarea.tag_config("resize15",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n6. Cineflix Nehru Place","resize16")
            textarea.insert(END,"\n\nPVR Cineflix Limited., Plot No. 45D, Nehru Place,New\nDelhi - 110019","resize17")
            textarea.insert(END,"\n\nPhone No.- 8976759121","resize18")
            textarea.tag_config("resize16",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize17",font=("times new roman",13,"bold"))
            textarea.tag_config("resize18",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n7. Cineflix Odeon,Connaught Place","resize19")
            textarea.insert(END,"\n\nPVR Cineflix Limited., Delhi Odeon, 2nd Floor, Odeon\nCinema Complex,D-Block, Connaught Place,New Delhi-\n110001.","resize20")
            textarea.insert(END,"\n\nPhone No.- 8452003364","resize21")
            textarea.tag_config("resize19",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize20",font=("times new roman",13,"bold"))
            textarea.tag_config("resize21",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n8. Cineflix Pacific Mall, Jasola","resize22")
            textarea.insert(END,"\n\nPVR Cineflix Limited.,Delhi Pacific Mall, Pacific Mall,","resize23")
            textarea.insert(END,"\n\nPhone No.- 8454931219","resize24")
            textarea.tag_config("resize22",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize23",font=("times new roman",13,"bold"))
            textarea.tag_config("resize24",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n9. Cineflix Patel Nagar","resize25")
            textarea.insert(END,"\n\nPVR Cineflix Limited., Suman Lata Bhadola Marg, Patel\nNagar,New Delhi - 110008","resize26")
            textarea.insert(END,"\n\nPhone No.- 9899212626","resize27")
            textarea.tag_config("resize25",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize26",font=("times new roman",13,"bold"))
            textarea.tag_config("resize27",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n10. Cineflix Vishal Mall, Rajouri Garden","resize28")
            textarea.insert(END,"\n\nPVR Cineflix Limited.,Delhi Vishal Mall, Vishal Cinema\nComplex,Plot No 1,District Center Rajouri Garden,New\nDelhi 110027","resize29")
            textarea.insert(END,"\n\nPhone No.- 7899729012\n\n\n\n\n","resize30")
            textarea.tag_config("resize28",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize29",font=("times new roman",13,"bold"))
            textarea.tag_config("resize30",font=("times new roman",13,"bold"))
            textarea.config(state=DISABLED,bg="powder blue",bd=0)

            btn1.config(text="Ahemdabad")
            btn2.config(text="Jaipur")
            btn3.config(text="Banglore")
            btn4.config(text="Delhi >>>")
            btn5.config(text="Mumbai")

        def Mumbai():
            frameLocations=Frame(self.root1,bd=2,relief=SOLID,padx=20,bg="powder blue")
            frameLocations.place(x=202,y=120,width=1078,height=600)

            scrollbar=Scrollbar(frameLocations,orient=VERTICAL)
            scrollbar.pack(side=RIGHT,fill=Y)

            textarea=Text(frameLocations,height=600,width=1078,yscrollcommand=scrollbar.set)
            textarea.pack()

            scrollbar.config(command=textarea.yview)

            textarea.insert(END,"\n1. Cineflix Insignia at Atria Mall, Worli","resize1")
            textarea.insert(END,"\n\nPVR Cineflix Limited., Atria The Millenium Mall, Dr. Annie\nBesant Road, Worli,Mumbai - 400018, Maharashtra","resize2")
            textarea.insert(END,"\n\nPhone No.- 8291000044","resize3")
            textarea.tag_config("resize1",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize2",font=("times new roman",13,"bold"))
            textarea.tag_config("resize3",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n2. Cineflix Laserplex, CR2, Nariman Point","resize4")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 2nd Floor, CR2 Mall, Cross Road-2,\nBarrister Rajani Patel Marg, Nariman Point, Mumbai -\n400021, Maharashtra","resize5")
            textarea.insert(END,"\n\nPhone No.- 9769877749","resize6")
            textarea.tag_config("resize4",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize5",font=("times new roman",13,"bold"))
            textarea.tag_config("resize6",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n3. Cineflix Maison JIO World Plaza, BKC","resize7")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 3rd Floor, Jio World Plaza G Block\nBKC, Bandra Kurla Complex,Bandra East, Mumbai,\nMaharashtra 400055","resize8")
            textarea.insert(END,"\n\nPhone No.- 7836030000","resize9")
            textarea.tag_config("resize7",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize8",font=("times new roman",13,"bold"))
            textarea.tag_config("resize9",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n4. Cineflix Megaplex, Inorbit Mall,Malad(W)","resize10")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 2nd Floor, Inorbit Mall, Link Road,\nMalad - West, Mumbai - 400064, Maharashtra","resize11")
            textarea.insert(END,"\n\nPhone No.- 7506651231","resize12")
            textarea.tag_config("resize10",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize11",font=("times new roman",13,"bold"))
            textarea.tag_config("resize12",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n5. Cineflix Nakshatra Mall,Dadar (W)","resize13")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 2nd Floor, Nakshtra Cine Shoppe,\nRanade Road, Dadar - West, Mumbai - 400028,\nMaharashtra","resize14")
            textarea.insert(END,"\n\nPhone No.- 7506651221","resize15")
            textarea.tag_config("resize13",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize14",font=("times new roman",13,"bold"))
            textarea.tag_config("resize15",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n6. Cineflix Neelyog Square Mall,Ghatkopar (E)","resize16")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 3rd Floor, Neelyog Square Mall, R.B.\nMehta Road, Ghatkopar - East,Mumbai - 400077,\nMaharashtra","resize17")
            textarea.insert(END,"\n\nPhone No.- 8291027447","resize18")
            textarea.tag_config("resize16",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize17",font=("times new roman",13,"bold"))
            textarea.tag_config("resize18",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n7. Cineflix R-City Ghatkopar","resize19")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 3rd Floor, R City Mall, Amrut Nagar,\nL.B.S. Marg, Ghatkopar - West, Mumbai - 400086,\nMaharashtra","resize20")
            textarea.insert(END,"\n\nPhone No.- 7045518494","resize21")
            textarea.tag_config("resize19",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize20",font=("times new roman",13,"bold"))
            textarea.tag_config("resize21",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n8. Cineflix Raghuleela Mega Mall, Kandivali (W)","resize22")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 2nd Floor, Raghuleela Mega Mall,\nS.V Road, Kandivali - West,Mumbai - 400067,\nMaharashtra","resize23")
            textarea.insert(END,"\n\nPhone No.- 8291184838","resize24")
            textarea.tag_config("resize22",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize23",font=("times new roman",13,"bold"))
            textarea.tag_config("resize24",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n9. Cineflix Thakur Mall,Dahisar (E)","resize25")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 3rd Floor, Thakur Mall, Dahisar -\nEast, Mumbai – 400068, Maharashtra","resize26")
            textarea.insert(END,"\n\nPhone No.- 7506651225","resize27")
            textarea.tag_config("resize25",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize26",font=("times new roman",13,"bold"))
            textarea.tag_config("resize27",font=("times new roman",13,"bold"))

            textarea.insert(END,"\n\n10. Cineflix Thakur Movie,Kandivali (E)","resize28")
            textarea.insert(END,"\n\nPVR Cineflix Limited., 4th Floor, Vishnu Shivam Mall,\nThakur Village, Kandivali - East, Mumbai - 400101,\nMaharashtra","resize29")
            textarea.insert(END,"\n\nPhone No.- 7506651224","resize30")
            textarea.tag_config("resize28",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize29",font=("times new roman",13,"bold"))
            textarea.tag_config("resize30",font=("times new roman",13,"bold"))    

            textarea.insert(END,"\n\n11. METRO Cineflix Cinemas,Marine Lines","resize31")
            textarea.insert(END,"\n\nPVR Cineflix Limited., Metro House, M.G Road,\nDhobitalao, Marine Lines, Mumbai - 400020,\nMaharashtra","resize32")
            textarea.insert(END,"\n\nPhone No.- 7506651224\n\n\n\n\n","resize33")
            textarea.tag_config("resize31",foreground="blue",font=("times new roman",18,"bold"))
            textarea.tag_config("resize32",font=("times new roman",13,"bold"))
            textarea.tag_config("resize33",font=("times new roman",13,"bold"))
            textarea.config(state=DISABLED,bg="powder blue",bd=0)    

            btn1.config(text="Ahemdabad")
            btn2.config(text="Jaipur")
            btn3.config(text="Banglore")
            btn4.config(text="Delhi")
            btn5.config(text="Mumbai >>>")        

        frameMovieslist=Frame(self.root1,bd=0,relief=SOLID,padx=20,bg="powder blue")
        frameMovieslist.place(x=0,y=60,width=1280,height=60)

        lbltitle=Label(frameMovieslist,text="Locations",bg="powder blue",fg="red",bd=0,relief=RAISED,font=("times new roman",25,"bold"))
        lbltitle.place(x=550,y=0,width=200,height=50)

        frameMovieslist=Frame(self.root1,bd=2,relief=SOLID,padx=20,bg="white")
        frameMovieslist.place(x=0,y=120,width=200,height=600)

        btn1=Button(frameMovieslist,text="Ahmedabad",font=("Times new roman",20),fg="red",width=13,bg="white",command=Ahemdabad)
        btn1.place(x=-20,y=0,width=195,height=50)
        btn1.configure(highlightcolor="black",borderwidth=0,relief="solid")


        btn2=Button(frameMovieslist,text="Jaipur",font=("Times new roman",20),fg="red",width=13,bg="white",command=Jaipur)
        btn2.place(x=-20,y=60,width=195,height=50)
        btn2.configure(highlightcolor="black",borderwidth=0,relief="solid")

        btn3=Button(frameMovieslist,text="Banglore",font=("Times new roman",20),fg="red",width=13,bg="white",command=Banglore)
        btn3.place(x=-20,y=120,width=195,height=50)
        btn3.configure(highlightcolor="black",borderwidth=0,relief="solid")

        btn4=Button(frameMovieslist,text="Delhi",font=("Times new roman",20),fg="red",width=13,bg="white",command=Delhi)
        btn4.place(x=-20,y=180,width=195,height=50)
        btn4.configure(highlightcolor="black",borderwidth=0,relief="solid")

        btn5=Button(frameMovieslist,text="Mumbai",font=("Times new roman",20),fg="red",width=13,bg="white",command=Mumbai)
        btn5.place(x=-20,y=240,width=195,height=50)
        btn5.configure(highlightcolor="black",borderwidth=0,relief="solid")

        btn1.invoke()        

#------------------------------------------------------Schedule Page----------------------------------------------------------        
#-----------------------------------------------------------------------------------------------------------------------------        
        
    def schedule(self):

        frameAboutus1=Frame(self.root1,bd=1,relief="solid",padx=20,bg="white")
        frameAboutus1.place(x=0,y=70,width=1280,height=50)

        name=Label(frameAboutus1,font=("arial",16,"bold"),text="Movies",bg="white")
        name.place(x=10,y=10)


        frameAboutus=Frame(self.root1,bd=1,relief="solid",padx=20,bg="powder blue")
        frameAboutus.place(x=0,y=120,width=1280,height=600)

        scrollbar=Scrollbar(frameAboutus,orient="vertical")
        scrollbar.pack(side="right",fill="y")

        textarea=Text(frameAboutus,height=600,width=1078,yscrollcommand=scrollbar.set)
        textarea.pack()

        scrollbar.config(command=textarea.yview)


        textarea.insert(END,"\n1. Fighter","rohit")

        textarea.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Drama|141 min|Now Showing","rohit3")


        textarea.insert(END,"\n_____________________________________________________________________________________________________","rohit")

        textarea.insert(END,"\n\n2. Teri Baaton Mein Aisa Uljha Diya","rohit")

        textarea.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Drama|141 min|Now Showing","rohit3")

        textarea.insert(END,"\n_____________________________________________________________________________________________________","rohit")

        textarea.insert(END,"\n\n3. Hanuman","rohit")

        textarea.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Drama|141 min|Now Showing","rohit3")

        textarea.insert(END,"\n_____________________________________________________________________________________________________","rohit")

        textarea.insert(END,"\n\n4. Argylle","rohit")

        textarea.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Drama|141 min|Now Showing","rohit3")

        textarea.insert(END,"\n_____________________________________________________________________________________________________","rohit")

        textarea.insert(END,"\n\n5. 12th Fail","rohit")

        textarea.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Drama|141 min|Now Showing","rohit3")

        textarea.insert(END,"\n_____________________________________________________________________________________________________","rohit")

        textarea.insert(END,"\n\n6. Mein Atal Hoon ","rohit")

        textarea.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Drama|141 min|Now Showing","rohit3")

        textarea.insert(END,"\n_____________________________________________________________________________________________________","rohit")

        textarea.insert(END,"\n\n7. Dunki","rohit")

        textarea.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Drama|141 min|Now Showing","rohit3")

        textarea.insert(END,"\n_____________________________________________________________________________________________________","rohit")

        textarea.insert(END,"\n\n8. Warning 2","rohit")

        textarea.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Drama|141 min|Now Showing","rohit3")

        textarea.insert(END,"\n_____________________________________________________________________________________________________","rohit")

        textarea.insert(END,"\n\n9. Article 370","rohit")

        textarea.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Drama|141 min|Coming Soon","rohit3")

        textarea.insert(END,"\n_____________________________________________________________________________________________________","rohit")

        textarea.insert(END,"\n\n10. Vedaa","rohit")

        textarea.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Drama|141 min|Coming Soon","rohit3")

        textarea.insert(END,"\n_____________________________________________________________________________________________________","rohit")

        textarea.insert(END,"\n\n11. Pushpa 2 Rule","rohit")

        textarea.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Drama|141 min|Coming Soon","rohit3")

        textarea.insert(END,"\n_____________________________________________________________________________________________________","rohit")

        textarea.insert(END,"\n\n12. Stree 2","rohit")

        textarea.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Drama|141 min|Coming Soon\n\n\n\n\n","rohit3")

        textarea.tag_config("rohit",foreground="blue",font=("times new roman",18))
        textarea.tag_config("rohit1",foreground="blue",font=("times new roman",18,"bold"))
        textarea.tag_config("rohit3",foreground="blue",font=("times new roman",13))



        textarea.config(state="disabled",bg="powder blue",bd=0) 
###------------------------------------------------------Advertise Page-------------------------------------------------------
### --------------------------------------------------------------------------------------------------------------------------  
    
    def advertise(self):            
            
        framebutton2=Frame(self.root1,bd=0,relief=RIDGE,padx=20,bg="powder blue")
        framebutton2.place(x=0,y=70,width=1320,height=670)
            
            
        lb1Member = tk.Label(framebutton2, font=("arial", 14, "bold"), text="Want To Advertise With Us - Get In Touch",bg="powder blue")
        lb1Member.place(x=30, y=20)
            
        lb1Member = tk.Label(framebutton2, font=("arial", 14, "bold"), text="_____________________________________",bg="powder blue")
        lb1Member.place(x=5, y=45)
            
            
        lb2Member = tk.Label(framebutton2, font=("arial", 14, "bold"), text="We will be happy to here from you", bg="powder blue")
        lb2Member.place(x=30, y=80)
        
            
            
        self.name=Label(framebutton2,font=("arial",16,"bold"),text="Name :",bg="powder blue")
        self.name.place(x=30,y=140)
        self.name=Entry(framebutton2,font=("arial",10,"bold"),width=40)
        self.name.place(x=160,y=140,height=35)
            
        self.email=Label(framebutton2,font=("arial",16,"bold"),text="Email :",bg="powder blue")
        self.email.place(x=30,y=190)
        self.email=Entry(framebutton2,font=("arial",10,"bold"),width=40)
        self.email.place(x=160,y=190,height=35)
            
        self.contact1=Label(framebutton2,font=("arial",16,"bold"),text="Contact No :",bg="powder blue")
        self.contact1.place(x=30,y=240)
        self.contact1=Entry(framebutton2,font=("arial",10,"bold"),width=40)
        self.contact1.place(x=160,y=240,height=35)
            
        self.city=Label(framebutton2,font=("arial",16,"bold"),text="City :",bg="powder blue")
        self.city.place(x=30,y=290)
        self.city=Entry(framebutton2,font=("arial",10,"bold"),width=40)
        self.city.place(x=160,y=290,height=35)
            
        self.pincode=Label(framebutton2,font=("arial",16,"bold"),text="Pincode :",bg="powder blue")
        self.pincode.place(x=30,y=340)
        self.pincode=Entry(framebutton2,font=("arial",10,"bold"),width=40)
        self.pincode.place(x=160,y=340,height=35)
            
            
        self.subject=Label(framebutton2,font=("arial",16,"bold"),text="Subject:",bg="powder blue")
        self.subject.place(x=30,y=390)
        self.subject=Entry(framebutton2,font=("arial",10,"bold"),width=40)
        self.subject.place(x=160,y=390,height=35)
            
            
        button = tk.Button(self.root1, text="Proceed", command=self.advertise_input)
        button.place(x=210, y=520, height=35, width=180)
        
        self.result_label1 = tk.Label(self.root1, font=("arial", 12),bg="powder blue")
        self.result_label1.place(x=160, y=580)
        
    def advertise_input(self):
        
        self.Name1=self.name.get()
        self.email_id1=self.email.get()
        self.contact_no1=self.contact1.get()
        self.city1=self.city.get()
        self.pcode1=self.pincode.get()
        self.subject1=self.subject.get()
        length=len(self.email_id1)
        a=0
        b=0
        c=0
        if length>=5:
            if ("@" in self.email_id1) and (self.email_id1.count("@")==1):
                if self.email_id1[0].isalpha():
                    if (self.email_id1[-4]==".") ^ (self.email_id1[-3]=="."):
                        for k in self.email_id1:
                            if k==k.isspace():
                                a=1
                            elif k.isalpha():
                                if k==k.upper():
                                    b=1
                            elif k.isdigit():
                                continue
                            elif k=="_" or k=="." or k=="@":
                                continue
                            else:
                                c=1
                        if a==1 or b==1 or c==1:
                            self.result_label1.config(text="Invalid Email..!",bg="white",fg="black")
                            self.result_label1.place(x=250, y=580)
                        else:
                            contact1 = self.contact1.get()
                            a=len(contact1)

                            if contact1.isdigit() and a==10:
                                self.result_label1.config(text="We have recieved your information.\nWe will contact you shortly via email or No",bg="white",fg="black")
                                insert_query="Insert into advertise(Name,e_mail_id,contact_no,city,pincode,subject) values (%s,%s,%s,%s,%s,%s)"
                                vals=[self.Name1,self.email_id1,self.contact_no1,self.city1,self.pcode1,self.subject1]
                                self.my_cursor.execute(insert_query,vals)
                                self.conn.commit()

                            else:
                                self.result_label1.config(text="Please give Correct Mobile NO.",bg="white",fg="black")
                                self.result_label1.place(x=190, y=580)
                    else:
                        self.result_label1.config(text="Invalid Email..!",bg="white",fg="black")
                        self.result_label1.place(x=250, y=580)
                        
                else:
                    self.result_label1.config(text="Invalid Email..!",bg="white",fg="black")
                    self.result_label1.place(x=250, y=580)
            else:
                self.result_label1.config(text="Invalid Email..!",bg="white",fg="black")
                self.result_label1.place(x=250, y=580)
        else:
            self.result_label1.config(text="Invalid Email..!",bg="white",fg="black")
            self.result_label1.place(x=250, y=580)
    

        

## ----------------------------------------------------Support Window--------------------------------------------------------
## ----------------------------------------------------Support Window--------------------------------------------------------
        
    def support(self):
#         


        framebutton2=Frame(self.root1,bd=5,relief=RIDGE,padx=20,bg="powder blue")
        framebutton2.place(x=0,y=70,width=1320,height=720)


        first = tk.Label(framebutton2, font=("arial", 22, "bold"), text="Raise a ticket",bg="powder blue")
        first.place(x=510, y=20)


        button = tk.Button(framebutton2,font=("arial", 13, "bold"), text="Click Here",command=self.ticket)
        button.place(x=550, y=70,width=100,height=30)

        first = tk.Label(framebutton2, font=("arial", 18, "bold"),fg="blue",text="OR",bg="powder blue")
        first.place(x=570, y=130)

        first = tk.Label(framebutton2, font=("arial", 20, "bold"), text="Contact Us :",bg="powder blue")
        first.place(x=520, y=200)

        first = tk.Label(framebutton2, font=("arial", 15, "bold"), text="E-mail :",bg="powder blue")
        first.place(x=280, y=260)
        
        first = tk.Label(framebutton2, font=("arial", 14), text="rawat.rohit1809@gmail.com",bg="powder blue")
        first.place(x=200, y=290)
        
        first = tk.Label(framebutton2, font=("arial", 15, "bold"), text="Mobile No :",bg="powder blue")
        first.place(x=570, y=260)
        
        first = tk.Label(framebutton2, font=("arial", 14), text="7742252388, 9549040152",bg="powder blue")
        first.place(x=510, y=290)
        
        first = tk.Label(framebutton2, font=("arial", 15,"bold"), text="WhatsApp :",bg="powder blue")
        first.place(x=840, y=260)
        
        first = tk.Label(framebutton2, font=("arial", 14), text="9461469751",bg="powder blue")
        first.place(x=840, y=290)
        
        first = tk.Label(framebutton2, font=("arial", 14), text="----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg="powder blue")
        first.place(x=10, y=330)
               
        first = tk.Label(framebutton2,fg="white", font=("arial", 65,"italic"), text="Have a \nHappy Day! ",bg="powder blue")
        first.place(x=400, y=350)
        
## ----------------------------------------------------Raise Ticket Window--------------------------------------------------------
## ------------------------------------------------------------------------------------------------------------------------------
        
    def ticket(self):
        self.root3=Tk()
        self.root3.geometry("680x420+0+0")
        self.root3.title("Cineflix Raise Ticket")
        self.root3.configure(bg="powder blue")
        
        self.name=Label(self.root3,font=("arial",16,"bold"),text="Name :",bg="powder blue")
        self.name.place(x=30,y=10)
        self.name=Entry(self.root3,font=("arial",10,"bold"),width=40)
        self.name.place(x=170,y=10,height=35)
            
        self.email=Label(self.root3,font=("arial",16,"bold"),text="Email :",bg="powder blue")
        self.email.place(x=30,y=60)
        self.email=Entry(self.root3,font=("arial",10,"bold"),width=40)
        self.email.place(x=170,y=60,height=35)
            
        self.contact=Label(self.root3,font=("arial",16,"bold"),text="Contact No :",bg="powder blue")
        self.contact.place(x=30,y=110)
        self.contact=Entry(self.root3,font=("arial",10,"bold"),width=40)
        self.contact.place(x=170,y=110,height=35)
        
        
        self.subject=Label(self.root3,font=("arial",16,"bold"),text="Query :",bg="powder blue")
        self.subject.place(x=30,y=160)
        self.subject=Entry(self.root3,font=("arial",10,"bold"),width=40)
        self.subject.place(x=170,y=160,height=35)
        
        self.options = ["Refund Related Query", "Booking Related Query", "Money Debited But Ticket Not Recieved", "Refund Amount Not Recieved yet", "Cancellation","Query Not Listed Here"]
        self.dropdown_var = tk.StringVar(self.root3)
        self.dropdown = ttk.Combobox(self.root3, textvariable=self.dropdown_var, values=self.options)
        self.dropdown.place(x=170, y=160,width=285,height=35)
        
        
        self.ticketnumber = random.randint(1, 100000)
            
            
        button = tk.Button(self.root3, font=("arial",12,"bold"),text="Raise a Ticket",command=self.raise_ticket_input)
        button.place(x=200, y=220, height=35, width=180)
        
        self.result_label = tk.Label(self.root3, font=("arial", 12),bg="powder blue")
        self.result_label.place(x=160, y=280)
        
        
        
        
    def raise_ticket_input(self):
        
        contact=self.contact.get()
        a=len(contact)
        
        if contact.isdigit() and a==10:
            self.result_label.config(text="Ticket has been raised.\nWe will contact you shortly via email or No",bg="white",fg="black")
            self.Name=self.name.get()
            self.email_id=self.email.get()
            self.contact_no=self.contact.get()
            self.query=self.dropdown.get()
            self.ticketno=self.ticketnumber
            insert_query="Insert into raise_ticket(Name,e_mail_id,contact_no,query,ticket_no) values (%s,%s,%s,%s,%s)"
            vals=[self.Name,self.email_id,self.contact_no,self.query,self.ticketno]
            self.my_cursor.execute(insert_query,vals)
            self.conn.commit()
            
        else:
            self.result_label.config(text="Please give Correct Mobile NO.",bg="white",fg="black")


    
# ------------------------------------------------------ About Page ------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------
   
    def about(self):

        frameAboutus=Frame(self.root1,bd=1,relief=SOLID,padx=20,bg="powder blue")
        frameAboutus.place(x=0,y=70,width=1280,height=660)

        scrollbar=Scrollbar(frameAboutus,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)

        textarea=Text(frameAboutus,height=600,width=1078,yscrollcommand=scrollbar.set)
        textarea.pack()

        scrollbar.config(command=textarea.yview)

        # textarea.insert(END,"\nAbout Us","resize1")
        # textarea.tag_config("resize1",foreground="black",font=("times new roman",18,"bold"))

        textarea.insert(END,"\n\t\t\t\t\t\t\t\tCineflix","resize2")
        textarea.tag_config("resize2",foreground="blue",font=("times new roman",47,"bold","underline"))

        textarea.insert(END,"\n\t\t\t\t\t\t\t\t    LIVE the MOVIE","resize3")
        textarea.tag_config("resize3",foreground="black",font=("lucida handwriting",14))

        textarea.insert(END,"\n\n\n\t\t\t\t\t\t      SERVING HAPPINESS!","resize4")
        textarea.tag_config("resize4",foreground="red",font=("calibri",30,"bold"))

        para='''\nAs a flagship venture of the USD 5 Bn Cineflix Group, Cineflix Leisure Limited has always worked upon enhancing the experiences, right from creating a world-class infrastructure which is high on comfort and aesthetics, to staying updated with the latest in the cinema technology space. Ever since commencing operations in year 2002, Cineflix has already entertained more than 700 Mn guests in its glorious journey. With 746 perfectly appointed screens in 173 multiplexes across the country, Cineflix continues to get closer to the Indian cinema lovers, and also remain on a growth path which is envied across the globe.
                Cineflix has pioneered plenty of ‘firsts’ in the Indian cinema exhibition industry. Cineflix operates Megaplex at the Inorbit Mall Malad, Mumbai, a multiplex with highest number of cinema viewing experiences in the world, which is also home to India’s first ScreenX as well as India’s first screen with MX4D® Theater Effects. Cineflix was the 1st cinema chain in the country to operate a Laserplex, a multiplex with all the screens enabled with Laser Projection. With the grand & immersive IMAX screens already a part of its repertoire, Cineflix also has to its credit, Mumbai’s first Samsung ONYX LED screen at the Megaplex. Cineflix’s 7-star cinema viewing experience, INSIGNIA, has emerged as top luxury proposition in the country. Cineflix’s desire to offer tailor-made experiences to its patrons led to the creation of home-grown formats like the vibrant and lively KIDDLES for the young audience, the smart luxury experience CLUB for the discerning guests and BIGPIX a premium giant screen cinema format.
                Driven by the vision of being the most loved cinema brand across the globe, thousands of Cineflix’s happiness agents working in 74 Indian cities are always on their toes, with open arms, accomplished to bring emotions to life, and win hearts, every single day!'''

        textarea.insert(END,para,"resize5")
        textarea.tag_config("resize5",foreground="black",justify="left",font=("calibri",18,"bold"))

        textarea.insert(END,"\n\n\n_____________________________________________________________________________________","resize10")
        textarea.tag_config("resize10",foreground="red",font=("calibri",22))

        textarea.insert(END,"\n\n\t\t\t\t      THE Entertainment DESTINATION OF INDIA","resize11")
        textarea.tag_config("resize11",foreground="black",font=("Kaufmann BT",25,"bold"))

        textarea.insert(END,"\n\t\t\t\t ************************************************","resize10")
        textarea.tag_config("resize10",foreground="red",font=("calibri",22))

        textarea.insert(END,"\n\n\t\t\t150\t\t\t5\t\t\t15mn\t\t\t40\t\t\t23105","resize7")
        textarea.insert(END,"\n\t\t      ---------\t\t\t     ---------\t\t\t        ---------\t\t\t      ---------\t\t\t         ---------","resize10")
        textarea.insert(END,"\n\t\t        SCREENS\t\t\t         CITIES\t\t\t            GUEST\t\t\t       CINEMAS\t\t\t              SEATS","resize7")

        textarea.tag_config("resize7",foreground="black",justify="left",font=("calibri",18))


        textarea.insert(END,"\n\n\n_____________________________________________________________________________________","resize10")
        textarea.tag_config("resize10",foreground="red",font=("calibri",22))


        textarea.insert(END,"\n\n\t\t\t\t\t\t\t      WHAT DRIVES US","resize8")
        textarea.tag_config("resize8",foreground="black",font=("calibri",22,))

        textarea.insert(END,"\n\t\t\t\t\t\t\t*********************","resize10")
        textarea.tag_config("resize10",foreground="red",font=("calibri",22))


        textarea.insert(END,"\n\n\t\tLUXURY\t\t\t\t\t\t     SERVICE\t\t\t\t\t\t     TECHNOLOGY","resize6")
        textarea.tag_config("resize6",foreground="black",justify="left",font=("calibri",22))

        textarea.insert(END,"\n\t\t*******\t\t\t\t\t\t     *******\t\t\t\t\t\t     ************","resize9")
        textarea.tag_config("resize9",foreground="black",font=("calibri",22))

        textarea.insert(END,"\n      Cineflix has set new benchmarks\t\t\t\t\t\t             We are committed to provide\t\t\t\t\t\t\t     Be it projection & sound or our\n","resize7")
        textarea.insert(END,"    in cinema luxury, only to ensure\t\t\t\t\t\t           our guests with an unparalleled\t\t\t\t\t\t\t        advanced cinema formats or\n","resize7")
        textarea.insert(END,"      that the guests are pampered\t\t\t\t\t\t\t     cinema journey, which is\t\t\t\t\t\t      reservations, check-ins & food\n","resize7")
        textarea.insert(END,"      with the slickest of experience\t\t\t\t\t\t          underlined by the warmth of our\t\t\t\t\t\t              ordering, we aim to amplify your\n","resize7")
        textarea.insert(END,"      \t\t\t\t\t\t\t          top notch service\t\t\t\t\t\t       experience with the finest use\n","resize7")
        textarea.insert(END,"      \t\t\t\t\t\t\t\t\t\t\t\t\t\t         of technology","resize7")

        textarea.insert(END,"\n_____________________________________________________________________________________\n\n","resize10")
        textarea.tag_config("resize10",foreground="red",font=("calibri",22))


        textarea.tag_config("resize7",foreground="black",justify="left",font=("calibri",18))

        textarea.config(state=DISABLED,bg="powder blue",bd=0)


# ----------------------------------------------- Database Connection ------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------
    conn=mysql.connector.connect(host="localhost",database="cinema",user="root",password="redhat")
    my_cursor = conn.cursor()
    
if __name__ == "__main__":
    root = tk.Tk()
    obj = Cinema()
    show_label = tk.Label(root, font=("arial", 12),bg="white")
    show_label.place(x=530, y=420)
    root.mainloop()


# In[ ]:


pip install mysql-connector-python
pip install random
pip install tkinter
pip install webbrowser

