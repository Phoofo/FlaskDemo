from tkinter import *
from tkinter import ttk

"会话框案例-在会话框关闭以前阻止应用程序的操作"

root = Tk()

# 创建一个用于交互的输入框，使用 grid() 方法放置在窗口上
ttk.Entry(root).grid()


def dismiss():
    # 解除对对话框的掌控权
    dlg.grab_release()
    # 销毁对话框
    dlg.destroy()


dlg = Toplevel(root)  # 创建一个顶级窗口作为对话框
ttk.Button(dlg, text="确认", command=dismiss).grid()  # 在对话框上创建一个按钮，点击后调用 dismiss() 函数
dlg.protocol("WM_DELETE_WINDOW", dismiss)  # 拦截关闭按钮，调用 dismiss() 函数
dlg.transient(root)  # 将对话框与主窗口关联
dlg.wait_visibility()  # 等待对话框窗口显示出来，确保能够正常抓取输入事件
dlg.grab_set()  # 确保所有输入都被定向到对话框
dlg.wait_window()  # 阻塞直到对话框被销毁

root.mainloop()
