from tkinter import Tk
from tkinter import Frame
from tkinter import Button
from tkinter import Text
from tkinter import Menu

from tkinter import END
from tkinter import SEL
from tkinter import INSERT

from src.action import Action
from src.core import Core

class TE:
    def __init__(self):
        self.root = Tk()
        self.actions = Action(root=self.root)
        self.cores = Core()

        self.screensize = "400x600" # default screen size

        self.filename = ""
        self.savepath = ""

        self.tabs = None

    #========== Command callback ==========#
    #---------- Files menu bar callback ----------#
    def newfile_callback(self, event=None):
        if self.tabs == None:
            self.root.title("Untitled* - Text Editor")
            self.filename = "untitled.txt"
            self.tabs = self.actions.newTabs()
        else:
            self.closewidget_callback()
            self.tabs = None
            self.newfile_callback()

    def openfile_callback(self, event=None):
        if self.tabs == None:
            path = self.actions.askOpenFile()
            names = self.cores.get_filename(path)[0]
            self.root.title(names + " - Text Editor")

            self.filename = path
            self.savepath = path
            content = self.cores.readfile(path=self.filename)

            self.tabs = self.actions.newTabs(content=content)
        else:
            self.closewidget_callback()
            self.tabs = None
            self.openfile_callback()

    def savefile_callback(self, event=None):
        if self.tabs != None:
            if self.savepath == "":
                self.savepath = self.actions.askSaveFile()
            
            print (self.savepath)
            names = self.cores.get_filename(self.savepath)[0]
            self.root.title(names + " - Text Editor")

            self.cores.writeFile(self.savepath, self.tabs.get("1.0", END))

    def saveasfile_callback(self, event=None):
        if self.tabs != None:
            self.savepath = self.actions.askSaveFile()
            print (self.savepath)
            names = self.cores.get_filename(self.savepath)[0]
            self.root.title(names + " - Text Editor")

            self.cores.writeFile(self.savepath, self.tabs.get("1.0", END))
    
    def closewidget_callback(self, event=None):
        if self.tabs != None:
            self.tabs.pack_forget()

    def quit_callback(self, event=None):
        self.root.destroy()

    #---------- Edit menu bar callback ----------#
    def undo_callback(self, event=None):
        if self.tabs != None:
            self.tabs.event_generate("<<Undo>>")

    def reundo_callback(self, event=None):
        if self.tabs != None:
            self.tabs.event_generate("<<Redo>>")
    
    def cuttext_callback(self):
        if self.tabs != None:
            self.tabs.event_generate("<<Cut>>")

    def copytext_callback(self):
        if self.tabs != None:
            self.tabs.event_generate("<<Copy>>")

    def pastetext_callback(self):
        if self.tabs != None:
            self.tabs.event_generate("<<Paste>>")

    def selectall_callback(self, event=None):
        if self.tabs != None:
            self.tabs.tag_add(SEL, "1.0", END)
            self.tabs.mark_set(INSERT, "1.0")
            self.tabs.see(INSERT)

    #---------- Help menu bar callback ----------#
    def about_callback(self):
        self.actions.about()

    #---------- Get screen size ----------#
    def get_screen_size(self):
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.screensize = str(width) + "x" + str(height)
        return width, height

    #---------- Set menubar ----------#
    def set_menubar(self):
        menubar = Menu(self.root)
        #---------- Files menu ----------#
        files = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=files)
        files.add_command(label="New file", command=self.newfile_callback)
        files.add_command(label="Open file", command=self.openfile_callback)
        files.add_command(label="Save", command=self.savefile_callback)
        files.add_command(label="Save as", command=self.saveasfile_callback)
        files.add_separator()
        files.add_command(label="Close window", command=self.closewidget_callback)
        files.add_command(label="Quit", command=self.quit_callback)
        #---------- CTRL + N (New tabs) ----------#
        self.root.bind("<Control-n>", self.newfile_callback)
        self.root.bind("<Control-N>", self.newfile_callback)
        #---------- CTRL + O (Open file) ----------#
        self.root.bind("<Control-o>", self.openfile_callback)
        self.root.bind("<Control-O>", self.openfile_callback)
        #---------- CTRL + S (Save file) ----------#
        self.root.bind("<Control-s>", self.savefile_callback)
        self.root.bind("<Control-S>", self.savefile_callback)
        #---------- CTRL + Shift + S (Save as file) ----------#
        self.root.bind("<Control-Shift-s>", self.saveasfile_callback)
        self.root.bind("<Control-Shift-S>", self.saveasfile_callback)
        #---------- CTRL + W (Close window) ----------#
        self.root.bind("<Control-w>", self.closewidget_callback)
        self.root.bind("<Control-W>", self.closewidget_callback)
        #---------- CTRL + Q (Quit) ----------#
        self.root.bind("<Control-q>", self.quit_callback)
        self.root.bind("<Control-Q>", self.quit_callback)

        #---------- Edit menu ----------#
        edits = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edits)
        edits.add_command(label="Undo", command=self.undo_callback)

        edits.add_command(label="Reundo", command=self.reundo_callback)
        edits.add_separator()
        edits.add_command(label="Cut", command=self.cuttext_callback)
        edits.add_command(label="Copy", command=self.copytext_callback)
        edits.add_command(label="Paste", command=self.pastetext_callback)
        edits.add_command(label="Select all", command=self.selectall_callback)
        #---------- CTRL + Z (Undo) ----------#
        self.root.bind("<Control-z>", self.undo_callback)
        self.root.bind("<Control-Z>", self.undo_callback)
        #---------- CTRL + Shift + Z (Redo) ----------#
        self.root.bind("<Control-Shift-z>", self.reundo_callback)
        self.root.bind("<Control-Shift-Z>", self.reundo_callback)
        #---------- CTRL + A (Select All) ----------#
        self.root.bind("<Control-a>", self.selectall_callback)
        self.root.bind("<Control-A>", self.selectall_callback)

        #---------- Help menu ----------#
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about_callback)

        self.root.config(menu=menubar)

    #---------- Setup window ----------#
    def setup(self):
        self.get_screen_size()

        self.root.title("Text Editor")
        self.root.geometry(self.screensize)

        self.set_menubar()
        
    def main(self):
        self.root.mainloop()