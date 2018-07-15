

from tkinter import *
from tkinter import messagebox
import datetime
import random


root = Tk()
root.title("Resturant Managment System App")
root.configure(bg = "#ff8000")

########################################################################################
########################__Resturant Management System App__#############################
########################################################################################


seperate = Frame(height=2, bd=1, relief=SUNKEN)
seperate.pack(fill=X, padx=5, pady=5)

resturant = Label(root , text = "Resturant Managment System" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
resturant.pack()

date = Label(root , text = datetime.datetime.now().strftime("(%A) %B %d, %Y %I:%M:%S %p") , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','10','bold italic'))
date.pack()

seperate = Frame(height=2, bd=1, relief=SUNKEN)
seperate.pack(fill=X, padx=5, pady=5)

calculator = Label(root , text = "Calculator" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','18','bold'))
calculator.place(x=1050 , y=100)

made = Label(root , text = "*Sahil Mehra" ,  bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
made.place(x=1200 ,y=650)


#########################################################################################
#############################___Left_Labels_Design___####################################
#########################################################################################

lab1 = Label(root , text = "Order No." , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
lab1.place(x=40, y=100)

ent1 = Entry(root , bd =5 , justify='right')
ent1.place(x=220, y=100)

########################

lab2 = Label(root , text = "Fried Meal" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
lab2.place(x=40, y=140)

ent2 = Entry(root , bd =5 , justify='right')
ent2.place(x=220, y=140)

########################

lab3 = Label(root , text = "Lunch Meal" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
lab3.place(x=40, y=180)

ent3 = Entry(root , bd =5 , justify='right')
ent3.place(x=220, y=180)

########################

lab4 = Label(root , text = "Burger Meal" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
lab4.place(x=40, y=220)

ent4 = Entry(root , bd =5 , justify='right')
ent4.place(x=220, y=220)

########################

lab5 = Label(root , text = "Pizza Meal" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
lab5.place(x=40, y=260)

ent5 = Entry(root , bd =5 , justify='right')
ent5.place(x=220, y=260)

########################

lab6 = Label(root , text = "Cheese Meal" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
lab6.place(x=40, y=300)

ent6 = Entry(root , bd =5 , justify='right')
ent6.place(x=220, y=300)

#########################################################################################
###############################___Right_Label_Design___##################################
#########################################################################################


lab7 = Label(root , text = "Drink" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
lab7.place(x=500, y=100)

ent7 = Entry(root , bd =5 , justify='right')
ent7.place(x=660, y=100)

########################

lab8 = Label(root , text = "Cost" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
lab8.place(x=500, y=140)

ent8 = Entry(root , bd =5 , justify='right')
ent8.place(x=660, y=140)

########################

lab9 = Label(root , text = "Service Tax" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
lab9.place(x=500, y=180)

ent9 = Entry(root , bd =5 , justify='right')
ent9.place(x=660, y=180)

########################

lab10 = Label(root , text = "Tax" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
lab10.place(x=500, y=220)

ent10 = Entry(root , bd =5 , justify='right')
ent10.place(x=660, y=220)

########################

lab11 = Label(root , text = "Subtotal" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
lab11.place(x=500, y=260)

ent11 = Entry(root , bd =5 , justify='right')
ent11.place(x=660, y=260)

########################

lab12 = Label(root , text = "Total" , bg = "#ff8000" , fg = "cyan" , font = ('helevetica','15','bold italic'))
lab12.place(x=500, y=300)

ent12 = Entry(root , bd =5 , justify='right')
ent12.place(x=660, y=300)

#########################################################################################
###############################___Calculator_Button___###################################
#########################################################################################
text = Stringvar()
operator =""

def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def equal():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

disp = Entry(root , text = text , bd=5 ,width=30 ,bg="white",justify='right')
disp.place(x=1000 , y=140)

                    #----------------------------Calvulator_Buttons------------------------------#
btn7=Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="7",bg="powder blue", command=lambda: btnclick(7) )
btn7.place(x=1000 , y=180)

btn8=Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="8",bg="powder blue", command=lambda: btnclick(8) )
btn8.place(x=1070 , y=180)

btn9=Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="9",bg="powder blue", command=lambda: btnclick(9) )
btn9.place(x=1140 , y=180)
                                #--------------------------------------------------#
btn4=Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="4",bg="powder blue", command=lambda: btnclick(4) )
btn4.place(x=1000 , y=250)

btn5=Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="5",bg="powder blue", command=lambda: btnclick(5) )
btn5.place(x=1070 , y=250)

btn6=Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="6",bg="powder blue", command=lambda: btnclick(6) )
btn6.place(x=1140 , y=250)
                                #--------------------------------------------------#
btn1=Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="1",bg="powder blue", command=lambda: btnclick(1) )
btn1.place(x=1000 , y=320)

btn2=Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="2",bg="powder blue", command=lambda: btnclick(2) )
btn2.place(x=1070 , y=320)

btn3=Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="3",bg="powder blue", command=lambda: btnclick(3) )
btn3.place(x=1140 , y=320)
                                #---------------------------------------------------#
btn0=Button(root,padx=45,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="0",bg="powder blue", command=lambda: btnclick(0) )
btn0.place(x=1000 , y=390)

add = Button(root,padx=9,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="+",bg="powder blue", command=lambda: btnclick('+') )
add.place(x=1208 , y=180)

sub = Button(root,padx=14,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="-",bg="powder blue", command=lambda: btnclick('-') )
sub.place(x=1208 , y=250)

mul = Button(root,padx=12,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="*",bg="powder blue", command=lambda: btnclick('*') )
mul.place(x=1140 , y=390)

div = Button(root,padx=15,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="/",bg="powder blue", command=lambda: btnclick('/') )
div.place(x=1208 , y=320)

equal = Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="=",bg="powder blue", command=lambda: btnclick('=') )
equal.place(x=1208 , y=390)

#########################################################################################
###############################___Functions___###########################################
#########################################################################################

                            #---Price List---#
def price():
    roo = Tk()
    roo.title("Price List")

    iteminfo = Label(roo, font = ('helevetica','15','bold italic'), text="ITEMS", fg="black", bd=5)
    iteminfo.grid(row=0, column=0)

    item = Label(roo, font=('aria', 15, 'bold'), text="_________________________", fg="white", anchor=W)
    item.grid(row=0, column=2)

    item = Label(roo, font = ('helevetica','15','bold italic'), text="PRICE", fg="black", anchor=W)
    item.grid(row=0, column=3)

    item1 = Label(roo, font = ('helevetica','15','bold italic'), text="  1.) Fries Meal", fg="steel blue", anchor=W)
    item1.grid(row=1, column=0)

    item1 = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    item1.grid(row=1, column=3)

    item2 = Label(roo, font = ('helevetica','15','bold italic'), text="   2.) Lunch Meal", fg="steel blue", anchor=W)
    item2.grid(row=2, column=0)

    item2 = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    item2.grid(row=2, column=3)

    item3 = Label(roo, font = ('helevetica','15','bold italic'), text="    3.) Burger Meal", fg="steel blue", anchor=W)
    item3.grid(row=3, column=0)

    item3 = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    item3.grid(row=3, column=3)

    item4 = Label(roo, font = ('helevetica','15','bold italic'), text=" 4.) Pizza Meal", fg="steel blue", anchor=W)
    item4.grid(row=4, column=0)

    item4 = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    item4.grid(row=4, column=3)

    item5 = Label(roo, font = ('helevetica','15','bold italic'), text="       5.) Cheese Burger", fg="steel blue", anchor=W)
    item5.grid(row=5, column=0)

    item6 = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    item6.grid(row=5, column=3)

    item7 = Label(roo, font = ('helevetica','15','bold italic'), text="6.) Drinks", fg="steel blue", anchor=W)
    item7.grid(row=6, column=0)

    item7 = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    item7.grid(row=6, column=3)

    root.mainloop()

                            #---Generate Invoice Bill---#


                                    #---Total---#
def total():
    x = random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    fried = float(ent1.get())
    lunch = float(ent2.get())
    burger = float(ent3.get())
    pizza = float(ent4.get())
    cheese = float(ent5.get())
    drink = float(ent6.get())

    fri_price = fried * 25
    lunch_price = lunch * 40
    burger_price = burger * 35
    pizza_price = pizza * 50
    cheese_price = cheese * 50
    drink_price = drink * 35

    cost_of_meal = "Rs.", str('%.2f' % (fri_price + lunch_price + burger_price + pizza_price + cheese_price + drink_price))
    PayTax = ((fri_price + lunch_price + burger_price + pizza_price + cheese_price + drink_price) * 0.33)
    Totalcost = (fri_price + lunch_price + burger_price + pizza_price + cheese_price + drink_price)
    Ser_Charge = ((fri_price + lunch_price + burger_price + pizza_price + cheese_price + drink_price) / 99)
    Service = "Rs.", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs.", str(PayTax + Totalcost + Ser_Charge)
    PaidTax = "Rs.", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)

        #---Reset---#
def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")

        #---Exit---#
def exit():
    global root
    root.quit()

#########################################################################################
#######################################___Buttons__######################################
#########################################################################################

invoice = Button(root, bd=5 ,fg="black",font=('ariel' ,16,'bold'),width=51, text="Generate Invoice Bill", bg="red",command=price)
invoice.place(x=40 ,y=405)

price = Button(root, bd=5 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Price", bg="red",command=price)
price.place(x=40 ,y=460)

total = Button(root, bd=5 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Total", bg="red",command=total)
total.place(x=245 ,y=460)

reset = Button(root, bd=5 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Reset", bg="red",command=reset)
reset.place(x=450 ,y=460)

exit = Button(root, bd=5 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Exit", bg="red",command=exit)
exit.place(x=655 , y=460)

#########################################################################################

root.mainloop()