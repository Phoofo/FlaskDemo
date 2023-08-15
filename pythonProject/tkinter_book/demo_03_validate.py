from tkinter import *
from tkinter import ttk

import re

"输入框校验案例"
# 创建根窗口对象
root = Tk()
# 存储错误信息的文本变量
errmsg = StringVar()
# 格式错误的消息
formatmsg = "Zip should be ##### or #####-####"


def check_zip(newval, op):
    # 清空错误信息
    errmsg.set('')
    # 使用正则表达式验证zip代码格式是否正确
    valid = re.match('^[0-9]{5}(\-[0-9]{4})?$', newval) is not None
    # 设置按钮状态，只有当zip代码格式正确时启用按钮
    btn.state(['!disabled'] if valid else ['disabled'])
    if op == 'key':
        ok_so_far = re.match('^[0-9\-]*$', newval) is not None and len(newval) <= 10
        if not ok_so_far:
            # 设置格式错误的消息
            errmsg.set(formatmsg)
        return ok_so_far
    elif op == 'focusout':
        if not valid:
            # 设置格式错误的消息
            errmsg.set(formatmsg)
    return valid


# 注册 zip验证函数
check_zip_wrapper = (root.register(check_zip), '%P', '%V')
# 存储zip代码的动态字符串
zip = StringVar()
# 创建Frame框架
f = ttk.Frame(root)
# 指定框架在根窗口中的位置
f.grid(column=0, row=0)

# 创建两个标签控件，一个是"Name:"标签，另一个是"Zip:"标签
ttk.Label(f, text='Name:').grid(column=0, row=0, padx=5, pady=5)
ttk.Entry(f).grid(column=1, row=0, padx=5, pady=5)
ttk.Label(f, text='Zip:').grid(column=0, row=1, padx=5, pady=5)
# 创建输入框，并绑定验证选项和验证命令
#
# validate参数值说明
# focus	当 Entry 组件获得或失去焦点的时候验证
# focusin	当 Entry 组件获得焦点的时候验证
# focusout	当 Entry 组件失去焦点的时候验证
# key	当输入框被编辑的时候验证
# all	当出现上边任何一种情况的时候验证
# none	 默认不启用验证功能，需要注意的是这里是字符串的 'none'
e = ttk.Entry(f, textvariable=zip, validate='all', validatecommand=check_zip_wrapper)
# 将输入框放置在适当的位置
e.grid(column=1, row=1, padx=5, pady=5)
# 创建按钮
btn = ttk.Button(f, text="Process")
# 将按钮放置在适当的位置
btn.grid(column=2, row=1, padx=5, pady=5)
# 设置按钮状态为禁用
btn.state(['disabled'])
# 创建标签控件
msg = ttk.Label(f, font='TkSmallCaptionFont', foreground='red', textvariable=errmsg)
# 将标签控件放置在适当的位置
msg.grid(column=1, row=2, padx=5, pady=5, sticky='w')
# 启动主事件循环，使应用程序开始运行
root.mainloop()
