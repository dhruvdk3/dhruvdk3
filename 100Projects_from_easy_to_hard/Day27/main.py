from tkinter import *

def miles_to_km():
    miles = float(entry.get())
    km = miles*1.609
    lable3.config(text=f"{km}")

window = Tk()
window.minsize(200,100)
window.title("Miles to Km")
window.config(padx=10,pady=10)

entry = Entry(width=8)
entry.grid(column=1, row=0)

# lable
lable = Label(text="is equal to ", font=("Ariel",12,"bold"))
lable1 = Label(text="Miles", font=("Ariel",12,"bold"))
lable2 = Label(text="Km", font=("Ariel",12,"bold"))
lable3 = Label(text="0", font=("Ariel",12,"bold"))
lable.grid(column=0,row=1)
lable3.grid(column=1,row=1)
lable1.grid(column=2,row=0)
lable2.grid(column=2,row=1)



button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1,row=2)

window.mainloop()

