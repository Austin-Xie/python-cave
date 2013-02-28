'''
Created on 2012-12-25

@author: Austin
'''

import os

from au.com.elieen.pet.python.filesynchronizer.DirectoryTree import *
from au.com.elieen.pet.python.filesynchronizer.FileSyncUtil import *
from au.com.elieen.pet.python.filesynchronizer.SyncProgress import *

from tkinter import filedialog

import filecmp

class EventHandler:
    def __init__(self, mainWindow):
        # Put body here
        print("Init Called")
        self.window = mainWindow

    def quit(self):
        self.window.parent.destroy()


    def leftDirChanged(self, event):
        # Left Dir Changed
        tree = self.window.ltree
        leftDir = event.widget
        self._setTree(tree, leftDir)
    
    def rightDirChanged(self, event):
        # Right Dir Changed
        tree = self.window.rtree
        rightDir = event.widget
        self._setTree(tree, rightDir)

    def _setTree(self, tree, directory):
        path = directory.get().replace('\\', '/')
        print(path)
        valid = (os.path.exists(path) and os.path.isdir(path))
        if (valid):
            self._clearTree(tree)
            parent = tree.insert('', END, text=path, values=[path, 'directory'])
            # add the files and sub-directories
            populate_tree(tree, parent) #, path, os.listdir(path))
        else:
            print("invalid path")
            self._clearTree(tree)
    
    def chooseLeftDirectory(self):
        folder = filedialog.askdirectory(title="Please select your directory")
        print(folder)
        if (folder):
            self.window.leftDir.delete(0, END)
            self.window.leftDir.insert(0, folder)
            self._setTree(self.window.ltree, self.window.leftDir)
    

    def chooseRightDirectory(self):
        folder = filedialog.askdirectory(title="Please select your directory")
        print(folder)
        if (folder):
            self.window.rightDir.delete(0, END)
            self.window.rightDir.insert(0, folder)
            self._setTree(self.window.rtree, self.window.rightDir)

    def _clearTree(self, tree):
        rootNode = tree.get_children()
        if (rootNode):
            tree.delete(rootNode)
    
    def openTree(self, event):
#        tree = event.widget
        update_tree(event)
    
    def leftRightSynch(self):
        syncProgress = SyncProgress(self.window, [synchronize, self.window.leftDir.get(), self.window.rightDir.get(), TWO_WAY])
        synchronize(self.window.leftDir.get(), self.window.rightDir.get(), TWO_WAY, syncProgress.logProgress)
    
    def left2RightSynch(self):
        synchronize(self.window.leftDir.get(), self.window.rightDir.get(), ONE_WAY, self.log)
    
    def right2LeftSynch(self):
        synchronize(self.window.rightDir.get(), self.window.leftDir.get(), ONE_WAY, self.log)
        
    def log(self, message):
        print(message)