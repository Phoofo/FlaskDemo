from tkinter import *
from tkinter import ttk

"指定国家发送礼物案例"
root = Tk()
# list数据定义
# 初始化国家简称，国家，国家代码，礼物数据集：
countrycodes = (
    'ar', 'au', 'be', 'br', 'ca', 'cn', 'dk', 'fi', 'fr', 'gr', 'in', 'it', 'jp', 'mx', 'nl', 'no', 'es', 'se', 'ch')
countrynames = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
                'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
                'Sweden', 'Switzerland')
populations = {'ar': 41000000, 'au': 21179211, 'be': 10584534, 'br': 185971537, \
               'ca': 33148682, 'cn': 1323128240, 'dk': 5457415, 'fi': 5302000, 'fr': 64102140, 'gr': 11147000, \
               'in': 1131043000, 'it': 59206382, 'jp': 127718000, 'mx': 106535000, 'nl': 16402414, \
               'no': 4738085, 'es': 45116894, 'se': 9174082, 'ch': 7508700}
gifts = {'card': 'Greeting card', 'flowers': 'Flowers', 'nastygram': 'Nastygram'}
# ===============================================================================================

# 定义一个包含一些国家代码和国家名称的元组。
cnames = StringVar(value=countrynames)
# 定义了用于存储选择的礼物、发送信息和状态信息的变量。
gift = StringVar()
sentmsg = StringVar()
statusmsg = StringVar()


# 定义一个函数showPopulation，
# 当在列表框中选择项改变时调用。该函数用于显示选定国家的人口，并清除发送礼物的消息。
def showPopulation(*args):
    idxs = lbox.curselection()
    if len(idxs) == 1:
        idx = int(idxs[0])
        code = countrycodes[idx]
        name = countrynames[idx]
        popn = populations[code]
        statusmsg.set("The population of %s (%s) is %d" % (name, code, popn))
    sentmsg.set('')


# 定义一个函数sendGift，当双击列表框中的项目、
# 点击"Send Gift"按钮或按下回车键时调用。该函数用于发送礼物，并提供发送成功的反馈
def sendGift(*args):
    idxs = lbox.curselection()
    if len(idxs) == 1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = countrynames[idx]
        # 并提供发送成功的反馈
        sentmsg.set("Sent %s to leader of %s" % (gifts[gift.get()], name))


# 创建一个ttk.Frame实例作为内容窗格，并将其放置在根窗口上。
c = ttk.Frame(root, padding=(5, 5, 12, 0))
# 将内容窗格放置在根窗口的第0列第0行，并使用 sticky 参数指定对齐方式为顶部、左侧、右侧和底部。
c.grid(column=0, row=0, sticky=(N, W, E, S))
# 设置根窗口中第0列的宽度权重为1，使其可以自动调整大小
root.grid_columnconfigure(0, weight=1)
# 设置根窗口中第0行的高度权重为1，使其可以自动调整大小。
root.grid_rowconfigure(0, weight=1)

# 创建列表框、标签和按钮等小部件，并将它们放置在内容窗格中。
lbox = Listbox(c, listvariable=cnames, height=5)
lbl = ttk.Label(c, text="Send to country's leader:")
# 创建礼物的单选框
g1 = ttk.Radiobutton(c, text=gifts['card'], variable=gift, value='card')
g2 = ttk.Radiobutton(c, text=gifts['flowers'], variable=gift, value='flowers')
g3 = ttk.Radiobutton(c, text=gifts['nastygram'], variable=gift, value='nastygram')
# Send按钮绑定事件
send = ttk.Button(c, text='Send Gift', command=sendGift, default='active')
sentlbl = ttk.Label(c, textvariable=sentmsg, anchor='center')
status = ttk.Label(c, textvariable=statusmsg, anchor=W)

# 布局代码
lbox.grid(column=0, row=0, rowspan=6, sticky=(N, S, E, W))
lbl.grid(column=1, row=0, padx=10, pady=5)
g1.grid(column=1, row=1, sticky=W, padx=20)
g2.grid(column=1, row=2, sticky=W, padx=20)
g3.grid(column=1, row=3, sticky=W, padx=20)
send.grid(column=2, row=4, sticky=E)
sentlbl.grid(column=1, row=5, columnspan=2, sticky=N, pady=5, padx=5)
status.grid(column=0, row=6, columnspan=2, sticky=(W, E))
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)

# 绑定事件处理程序，使得当选择列表框中的项改变、
# 双击列表框中的项或按下回车键时，执行相应的函数。
lbox.bind('<<ListboxSelect>>', showPopulation)
lbox.bind('<Double-1>', sendGift)
root.bind('<Return>', sendGift)

# 为列表框的交替行添加背景颜色。
for i in range(0, len(countrynames), 2):
    lbox.itemconfigure(i, background='#f0f0ff')

# 设置默认的礼物选项，
gift.set('card')
# 清空发送消息和状态消息，
sentmsg.set('')
statusmsg.set('')
# 并选择列表框中的第一个国家。
lbox.selection_set(0)
# 同时调用showPopulation函数以显示所选国家的人口。
showPopulation()

root.mainloop()
