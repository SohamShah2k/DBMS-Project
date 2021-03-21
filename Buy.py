import tkinter as tk
from tkinter import *
from tkinter import ttk
from all_imports import mysql as ms
buysql = ms()
buymycursor = buysql.mycursor
buydb = buysql.mydb
class Buy(tk.Frame):
    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        menu = Frame(self)
        l = Label(menu, text="Menu: ").pack(side=LEFT)
        bd = Button(menu, text="Dashboard", command=lambda: obj.display_page(obj.DashBoard)).pack(side = LEFT)
        bs = Button(menu, text="Sell", command=lambda: obj.display_page(obj.Sell)).pack(side = LEFT)
        bw = Button(menu, text="Watchlist", command=lambda: obj.display_page(obj.Watchlist)).pack(side = LEFT)
        menu.pack()
        buymycursor.execute("select stock_name from Stocks ")
        stock_list=[]
        for row in buymycursor.fetchall():
            stock_list.append(row[0])
        #print(stock_list)
        stock_frame = Frame(self)
        l2 = Label(stock_frame,text="Select stock you want to buy: ").pack(side = LEFT)
        stock_sel = StringVar()
        def set_price(stock_sel):
            x = stock_sel.get()
            sql = "select pps,quantity from Stocks where stock_name = \"{}\" "
            buymycursor.execute(sql.format(x))
            qp = buymycursor.fetchall()[0]
            global price
            price= qp[0]
            qty = qp[1]
            out1.delete(1.0, END)
            out1.insert(END, price)
            out2.delete(1.0, END)
            out2.insert(END, qty)

        sel1 = ttk.Combobox(stock_frame,values = stock_list,textvariable = stock_sel).pack(side = LEFT)
        print(stock_sel)
        price_frame = Frame(self)
        selb = Button(stock_frame,text = "Select",command = lambda : set_price(stock_sel)).pack(side = LEFT)
        l3 = Label(price_frame,text="Price of the stock: ").pack(side = LEFT)
        out1 = Text(price_frame,height = 2, width =15)
        out1.pack(side = LEFT)
        stock_frame.pack()
        price_frame.pack()
        qty_avail_frame = Frame(self)
        l3 = Label(qty_avail_frame, text="Quantity of the stock available: ").pack(side=LEFT)
        out2 = Text(qty_avail_frame, height=2, width=15)
        out2.pack(side=LEFT)
        qty_avail_frame.pack()
        buy_frame = Frame(self)
        l4 = Label(buy_frame,text = "How many stocks do you want to buy: ").pack(side = LEFT)
        quant = IntVar()
        qty = Entry(buy_frame,textvariable = quant).pack(side=LEFT)
        buy_frame.pack()
        confirm_frame = Frame(self)
        l5 = Label(confirm_frame,text = "Total ammount: ").pack(side = LEFT)
        out3 = Text(confirm_frame, height=2, width=15)
        out3.pack(side = LEFT)
        conbut = Button(confirm_frame,text = "Total ammount",command = lambda : out3.insert(END,(price*quant.get()))).pack()
        confirm_frame.pack()
        buy_button = Button(self,text=" BUY ",command=lambda: print(obj.uname))
        #print(obj.uname)