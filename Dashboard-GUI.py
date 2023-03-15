from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import datetime
from Mini_project_data import  Database as db


class Design:
    def __init__(self):
        self.root=Tk()
        self.root.state('zoomed')
        self.root.title("Dashboard")
        self.bt_save=Button()
        self.bt_clear=Button()
        self.bt_clear_ord=Button()
        self.bt_save_ord=Button()

        self.bt_add_cust=Button()
        self.bt_add_order=Button()

        self.serch_box=Entry()
        self.bt_bill=Button()
        self.bt_report=Button()

    def Menu_design(self):
        root=self.root
        menu=PanedWindow(root,width=200,height=620,bg='red')
        menu.place(x=10,y=10)

        self.bt_add_cust=Button(menu,text="ADD CUSTOMER",width=19,height=2,font=('bold',12))
        self.bt_add_cust.place(x=10,y=10)

        self.bt_add_order=Button(menu,text="ADD ORDER",width=19,height=2,font=('bold',12))
        self.bt_add_order.place(x=10,y=70)

        self.bt_bill=Button(menu,text="BILLING",width=19,height=2,font=('bold',12))
        self.bt_bill.place(x=10,y=130)

        self.bt_report=Button(menu,text="REPORT'S",width=19,height=2,font=('bold',12))
        self.bt_report.place(x=10,y=190)

        self.bt_report=Button(menu,text="SET PRICE",width=19,height=2,font=('bold',12))
        self.bt_report.place(x=10,y=250)

    def Display_design(self):
        root=self.root
        panel=PanedWindow(root,width=1030,height=620,bg='grey')
        panel.place(x=230,y=10)

    def Add_cust_design(self):

        bcol='grey'

        root=self.root

        panel1=PanedWindow(root,width=1030,height=620,bg=bcol)
        panel1.place(x=230,y=10)
        self.panel1=panel1
        f=25
        f1=25
        sz=-50
        lb1=Label(panel1,text="Name :",font=f,bg=bcol)
        lb1.place(x=160+sz,y=100)
        lb1=Label(panel1,text="Mobile No :",font=f,bg=bcol)
        lb1.place(x=130+sz,y=140)
        lb1=Label(panel1,text="Flat No :",font=f,bg=bcol)
        lb1.place(x=150+sz,y=180)
        lb1=Label(panel1,text="Landmark :",font=f,bg=bcol)
        lb1.place(x=130+sz,y=220)

        self.name=Entry(panel1,font=f1,width=35)
        self.name.place(x=220+sz,y=102)

        self.mob=Entry(panel1,font=f1,width=20)
        self.mob.place(x=220+sz,y=142)

        self.flt_no=Entry(panel1,font=f1,width=20)
        self.flt_no.place(x=220+sz,y=182)

        self.ldm=Entry(panel1,font=f1,width=20)
        self.ldm.place(x=220+sz,y=222)

        self.cal = Calendar(panel1, selectmode = 'day',
               year = 2022, month = 12,
               day = 18)

        self.cal.place(x=220+sz,y=272)

        self.bt_save=Button(panel1,text="SAVE",font=f1,width=10)
        self.bt_save.place(x=230+sz,y=472)
        self.bt_clear=Button(panel1,text="CLEAR",font=f1,width=10)
        self.bt_clear.place(x=350+sz,y=472)


    def Display_cust(self):

        columns=["ID","Name","Mobile_No","Flat_NO","Landmark","Date"]

        tree=ttk.Treeview(self.panel1,columns=columns,show='headings')
        tree.place(x=470,y=200)

        vsb = ttk.Scrollbar(self.panel1, orient="vertical", command=tree.yview)
        vsb.place(x=1010,y=200,height=225)

        tree.configure(yscrollcommand=vsb.set)

        for i in columns:
            tree.heading(i,text=i)
        tree.column("#0",anchor=CENTER, stretch=NO, width=0)
        tree.column(columns[0],anchor=CENTER, stretch=NO, width=40)
        tree.column(columns[1],anchor=W, stretch=NO, width=120)
        tree.column(columns[2],anchor=CENTER, stretch=NO, width=100)
        tree.column(columns[3],anchor=W, stretch=NO, width=60)
        tree.column(columns[4],anchor=W, stretch=NO, width=100)
        tree.column(columns[5],anchor=W, stretch=NO, width=120)


        for i in db().Customer_list():
            tree.insert('', END, values=(i[0],i[1],i[2],i[3],i[4],i[5]))

    def Clear_cust_add(self):
        self.name.delete(0,'end')
        self.mob.delete(0,'end')
        self.flt_no.delete(0,'end')
        self.ldm.delete(0,'end')

    def Validate_before_inserting_cust(self):
        name=self.name.get()
        mob=self.mob.get()
        flt=self.flt_no.get()
        ldm=self.ldm.get()
        cal=self.cal.get_date()
        dt=datetime.datetime.strptime(cal,'%m/%d/%y')
        dt=dt.strftime('%d-%b-%y')

        if (name=='' or mob=='' or flt==''):
            messagebox.showerror("Error Box", "Name,Mobile,Flat should not be blank!")
        elif db().check_customer(name,mob,flt,ldm,dt)>0:
            messagebox.showerror("Error Box", "Entered Data Already Exists!")

        else:
            db().Customer_insert(name,mob,flt,ldm,dt)
            self.Clear_cust_add()



    def Add_order_design(self):

        bcol='grey'

        root=self.root
        panel2=PanedWindow(root,width=1030,height=620,bg=bcol)
        panel2.place(x=230,y=10)
        self.panel2=panel2

        f=25
        f1=25
        xv=80
        lb1=Label(panel2,text="Name :",font=f,bg=bcol)
        lb1.place(x=200-xv,y=100)
        lb1=Label(panel2,text="Weight :",font=f,bg=bcol)
        lb1.place(x=190-xv,y=140)
        lb1=Label(panel2,text="No of Shirts :",font=f,bg=bcol)
        lb1.place(x=160-xv,y=180)
        lb1=Label(panel2,text="No of Pants :",font=f,bg=bcol)
        lb1.place(x=160-xv,y=220)
        lb1=Label(panel2,text="Action :",font=f,bg=bcol)
        lb1.place(x=200-xv,y=260)


        self.name_lt=ttk.Combobox(panel2,font=f1,width=20)
        self.name_lt.place(x=260-xv,y=102)
        self.name_lt['values']=db().Name_list()

        self.wet=Entry(panel2,font=f1,width=10)
        self.wet.place(x=260-xv,y=142)

        self.no_of_shirt=Entry(panel2,font=f1,width=10)
        self.no_of_shirt.place(x=260-xv,y=182)

        self.no_of_pants=Entry(panel2,font=f1,width=10)
        self.no_of_pants.place(x=260-xv,y=222)

        self.action_lt=ttk.Combobox(panel2,font=f1,width=5)
        self.action_lt.place(x=260-xv,y=262)
        self.action_lt['values']=[1,2,3]

        self.cal_date = Calendar(panel2, selectmode = 'day',
               year = 2022, month = 12,
               day = 18)

        self.cal_date.place(x=260-xv,y=312)

        self.bt_save_ord=Button(panel2,text="SAVE",font=f1,width=10)
        self.bt_save_ord.place(x=200-xv,y=512)
        self.bt_clear_ord=Button(panel2,text="CLEAR",font=f1,width=10)
        self.bt_clear_ord.place(x=320-xv,y=512)

    def Display_order(self):

        columns=["Ord_ID","CID","Name","Weight","No_Of_Shirt","No_Of_Pants","Date"]

        tree=ttk.Treeview(self.panel2,columns=columns,show='headings')
        tree.place(x=460,y=200)

        vsb = ttk.Scrollbar(self.panel2, orient="vertical", command=tree.yview)
        vsb.place(x=1005,y=200,height=225)

        tree.configure(yscrollcommand=vsb.set)

        for i in columns:
            tree.heading(i,text=i)
        tree.column("#0",anchor=CENTER, stretch=NO, width=0)
        tree.column(columns[0],anchor=CENTER, stretch=NO, width=50)
        tree.column(columns[1],anchor=CENTER, stretch=NO, width=50)
        tree.column(columns[2],anchor=W, stretch=NO, width=100)
        tree.column(columns[3],anchor=CENTER, stretch=NO, width=60)
        tree.column(columns[4],anchor=CENTER, stretch=NO, width=80)
        tree.column(columns[5],anchor=CENTER, stretch=NO, width=80)
        tree.column(columns[6],anchor=CENTER, stretch=NO, width=120)


        for i in db().Order_Data_list():
            tree.insert('', END, values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))



    def Clear_order_add(self):

        self.name_lt.set('')
        self.wet.delete(0,'end')
        self.no_of_shirt.delete(0,'end')
        self.no_of_pants.delete(0,'end')
        self.action_lt.set('')

    def Validate_before_inserting_order(self):
        name_lt=self.name_lt.get()
        wet=self.wet.get()
        no_of_shirt=self.no_of_shirt.get()
        no_of_pants=self.no_of_pants.get()
        action_lt=self.action_lt.get()
        cal=self.cal_date.get_date()
        dt=datetime.datetime.strptime(cal,'%m/%d/%y')
        dt=dt.strftime('%d-%b-%y')

        #If user not entered no_shirt then take it as 0
        if no_of_shirt=='' :
            no_of_shir=0

        if no_of_pants=='' :
            no_of_pants=0

        #Checking user entered minimum info or not
        if (name_lt=='' or wet=='' or action_lt==''):
            messagebox.showerror("Error Box", "Name,Weight,Action should not be blank!")
        else:
            db().Order_insert(name_lt,wet,no_of_shirt,no_of_pants,action_lt,dt)
            self.Clear_order_add()
            messagebox.showinfo("Message Box", "Data Successfully Saved!")

    def Add_Billing_design(self):

        bcol='grey'

        root=self.root
        panel3=PanedWindow(root,width=1030,height=620,bg=bcol)
        panel3.place(x=230,y=10)
        self.panel3=panel3

        f1=10

        self.opt=ttk.Combobox(panel3,font=f1,width=20)
        self.opt.place(x=260,y=10)
        self.opt['values']=['cid','Name','order_id','Weight','Date','No_of_Shirt','No_of_Pants']
        self.opt.set('cid')

        self.serch_box=Entry(panel3,font=10,width=20)
        self.serch_box.place(x=480,y=10)


    def Display_billing(self,event):
        print("Run")
        f1=self.opt.get()
        f2=self.serch_box.get()
        columns=["Ord_ID","CID","Name","Weight","No_Of_Shirt","No_Of_Pants","Date"]

        tree=ttk.Treeview(self.panel3,columns=columns,show='headings')
        tree.place(x=460,y=200)

        vsb = ttk.Scrollbar(self.panel3, orient="vertical", command=tree.yview)
        vsb.place(x=1005,y=200,height=225)

        tree.configure(yscrollcommand=vsb.set)

        for i in columns:
            tree.heading(i,text=i)
        tree.column("#0",anchor=CENTER, stretch=NO, width=0)
        tree.column(columns[0],anchor=CENTER, stretch=NO, width=50)
        tree.column(columns[1],anchor=CENTER, stretch=NO, width=50)
        tree.column(columns[2],anchor=W, stretch=NO, width=100)
        tree.column(columns[3],anchor=CENTER, stretch=NO, width=60)
        tree.column(columns[4],anchor=CENTER, stretch=NO, width=80)
        tree.column(columns[5],anchor=CENTER, stretch=NO, width=80)
        tree.column(columns[6],anchor=CENTER, stretch=NO, width=120)


        for i in db().Order_Data_list_filter(f1,f2):
            tree.insert('', END, values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

    def ending(self):
        self.bt_save.configure(command=self.Validate_before_inserting_cust)
        self.bt_clear.configure(command=self.Clear_cust_add)
        self.bt_clear_ord.configure(command=self.Clear_order_add)
        self.bt_save_ord.configure(command=self.Validate_before_inserting_order)

       
        self.bt_add_cust.configure(command=self.Custome_main)
        self.bt_add_order.configure(command=self.Order_main)
        self.bt_bill.configure(command=self.billing_final)
        self.bt_report.configure(command=self.billing_final)
        self.serch_box.bind("<KeyRelease>",self.Display_billing)

    def Order_main(self):
        self.Add_order_design()
        self.Display_order()
        self.ending()
    def billing_final(self):
        self.Add_Billing_design()
        self.Display_billing
        self.ending()
    def Custome_main(self):
        self.Add_cust_design()
        self.Display_cust()
        self.ending()
    def Report_design(self):
        bcol='grey'

        root=self.root
        panel3=PanedWindow(root,width=1030,height=620,bg=bcol)
        panel3.place(x=230,y=10)

        self._lt=ttk.Combobox(self.panel2,font=f1,width=5)
        self.action_lt.place(x=260,y=262)
        self.action_lt['values']=[1,2,3]

        report1=PanedWindow(root,width=1030,height=620,bg=bcol)
        report1.place(x=230,y=10)


d=Design()
d.Menu_design()
d.Display_design()
d.Custome_main()
d.Order_main()

d.ending()

mainloop()
