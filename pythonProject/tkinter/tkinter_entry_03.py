import tkinter as tk

win = tk.Tk()
# 设置主窗口
win.geometry('250x100')
win.title("输入实例demo03")

win.resizable(0, 0)
# 新建文本标签
labe1 = tk.Label(win, text="账号：")
labe2 = tk.Label(win, text="密码：")
# grid()控件布局管理器，以行、列的形式对控件进行布局，后续会做详细介绍
labe1.grid(row=0)
labe2.grid(row=1)
# 为上面的文本标签，创建两个输入框控件
entry1 = tk.Entry(win)
entry2 = tk.Entry(win)
# 对控件进行布局管理，放在文本标签的后面
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
# 显示主窗口
win.mainloop()
