
from tkinter import *

def count_cals():
    gender=str(gender1.get())
    age=int(age1.get())
    weight=float(weight1.get())
    heart_rate=int(heart_rate1.get())
    time=float(time1.get())
    
    if gender=="male" and age>0 and weight>0 and heart_rate>0:
        calories=round(abs(((age*0.2017)+(weight*0.09036)+(heart_rate*0.6409)-(55.0969*time))/4.184),2)
        output = "Calories burnt is " + str(calories)
    elif gender=="female" and age>0 and weight>0 and heart_rate>0:
        calories=round(abs(((age*0.074)+(weight*0.05741)+(heart_rate*0.4472)-(20.4022*time))/4.184),2)
        output = "Calories burnt is " + str(calories)
    else:
        output = "INVALID INPUTS ENETERED"

    label.config(text=output)
    return output


window1=Tk(screenName=None,baseName=None,className="__Calorie_Calculator__")
window1.geometry("910x633")

bg = PhotoImage(file = "bg1.png")
label1 = Label( window1, image = bg) 
label1.place(x = 0, y = 0) 

Label(window1, text='Select gender: ',height=1,font=('Times',13),relief="flat",bg="#E1E6EB").grid(row=1, padx=10, pady=10)
gender1 = StringVar()
gender1.set(False)
Radiobutton(window1, text = "Male", variable = gender1, value = "male").grid(row=1,column=2,sticky=W)
Radiobutton(window1, text = "Female", variable = gender1, value = "female").grid(row =2,column=2,sticky=W)
# gender1 = Entry(window1, width=40)
# gender1.grid(row=1,column=2)
Label(window1, text='Enter age: ',height=1,font=('Times',13),relief="flat",bg="#E1E6EB").grid(row=3, padx=10, pady=5)
age1 = Entry(window1, width=40)
age1.grid(row=3,column=2)
Label(window1,text='Enter weight:',height=1,font=('Times',13),relief="flat",bg="#E1E6EB").grid(row=4, padx=10, pady=5)
weight1= Entry(window1, width=40)
weight1.grid(row=4,column=2)
Label(window1, text='Enter heart_rate: ',height=1,font=('Times',13),relief="flat",bg="#E1E6EB").grid(row=5, padx=10, pady=5)
heart_rate1= Entry(window1, width=40)
heart_rate1.grid(row=5,column=2)
Label(window1, text='Enter time in minutes only: ',height=1,font=('Times',13),relief="flat",bg="#E1E6EB").grid(row=6, padx=10, pady=5)
time1= Entry(window1, width=40)
time1.grid(row=6,column=2)

label=Label(window1, text="", font=('Comic Sans MS',15),bg="#DCE1E6")
label.grid(row=9,column=0,columnspan=3,sticky=NSEW, padx=5, pady=10)

Button(window1, text="Calculate calories", command=count_cals, height=1,font=('Comic Sans MS',13)).grid(row=7,column=2,sticky=NS, padx=2, pady=5)

mainloop()