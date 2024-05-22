from datetime import datetime
from tkinter import *
from tkcalendar import *

root=Tk()

def selectDate():
    myDate=mycal.get_date()
    selectedDate=Label(text=myDate)
    selectedDate.pack(padx=2,pady=2)

mycal=Calendar(root,mindate = datetime(2024, 1, 1),
                    maxdate = datetime (2024, 12, 30), 
                    showweeknumbers = False, 
                    showothermonthdays = False)
mycal.pack(padx=15,pady=15)

open_cal=Button(root,text="select Date",command=selectDate)
open_cal.pack(padx=15,pady=15)

root.geometry("300x300")
root.title("Calendar")
root.configure(bg="#F6277F")

root.mainloop()