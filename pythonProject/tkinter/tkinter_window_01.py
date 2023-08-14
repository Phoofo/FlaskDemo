import tkinter as tk

root = tk.Tk()
root.title('Python窗体显示实例')  # 设置窗口标题。
# root.iconbitmap('moon.ico')  # 设置窗口左上角的图标。
# root.geometry('720x720')  # 自定义设置窗口位置，这里的乘号不是 * ，而是小写英文字母 x

"获取电脑屏幕尺寸大小"
window_x = root.winfo_screenwidth()
window_y = root.winfo_screenheight()

"设置窗口大小参数"
WIDTH = 500
HEIGHT = 350

"获取窗口左上角的X, Y坐标，用来设置窗口的放置位置为屏幕的中间。"
x = (window_x - WIDTH) / 2
y = (window_y - HEIGHT) / 2

# root.geometry(f'{WIDTH}x{HEIGHT}+{int(x)}+{int(y)}')  # 设置窗口尺寸与窗口的放置位置为屏幕的中间。
# root.resizable(width=True, height=True)  # 设置是否禁止调整窗口的宽和高。
# root.minsize(250, 250)  # 设置窗口的最小尺寸。
# root.maxsize(800, 600)  # 设置窗口的最大尺寸。

# win_width = root.winfo_width()  # 获取窗口宽度（单位：像素）
# win_height = root.winfo_height()  # 获取窗口高度（单位：像素）
# x = root.winfo_x()  # 获取窗口左上角的 x 坐标（单位：像素）
# y = root.winfo_y()  # 获取窗口左上角的 y 坐标（单位：像素）
# print(win_width, win_height, x, y)

# root.aspect(4, 3, 4, 3)
# aspect(minNumer=None, minDenom=None, maxNumer=None, maxDenom=None)
# -- 控制该窗口的宽高比（width:height）
# -- 宽高比限制在：minNumer / minDenom ~ maxNumer / maxDenom
# -- 如果忽略参数，则返回一个 4 元组表示当前的限制（如果有的话）


# root.attributes("-toolwindow", 1)            # 工具栏样式。参数1：没有最大化/最小化按钮。
# root.attributes("-topmost", 1)               # 窗口置顶显示。
# root.overrideredirect(True)                 #参数True，隐藏窗口标题栏。即不显示窗口标题和最大化、最小化、关闭按钮。

# root.state("iconic")                        # 隐藏窗口,可以在任务管理器中查看，相当于在后台运行了。
# root.state("normal")                        # 设置为普通窗口。
# root.withdraw()                             # 从屏幕中移除窗口。相当于影藏窗口了（并没有销毁）。
# root.deiconify()							  # 使窗口重新显示在电脑屏幕上。
# root.attributes("-fullscreen", True)        # 全屏显示，用 Windows 热键 “ Alt+F4 ” 关闭这个全屏的Tkinter窗口。
root.attributes("-alpha", 0.8)  # 设置窗口的透明度 0.8, 参数为 0 到 1。
"alpha"
"1.（Windows，Mac）控制窗口的透明度"
"2. 1.0 表示不透明，0.0 表示完全透明"
"3. 该选项并不支持所有的系统，对于不支持的系统，Tkinter 绘制一个不透明（1.0）的窗口"

"Toplevel有和顶层窗口一样的属性。"
# top_window = tk.Toplevel(root)  # 创建第二个窗口
# top_window.title('Python顶部窗体显示实例')  # 设置窗口标题。
# top_window.geometry(f'260x200+{int(x) + 50}+{int(y) + 50}')  # 自定义设置窗口位置
# top_window.transient(root)  # 使弹出窗口一直置于 root 窗口之上。

tk.mainloop()
