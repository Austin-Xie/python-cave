'''
Created on 2012-12-25

@author: Austin
'''
import os

from tkinter import *
from tkinter.ttk import Style, Separator, Treeview

from au.com.elieen.pet.python.filesynchronizer.DirectoryTree import *
from au.com.elieen.pet.python.filesynchronizer.EventHandler import *

import filecmp

class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.eventHandler = EventHandler(self)
        self.parent = parent
        self.initUI()
        

    def initUI(self):

        self.parent.title("File synchronizer")

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        # 3X3 Grid
        self.columnconfigure(0, pad=3, weight=1)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3, weight=1)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3, weight=1)
        self.rowconfigure(2, pad=3)

        ltf = Frame(self)
        ltf.grid(row=0, column=0, sticky=W+E)
        # 1X4 Grid
        ltf.columnconfigure(0, pad=3)
        ltf.columnconfigure(1, pad=3, weight=1)
        ltf.columnconfigure(2, pad=3, weight=1)
        ltf.columnconfigure(3, pad=3)
        ltf.rowconfigure(0, pad=3, weight=1)
        llabel = Label(ltf, text="Direcotry:")
        llabel.grid(row=0, column=0, sticky=W+E)
        self.leftDir = Entry(ltf)
        self.leftDir.bind('<Return>', self.eventHandler.leftDirChanged)
        self.leftDir.grid(row=0, column=1, columnspan=2, sticky=W + E)
        # Left browse button
        lBtn = Button(ltf, text="browse...", command=self.eventHandler.chooseLeftDirectory)
        lBtn.grid(row=0, column=3, sticky=E)

        rtf = Frame(self)
        rtf.grid(row=0, column=2, sticky=W+E)
        # 1X4 Grid
        rtf.columnconfigure(0, pad=3)
        rtf.columnconfigure(1, pad=3, weight=1)
        rtf.columnconfigure(2, pad=3, weight=1)
        rtf.columnconfigure(3, pad=3)
        rtf.rowconfigure(0, pad=3, weight=1)
        rlabel = Label(rtf, text="Direcotry:")
        rlabel.grid(row=0, column=0, sticky=W+E)
        self.rightDir = Entry(rtf)
        self.rightDir.bind('<Return>', self.eventHandler.rightDirChanged)
        self.rightDir.grid(row=0, column=1, columnspan=2, sticky=W + E)
        # Right browse button
        rBtn = Button(rtf, text="browse...", command=self.eventHandler.chooseRightDirectory)
        rBtn.grid(row=0, column=3,  sticky=E)

        # Left TreeView frame
        ltf1 = Frame(self)
        ltf1.grid(row=1, column=0, sticky=N+S+W+E)
        # 2 X 2 Grid
        ltf1.columnconfigure(0, pad=3, weight=1)
        ltf1.columnconfigure(1, pad=3)
        ltf1.rowconfigure(0, pad=3, weight=1)
        ltf1.rowconfigure(1, pad=3)
        self.ltree = Treeview(ltf1, columns=("fullpath", "type", "size"), displaycolumns="size")
        self.ltree.grid(row=0, column=0, sticky=E + W + S + N)
        lysb = ttk.Scrollbar(ltf1, orient=VERTICAL, command= self.ltree.yview)
        lysb.grid(row=0, column=1, sticky=NS)
        lxsb = ttk.Scrollbar(ltf1, orient=HORIZONTAL, command= self.ltree.xview)
        lxsb.grid(row=1, column=0, columnspan=3, sticky=EW)
        self.ltree['yscroll'] = lysb.set
        self.ltree['xscroll'] = lxsb.set
        self.ltree.heading("#0", text="Directory Structure", anchor='w')
        self.ltree.heading("size", text="File Size", anchor='w')
        self.ltree.column("size", stretch=0, width=100)
        self.ltree.bind('<<TreeviewOpen>>', self.eventHandler.openTree)

        # Right TreeView frame
        rtf1 = Frame(self)
        rtf1.grid(row=1, column=2, sticky=N+S+W+E)
        # 2 X 2 Grid
        rtf1.columnconfigure(0, pad=3, weight=1)
        rtf1.columnconfigure(1, pad=3)
        rtf1.rowconfigure(0, pad=3, weight=1)
        rtf1.rowconfigure(1, pad=3)
        self.rtree = Treeview(rtf1, columns=("fullpath", "type", "size"), displaycolumns="size")
        self.rtree.grid(row=0, column=0,  sticky=E + W + S + N)
        rysb = ttk.Scrollbar(rtf1, orient=VERTICAL, command= self.ltree.yview)
        rysb.grid(row=0, column=1, sticky=NS)
        rxsb = ttk.Scrollbar(rtf1, orient=HORIZONTAL, command= self.ltree.xview)
        rxsb.grid(row=1, column=0, columnspan=3, sticky=EW)
        self.rtree['yscroll'] = rysb.set
        self.rtree['xscroll'] = rxsb.set
        self.rtree.heading("#0", text="Directory Structure", anchor='w')
        self.rtree.heading("size", text="File Size", anchor='w')
        self.rtree.column("size", stretch=0, width=100)
        self.rtree.bind('<<TreeviewOpen>>', self.eventHandler.openTree)
       
        # Command Button frame
        btnf = Frame(self)
        btnf.grid(row=1, column=1, sticky=W+E+N+S)
        btnf.columnconfigure(0, pad=3, weight=1)
        btnf.rowconfigure(0, pad=3, weight=1)
        btnf.rowconfigure(1, pad=3, weight=1)
        btnf.rowconfigure(2, pad=3, weight=1)
        btnf.rowconfigure(3, pad=3, weight=1)
        btnf.rowconfigure(4, pad=3, weight=1)
        btnf.rowconfigure(5, pad=3, weight=1)
        btnf.rowconfigure(6, pad=3, weight=1)
        btnf.rowconfigure(7, pad=3, weight=1)
        l2rBtn = Button(btnf, text="Left >> Right", command=self.eventHandler.left2RightSynch)
        l2rBtn.grid(row=1, column=0, sticky=W+E)
        
        syncBtn = Button(btnf, text="<< Sync >>", command=self.eventHandler.leftRightSynch)
        syncBtn.grid(row=3, column=0, sticky=W+E)
        
        r2lBtn = Button(btnf, text="Left << Right", command=self.eventHandler.right2LeftSynch)
        r2lBtn.grid(row=5, column=0, sticky=W+E)
        
        closeBtn = Button(self, text="Close", command=self.eventHandler.quit)
        closeBtn.grid(row=2, column=2, sticky=E)
        
        self.pack(fill=BOTH, expand=1)

def autoscroll(sbar, first, last):
    """Hide and show scrollbar as needed."""
    first, last = float(first), float(last)
    if first <= 0 and last >= 1:
        sbar.grid_remove()
    else:
        sbar.grid()
    sbar.set(first, last)

def main():
    root = Tk()
    root.geometry("800x600")
    app = MainWindow(root)
    root.mainloop()  


if __name__ == '__main__':
    main()
