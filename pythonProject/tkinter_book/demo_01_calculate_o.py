from tkinter import *
from tkinter import ttk

"这是一个使用Tkinter创建一个简单的小应用程序，将输入的英尺值转换为米值。"


# "封装成面向对象"
# FeetToMeters类来封装应用程序的界面和功能。
# 通过使用类，可以将代码组织得更加清晰和易于管理，提供了更好的可重用性和扩展性，使得代码更具结构化和面向对象的特点。
# 类可以将相关的属性和方法组合在一起，并且可以创建多个实例来处理不同的情况。
# 类可以更好地封装数据和行为，并且可以实现更好的代码组织和结构化。
# 通过定义适当的属性和方法，可以使代码更易读、可维护和可测试。


class FeetToMeters:
    # FeetToMeters类有一个构造函数__init__，用于初始化应用程序的界面和各个控件。
    def __init__(self, root):
        root.title("Feet to Meters")
        # 创建一个框架，并设定内边距
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        # 设置主窗口的权重
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        # 创建一个StringVar类型的变量feet，用于保存用户输入的英尺值
        self.feet = StringVar()
        # 创建一个文本输入框Entry，并将其与feet(英尺)变量绑定
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        # 将文本框放置在mainframe中的指定位置
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        # 创建一个StringVar类型的变量meters，用于显示转换后的米值
        self.meters = StringVar()
        # 创建一个标签，并将其与meters变量绑定
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        # 创建一个按钮，点击时触发calculate函数进行英尺到米的转换
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)
        # 在框架中创建其他一些标签，用于显示文字内容
        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
        # 配置框架中的所有组件的外边距
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        # 设置焦点在文本框上，使得用户可以直接输入英尺值
        feet_entry.focus()
        # 绑定回车键事件，当按下回车键时会执行calculate方法进行转换
        root.bind("<Return>", self.calculate)

    # 定义calculate函数，用于进行英尺到米的转换
    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass


root = Tk()
FeetToMeters(root)
root.mainloop()
