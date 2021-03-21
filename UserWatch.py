import tkinter as tk
from tkinter import *
from all_imports import mysql as ms
uwsql = ms()
uwmycursor = uwsql.mycursor
uwdb = uwsql.mydb
class UserWatch(tk.Frame):
    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        menu = Frame(self)
        l = Label(menu, text="Menu: ").grid(row = 0, column = 0 )
        bb = Button(menu, text="Buy", command=lambda: obj.display_page(obj.Buy)).grid(row = 0, column = 1 )
        bd = Button(menu, text="Dashboard", command=lambda: obj.display_page(obj.DashBoard)).grid(row = 0, column = 2 )
        bs = Button(menu, text="Sell", command=lambda: obj.display_page(obj.Sell)).grid(row = 0, column = 3 )
        bw = Button(menu, text="Watchlist", command=lambda: obj.display_page(obj.Watchlist)).grid(row = 0, column = 4 )
        menu.pack()
        uwmycursor.execute("select user_id from users where user_name = \"{}\"".format(obj.uname))
        stock_list = []
        uid = uwmycursor.fetchone()[0]
        #print(uid)
        uwmycursor.execute("select stock_id,quantity from user_has where user_id = {}".format(uid))
        sid = []
        sqty = []
        for i in uwmycursor.fetchall():
            sid.append(i[0])
            sqty.append(i[1])
        sname = []
        pps = []
        for i in sid:
            uwmycursor.execute("select stock_name,pps from stocks where stock_id = {}".format(i))
            for j in uwmycursor.fetchall():
                sname.append(j[0])
                pps.append(j[1])
        #print(sid, sqty,sname,pps)
        table = Frame(self)
        row = Frame(table)
        idl = Text(row, height=2, width=15)
        idl.insert(END, "Stock ID")
        idl.pack(side=LEFT)
        namel = Text(row, height=2, width=25)
        namel.insert(END, "Stock Name")
        namel.pack(side=LEFT)
        pricel = Text(row, height=2, width=15)
        pricel.insert(END, "Stock Name")
        pricel.pack(side=LEFT)
        qtyl = Text(row, height=2, width=15)
        qtyl.insert(END, "Stock Name")
        qtyl.pack(side=LEFT)
        row.pack()
        for i in range (0,len(sid)):
            row = Frame(table)
            idl = Text(row, height=2, width=15)
            idl.insert(END,sid[i])
            idl.pack(side = LEFT)
            namel= Text(row, height=2, width=25)
            namel.insert(END,sname[i])
            namel.pack(side = LEFT)
            pricel= Text(row, height=2, width=15)
            pricel.insert(END,pps[i])
            pricel.pack(side = LEFT)
            qtyl= Text(row, height=2, width=15)
            qtyl.insert(END,sqty[i])
            qtyl.pack(side = LEFT)
            row.pack()
        table.pack()