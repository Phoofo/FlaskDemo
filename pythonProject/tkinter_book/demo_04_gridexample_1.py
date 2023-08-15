from tkinter import *
from tkinter import ttk

"网格布局案例_1"

# 创建根窗口对象
root = Tk()
# 创建一个框架，作为容器
content = ttk.Frame(root)
# 在框架中创建一个带边框的矩形区域
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
# 创建一个标签控件，显示文本"Name"
namelbl = ttk.Label(content, text="Name")
# 创建一个文本输入框
name = ttk.Entry(content)
# 创建三个布尔类型的变量 用来控制Checkbutton多选框
onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
# 设置变量的初始值
onevar.set(True)
twovar.set(False)  # 默认不勾选
threevar.set(True)

# 创建一个复选框控件，显示文本"One"，绑定到变量onevar
one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
# 创建一个复选框控件，显示文本"Two"，绑定到变量twovar
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
# 创建一个复选框控件，显示文本"Three"，绑定到变量threevar
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
# 创建一个按钮，显示文本"Okay"
ok = ttk.Button(content, text="Okay")
# 创建一个按钮，显示文本"Cancel"
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0)  # 将容器框架放置在根窗口中的指定位置
frame.grid(column=0, row=0, columnspan=3, rowspan=2)  # 将矩形区域框架放置在容器框架中的指定位置，并占据多个网格单元
namelbl.grid(column=3, row=0, columnspan=2)  # 将"Name"标签控件放置在容器框架中的指定位置，并跨越多个网格单元
name.grid(column=3, row=1, columnspan=2)  # 将文本输入框放置在容器框架中的指定位置，并跨越多个网格单元
# 将复选框控件one,two,three 放置在容器框架中的指定位置
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
# 将按钮控件"Okay"，"Cancel"放置在容器框架中的指定位置
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.mainloop()
