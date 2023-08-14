import tkinter as tk

win = tk.Tk()
# 设置主窗口
win.geometry('250x100')
win.title("输入实例demo02")
win.resizable(0, 0)
# 创建输入框控件
entry1 = tk.Entry(win)
# 放置输入框，并设置位置
entry1.pack(padx=20, pady=20)

entry1.delete(0, "end")
# 插入默认文本
entry1.insert(0, '比不起美丽照片得到那保护  到头来一天 秦淮干枯')
# 得到输入框字符串
print(entry1.get())
# 删除所有字符
# entry1.delete(0, tk.END)
win.mainloop()
