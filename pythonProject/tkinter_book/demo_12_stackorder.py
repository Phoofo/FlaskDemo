from tkinter import *
from tkinter import ttk

"root.after() 案例-延时覆盖"
root = Tk()
# 创建两个标签控件
little = ttk.Label(root, text="红红火火")
bigger = ttk.Label(root, text="山山水水")

# 将小标签放在(0, 0)位置
little.grid(column=0, row=0)
# 将大标签放在(0, 0)位置
bigger.grid(column=0, row=0)
# 在2秒后将执行后面的方法
# lambda 表达式用来创建一个匿名函数，在函数中调用 lift() 方法将小标签提升到最上层。
root.after(2000, lambda: little.lift())
root.mainloop()
