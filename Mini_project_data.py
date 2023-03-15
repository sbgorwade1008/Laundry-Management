import cx_Oracle


class Database:
    def __init__(self):
        self.con = cx_Oracle.connect('sanmeet/1008@127.0.0.1:1521/xe')
        self.cursor = self.con.cursor()
    def display_custdetail(self):
         con=self.con
         cursor=self.cursor

         x=cursor.execute("select * from l_billing")
         x=list(x)
         for i in x:
             print(i[0])

    def Connection_close(self):
        self.cursor.close()
        self.con.close()


    def Customer_key(self):
        con=self.con
        cursor=self.cursor
        x=cursor.execute('select max(cid) from l_customer')
        x=[i[0] for i in x]

        if x[0]==None :
            return 1
        else:
            return x[0]+1

        self.Connection_close()


    def Customer_insert(self,nam,mob,flt,lnd,dt):
        con=self.con
        cursor=self.cursor

        cursor.callproc('l_insert_customer',[self.Customer_key(),nam,mob,flt,lnd,dt])
        cursor.execute('commit')

        self.Connection_close()

        return 1

    def check_customer(self,nam,mob,flt,lnd,dt):
         '''This function will check customer all details are matching in db or not '''

         con=self.con
         cursor=self.cursor

         x=cursor.execute("select count(*) from l_customer where name='{}' and mob_no='{}' and flat_no='{}' and landmark='{}' and c_date='{}'".format(nam,mob,flt,lnd,dt))
         x=[i[0] for i in x]

         return x[0]

    def Order_key(self):
        con=self.con
        cursor=self.cursor
        x=cursor.execute('select max(order_id) from l_order')
        x=[i[0] for i in x]

        if x[0]==None :
            return 1
        else:
            return x[0]+1

        self.Connection_close()

    def Ord_cust_key(self,name):
        con=self.con
        cursor=self.cursor

        x=cursor.execute("select cid from l_customer where name='{}'".format(name))
        x=[i[0] for i in x]

        return x[0]

        self.Connection_close()
    def Order_insert(self,name,wet,sh,pt,act,dt):
        con=self.con
        cursor=self.cursor

        cursor.callproc('l_insert_order',[self.Order_key(),self.Ord_cust_key(name),wet,sh,pt,act,dt])
        cursor.execute('commit')

        self.Connection_close()

        return 1

    def Bill_Amount(self,oid):
        con=self.con
        cursor=self.cursor

        x=cursor.execute("select weight,no_of_shirt,no_of_pants,action from l_order where order_id={}".format(oid))
        lst=list(x)
        wet=lst[0][0]
        no_sh=lst[0][1]
        no_pt=lst[0][2]
        act=lst[0][3]

        y1=cursor.execute("select price from l_action")
        y1=list(y1)
        press_price=float(([i[0]for i in y1][1]))
        wash_price=float(([i[0]for i in y1][0]))

        res=0
        res1=0
        if act==1:
            res=wash_price*wet
            res1=0
            return res,res1
        elif act==2:
            res=0
            res1=(no_sh+no_pt)*press_price
            return res,res1
        else:
            res=wash_price*wet
            res1=(no_sh+no_pt)*press_price
            return res,res1

        self.Connection_close()

    def Billing_insert(self,oid,dt):
        con=self.con
        cursor=self.cursor
        val=self.Bill_Amount(oid)
        cursor.callproc('l_insert_billing',[oid,dt,val[0],val[1]])
        cursor.execute('commit')
        self.Connection_close()

        return 1
    def Name_list(self):
        con=self.con
        cursor=self.cursor

        x=cursor.execute("select name from l_customer")
        x=list(x)
        list1=[]
        for i in x:
            list1.append(i[0])
        self.Connection_close()
        return list1
    def Customer_list(self):
        con=self.con
        cursor=self.cursor

        x=cursor.execute("select * from l_customer")
        x=list(x)
        self.Connection_close()
        return x

    def Order_Data_list(self):
        con=self.con
        cursor=self.cursor

        x=cursor.execute("select o.order_id,o.cid,a.name,o.no_of_shirt,o.no_of_pants,o.action,o.ord_date from l_order o,l_customer a where a.cid=o.cid")
        x=list(x)
        self.Connection_close()
        return x
    def Order_Data_list_filter(self,f1,f2):
        con=self.con
        cursor=self.cursor

        x=cursor.execute("select o.order_id,o.cid,a.name,o.no_of_shirt,o.no_of_pants,o.action,o.ord_date from l_order o,l_customer a where a.cid=o.cid and o.{} like '%{}'".format(f1,f2))
        x=list(x)
        self.Connection_close()
        return x

if __name__=="__main__":
    try:
        d=Database()
        #d.Name_list()
        d.display_custdetail()
        #print(d.Billing_insert(3,'17-DEC-22'))

        #print(d.Order_insert('Sanmeet',3,4,4,2,"17-DEC-22"))
        #d.Customer_insert("Shubham",9096628042,924,"Vishal Nagar","17-DEC-22")
    except cx_Oracle.DatabaseError as e:
        print(e)

