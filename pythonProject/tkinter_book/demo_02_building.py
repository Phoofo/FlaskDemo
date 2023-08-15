from tkinter import *
from tkinter import ttk

"bind()函数为标签绑定事件"
root = Tk()
label = ttk.Label(root, text="Starting...")
label.grid()

# <Enter>事件：当 鼠标进入标签 时，使用lambda函数将标签的文本设置为"Moved mouse inside"。
label.bind('<Enter>', lambda e: label.configure(text='我进来了'))
# <Leave>事件：当 鼠标离开标签 时，将标签的文本设置为"Moved mouse outside"。
label.bind('<Leave>', lambda e: label.configure(text='我又出来了'))
# <1>事件：当 左键点击标签 时，将标签的文本设置为"Clicked left mouse button"。
label.bind('<1>', lambda e: label.configure(text='左键点击标签'))
# <Double-1>事件：当 双击左键 时，将标签的文本设置为"Double clicked"。
label.bind('<Double-1>', lambda e: label.configure(text='双击左键'))
# <B3-Motion>事件：当 按住鼠标右键并拖动 时，将标签的文本设置为"right button drag to X,Y"，其中X和Y是鼠标的坐标值。
label.bind('<B3-Motion>', lambda e: label.configure(text='按住鼠标右键并拖动' % (e.x, e.y)))
root.mainloop()
