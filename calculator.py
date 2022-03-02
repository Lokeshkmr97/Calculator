from tkinter import *

root=Tk()
root.title('Lokesh Calculator')
root.geometry('300x400')
var=StringVar()

exp=''
def show(number):
    global var
    global exp
    
    exp=exp+str(number)
    var.set(exp)

def clear(number):
    global var
    global exp
    exp=''
    var.set(exp)
    
def equal(number):
    global var
    global exp
    res=str(eval(exp))
    var.set(res)
    
    
    
    

entry=Entry(root,font=('Arial',30),textvariable=var,justify=RIGHT)
entry.place(x=0,y=0,height=80,width=300)

btn7=Button(root,font=('Arial',20),text=7,padx=18,pady=12,bd=0,command=lambda:show(7))
btn7.place(x=0,y=80)
btn8=Button(root,font=('Arial',20),text=8,padx=18,pady=12,bd=0,command=lambda:show(8))
btn8.place(x=75,y=80)
btn9=Button(root,font=('Arial',20),text=9,padx=18,pady=12,bd=0,command=lambda:show(9))
btn9.place(x=150,y=80)
btndiv=Button(root,font=('Arial',20),text='/',padx=18,pady=12,bd=0,command=lambda:show('/'))
btndiv.place(x=225,y=80)

btn4=Button(root,font=('Arial',20),text=4,padx=18,pady=12,bd=0,command=lambda:show(4))
btn4.place(x=0,y=160)
btn5=Button(root,font=('Arial',20),text=5,padx=18,pady=12,bd=0,command=lambda:show(5))
btn5.place(x=75,y=160)
btn6=Button(root,font=('Arial',20),text=6,padx=18,pady=12,bd=0,command=lambda:show(6))
btn6.place(x=150,y=160)
btnmulti=Button(root,font=('Arial',20),text='*',padx=18,pady=12,bd=0,command=lambda:show('*'))
btnmulti.place(x=225,y=160)

btn1=Button(root,font=('Arial',20),text=1,padx=18,pady=12,bd=0,command=lambda:show(1))
btn1.place(x=0,y=240)
btn2=Button(root,font=('Arial',20),text=2,padx=18,pady=12,bd=0,command=lambda:show(2))
btn2.place(x=75,y=240)
btn3=Button(root,font=('Arial',20),text=3,padx=18,pady=12,bd=0,command=lambda:show(3))
btn3.place(x=150,y=240)
btnminus=Button(root,font=('Arial',20),text='-',padx=18,pady=12,bd=0,command=lambda:show('-'))
btnminus.place(x=225,y=240)

btn0=Button(root,font=('Arial',20),text=0,padx=18,pady=12,bd=0,command=lambda:show(0))
btn0.place(x=0,y=320)
btnc=Button(root,font=('Arial',20),text='C',padx=18,pady=12,bd=0,command=lambda:clear('C'))
btnc.place(x=75,y=320)
btnequal=Button(root,font=('Arial',20),text='=',padx=18,pady=12,bd=0,command=lambda:equal('='))
btnequal.place(x=150,y=320)
btnadd=Button(root,font=('Arial',20),text='+',padx=18,pady=12,bd=0,command=lambda:show('+'))
btnadd.place(x=225,y=320)





mainloop()