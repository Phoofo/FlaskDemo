from tkinter import *

"画布-最基础"
# 定义全局变量 lastx 和 lasty
lastx, lasty = 0, 0


# xy 函数用于处理鼠标点击事件，它获取事件对象的 x 和 y 坐标，
# 并将其存储在全局变量 lastx 和 lasty 中。这样，在绘制线条时，就可以使用上一次点击的坐标作为起始点。
def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y


# addLine 函数用于处理鼠标拖动事件，它通过调用 create_line 方法在画布上绘制线条。
# 线条的起始点是先前保存的 lastx 和 lasty 值，终止点是当前事件对象的 x 和 y 坐标。
# 同时，它还更新了 lastx 和 lasty 的值，以便下次绘制取得正确的起始点。
def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# 创建画布组件
canvas = Canvas(root)
# 将画布放置在根窗口上，并使用布局管理器将其铺满整个窗口
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

# xy 函数,addLine 函数这两个函数组合在一起，实现了在画布上绘制连续线条的功能。
# 通过捕捉鼠标点击和拖动事件，并保存相应的坐标信息，可以与用户交互并实时更新绘图结果。
# 绑定鼠标左键点击事件，调用 xy 函数
canvas.bind("<Button-1>", xy)
# 绑定鼠标左键拖动事件，调用 addLine 函数
canvas.bind("<B1-Motion>", addLine)

root.mainloop()
