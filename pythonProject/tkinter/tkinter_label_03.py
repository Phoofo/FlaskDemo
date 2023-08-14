from tkinter import *

# 创建主窗口
win = Tk()
win.config(bg='#8DB6CD')
win.title("标签实例demo03")
win.geometry('400x300')

text = "圈圈点点圈圈 淅淅沥沥依依稀稀"
msg = Message(win, text=text, width=60, font=('微软雅黑', 10, 'bold'))
msg.pack(side=LEFT)
# 开始程序循环
win.mainloop()
