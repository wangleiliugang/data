from tkinter import *
from tkinter.scrolledtext import ScrolledText


# 给按钮添加事件行为
def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())


def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))


# 实例化一个Tk对象。
top = Tk()
top.title("Simple Editor")

# 创建大型文本区域的控件
contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

# 创建输入控件，用于显示简单的文本内容。
filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)

# 创建按钮控件，在程序中显示按钮；Tkinter的几何管理类：包装 pack()
Button(text='Open', command=load).pack(side=LEFT)
Button(text='Save', command=save).pack(side=LEFT)

mainloop()
