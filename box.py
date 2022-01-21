from tkinter import *
import sys
import phonenumbers
a=Tk()
a.title('Mobile')
a.geometry('400x200')

#def q():
    #a.destroy

def data(no):
    from phonenumbers import geocoder
    ch_no=phonenumbers.parse(no,'CH')
    b=geocoder.description_for_number(ch_no,'en')
    g=b+'#'

    from phonenumbers import carrier
    service_no=phonenumbers.parse(no,'RO')
    c=carrier.name_for_number(service_no,'en')
    
    
    return g,c

def printinput():
    inp=inputtxt.get(1.0,'end-1c')
    e,f=data(inp)
    
    lbl1.config(text='country nd provider:'+e+f)

extbutton=Button(a,text='exit',command=a.destroy)
extbutton.pack(side=TOP,anchor=NE)

lbl=Label(a,text='Enter mobile no.(with country code)')
lbl.pack()



inputtxt=Text(a,height=1,width=14)
inputtxt.pack()

printbutton=Button(a,text='print',command=printinput)
printbutton.pack()

lbl1=Label(a)
lbl1.pack()

a.mainloop()

