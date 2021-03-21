sector_frame.pack()
        sname = []
        pps = []
        print(sid, sqty, sname, pps)

        for i in range(0, len(sid)):
            row = Frame(self)
            idl = Text(row, height=2, width=15)
            idl.insert(END, sid[i])
            idl.pack(side=LEFT)
            namel = Text(row, height=2, width=15)
            namel.insert(END, sname[i])
            namel.pack(side=LEFT)
            pricel = Text(row, height=2, width=15)
            pricel.insert(END, pps[i])
            pricel.pack(side=LEFT)
            qtyl = Text(row, height=2, width=15)
            qtyl.insert(END, sqty[i])
            qtyl.pack(side=LEFT)
            row.pack()