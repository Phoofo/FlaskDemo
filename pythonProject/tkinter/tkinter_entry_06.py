from tkinter import *

# 创建窗体
win = Tk()
win.title("输入实例demo06_计算器")
win.geometry('300x300')

# 创建一个容器来包括其他控件
frame = Frame(win)


# 创建一个计算器
def calc():
    # 用户输入的表达式，计算结果后转换为字符串
    result = "= " + str(eval(expression.get()))
    # 将计算的结果显示在Label控件上
    label.config(text=result)


# 创建一个Label控件
label = Label(frame)
# 创建一个Entry控件
entry = Entry(frame)
# 读取用户输入的表达式
expression = StringVar()
# 将用户输入的表达式显示在Entry控件上
entry["textvariable"] = expression
# 创建-一个 Button控件.当用户输入完毕后，单击此按钮即计算表达式的结果
button1 = Button(frame, text=" = ", command=calc)
# 设置Entry控件为焦点所在
entry.focus()
frame.pack()
# Entry控件位于窗体的上方
entry.pack()
# Label控件位于窗体的左方
label.pack(side="left")
# Button控件位于窗体的右方
button1.pack(side="right")
# 开始程序循环
frame.mainloop()
