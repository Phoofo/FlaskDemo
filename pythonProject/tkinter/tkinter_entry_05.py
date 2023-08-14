import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
# 设置主窗口
win.geometry('250x200+250+200')
win.title("输入实例demo05")
win.resizable(0, 0)
# 新建文本标签
labe1 = tk.Label(win, text="账号：")
labe2 = tk.Label(win, text="密码：")
labe1.grid(row=0)
labe2.grid(row=1)
# 创建动字符串
Dy_String = tk.StringVar()


# 创建验证函数
def check(strings, reason, id):
    if entry1.get() == "root":
        messagebox.showinfo("输入正确")
        print(strings, reason, id)
        return True
    else:
        messagebox.showwarning("输入不正确")
        print(strings, reason, id)
        return False


# 对验证函数进行注册
CheckTest = win.register(check)

# 使用验证参数 validata,参数值为 focusout 当失去焦点的时验证输入框内容是否正确
entry1 = tk.Entry(win, textvariable=Dy_String, validate="focusout", validatecommand=(CheckTest, '%P', '%V', '%W'))
entry2 = tk.Entry(win)

# 对控件进行布局管理，放在文本标签的后面
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
win.mainloop()
