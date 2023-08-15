from tkinter import *
from tkinter import ttk

"进度条案例"
root = Tk()


# 开始按钮的回调函数
def start():
    # 将按钮文本修改为"Stop"，并将按钮的回调函数设置为stop
    b.configure(text='Stop', command=stop)
    l['text'] = 'Working...'  # 修改标签的文本为"Working..."
    global interrupt;
    interrupt = False
    root.after(1, step)  # 使用root.after方法在1毫秒后执行step函数


# 停止按钮的回调函数
def stop():
    global interrupt;
    interrupt = True  # 将全局变量interrupt设置为True


# step函数，用于更新进度条和执行操作
def step(count=0):
    p['value'] = count  # 设置进度条的值为count
    if interrupt:
        result(None)  # 如果interrupt为True，则调用result函数，并传入None作为参数，用于结束操作
        return
    root.after(100)  # 等待100毫秒
    if count == 20:  # 判断操作是否完成（这里以count等于20作为判断条件）
        result(42)  # 调用result函数，并传入42作为参数，用于显示操作结果
        return
    root.after(1, lambda: step(count + 1))  # 递归调用step函数，并将count加1


# result函数，用于处理操作结果
def result(answer):
    p['value'] = 0  # 将进度条的值设置为0
    b.configure(text='Start', command=start)  # 将按钮文本修改为"Start"，并将按钮的回调函数设置为start
    l['text'] = "Answer: " + str(answer) if answer else "No Answer"  # 根据answer是否存在，修改标签的文本


# 创建Frame控件
f = ttk.Frame(root);
f.grid()
# 创建开始按钮
b = ttk.Button(f, text="Start!", command=start);
b.grid(column=1, row=0, padx=5, pady=5)
# 创建用于显示结果的Label控件
l = ttk.Label(f, text="No Answer")
l.grid(column=0, row=0, padx=5, pady=5)
# 创建进度条
p = ttk.Progressbar(f, orient="horizontal", mode="determinate", maximum=20);
p.grid(column=0, row=1, padx=5, pady=5)

root.mainloop()
