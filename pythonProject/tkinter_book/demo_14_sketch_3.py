from tkinter import *

"画布-选择颜色且线条拖动变粗"
# 定义全局变量
lastx, lasty = 0, 0
color = "black"  # 默认颜色为黑色


# 定义函数 xy(event) 用于获取鼠标点击的坐标，并更新 lastx 和 lasty 的值。
def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y


# 选择颜色
def setColor(newcolor):
    global color
    color = newcolor
    # 清除所有标记为 'paletteSelected' 的标签。这是为了确保在选择新颜色时只有一个矩形框被突出显示。
    canvas.dtag('all', 'paletteSelected')
    # 将所有带有标签 'palette' 的矩形框的描边设置为白色。这是为了重置之前选择的颜色矩形框的描边颜色。
    canvas.itemconfigure('palette', outline='white')
    # 将标签 'paletteSelected' 添加到带有标签 'palette%s' % color 的矩形框。这样，当前选定的颜色矩形框就被突出显示。
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
    # 将所有带有标签 'paletteSelected' 的矩形框的描边颜色设置为灰色，以突出显示当前选定的颜色矩形框。
    canvas.itemconfigure('paletteSelected', outline='#999999')


def addLine(event):
    global lastx, lasty
    # 在画布上创建一条线段，颜色为当前选定的颜色，宽度为 5 像素，
    # 标签为 'currentline'。这条线段是用户正在绘制的线段。
    canvas.create_line((lastx, lasty, event.x, event.y), fill=color, width=5, tags='currentline')
    lastx, lasty = event.x, event.y


def doneStroke(event):
    # 设置标签为 'currentline' 的线段的宽度为 1 像素。
    # 这是为了在用户完成绘制后，将线段宽度恢复为默认值。
    canvas.itemconfigure('currentline', width=1)


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", doneStroke)

id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

root.mainloop()
