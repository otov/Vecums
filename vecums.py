import tkinter as tk
import datetime
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

logs = Tk()
logs.geometry("600x600")
logs.title("Vecuma aprekins")
logs.configure(background="green")

title_frame = tk.Frame(logs)
title_frame.pack(pady=5)

title=tk.Label(title_frame, text="Vecuma aprēķins", font=("Arial",20,"bold"))
title.grid(row=0,column=1)

input_frame = tk.Frame(logs, bg="green")
input_frame.pack(pady=10)

name_label=tk.Label(input_frame, text="Vārds: ")
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=1, column=1)

year_label=tk.Label(input_frame, text="Dzimšanas gads: : ")
year_label.grid(row=2, column=0, padx=5, pady=5)
year_entry = tk.Entry(input_frame)
year_entry.grid(row=2, column=1)

month_label=tk.Label(input_frame, text="Dzimšanas mēnesis: ")
month_label.grid(row=3, column=0, padx=5, pady=5)
month_entry = tk.Entry(input_frame)
month_entry.grid(row=3, column=1)

day_label=tk.Label(input_frame, text="Dzimšanas diena: ")
day_label.grid(row=4, column=0, padx=5, pady=5)
day_entry = tk.Entry(input_frame)
day_entry.grid(row=4, column=1)

age_listbox=tk.Listbox(logs,width=60,bg="white",fg="black")
age_listbox.pack(pady=5)

def get_info():
    name=name_entry.get()
    year=int(year_entry.get())
    month=int(month_entry.get())
    day=int(day_entry.get())

    dzimsana=datetime.date(year, month, day)
    today=datetime.date.today()

    vecums=today.year-dzimsana.year

    age_listbox.insert(tk.END, f"Mani sauc {name} Es esmu {vecums} gadus vecs")

    name_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    month_entry.delete(0, tk.END)
    day_entry.delete(0, tk.END)


button=tk.Button(logs, text="Aprēķināt vecumu",command=get_info)
button.pack(pady=5)

#button1=tk.Button(logs, text="Notīrīt", command=)
#button.pack(pady=5)


logs.mainloop()