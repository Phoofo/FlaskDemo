from tkinter import *
"菜单案例-弹出使菜单栏"
root = Tk()

# 创建菜单
menu = Menu(root)

# 添加菜单项
for i in ('One', 'Two', 'Three'):
    menu.add_command(label=i)
# 根据操作系统判断绑定的事件
if root.tk.call('tk', 'windowingsystem') != 'aqua':  # Windows和Linux
    # 当点击鼠标右键时，弹出菜单
    root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))
else:  # macOS
    # 当点击鼠标右键或按下Control键加左键时，弹出菜单
    root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
    root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
root.mainloop()
