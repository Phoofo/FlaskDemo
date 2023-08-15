import tkinter as tk

from PIL import ImageTk, Image

win = tk.Tk()
win.title("标签实例demo02")

# 显示图片(注意这里默认支持的图片格式为GIF)
# photo = tk.PhotoImage(file='D:/apython/FlaskDemo/pythonProject/tkinter/img/104147976_p0.png')
# print(type(photo))
# 将图片放在主窗口的右边
img = Image.open("./img/104147976_p0.png")  # 打开图片
# photo = ImageTk.PhotoImage(img)  # 使用ImageTk的PhotoImage方法
# tk.Label(win, image=photo).pack(side="right")
# 显示文字，设置文本格式
text = "迷漫雨点中发现 现实是爱不过为留念,\n" \
       "缘分寄生三世石 石上附载约誓未兑现,\n " \
       "情是最艰辛试练 练就下世的爱在沉淀"
lab_text = tk.Label(win, text=text, font=("华文行楷", 20), bg="yellow", fg="green")
win.mainloop()
