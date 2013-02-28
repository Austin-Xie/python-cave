'''
Created on 2012-12-26

@author: Austin
'''
from tkinter import *

root = Tk()

def go():
    wdw = Toplevel()
    wdw.geometry('+400+400')
    
    mf = Frame(wdw)
    mf.columnconfigure(0, pad=3)
    mf.rowconfigure(0, pad=3, weight=1)
    mf.rowconfigure(1, pad=3)
    
        
    text = Text(mf)
    text.grid(row=0, column=0, sticky=N+S+W+E)
#        self.text.pack()
    btn = Button(mf, text="Close")
    btn.grid(row=1, column=0, sticky=E)
       
    wdw.wm_transient(root)
    wdw.grab_set()
#        parentWindow.wait_window(wdw)
    print('done!')
    mf.pack()
    
    
#    text = Text(wdw)
#    text.insert(END, "XIE\n")
#    text.insert(INSERT, "jlsjfldsf\n")
#    text.pack()
#   
#    wdw.wm_transient(root)
#    wdw.grab_set()
#    root.wait_window(wdw)
#    # print 'done!'

Button(root, text='Go', command=go).pack()
Button(root, text='Quit', command=root.destroy).pack()

root.mainloop()
