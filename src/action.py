from tkinter import Text
from tkinter import Frame
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showinfo

from tkinter import END

from src.core import Core

class Action:
    def __init__(self, root=None):
        self.root = root

        self.cores = Core()

        self.filetypes = [("All files", "*"), ("Text file", "*.txt")]

    def newTabs(self, content=""):
        w = (self.root.winfo_screenwidth()-10)
        h = (self.root.winfo_screenheight()-50)

        texts = Text(self.root, width=w, height=h)
        texts.pack()
        texts.configure(undo=True, maxundo=-1, autoseparators=True)
        texts.focus()

        if content != "":
            texts.insert("1.0", content)
        return texts

    def about(self):
        info_dict = self.cores.get_info()["info"]
        showinfo("About!", "TE is a very simple Text Editor\n\nAuthor: " + info_dict["author"] + "\nVersion: " + str(info_dict["version"]) + "\nSource: " + info_dict["source"])

    def askOpenFile(self):
        openfile = askopenfilename(filetypes=self.filetypes)
        if openfile != "":
            return openfile

    def askSaveFile(self):
        savefile = asksaveasfilename(filetypes=self.filetypes)
        if savefile != "":
            return savefile