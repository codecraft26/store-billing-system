import pymysql as py
from tkinter import *
import tkinter.messagebox
conn=py.connect(user='root',password="",host='localhost',database='store')
c=conn.cursor()
c.execute("select max(id) from inventory")
result=c.fetchall()
for r in result:
    id=r[0]
class Database:

    def __init__(self, master, *args, **kwargs):

        self.master = master
        self.heading = Label(master, text="Add to database", font='ariel 18 bold', fg='steelblue')
        self.heading.place(x=400, y=0)
        # labels for windows
        self.name_l = Label(master, text='Enter product Name', font=('ariel 18 bold'))
        self.name_l.place(x=0, y=70)
        self.stock_l = Label(master, text='stock', font=('ariel 18 bold'))
        self.stock_l.place(x=0, y=120)
        self.cp_l = Label(master, text='Enter Cost price', font=('ariel 18 bold'))
        self.cp_l.place(x=0, y=170)
        self.sp_l = Label(master, text='Enter Selling Price', font=('ariel 18 bold'))
        self.sp_l.place(x=0, y=220)
        self.vendor_l = Label(master, text='Enter Vendor  Name', font=('ariel 18 bold'))
        self.vendor_l.place(x=0, y=270)
        self.vendorphn_l = Label(master, text='Enter Vendor phone number', font=('ariel 18 bold'))
        self.vendorphn_l.place(x=0, y=320)
        self.id_l=Label(master,text="Enter the id",font=('ariel 18 bold'))
        self.id_l.place(x=0,y=370)
        # eneries for label
        self.name_e = Entry(master, width=25, font=('ariel 18 bold'))
        self.name_e.place(x=380, y=70)
        self.stock_e = Entry(master, width=25, font=('ariel 18 bold'))
        self.stock_e.place(x=380, y=120)
        self.sp_e = Entry(master, width=25, font=('ariel 18 bold'))
        self.sp_e.place(x=380, y=170)
        self.cp_e = Entry(master, width=25, font=('ariel 18 bold'))
        self.cp_e.place(x=380, y=220)
        self.vendor_e = Entry(master, width=25, font=('ariel 18 bold'))
        self.vendor_e.place(x=380, y=270)
        self.vendorphn_e = Entry(master, width=25, font=('ariel 18 bold'))
        self.vendorphn_e.place(x=380, y=320)
        self.id_e=Entry(master,width=25,font=('ariel 18 bold'))
        self.id_e.place(x=380,y=370)
        # buttons to add databases#################################################################
        self.btn_add = Button(master, text='Add to Databases', width=25, height=2, bg='steel blue', fg='white',command=self.get_items)
        self.btn_add.place(x=520, y=420)
        #############################################################################
        # text box###############################
        self.tbox= Text(master, width=50 ,height=22)
        self.tbox.place(x=750,y=70)
        self.tbox.insert(END,"ID has reached up to "+str(id)+"\n")
        ####button to clear all
        self.btn_clear = Button(master, text='clear all field', width=18, height=2, bg='green', command=self.clear_all,fg='white')
        self.btn_clear.place(x=350, y=420)


        #####################
        # self.master.bind('<RETURN>',self.get_items)
        # self.master.bind('<Up',self.clear_all)
        ############################################################
        ##############################################
    def get_items(self, *args, **kwargs):
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendorphn = self.vendorphn_e.get()
        self.id=self.id_e.get()
       # dyanamic enteries
       #  .totalcp = float((self.cp) * (self.stock))
       #  self.totalsp = float((self.sp) -(self.stock))
       #  self.assumedprofit = ((self.totalsp - self.totalcp))

        if self.name =='' or self.stock =='' or self.sp=='':

            tkinter.messagebox.showinfo("Error","Please fill all the Enteries")
        else:


            inserttable="insert into inventory(ID,name,stock,cp,sp,totalcp,totalsp,assumedprofit,vendor,vendor_phn) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(self.id,self.name, self.stock, self.cp, self.sp,522, 4545,5415, self.vendor,self.vendorphn)
            c.execute(inserttable,val)
            conn.commit()

            tkinter.messagebox.showinfo("success","successfully added to the database")
            #textbox inserted
            self.tbox.insert(END, 'inserted \t\t' + str(self.name) + 'into the databases\t'+str(self.id_e.get()))


    def clear_all(self,*args,**kwargs):
        # num = id + 1
        self.name_e.delete(0,END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendorphn_e.delete(0, END)
        self.id_e.delete(0,END)

root=Tk()
b=Database(root)
root.geometry('1366x468+0+0')
root.title("ADD TO DATABASE")

root.mainloop()