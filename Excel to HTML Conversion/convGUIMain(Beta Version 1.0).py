
#Program: conGUIMain
#Author: Dylan Fahr
#Date: 21 January, 2017
#Description: The goal of this python GUI is to execute multiple scripts that collect Microsoft Excel data and parses them to custom HTML files

from Tkinter import *
import sys
import os
import tkMessageBox
root = Tk()
root.title("Excel Map Conversion")
root.geometry("450x400")# width x height

filepath = StringVar()

def texas():
     os.startfile(filepath.get() + '/Texas/Texas_conversion.py')

def state():
    os.startfile(filepath.get() + '\State\StateConv.py')
    
def college():

     os.startfile(filepath.get() + '\College\CollegeConv.py')
 
def underGrad():
    os.startfile(filepath.get() + '\Undergraduate\undergrad_conversion.py')
    
def grad():
    os.startfile(filepath.get()+ '\Graduate\graduate_conversion.py')
    
#Copy and paste the folder location of the main location where the scripts exist.
#This can either be 100% online or any online
    
label = Label(root, text="\nEnter in the filepath for the map files: \n").pack()
link = Entry(root, textvariable = filepath).pack()


label2 = Label(root, text ="\n\tPlease select from the following options:\n").pack()

button1 = Button(root, text = "College", command = college).pack()

button2 = Button(root, text= "State", command = state).pack()

button3 = Button(root, text="Texas", command = texas).pack()

button4 = Button(root, text ="Undergraduate", command = underGrad).pack()

button5 = Button(root, text ="Graduate", command = grad).pack()

#kick off the event loop
root.mainloop()

# To view the output, go to the folder location where the scripts are located
# Within their folder locations, the HTML files will be created.
# Make sure image files exist in the same folder location in each folder.

#IMPORTANT!!!: The process of conversion from Excel to HMTL outputs the entrollment numbers for the various degree listings as floating point
# In order to fix this error, open each HTML file within a text editor and delete the decimal point and number following the decimal.


