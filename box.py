from tkinter import *
import sys
import phonenumbers

#def q():
    #a.destroy

def data(no):
    from phonenumbers import geocoder
    ch_no=phonenumbers.parse(no,'CH')
    b=geocoder.description_for_number(ch_no,'en')
    

    from phonenumbers import carrier
    service_no=phonenumbers.parse(no,'RO')
    c=carrier.name_for_number(service_no,'en')
    
    
    return b,c

def printinput():
    inp=inputtxt.get(1.0,'end-1c')
    e,f=data(inp)
    
    #lbl1.config(text='country nd provider:'+e+f)
    a=Label(text="country:"+e)
    a.place(x=30,y=55)
    b=Label(text="Carrier:"+f)
    b.place(x=30,y=75)
	
a=Tk()
a.title('Mobile')
a.geometry('400x200')


extbutton=Button(a,text='exit',command=a.destroy)
extbutton.pack(side=TOP,anchor=NE)

lbl=Label(a,text='Enter mobile no.(with country code)')
lbl.place(x=10,y=10)



inputtxt=Text(a,height=1,width=14)
inputtxt.place(x=10,y=30)

printbutton=Button(a,text='Search',command=printinput)
printbutton.pack()



lbl1=Label(a)
lbl1.pack()

a.mainloop()

