from Tkinter import *
from tkFileDialog import askopenfile, asksaveasfile

class App(object):

    def __init__(self, root):


        self.lbl2 = Label(root, text="To:")
        self.lbl2.pack(side=LEFT)

        self.txt2 = Entry(root)
        self.txt2.config(font=("Arial", 12))
        self.txt2.pack(side=LEFT)

        self.lbl1 = Label(root, text="Type")
        self.lbl1.pack(side=LEFT)

        self.txt1 = Text(root, borderwidth=3, relief="sunken", height=10, width=55)
        self.txt1.config(font=("Arial", 12), undo=True, wrap='word')
        self.txt1.pack(side=LEFT)

        scrollb1 = Scrollbar(root, command=self.txt1.yview)
        scrollb1.pack(side=LEFT, fill=BOTH)
        self.txt1['yscrollcommand'] = scrollb1.set



    def open_file(self):
        f = askopenfile(defaultextension=".txt", filetypes=[("All Types", ".*")])
        if not f:
            return
        self.txt1.delete(1.0, END)
        self.txt1.insert(END, f.read())
        f.close()

    def file_save(self):
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if not f:
            return
        f.write(self.txt1.get(1.0, END))
        f.close()

root = Tk()
app = App(root)
menubar = Menu(root)
root.configure(menu=menubar)
root.wm_title("Compose New Message | Shake")

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save", command=app.file_save)
filemenu.add_command(label='Open', command=app.open_file)
filemenu.add_command(label='Exit', command=root.quit)



root.mainloop()
