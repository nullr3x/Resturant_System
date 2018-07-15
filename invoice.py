from tkinter import *

root = Tk()
root.geometry("1000x600+0+0")
root.title('Invoice Bill')

v = '_'*700
s = '-'*100

def print():
    print('test')

print = Button(root, bd=5 ,fg="black",font=('ariel' , 10 ,'bold'),width=7, text="Print", bg="red",command=print)
print.place(x=870 , y=150)

seperate = Label(root , text = v , font = ('helevetica','5','bold') , fg = 'black')
seperate.place(y=0)

lab1 = Label(root , text = "Invoice Bill" , font = ('helevetica','15','bold') , fg = 'blue')
lab1.place(x=420 , y=20)

seperate = Label(root , text = v , font = ('helevetica','5','bold') , fg = 'black')
seperate.place(y=45)

                    ################################################

lab2 = Label(root , text = "Shmeisani - Facing A1 Qsar Hotel" , font = ('helevetica','10','bold') , fg = 'blue')
lab2.place(x=350 , y=60)

lab3 = Label(root , text = "Tel: 5660250/8" , font = ('helevetica','10','bold') , fg = 'blue')
lab3.place(x=430 , y=80)

lab4 = Label(root , text = "Sales Tax No. : 048124320" , font = ('helevetica','10','bold') , fg = 'blue')
lab4.place(x=380 , y=100)

seperate = Label(root , text = v , font = ('helevetica','5','bold') , fg = 'black')
seperate.place(y=115)

                    #################################################

lab5= Label(root , text = "Order No.: " , font = ('helevetica','13','bold') , fg = 'blue')
lab5.place(x=20 , y=150)

lab6= Label(root , text = "Date: " , font = ('helevetica','13','bold') , fg = 'blue')
lab6.place(x=20 , y=170)

lab7= Label(root , text = "Time:" , font = ('helevetica','13','bold') , fg = 'blue')
lab7.place(x=20 , y=190)

seperate = Label(root , text = v , font = ('helevetica','5','bold') , fg = 'black')
seperate.place(y=215)


                    #################################################

lab8= Label(root , text = "Item Description" , font = ('helevetica','13','bold') , fg = 'blue')
lab8.place(x=20 , y=240)

lab9= Label(root , text = "Qty" , font = ('helevetica','13','bold') , fg = 'blue')
lab9.place(x=700 , y=240)

lab10= Label(root , text = "Amount" , font = ('helevetica','13','bold') , fg = 'blue')
lab10.place(x=900 , y=240)

seperate = Label(root , text = v , font = ('helevetica','5','bold') , fg = 'black')
seperate.place(y=265)


                    #################################################

seperate = Label(root , text = v , font = ('helevetica','5','bold') , fg = 'black')
seperate.place(y=385)

lab11= Label(root , text = "Subtotal" , font = ('helevetica','13','bold') , fg = 'blue')
lab11.place(x=20 , y=400)

lab12= Label(root , text = "Service Tax" , font = ('helevetica','13','bold') , fg = 'blue')
lab12.place(x=20 , y=420)

lab13= Label(root , text = "Sales Tax" , font = ('helevetica','13','bold') , fg = 'blue')
lab13.place(x=20 , y=440)

seperate = Label(root , text = s , font = ('helevetica','5','bold') , fg = 'black')
seperate.place(x=860 , y=460)

lab14= Label(root , text = "Total Invoice" , font = ('helevetica','13','bold') , fg = 'blue')
lab14.place(x=20 , y=480)

seperate = Label(root , text = v , font = ('helevetica','5','bold') , fg = 'black')
seperate.place(y=500)

                    #################################################

lab15= Label(root , text = "_________________________________Thank You For Choosing Us_________________________________" , font = ('helevetica','13','bold') , fg = 'blue')
lab15.pack(side=BOTTOM)

root.mainloop()
