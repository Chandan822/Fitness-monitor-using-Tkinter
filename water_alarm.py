import time
from plyer import notification
from tkinter import *

def water_alarm():
    duration = int(duration1.get())
    minute= float(minutes.get())
    while duration:   
        time.sleep(60*minute)
        notification.notify(title='Drink water', message="It's time to drink water")
        duration-=1
    return

window2=Tk(screenName=None,baseName=None,className="__Water_Alarm__")
window2.geometry("750x300")

bg = PhotoImage(file = "bg2.png")
label1 = Label( window2, image = bg) 
label1.place(x = 0, y = 0) 

Label(window2, text='Enter the number of times you want to be reminded in a day: ',height=1,font=('Comic Sans MS',11,'bold'),relief="flat",bg="#00A2E8",fg="#FFFFFF").grid(row=1, padx=10, pady=5)
duration1 = Entry(window2, width=10)
duration1.grid(row=1,column=2)
Label(window2, text='Enter how many minutes once you want to be reminded: ',height=1,font=('Comic Sans MS',11,'bold'),relief="flat",bg="#00A2E8",fg="#FFFFFF").grid(row=2, padx=10, pady=5)
minutes = Entry(window2, width=10)
minutes.grid(row=2,column=2)

Button(window2, text="Set Reminder", command=water_alarm, height=1,font=('Comic Sans MS',13),relief="ridge",bg="#FFFFFF",fg="#00A2E8").grid(row=1,rowspan=2,column=3,sticky=NS, padx=50, pady=5)

mainloop()