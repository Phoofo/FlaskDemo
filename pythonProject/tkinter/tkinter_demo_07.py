import tkinter as tk
import tkinter.messagebox
import json
studentInfos=[]
root=tk.Tk()
root['height']=200
root['width']=250
root.title('学生管理系统')
choice=tk.IntVar()
choice.set(1)
radioAdd=tk.Radiobutton(root,
                        variable=choice,
                        value=1,
                        text='添加学生信息')
radioAdd.place(x=70,y=10,width=100,height=20)
radioDel=tk.Radiobutton(root,
                        variable=choice,
                        value=2,
                        text='删除学生信息')
radioDel.place(x=70,y=40,width=100,height=20)
radioDel=tk.Radiobutton(root,
                        variable=choice,
                        value=3,
                        text='修改学生信息')
radioDel.place(x=70,y=70,width=100,height=20)
radioDel=tk.Radiobutton(root,
                        variable=choice,
                        value=4,
                        text='显示学生信息')
radioDel.place(x=70,y=100,width=100,height=20)
def makechoice(delNum=None):
    if choice.get()==1:
        print("="*30)
        tk.messagebox.showinfo(title='提示',message='添加学生信息')
        newName=input("请输入新的学生的名字：")
        newSex=input("请输入新的学生性别（男/女）：")
        newPhone=input("请输入新的学生电话：")
        print("="*30)
        newInfo={}
        newInfo["name"]=newName
        newInfo["sex"]=newSex
        newInfo["phone"]=newPhone
        studentInfos.append(newInfo)
    elif choice.get()==2:
        tk.messagebox.showinfo(title='提示',message='删除学生信息')
        print("="*30)
        defNum=int(input("请输入要删除的序号："))-1
        print("="*30)
        del studentInfos[delNum]
    elif choice.get()==3:
        tk.messagebox.showinfo(title='提示',message='修改学生信息')
        print("="*30)
        studentId=int(input("请输入要修改的序号："))-1
        newName=input("请输入新的学生的名字：")
        newSex=input("请输入新的学生性别（男/女）：")
        newPhone=input("请输入新的学生电话：")
        print("="*30)
        newInfo={}
        newInfo["name"]=newName
        newInfo["sex"]=newSex
        newInfo["phone"]=newPhone
        studentInfos[studentId]=newInfo
    elif choice.get()==4:
        tk.messagebox.showinfo(title='提示',message='显示学生信息')
        print("="*30)
        print("学生信息如下")
        print("="*30)
        print("序号\t姓名\t性别\t手机号")
        num=1
        for tempInfo in studentInfos:
            print("%d\t%s\t%s\t%s"%(num,tempInfo["name"],tempInfo["sex"],tempInfo["phone"]))
            num+=1
        input("按任意键继续...")
        print("="*30)
buttonChoice=tk.Button(root,
                       text="确定",
                       width=40,
                       command=makechoice)
buttonChoice.place(x=50,y=140,width=40,height=20)
def quitsys():
    if tk.messagebox.askokcancel("提示","退出系统"):
        with open("info.txt","w+") as f:
            for item in studentInfos:
                output=json.dumps(item)
                f.write(output+'\n')
        root.destroy()
buttonQuit=tk.Button(root,
                     text="退出",
                     width=40,
                     command=quitsys)
buttonQuit.place(x=150,y=140,width=40,height=20)
root.mainloop()