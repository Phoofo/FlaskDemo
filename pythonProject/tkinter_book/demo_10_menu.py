from tkinter import *
from tkinter import ttk, messagebox

"菜单案例-剪切和查找"
root = Tk()
# 创建输入框
ttk.Entry(root).grid()
# 创建菜单栏
m = Menu(root)
m_edit = Menu(m)
m.add_cascade(menu=m_edit, label="Edit")
# 在编辑菜单中添加剪切和查找命令
m_edit.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))
m_edit.add_command(label="Find...", command=lambda: root.event_generate("<<OpenFindDialog>>"))
# 将菜单栏设置为根窗口的菜单
root['menu'] = m


# 查找对话框的回调函数
def launchFindDialog(*args):
    messagebox.showinfo("哈哈哈", "嘿嘿嘿")


# 绑定打开查找对话框事件到launchFindDialog函数
root.bind("<<OpenFindDialog>>", launchFindDialog)
root.mainloop()
