# -*- coding: utf-8 -*-

"""
@Time : 2023/7/4 18:22
@Author : 金圣聪
@File : 作业2.py
@Project : pythonStudy
"""

"""
第一题
    写一个进程的创建的代码
"""
from multiprocessing import Process


def son_proc():
    """子进程要执行的代码"""
    print("当前[son]进程运行ing...")


if __name__ == '__main__':
    p = Process(target=son_proc)
    p.start()
    print("当前[main]进程运行ing...")

"""
第二题
    描述一下进程和线程的区别
答：
    一个程序至少一个进程
    一个进程至少一个线程
    
    进程的运行依赖程序
    线程的运行依赖进程
    
    进程拥有独立的内存单元
    由一个进程创建的线程共享内存单元
"""

"""
第三题
    写一个进程的之间的通信的代码
"""
from multiprocessing import Process, Queue


def producer(queue: Queue, values: list) -> None:
    for value in values:
        queue.put(value)


def consumer(queue: Queue):
    while True:
        if not queue.empty():
            value = queue.get(True)
            print(f"消费了： {value}")
        else:
            break


if __name__ == '__main__':
    input_str = input("请输入一个列表,用','隔开:")
    strs = input_str.split(",")
    queue = Queue()
    p = Process(target=producer, args=(queue, strs))
    c = Process(target=consumer, args=(queue,))
    p.start()
    p.join()
    c.start()
    c.join()
