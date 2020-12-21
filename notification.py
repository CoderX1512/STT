from tkinter import *

from tkinter import messagebox

top = Tk()

top.withdraw()     #Removes the tkinter's extra window
top.geometry("100x100")

messagebox.showinfo("Alert!!","Your customer wants to say something")

top.mainloop()  
