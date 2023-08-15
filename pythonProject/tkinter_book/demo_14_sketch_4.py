from tkinter import *
from tkinter import ttk

"画布-选择颜色且线条拖动变粗plus"
# 创建一个 Tkinter 窗口
root = Tk()
# 创建一个带有滚动条的画布。
h = ttk.Scrollbar(root, orient=HORIZONTAL)
v = ttk.Scrollbar(root, orient=VERTICAL)
canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview

canvas.grid(column=0, row=0, sticky=(N, W, E, S))
h.grid(column=0, row=1, sticky=(W, E))
v.grid(column=1, row=0, sticky=(N, S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
# 定义全局变量 lastx 和 lasty，用于存储上一个鼠标位置的坐标。
lastx, lasty = 0, 0


# 定义函数 xy(event) 用于获取鼠标点击的坐标，并更新 lastx 和 lasty 的值。
def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)


# 定义函数 setColor(newcolor) 用于设置绘图的颜色。该函数会修改全局变量 color 的值，并根据选定的颜色突出显示颜色选择框。
def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', 'paletteSelected')
    canvas.itemconfigure('palette', outline='white')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
    canvas.itemconfigure('paletteSelected', outline='#999999')


# 定义函数 addLine(event) 用于绘制线条。它会获取当前鼠标位置的坐标，并在画布上创建一条线段，线段的颜色为选定的颜色。
def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
    lastx, lasty = x, y


# 定义函数 doneStroke(event) 用于结束绘制线条时，将线条的宽度恢复为默认值。
def doneStroke(event):
    canvas.itemconfigure('currentline', width=1)


# 绑定鼠标事件，使得在鼠标点击、拖动和释放时触发对应的函数。
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", doneStroke)
# 创建几个颜色选择框，并为每个框绑定点击事件，以便选择不同的颜色。
id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

setColor('black')
# 设置默认的绘图颜色为黑色，并将颜色选择框的宽度设置为 5 像素。
canvas.itemconfigure('palette', width=5)
root.mainloop()
