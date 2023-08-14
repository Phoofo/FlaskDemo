# from tkinter import Tk
# # 导入 对话框控件
# from tkinter import messagebox
#
# # 创建主窗口
# root = Tk()
#
# # 定义回调函数，当用户点击窗口x退出时，执行用户自定义的函数
# def QueryWindow():
#     # 显示一个警告信息，点击确后，销毁窗口
#     if messagebox.showwarning("警告", "出现了一个错误"):
#         # 这里必须使用 destory()关闭窗口
#         root.destroy()
#
# # 使用协议机制与窗口交互，并回调用户自定义的函数
# root.protocol('WM_DELETE_WINDOW', QueryWindow)
# root.mainloop()


import tkinter as tk

# 定义窗口
window = tk.Tk()
window.title('窗口实列demo03')
window.geometry('300x300')

# 定义回调函数
def callback():
    print("执行回调函数", "你好，来自江南的你")

# 点击执行按钮
button = tk.Button(window, text="执行", command=callback)
button.pack()
window.mainloop()
