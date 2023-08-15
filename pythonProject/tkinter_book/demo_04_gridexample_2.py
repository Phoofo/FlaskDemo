from tkinter import *
from tkinter import ttk

"网格布局案例_2"
root = Tk()
# 创建一个框架，作为容器
content = ttk.Frame(root, padding=(3, 3, 12, 12))
# 在容器中创建一个带边框的矩形区域框架
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
# 创建一个标签控件，显示文本"Name"
namelbl = ttk.Label(content, text="Name")
# 创建一个文本输入框
name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(True)
twovar.set(False)
threevar.set(True)
# onvalue	通过设置 onvalue 的值来自定义选中状态的值。
# offvalue	通过设置 offvalue 的值来自定义未选中状态的值。
# 创建复选框
one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
# 创建两个按钮控件，显示文本"Okay"和"Cancel"
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

# 使用网格布局将控件放置在适当的位置，设置对齐方式和边距
content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

# 设置根窗口的列和行权重
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# 设置容器的列权重
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
# 设置容器的行权重
content.rowconfigure(1, weight=1)

root.mainloop()
