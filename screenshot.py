import pyautogui #for using this 1st install pyauto gui using- pip install pyautogui
import tkinter as tk #pip instal tk
from tkinter.filedialog import *

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300) #canvas1 is the variable for addresing the tk canvas
canvas1.pack()

def take_ss(): #defineing the function take_ss to take screen shot and providing a save path
    myscreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path+"_screenshot.png")#

ss_button = tk.Button(text="TAKE SCREENSHOT", command= take_ss, font=15)
canvas1.create_window(100,100,window=ss_button)

root.mainloop()

