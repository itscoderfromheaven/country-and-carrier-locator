from tkinter import *

import phonenumbers

from phonenumbers import geocoder

from phonenumbers import carrier

new = Tk()


new.geometry("400x200")


new.title('Phone Number Tracker')

label1 = Label(text="Enter your number")


label1.pack()


def getlocation():

    ##get the number##

    num = number.get("1.0", END)
    num = phonenumbers.parse(num)
    result.insert(END, "The country of this number is " +
                  geocoder.description_for_number(num, "en"))
    result.insert(END, "\nThe sim card of this number is " +
                  carrier.name_for_number(num, "en"), END)

    
number = Text(height=5)

number.pack()

button = Button(text="Get Location & Sim Card Details", command=getlocation)

button.pack()

result = Text(height=5)

result.pack()


new.mainloop()
