from tkinter import *


class MenuDemo:

    def __init__(self):
        root = Tk()

        # create a popup menu
        self.menu = Menu(root, tearoff=0)
        self.menu.add_command(label="Undo", command=self.hello)
        self.menu.add_command(label="Redo", command=self.hello)

        # create a canvas
        self.frame = Frame(root, width=512, height=512)
        self.frame.pack()

        # attach popup to canvas
        self.frame.bind("<Button-1>", self.popup)
        # < Bi - Motion > 当拖拽小部件的时候
        # < Button - i > Button - 1、Button - 2、Button - 3
        # 表示左键、中间键、右键点击
        # < ButtonReleased - i > 当释放鼠标的时候
        # < Double - Button - i > 当双击鼠标的时候
        # < Enter > 当鼠标光圈进入小部件的时候
        # < Key > 当敲击一个键时候
        # < Leave > 当鼠标光圈离开小部件的时候
        # < Return > 当敲击“Enter”键时候，可以将键盘任意一个键和一个事件绑定
        # < Shift + A > 当敲击Shif + A的时候，可以和Alt、Control等组和
        # < Triple - Button - i > 点击鼠标3次的时候

        root.mainloop()

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)

    def hello(self):
        print("hello!")


MenuDemo()