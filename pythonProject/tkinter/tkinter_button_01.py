import tkinter as tk

# 创建窗口
window = tk.Tk()


# 设置回调函数
def callback():
    print("花瓣也许听见 迷途恋人们")

# 使用按钮控件调用函数
b = tk.Button(window, text="花瓣也许听见 迷途恋人们", command=callback).pack()
# 显示窗口
tk.mainloop()
