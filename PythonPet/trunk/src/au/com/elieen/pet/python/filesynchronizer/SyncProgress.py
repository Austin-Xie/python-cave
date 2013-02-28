'''
Created on 2012-12-26

@author: Austin
'''


from tkinter import *


#def go(mainWindow):
#    wdw = Toplevel()
#    wdw.geometry('+400+400')
#    text = Text(wdw)
#    text.insert(END, "XIE\n")
#    text.insert(INSERT, "jlsjfldsf\n")
#    text.pack()
#   
#    wdw.wm_transient(mainWindow)
#    wdw.grab_set()
#    mainWindow.wait_window(wdw)
#    # print 'done!'
#    return wdw

class SyncProgress:
    def __init__(self, parentWindow, callbackTask):
        wdw = Toplevel()
        wdw.geometry('+400+400')
        mf = Frame(wdw)
        mf.columnconfigure(0, pad=3, weight=1)
        mf.rowconfigure(0, pad=3, weight=1)
        mf.rowconfigure(1, pad=3)
        
        self.text = Text(mf)
        self.text.grid(row=0, column=0, sticky=N+S+W+E)
#        self.text.pack()
        btn = Button(mf, text="Close", command=wdw.destroy)
        btn.grid(row=1, column=0, sticky=E)
       
        wdw.wm_transient(parentWindow)
        wdw.grab_set()
#        parentWindow.wait_window(wdw)
        print('done!')
        mf.pack()
#        parentWindow.mainloop()
#        callbackTask[0](callbackTask[1], callbackTask[2], callbackTask[3], self.logProgress)
    
    def logProgress(self, message):
        print("log message")
        self.text.insert(END, message + "\n")
    
    
