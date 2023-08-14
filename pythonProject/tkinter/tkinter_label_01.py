import tkinter as tk

win = tk.Tk()
win.title("标签实例demo01")
# win.geometry('400x200')

# 若内容是文字则以字符为单位，图像则以像素为单位
label = tk.Label(win, text="沿岸听清风扑面 面目便带着怀念", font=('宋体', 20, 'bold italic'), bg="#70f9fe",
                 # 设置标签内容区大小
                 width=30, height=5,
                 # 设置填充区距离、边框宽度和其样式（凹陷式）
                 padx=10, pady=15, borderwidth=10, relief="sunken")
label.pack()
win.mainloop()
