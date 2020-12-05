import pymysql as py
from tkinter import *
from tkinter import Text
import tkinter.messagebox


conn=py.connect(user='root',password='',host='localhost',database='store')
c=conn.cursor()
c.execute("SELECT MAX(id) from inventory")
result=c.fetchall()

for r in result:
    id=r[0]
class Database:

    def __init__(self, master, *args, **kwargs):

        self.master = master
        self.haeding = Label(master, text="UPDATE THE ITEMS", font='ariel 18 bold', fg='steelblue')
        self.haeding.place(x=400, y=0)
        #LABEL AND ENTERY FOR LABEL
        self.id_le=Label(master,text='Enter the id',font=('ariel 18 bold'))
        self.id_le.place(x=0,y=70)
        self.id_leb=Entry(master,width=10,font=('ariel 18 bold'))
        self.id_leb.place(x=250,y=70)
        self.search_btn=Button(master,font=('ariel 18 bold'),width=10,bg='green',fg='white',text='SEARCH',command=self.search)
        self.search_btn.place(x=450,y=70)
        # labels for windows
        self.name_l = Label(master, text='Enter product Name', font=('ariel 18 bold'))
        self.name_l.place(x=0, y=120)
        self.stock_l = Label(master, text='stock', font=('ariel 18 bold'))
        self.stock_l.place(x=0, y=170)
        self.cp_l = Label(master, text='Enter Cost price', font=('ariel 18 bold'))
        self.cp_l.place(x=0, y=220)
        self.sp_l = Label(master, text='Enter Selling Price', font=('ariel 18 bold'))
        self.sp_l.place(x=0, y=270)
        self.vendor_l = Label(master, text='Enter Vendor  Name', font=('ariel 18 bold'))
        self.vendor_l.place(x=0, y=320)
        self.vendorphn_l = Label(master, text='Enter Vendor phone number', font=('ariel 18 bold'))
        self.vendorphn_l.place(x=0, y=370)

        # eneries for label
        self.name_e = Entry(master, width=25, font=('ariel 18 bold'))
        self.name_e.place(x=380, y=120)
        self.stock_e = Entry(master, width=25, font=('ariel 18 bold'))
        self.stock_e.place(x=380, y=170)
        self.sp_e = Entry(master, width=25, font=('ariel 18 bold'))
        self.sp_e.place(x=380, y=220)
        self.cp_e = Entry(master, width=25, font=('ariel 18 bold'))
        self.cp_e.place(x=380, y=270)
        self.vendor_e = Entry(master, width=25, font=('ariel 18 bold'))
        self.vendor_e.place(x=380, y=320)
        self.vendorphn_e = Entry(master, width=25, font=('ariel 18 bold'))
        self.vendorphn_e.place(x=380, y=370)

        # buttons to add databases
        self.btn_add = Button(master, text="update the database", width=25, height=2, bg='steel blue', fg='white',command=self.update)
        self.btn_add.place(x=520, y=470)

        # text box
        self.tbox= Text(master, width=30 ,height=22)
        self.tbox.place(x=750,y=70)
        #selelction for adding id number into text box
        self.tbox.insert(END, "ID has reached up to " + str(id))
        # self.tbox.insert(END,"id has reached up to"+str(self.id_leb.get()))
        # button for clear allself.btn_clear = B
        self.btn_clear=Button(master, text='clear all field', width=18 ,height=2, bg='green',fg='white',command=self.clear_all)
        self.btn_clear.place(x=350,y=470)
    def search(self,*args,**kwargs):
        sql='select * FROM inventory where id=%s'

        c.execute(sql,(self.id_leb.get()))
        result=c.fetchall()
        for r in result:



            self.n1=r[1]#name
            self.n2=r[2]#stock
            self.n3=r[3]#cp
            self.n4=r[4]#sp
            self.n5=r[5]#totalcp
            self.n6=r[6]#totaalsp
            self.n7=r[7]#asssumedprofit
            self.n8=r[8]#vendor
            self.n9=r[9]#vendorphone
        conn.commit()

        #######insert into the entries to udate

        self.name_e.delete(0, END)
        self.name_e.insert(0,str(self.n1))

        self.stock_e.delete(0, END)
        self.stock_e.insert(0, str(self.n2))

        self.cp_e.delete(0, END)
        self.cp_e.insert(0, str(self.n3))

        self.sp_e.delete(0, END)
        self.sp_e.insert(0, str(self.n4))

        self.vendor_e.delete(0, END)
        self.vendor_e.insert(0, str(self.n8))

        self.vendorphn_e.delete(0, END)
        self.vendorphn_e.insert(0, str(self.n9))

    def clear_all(self, *args, **kwargs):
        # num = id + 1
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendorphn_e.delete(0, END)
        self.id_e.delete(0, END)
    def update(self,*args,**kwargs):
        ##get all the updated value
        self.u1=self.name_e.get()
        self.u2=self.stock_e.get()
        self.u3=self.cp_e.get()
        self.u4=self.sp_e.get()
        # self.u5=8855
        # self.u6=855
        self.u7=self.vendor_e.get()
        self.u8=self.vendorphn_e.get()
        query='UPDATE inventory SET name=%s,stock=%s,cp=%s,sp=%s,vendor=%s,vendor_phn=%s where id=%s'
        val3=(self.u1,self.u2,self.u3,self.u4,self.u7,self.u8,self.id_leb.get())
        c.execute(query,val3)
        conn.commit()
        tkinter.messagebox.showinfo("done","addded to data bases")
root=Tk()
b=Database(root)
#root.geomatry("1366x468+0+0")
root.title("UPDATE TO DATABASES")
root.mainloop()
