#random password
from email.policy import strict
import random as r
import string 
from tkinter import *
from random import *
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
punc = string.punctuation
all = upper+num+lower+punc
def random_password(): 
    semboller = string.ascii_letters+string.punctuation+string.digits
    parola = ".join(choice(semboller))for x in range(r.randint(10))"
    print(semboller)
 
pencere = Tk()

pencere.title("RandomPassword")
pencere.geometry("600x300")


etiket = Label(pencere)
etiket.config(text="RANDOMPASSWORD",bg = "orange",font =("Arial",10))
etiket.place(x=250,y=250)

entry=Entry(pencere)
entry.place(x=250,y=50)

buton = Button(pencere)
buton.config(text ="Şifre",bg ="blue",fg ="black",comman =random_password)
buton.pack()

pencere.mainloop()


