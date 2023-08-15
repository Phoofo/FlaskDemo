# 导入Tkinter库和ttk模块
from tkinter import *
from tkinter import ttk

"这是一个使用Tkinter创建一个简单的小应用程序，将输入的英尺值转换为米值。"


# 这版代码是面向过程的，以一个顶级函数的形式组织的，所有的操作都是在全局命名空间中进行的。
# 没有类的概念，所有的操作都直接写在主程序中。


# 定义calculate函数，用于进行英尺到米的转换
def calculate(*args):
    try:
        value = float(feet.get())  # 获取输入的英尺值
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)  # 将英尺值转换为米值并设置到meters变量中
    except ValueError:
        pass


# 创建了一个窗口，并在窗口中放置了标签、输入框和按钮等组件。
root = Tk()
root.title("Feet to Meters")

# 创建一个框架，并设定内边距
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# 设置主窗口的权重
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# 创建一个StringVar类型的 动态字符串 变量，用于存储用户输入的英尺值
feet = StringVar()

# 在框架中创建一个文本输入框Entry，并将其与feet(英尺)变量绑定
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# 再创建一个StringVar类型的 动态字符串 变量，用于显示转换后的米值
meters = StringVar()
# 在框架中创建一个标签，并将其与meters变量绑定
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# 创建一个按钮，点击时触发calculate函数进行英尺到米的转换
ttk.Button(mainframe, text="计算", command=calculate).grid(column=3, row=3, sticky=W)

# 在框架中创建其他一些标签，用于显示文字内容
ttk.Label(mainframe, text="请输入：").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="英尺").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="等价于").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="米尺").grid(column=3, row=2, sticky=W)

# 配置框架中的所有组件的外边距
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# 设置焦点在文本输入框上
feet_entry.focus()

# 绑定回车键事件，当按下回车键时触发calculate函数进行转换
root.bind("<Return>", calculate)

# 要绑定其他键，你可以使用不同的事件字符串来替换"<Return>"。以下是一些常用的键盘事件的绑定方式：
#
# <Key>：捕捉任何按键事件。
# <KeyPress>：捕捉按键被按下事件。
# <KeyRelease>：捕捉按键被释放事件。
# <KeyPress-A>：捕捉"A"键被按下事件。
# <KeyPress-Shift_L>：捕捉左Shift键被按下事件。
# <Control-KeyPress-c>：捕捉按下组合键Ctrl+C事件。
# 字母A绑定calculate事件
# root.bind("<KeyPress-a>", calculate) # 此处是输入框，单独点击字母A，不会触发calculate事件
# 组合键Ctrl+S绑定calculate事件s
root.bind("<Control-KeyPress-s>", calculate)
# ====================================

# 进入主事件循环
root.mainloop()
