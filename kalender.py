from tkinter import ttk
import ttkbootstrap

root = ttkbootstrap.Window(thename="cyborg")
root.title("Calendar")

def see_date():
    date = cal.entry.get()
    date_label.config(text=date)

cal = ttkbootstrap.DateEntry(root, dateformat="%d/%m/%y", bootstyle="info")
cal.pack(padx=40, pady=40)

btn = ttk.Button(root, text="Show Date", bootstyle="light-outline", command= see_date)
btn.pack(padx=40, pady=45)

date_label = ttk.label(root, text="No date selcted")
date_label.pack(padx=40, pady=50)

root.mainloop()