#rnd Password 
# General Information: I want to use a program which can generate rnd password and display the result on user interface. Acceptance Criteria:
#Use tkinter package to solve the problem. (You can use the rnd student codes as template)
#Password length must be 10 characters long.
#It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
#You must import some required modules or packages.
#The GUI of program must contain at least a button and a label (customize the screen according to yourself)
#The result should be display on the password label when the user click the generate button.

#random password
import random as rnd
import string
import tkinter as tk



def rnd_key():
    key = rnd.sample(string.digits, 2) + rnd.sample(string.punctuation[0:14], 2) + \
          rnd.sample(string.ascii_uppercase, 2) + rnd.sample(string.printable[0:76], 4)
    print(*key)
    rnd.shuffle(key)
    print(*key)
    str = ''
    for i in key:
        str += i
    print(str)
    label.config(text=str)
    #return str


window = tk.Tk()

window.title("Your Password")
window.geometry("650x300")


key_application = tk.Frame(window)
key_application.grid()


# label
label_txt = tk.Label(key_application, text="Password Generation", font="arial 18 bold")
label_txt.grid(padx=100, pady=10)


# label
label = tk.Label(key_application, text="Please click the botton for a special password", font="arial 14")
label.grid(padx=110, pady=20)


# button
button1 = tk.Button(key_application, text=" GENERATE ", width=50, height=5, command=rnd_key)
button1.grid(padx=110, pady=40)

window.mainloop()