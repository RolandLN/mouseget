# 2019.3.9


import tkinter as tk
import random
import time
from tkinter import *


def right_buttondown(event):
    global RD, m, x, y, RD1
    # print("右键按下", event.x, event.y)
    # m += 1
    # if m > 5:              # 建议采集次数，，，，，，，，，，，，，，，，，，，，，，，，，，
    #     print("thanks for your help!\n"
    #           " you can exit now!")
    fobj.writelines("RTDW %d %d %d %d" % (event.x, event.y, event.time, time.time()))
    fobj.writelines('\n')
    x = event.x
    y = event.y
    RD = RD1 = True
    return [x, y]


def right_buttonup(event):
    # print("右键释放", event.x, event.y)
    fobj.writelines("RTUP %d %d %d %d" % (event.x, event.y, event.time, time.time()))
    fobj.writelines('\n')


def call_back(event):
    if RD:     # 右键按下后开始记录数据
        # print("右键按下过一次")
        fobj.writelines("MOVE %d %d %d %d" % (event.x, event.y, event.time, time.time()))
        fobj.writelines('\n')
    else:
        # print("右键未曾按下")
        pass


class Questions(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title('hello')
        self.withdraw()  # 实现主窗口隐藏
        self.run()

    def refresh_data(self):
        # 需要刷新数据的操作,五秒自动刷新
        def color_set1():
            cv.create_rectangle(0, 0, 1350, 670, fill='green')
            cv.create_rectangle(x1, y1, x1 + 30, y1 + 30, fill='blue')
            self.after(500, self.refresh_data)  # 1单位为毫秒,循环

        def color_set():
            global x, y, RD, x1, y1, x0, y0
            cv.create_rectangle(0, 0, 1350, 670, fill='green')
            cv.bind("<Button-3>", right_buttondown)
            cv.pack()
            if RD:
                if (x1 < x < x1+30) & (y1 < y < y1+30):
                    # print("击中蓝色框")

                    while (abs(x0-x1) < 300) & (abs(y0-y1) < 100):  # 判断下一个点的距离较大
                        x0 = random.randint(10, 1250)
                        y0 = random.randint(10, 640)
                        # color_set1()

                    cv.create_rectangle(x0, y0, x0 + 30, y0 + 30, fill='blue')
                    x1 = x0
                    y1 = y0
                    self.after(1, self.refresh_data)  # 1000单位为毫秒,1秒钟刷新
                else:
                    # print("未集中蓝色块")
                    color_set1()
            else:
                # print("未击中右键")
                color_set1()
        color_set()

    def run(self):

        i = 0
        while i < 3:
            n = input()
            if n == 'bg':
                self.refresh_data()
                self.mainloop()
            else:
                print("\n 输入[bg]，开始解锁....")
                continue
        pass


if __name__ == '__main__':
    # 建立日志文件
    T = input("\n请输入姓名首字母并按序输入录入次数（0,1,2....10）:")
    file_name = "D:\pycharm\pydataZ\mouse" + T + " .text"
    print("\n输入[bg]，开始解锁....")
    fobj = open(file_name, 'a')
    RD = RD1 = False
    m = 0
    x1 = y1 = 0
    x0 = y0 = 0

    root = Tk()
    root.title('右键点击蓝色方块...')

    # 创建一个框架，在这个框架中响应事件
    cv = Canvas(root, width=1350, height=670, bg='red')
    # cv.bind("<Button-3>", right_buttondown)
    cv.bind("<Motion>", call_back)
    cv.bind("<ButtonRelease - 3>", right_buttonup)
    cv.pack()

    question = Questions()

    # 关闭日志文件
    fobj.close()
