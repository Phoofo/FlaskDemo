import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
# 设置窗口的标题
window.title('按钮实例demo02')
# 设置并调整窗口的大小、位置
window.geometry('400x300+300+200')


# 当按钮被点击的时候执行click_button()函数
def click_button():
    # 使用消息对话框控件，showinfo()表示温馨提示
    messagebox.showinfo(title='温馨提示', message='以为江南情不变 明明越爱越错相恋多痛苦')


# 点击按钮时执行的函数
button = tk.Button(window, text='点击前往', bg='#7CCD7C', width=20, height=5, command=click_button).pack()

# 显示窗口
window.mainloop()
