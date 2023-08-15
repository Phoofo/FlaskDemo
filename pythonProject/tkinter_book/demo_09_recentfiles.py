from tkinter import *
import glob
import os.path

"菜单案例--最近的文件"
root = Tk()


# 打开文件的回调函数
def openFile(f):
    print(f)


# 获取最近打开的文件列表
recent_files = glob.glob(os.getcwd() + '/*.py')
# 创建菜单栏
menubar = Menu(root)
root['menu'] = menubar

# 创建文件菜单和编辑菜单
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')

# 创建最近打开菜单
menu_recent = Menu(menu_file)
menu_file.add_cascade(menu=menu_recent, label='Open Recent')
# 在最近打开菜单中添加文件列表
for f in recent_files:
    menu_recent.add_command(label=os.path.basename(f), command=lambda: openFile(f))

root.mainloop()
