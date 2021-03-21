import tkinter as tk

class dashboard(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self)

        window.pack(side="top", fill="both", expand=True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.pages = {}

        for F in (DashBoard, Buy, Sell,Watchlist):
            page = F(window, self)
            print(page)
            self.pages[F] = page

            page.grid(row=0, column=0, sticky="nsew")

        self.display_page(DashBoard)

    def display_page(self, cont):
        page = self.pages[cont]
        page.tkraise()


class DashBoard(tk.Frame):

    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        bb = tk.Button(self, text="Buy", command=lambda: obj.display_page(Buy)).pack()
        bs = tk.Button(self, text="Sell", command=lambda: obj.display_page(Sell)).pack()
        bw = tk.Button(self, text="Watchlist", command=lambda: obj.display_page(Watchlist)).pack()


class Buy(tk.Frame):

    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        bd = tk.Button(self, text="Dashboard", command=lambda: obj.display_page(DashBoard)).pack()
        bs = tk.Button(self, text="Sell", command=lambda: obj.display_page(Sell)).pack()
        bw = tk.Button(self, text="Watchlist", command=lambda: obj.display_page(Watchlist)).pack()


class Sell(tk.Frame):

    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        bb = tk.Button(self, text="Buy", command=lambda: obj.display_page(Buy)).pack()
        bd = tk.Button(self, text="Dashboard", command=lambda: obj.display_page(DashBoard)).pack()
        bw = tk.Button(self, text="Watchlist", command=lambda: obj.display_page(Watchlist)).pack()

class Watchlist(tk.Frame):

    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        bb = tk.Button(self, text="Buy", command=lambda: obj.display_page(Buy)).pack()
        bs = tk.Button(self, text="Sell", command=lambda: obj.display_page(Sell)).pack()
        bd = tk.Button(self, text="Dashboard", command=lambda: obj.display_page(DashBoard)).pack()

app = dashboard()
app.mainloop()