from tkinter import *
from tkinter import ttk

"Scale控件案例"
root = Tk()

# 创建label控件并绑定变量
num = StringVar()
ttk.Label(root, textvariable=num).grid(column=0, row=0, sticky='we')

# 创建了一个空的Label控件manual，用于手动更新通过Scale控件的回调函数来更新其内容。
manual = ttk.Label(root)
# 将manual控件放置在根窗口的第0列第1行，使用sticky参数指定对齐方式为水平方向的西和东。
manual.grid(column=0, row=1, sticky='we')


# 定义了一个名为update_lbl的回调函数，用于更新manual控件的内容。
def update_lbl(val):
    manual['text'] = "Scale at " + val


# 创建了一个Scale控件实例scale，并将num变量与之关联。
# 设置Scale控件的方向为水平，长度为200，范围从1.0到100.0。
# 指定了一个回调函数update_lbl，用于在Scale控件的值发生变化时更新manual控件的内容。
scale = ttk.Scale(root, orient='horizontal', length=200, from_=1.0, to=100.0, variable=num, command=update_lbl)
# 将scale控件放置在根窗口的第0列第2行，使用sticky参数指定对齐方式为水平方向的西和东。
scale.grid(column=0, row=2, sticky='we')
# 设置Scale控件的初始值。这里为20
scale.set(20)

root.mainloop()
