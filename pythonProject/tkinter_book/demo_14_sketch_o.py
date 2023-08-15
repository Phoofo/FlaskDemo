from tkinter import *

"画布-封装版"


# 定义一个名为 Sketchpad 的画布类，继承自 Canvas 类。
class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        # 在 Sketchpad 类的构造函数 __init__ 中，首先调用父类的构造函数初始化画布。
        # 然后通过绑定鼠标事件 <Button-1> 和 <B1-Motion> 来设置鼠标点击和拖动时的事件处理函数。
        super().__init__(parent, **kwargs)
        self.bind("<Button-1>", self.save_posn)
        self.bind("<B1-Motion>", self.add_line)

    def save_posn(self, event):
        # 在事件处理函数 save_posn 中，获取鼠标点击位置的坐标，
        # 并将其保存在实例变量 lastx 和 lasty 中。
        self.lastx, self.lasty = event.x, event.y

    def add_line(self, event):
        # 在事件处理函数 add_line 中，根据鼠标拖动的位置和上次保存的位置，
        # 创建一条线段，并添加到画布中。然后将当前位置保存为新的起始位置。
        self.create_line((self.lastx, self.lasty, event.x, event.y))
        self.save_posn(event)


# 创建一个 Tkinter 窗口 root。
root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# 使用 grid 方法将画布放置在窗口中，
# 并使用布局选项 sticky=(N, W, E, S) 将画布填充整个窗口。
sketch = Sketchpad(root)
sketch.grid(column=0, row=0, sticky=(N, W, E, S))

root.mainloop()
