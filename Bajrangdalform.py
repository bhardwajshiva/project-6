from tkinter import *


form=Tk()

form.geometry("500x300")

Label(form,text="Bajrang Dal Bharti",font="ar 15 bold ").grid(row=0,column=3)


name=Label(form,text="Name").grid(row=1,column=2)
age=Label(form,text="Age").grid(row=3,column=2)
caste=Label(form,text=" Caste").grid(row=5,column=2)
address=Label(form,text="Address").grid(row=7,column=2)
gender=Label(form,text="Gender").grid(row=9,column=2)
mobileno=Label(form,text="Mobileno").grid(row=11,column=2)

namevalue=StringVar
agevalue=StringVar
castevalue=StringVar
addressvalue=StringVar
gendervalue=StringVar
mobilenovalue=StringVar

#checkvalue=IntVar

nameentry=Entry(form,text="namevalue").grid(row=1,column=3)
ageentry=Entry(form,text="agevalue").grid(row=3,column=3)
casteentry=Entry(form,text="castvalue").grid(row=5,column=3)
addressentry=Entry(form,text="addressvalue").grid(row=7,column=3)
genderentry=Entry(form,text="gendervalue").grid(row=9,column=3)
mobilenoentry=Entry(form,text="mobilenovalue").grid(row=11,column=3)

Button(text="Submit").grid(row=13,column=3)
#Button(text="Cancel").grid(row=9,column=3)






form.mainloop()