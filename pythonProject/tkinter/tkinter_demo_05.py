import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser

tkinter.messagebox.showinfo("showinfo", "this is an info msg")
tkinter.messagebox.showwarning("showinfo", "this is an info msg")
tkinter.messagebox.showerror("showinfo", "this is an info msg")

isYes = tkinter.messagebox.askyesno("askyesno", "continue")
print(isYes)
isOK = tkinter.messagebox.askokcancel("askobcancel", "OK?")
print(isOK)

isYesNoCancel = tkinter.messagebox.askyesnocancel("sfs", "OK?")
print(isYesNoCancel)

name = tkinter.simpledialog.askstring("ssf", "sdfsdf ")
print(name)

age = tkinter.simpledialog.askinteger("df", "sdf")
print(age)