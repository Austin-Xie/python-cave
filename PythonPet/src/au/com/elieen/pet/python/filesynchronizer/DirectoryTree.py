'''
Created on 2012-12-25

@author: Austin
'''
import os

from tkinter import *
import glob
from tkinter.ttk import Style, Separator, Treeview

# Constants for formatting file sizes
KB = 1024.0
MB = KB * KB
GB = MB * KB

def populate_tree(tree, node):
    if tree.set(node, "type") != 'directory':
        return

    path = tree.set(node, "fullpath")
    print(path)
    tree.delete(*tree.get_children(node))

    parent = tree.parent(node)
    special_dirs = [] if parent else glob.glob('.') + glob.glob('..')
    print(special_dirs)
    print(os.listdir(path))

    for p in special_dirs + os.listdir(path):
        ptype = None
        p = os.path.join(path, p).replace('\\', '/')
        if os.path.isdir(p): ptype = "directory"
        elif os.path.isfile(p): ptype = "file"

        fname = os.path.split(p)[1]
        id = tree.insert(node, "end", text=fname, values=[p, ptype])

        if ptype == 'directory':
            if fname not in ('.', '..'):
                tree.insert(id, 0, text="dummy")
                tree.item(id, text=fname)
        elif ptype == 'file':
            size = os.stat(p).st_size
            tree.set(id, "size", "%d bytes" % size)


def populate_roots(tree):
    dir = os.path.abspath('.').replace('\\', '/')
    node = tree.insert('', 'end', text=dir, values=[dir, "directory"])
    populate_tree(tree, node)


def update_tree(event):
    tree = event.widget
    populate_tree(tree, tree.focus())


def formatSize(size):
    if size >= GB:
        return '{:,.1f} GB'.format(size / GB)

    if size >= MB:
        return '{:,.1f} MB'.format(size / MB)

    if size >= KB:
        return '{:,.1f} KB'.format(size / KB)

    return '{} bytes'.format(size)