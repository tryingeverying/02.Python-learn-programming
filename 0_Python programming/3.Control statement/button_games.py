import tkinter as tk
import random

# 按钮被点击之后执行该函数
def hit_me():
    print('go out')


# 当鼠标Enter button之后执行该函数
# 该函数把button给弄跑掉

def escape(event):
    b = event.widget

    # 获取按钮的宽度高度以及鼠标的xy坐标值
    width=b.winfo_width()
    height=b.winfo_height()
    mouse_x=b.winfo_x()+event.x
    mouse_y=b.winfo_y()+event.y

    while True:
        #随机生成新的按钮的位置,按钮的位置为左上就那个顶点的坐标值
        x=random.randint(0,800)
        y=random.randint(0,600)

        # 条件判断使之新生成的按钮的位置不在鼠标处
        if(x < mouse_x or x > mouse_x + width and x + width < 800) and (y < mouse_y 
        or y > mouse_y + height and y + height < 600):
            break

    # 将按钮移动到新位置
    b.place(x=x,y=y)

#创建一个窗口
window=tk.Tk()

window.title('button games')#窗口的标题
window.geometry('800x600')#窗口的大小为800x600

#创建一个按钮

button = tk.Button(
    window ,     #父控件,即这个button属于window
    text='go out',#显示在button上的文字
    command=hit_me#点击button时执行的命令
)
#监控button的消息，如果消息为<Enter>，即鼠标进入时，调用escape函数
button.bind('<Enter>',escape)

#把button打包到窗口上，默认情况为居中显示在最上面
button.pack() #按钮位置

# 显示窗口，开始处理各种窗口消息，循环不会退出，除非关闭窗口
window.mainloop()
