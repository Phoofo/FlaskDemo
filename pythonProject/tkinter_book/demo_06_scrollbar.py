from tkinter import *
from tkinter import ttk

"滚动条控件案例"

root = Tk()
# 创建了一个列表框实例l，设置列表框的高度为5。
l = Listbox(root, height=5)
# 将列表框放置在根窗口的第0列第0行，并使用sticky参数指定对齐方式为顶部、左侧、右侧和底部。
l.grid(column=0, row=0, sticky=(N, W, E, S))
# 创建了一个垂直方向的滚动条实例s，指定了滚动条与列表框之间的关联。
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
# 将滚动条放置在根窗口的第1列第0行，并使用sticky参数指定对齐方式为顶部和底部。
s.grid(column=1, row=0, sticky=(N, S))
# 将列表框的垂直滚动命令与滚动条相关联，以支持滚动功能。
l['yscrollcommand'] = s.set
# 创建了一个标签实例，并将其放置在根窗口的第0列第1行，跨越2列。
# 标签文本为 "Status message here"，并使用anchor参数指定对齐方式为左侧。
ttk.Label(root, text="Status message here", anchor=(W)).grid(column=0, columnspan=2, row=1, sticky=(W, E))
root.grid_columnconfigure(0, weight=1)  # 设置根窗口中第0列的宽度权重为1，使其可以自动调整大小。
root.grid_rowconfigure(0, weight=1)  # 设置根窗口中第0行的高度权重为1，使其可以自动调整大小。
for i in range(1, 101):
    l.insert('end', 'Line %d of 100' % i)
# 为列表框的交替行添加背景颜色。
for i in range(0, 100, 2):
    l.itemconfigure(i, background='#f0f0ff')
root.mainloop()
