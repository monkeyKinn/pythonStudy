# -*- coding: utf-8 -*-

"""
@Time : 2023/7/3 14:11
@Author : 金圣聪
@File : 作业.py
@Project : pythonStudy
"""
"""
第一题
	什么是进程。
答：
    计算机分配资源的最小单位，由 代码+资源组成
    是一个正在执行中的程序实例。
    它是操作系统分配资源的基本单位。
    每个进程都有自己独立的内存空间，包括代码、数据和堆栈。
    进程之间相互独立，互不干扰，每个进程都在自己的地址空间中执行
第二题
	什么是线程。
答：
    程序执行的最小单位。
    它是进程中的一个实体，一个进程可以拥有多个线程。
    线程共享进程的资源，包括内存、文件和其他系统资源。
    线程之间可以并发执行，共享同一进程的上下文环境。

第三题
	写一个多线程的程序。
"""

from threading import Thread
import time


def go_home(body_name):
    print(f'现在是： {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}，{body_name} 回家了,')
    time.sleep(2)


if __name__ == '__main__':
    print("下雨了....")
    xiao_ming = Thread(target=go_home, args=("小明",))
    xiao_hong = Thread(target=go_home, args=("小红",))
    xiao_ming.start()
    xiao_hong.start()
    print("收衣服了...")
