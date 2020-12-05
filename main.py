from tkinter import *
import pymysql as py
import tkinter.messagebox
import datetime
import pymysql as py
import math
import os
import random
conn=py.connect(user='root',password='',host='localhost',database='store')
c=conn.cursor()
date=datetime.datetime.now().date()
##temprory list like sessions
product_lists=[]
product_price=[]
product_quantity=[]
productid=[]
##list for label
label_list=[]


class application:
    def __init__(self,master,*args,**kwargs):
        self.master=master
        self.left=Frame(master,width=700,height=768,bg='white')
        self.left.pack(side=LEFT)
        self.right= Frame(master,width=666, height=768,bg='lightblue')
        self.right.pack(side=RIGHT)
        ####componnents
        self.heading=Label(self.left,text="STORE MANAGEMENT BILLING SYSTEM",font=('ariel 25 bold'),bg='white')
        self.heading.place(x=0,y=5)
        #####datee
        self.date_l=Label(self.right,text="TODAY DATE :-    "+str(date),font=("ariel 15 bold"),bg='lightblue')
        self.date_l.place(x=0,y=0)
        ############## TABLE INVOICE
        self.tproduct=Label(self.right,text="product",font=("ariel 18 bold"),bg="lightblue")
        self.tproduct.place(x=0,y=60)
        self.tquantity= Label(self.right, text="Quantity", font=("ariel 18 bold"), bg="lightblue")
        self.tquantity.place(x=300,y=60)
        self.tamount= Label(self.right, text="Amount", font=("ariel 18 bold"), bg="lightblue")
        self.tamount.place(x=500, y=60)
        #########entery stuff
        self.enterid=Label(self.left,text="Enter product id",font=("ariel 18 bold"),bg='white')
        self.enterid.place(x=0,y=80)
        self.enteride=Entry(self.left,width=25,font=("ariel 18 bold"),bg='white')
        self.enteride.place(x=195,y=80)
        ####butt to search
        self.search_btn=Button(self.left,width=22,height=2,text='search',bg='orange',command=self.ajax)
        self.search_btn.place(x=350,y=120)
        ####fill it later by ajax fucytiok
        self.productname=Label(self.left,text='',font=('ariel 18 bold'),fg='skyblue')
        self.productname.place(x=0,y=250)
        self.pprice=Label(self.left,text='',font=('ariel 18 bold'),fg='skyblue')
        self.pprice.place(x=0,y=290)
        ###total alabel
        self.total_l=Label(self.right,text="ffff",font=('ariel 18 bold'),bg='light blue',fg='white')
        self.total_l.place(x=0,y=600)
    def ajax(self):
        self.getId=self.enteride.get()
        query="select *  from inventory where id=%s"
        c.execute(query,self.getId)
        myresult=c.fetchall()
        for self.r in myresult:
            self.get_name=self.r[1]
            self.get_price=self.r[4]
            self.get_stock=self.r[3]
        self.productname.configure(text="PRODUCT NAME :- "+str(self.get_name))
        self.pprice.configure(text="PRICE:- RS"+str(self.get_price))
        ##### craete the quantity
        self.quantity_l=Label(self.left,text="Enter the quantity",font=('ariel 18 bold'),bg= 'white')
        self.quantity_l.place(x=0,y=370)
        self.quantity_e=Entry(self.left,width=25,font=('ariel 18 bold'),bg='light blue')
        self.quantity_e.place(x=220,y=370)
        self.quantity_e.focus()
        #### create for didcount
        self.discount_l = Label(self.left, text="Enter the Discount", font=('ariel 18 bold'), bg='white')
        self.discount_l.place(x=0, y=410)
        self.discount_e = Entry(self.left, width=25, font=('ariel 18 bold'), bg='light blue')
        self.discount_e.insert(END,0)
        self.discount_e.place(x=220, y=410)
        #### for add to car bitton
        self.add_tocart= Button(self.left, width=22, height=2, text='Add to cart', bg='orange',command=self.add_to_cart)
        self.add_tocart.place(x=370, y=450)
        ####genrate bill and cahnges
        self.change_l=Label(self.left,text='given amount',font=('ariel 18 bold'),bg='white')
        self.change_l.place(x=0,y=550)
        self.change_e=Entry(self.left,width=25,bg="light blue")
        self.change_e.place(x=190,y=550)
        ###button change
        self.changebtn=Button(self.left,text='calculate change',width=22,bg='orange',command=self.change_func)
        self.changebtn.place(x=350,y=590)
        ####generat bill button
        self.gnratebtn = Button(self.left, text='Generate Bill', width=100, height=2, bg='red',command=self.genrate_bill)
        self.gnratebtn.place(x=0, y=640)
    def add_to_cart(self,*args,**kwargs):
        #get the quqntirty value from database
        self.quantity_value=int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo('Error','not sufficeint stock')
        else:
            ###calculation  of price
            self.finalprice=float(self.quantity_value)*float(self.get_price)-float(self.discount_e.get())
            product_lists.append(self.get_name)
            product_price.append(self.finalprice)

            product_quantity.append(self.quantity_value)
            productid.append(self.getId)

            self.x_index=0
            self.y_index=100
            self.counter=0
            for self.p in product_lists:
                self.tempname=Label(self.right,text=str(product_lists[self.counter]),font=('ariel 18 bold'),bg='light blue',fg='black')
                self.tempname.place(x=0,y=self.y_index)
                label_list.append(self.tempname)
                self.tempqt=Label(self.right,text=str(product_quantity[self.counter]),font=('ariel 18 bold'),bg='light blue',fg='black')
                self.tempqt.place(x=300,y=self.y_index)
                label_list.append(self.tempqt)
                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('ariel 18 bold'), bg='light blue',fg='black')
                self.tempprice.place(x=500, y=self.y_index)
                label_list.append(self.tempprice)
                self.y_index+=40
                self.counter+=1
                #totalconfigure
                self.total_l.configure(text='Total'+str(sum(product_price)))
                ###delete the bhutton
                self.quantity_l.place_forget()
                self.quantity_e.place_forget()
                self.discount_e.place_forget()
                self.discount_l.place_forget()
                self.productname.configure(text='')
                self.pprice.configure(text='')
                self.add_tocart.destroy()


                ##autofocus to eneterid
                self.enterid.focus()
                self.enteride.delete(0,END)
    def change_func(self,*args,**kwargs):
        self.amount_given=float(self.change_e.get())
        self.our_total=float(sum(product_price))
        self.togiven=self.amount_given-self.our_total
        ####label for change
        self.c_amount=Label(self.left,text='change:RS'+str(self.togiven),font=('ariel 18 bold'),fg='red')
        self.c_amount.place(x=0,y=600)
    def genrate_bill(self,*args,**kwargs):
        ###create the bill before update the db
        directory=('C:/Users/Aman gupta/Desktop/sales/invoice/date')
        if not os.path.exists(directory):
            os.makedirs(directory)

        company="\t\t\t\t AMAN GENRAL STORE\n"
        address="\t\t\t\t\t\tLucknow\n"
        phone="\t\t\t\t\t8707711852\n"
        sample=" \t\t\t\t\t\tinvoice\n"
        datee=str(date)
        tableheader="\n\n\n--------------------------------------------------------\n--------------------------------------------------------\n\tsn.\t\tproduct\t\tqty\t\tamount\n\t\t\t"
        final=company+address+phone+sample+datee+tableheader
        ###open file to write it
        filename=str(directory)+str(random.randrange(5000,10000))+".rtf"
        f=open(filename,'w')
        f.write(final)
        r=1
        i=0
        for t in product_lists:
            f.write("\n\t"+str(r)+"\t\t"+str(product_lists[i])[:7]+"\t\t"+str(product_quantity[i])+"\t\t"+str(product_price[i]))
            i+=1
            r+=1
        f.write("\n\n\t\t total:-"+str(sum(product_price)))
        f.write("\n\n\n\t\t Thanks for visiting")
        os.startfile(filename,"print")
        f.close()

        #dectrease the stock
        self.x=0
        initial="select * from inventory where id=%s"
        result=c.execute(initial,(productid[self.x],))
        result1=c.fetchall()
        for i in product_lists:


            for r in result1:
                self.oldstock=r[2]


            self.newstock=(self.oldstock)-(product_quantity[self.x])
            ####update the stock
            sql="update inventory set stock=%s where id=%s"
            val1=(self.newstock,productid[self.x])
            c.execute(sql,val1)
            conn.commit()
            ######insert into transection
            sql2='''insert into transection(id,productname,quantity,amount,date) values(%s,%s,%s,%s,%s)'''
            val2=(self.getId,product_lists[self.x],product_quantity[self.x],product_price[self.x],date)
            c.execute(sql2,val2)
            conn.commit()
            self.x+=1
        for a in label_list:

            a.destroy()
            del(product_lists[:])
            del(productid[:])
            del(product_price[:])
            del(product_quantity[:])
            # self.total_l.configure(text='')
            # self.c_amount.configure(0,END)
            # self.change_e.configure(0,END)
            # self.enteride.focus()

root=Tk()
b=application(root)
root.geometry("1366x768+0+0")
root.title("Selling desk")
root.mainloop()


###############################doneee########################



