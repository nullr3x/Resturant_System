

from tkinter import *
from tkinter import messagebox
import datetime
import time
import random
import os

if __name__ == "__main__":
    root = Tk()
    root.geometry('1280x580')
    root.title("Resturant Managment System App")
    root.resizable(width=False, height=False)
    root.wm_attributes()
    root.config(bg="Black")


    #####################################____Running Time_Clock____#############################

    time1 = ''
    clock = Label(root, bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    clock.place(x=600, y=45)


    def tick():
        global time1
        time2 = time.strftime('%I:%M:%S')
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        clock.after(200, tick)


    tick()

    ########################################################################################
    ########################__Resturant Management System App__#############################
    ########################################################################################
    v = '_'*700

    seperate = Label(root , text = v , font = ('helevetica','5','bold') , fg = 'white', bg='black')
    seperate.place(y=2)

    resturant = Label(root , text = "Resturant Managment System" , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    resturant.place(x=480 , y=16)

    seperate = Label(root , text = v , font = ('helevetica','5','bold') , fg = 'white' , bg='black')
    seperate.place(y=70)

    calculator = Label(root , text = "Calculator" , bg = "black" , fg = "cyan" , font = ('helevetica','18','bold'))
    calculator.place(x=1050 , y=90)

    def made():
        w = Tk()
        w.geometry('500x80')
        w.resizable(width=False, height=False)
        w.title('Contact Us')
        w.config(bg='#06324c')

        name = Label(w, text="Name :-  Sahil Mehra", font=('helevetica', '12', 'bold'), fg='white' , bg='#06324c')
        name.pack()

        email = Label(w, text="Email :-  Sahilmehra1337@gmail.com", font=('helevetica', '12', 'bold'), fg='white' , bg='#06324c')
        email.pack()

        phone = Label(w, text="Contact No. :-  +91 8950881998", font=('helevetica', '12', 'bold'), fg='white' , bg='#06324c')
        phone.pack()

        w.after(5000, lambda: w.destroy())
        w.mainloop()


    made = Button(root , text = 'Devloped By' ,  bg = "red" ,bd =5 , fg = "black" , font = ('helevetica','10','bold italic'), width = 0 , command = made)
    made.place(x=1145 , y = 25)

    #########################################################################################
    ###############################___Functions___###########################################
    #########################################################################################

                                #---Price List---#
    def price():
        roo = Tk()
        roo.resizable(width=False, height=False)
        roo.title("Price List")
        roo.config(bg='#06324c')

        iteminfo = Label(roo, font = ('helevetica','15','bold italic'), text="ITEMS", fg="white", bd=5 ,bg='#06324c')
        iteminfo.grid(row=0, column=0)

        item0 = Label(roo, font=('aria', 15, 'bold'), text="___________________________", fg="white", anchor=W , bg='#06324c')
        item0.grid(row=0, column=2)

        item1 = Label(roo, font = ('helevetica','15','bold italic'), text="PRICE", fg="white",bg='#06324c', anchor=W)
        item1.grid(row=0, column=3)

        item2 = Label(roo, font = ('helevetica','15','bold italic'), text="  1.) Onion Pizza", fg="steel blue", anchor=W,bg='#06324c')
        item2.grid(row=1, column=0)

        item3 = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W ,bg='#06324c')
        item3.grid(row=1, column=3)

        item4 = Label(roo, font = ('helevetica','15','bold italic'), text="   2.) Capsicum Pizza", fg="steel blue" ,bg='#06324c')
        item4.grid(row=2, column=0)

        item5 = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W,bg='#06324c')
        item5.grid(row=2, column=3)

        item6 = Label(roo, font = ('helevetica','15','bold italic'), text="    3.) Soya Pizza", fg="steel blue",bg='#06324c')
        item6.grid(row=3, column=0)

        item7 = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W,bg='#06324c')
        item7.grid(row=3, column=3)

        item8 = Label(roo, font = ('helevetica','15','bold italic'), text=" 4.) Jalapeno Pizza", fg="steel blue",bg='#06324c')
        item8.grid(row=4, column=0)

        item9 = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W,bg='#06324c')
        item9.grid(row=4, column=3)

        item10 = Label(roo, font = ('helevetica','15','bold italic'), text="       5.) Paneer Pizza", fg="steel blue",bg='#06324c')
        item10.grid(row=5, column=0)

        item11 = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W,bg='#06324c')
        item11.grid(row=5, column=3)

        item12 = Label(roo, font = ('helevetica','15','bold italic'), text="6.) Soft Drinks", fg="steel blue",bg='#06324c')
        item12.grid(row=6, column=0)

        item13 = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W,bg='#06324c')
        item13.grid(row=6, column=3)

        roo.mainloop()


                                        #---Total---#
    def totcost():
        x = random.randint(10000, 99999)
        randomint = str(x)
        ranint.set(randomint)

        fries = float(ent2.get())
        lunch = float(ent3.get())
        burger = float(ent4.get())
        pizza = float(ent5.get())
        cheese = float(ent6.get())
        drink = float(ent7.get())

        fri_price = fries * 25
        lunch_price = lunch * 40
        burger_price = burger * 35
        pizza_price = pizza * 50
        cheese_price = cheese * 50
        drink_price = drink * 35

        sum = fri_price + lunch_price + burger_price + pizza_price + cheese_price + drink_price
        Sales_Tax = sum * 0.33
        Service_Tax = sum / 99

        Cost = "Rs.", str(sum)
        Service = "Rs.", str(round(Service_Tax, 2))
        Subtotal = "Rs.", str(sum)
        tax = "Rs.", str(round(Sales_Tax, 2))
        Total = "Rs.", str(round((sum + Sales_Tax + Service_Tax), 2))

        cost.set(Cost)
        service.set(Service)
        sales.set(tax)
        subtot.set(Subtotal)
        tot.set(Total)

            #---Reset---#
    def reset():
        ranint.set("")
        fries.set("")
        lunch.set("")
        burger.set("")
        pizza.set("")
        cheese.set("")
        drink.set("")
        cost.set("")
        service.set("")
        sales.set("")
        subtot.set("")
        tot.set("")

            #---Exit---#
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()




    #########################################################################################

    ranint = StringVar()
    fries = StringVar()
    lunch = StringVar()
    burger = StringVar()
    pizza = StringVar()
    cheese = StringVar()
    drink = StringVar()
    cost = StringVar()
    service = StringVar()
    sales = StringVar()
    subtot = StringVar()
    tot = StringVar()


    #########################################################################################
    #############################___Left_Labels_Design___####################################
    #########################################################################################


    lab1 = Label(root , text = "Order No." , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    lab1.place(x=40, y=100)

    ent1 = Entry(root , bd =5 , justify='right' , textvariable = ranint)
    ent1.place(x=220, y=100)

    ########################

    lab2 = Label(root , text = "Onion Pizza" , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    lab2.place(x=40, y=140)

    ent2 = Entry(root , bd =5 , justify='right' , textvariable = fries)
    ent2.place(x=220, y=140)

    ########################

    lab3 = Label(root , text = "Capsicum Pizza" , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    lab3.place(x=40, y=180)

    ent3 = Entry(root , bd =5 , justify='right' , textvariable = lunch)
    ent3.place(x=220, y=180)

    ########################

    lab4 = Label(root , text = "Soya Pizza" , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    lab4.place(x=40, y=220)

    ent4 = Entry(root , bd =5 , justify='right' , textvariable = burger)
    ent4.place(x=220, y=220)

    ########################

    lab5 = Label(root , text = "Jalapeno Pizza" , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    lab5.place(x=40, y=260)

    ent5 = Entry(root , bd =5 , justify='right' , textvariable = pizza)
    ent5.place(x=220, y=260)

    ########################

    lab6 = Label(root , text = "Paneer Pizza" , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    lab6.place(x=40, y=300)

    ent6 = Entry(root , bd =5 , justify='right' , textvariable = cheese)
    ent6.place(x=220, y=300)

    #########################################################################################
    ###############################___Right_Label_Design___##################################
    #########################################################################################


    lab7 = Label(root , text = "Soft Drinks" , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    lab7.place(x=500, y=100)

    ent7 = Entry(root , bd =5 , justify='right' , textvariable = drink)
    ent7.place(x=660, y=100)

    ########################

    lab8 = Label(root , text = "Cost" , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    lab8.place(x=500, y=140)

    ent8 = Entry(root , bd =5 , justify='right' , textvariable = cost)
    ent8.place(x=660, y=140)

    ########################

    lab9 = Label(root , text = "Service Tax" , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    lab9.place(x=500, y=180)

    ent9 = Entry(root , bd =5 , justify='right' , textvariable = service)
    ent9.place(x=660, y=180)

    ########################

    lab10 = Label(root , text = "Sales Tax" , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    lab10.place(x=500, y=220)

    ent10 = Entry(root , bd =5 , justify='right' , textvariable = sales)
    ent10.place(x=660, y=220)

    ########################

    lab11 = Label(root , text = "Subtotal" , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    lab11.place(x=500, y=260)

    ent11 = Entry(root , bd =5 , justify='right' , textvariable = subtot)
    ent11.place(x=660, y=260)

    ########################

    lab12 = Label(root , text = "Total" , bg = "black" , fg = "cyan" , font = ('helevetica','15','bold italic'))
    lab12.place(x=500, y=300)

    ent12 = Entry(root , bd =5 , justify='right' , textvariable = tot)
    ent12.place(x=660, y=300)

    #########################################################################################
    ###############################___Calculator_Button___###################################
    #########################################################################################
    text_input = StringVar()
    operator =""

    def  btnclick(numbers):
        global operator
        operator=operator + str(numbers)
        text_input.set(operator)

    def clrdisplay():
        global operator
        operator=""
        text_input.set("")

    def equal():
        global operator
        sumup=str(eval(operator))

        text_input.set(sumup)
        operator = ""

    disp = Entry(root , text = text_input , bd=5 ,width=19 ,bg="white",justify='right' , font =('ariel',15))
    disp.place(x=1000 , y=130)

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
    btn0=Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="0",bg="powder blue", command=lambda: btnclick(0) )
    btn0.place(x=1070 , y=390)

    clear=Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="C",bg="powder blue", command=clrdisplay)
    clear.place(x=1000 , y=390)

    add = Button(root,padx=9,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="+",bg="powder blue", command=lambda: btnclick('+') )
    add.place(x=1208 , y=180)

    sub = Button(root,padx=14,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="-",bg="powder blue", command=lambda: btnclick('-') )
    sub.place(x=1208 , y=250)

    mul = Button(root,padx=12,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="*",bg="powder blue", command=lambda: btnclick('*') )
    mul.place(x=1140 , y=390)

    div = Button(root,padx=15,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="/",bg="powder blue", command=lambda: btnclick('/') )
    div.place(x=1208 , y=320)

    equal = Button(root,padx=10,pady=8,bd=4, fg="black", font=('ariel', 15 ,'bold'),text="=",bg="powder blue", command=equal)
    equal.place(x=1208 , y=390)

    #########################################################################################
    #######################################___Buttons__######################################
    #########################################################################################

    price = Button(root, bd=5 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Price", bg="red",command=price)
    price.place(x=40 ,y=460)

    total = Button(root, bd=5 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Total", bg="red",command=totcost)
    total.place(x=245 ,y=460)

    reset = Button(root, bd=5 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Reset", bg="red",command=reset)
    reset.place(x=450 ,y=460)

    exit = Button(root, bd=5 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Exit", bg="red",command=on_closing)
    exit.place(x=655 , y=460)

    #########################################################################################

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
