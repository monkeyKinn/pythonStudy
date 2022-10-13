# 笔记

<!-- TOC -->
* [笔记](#)
* [使用pip管理Python包](#pippython)
* [修改pip下载源](#pip)
* [变量](#)
  * [数据类型](#)
    * [Number 数值](#number-)
    * [boolean   布尔](#boolean---)
    * [string 字符串](#string-)
    * [list 列表](#list-)
    * [tuple 元组](#tuple-)
    * [dict 字典](#dict-)
<!-- TOC -->

# 使用pip管理Python包

``pip install <包名>`` 安装指定的包

`` pip uninstall <包名>`` 别除指定的包

``pip list`` 显示已经安装的包

``pip freeze`` 显示已经安装的包，并且以指定的格式显示

# 修改pip下载源

运行``pip install``命令会从网站上下载指定的python包，默认是从``https:/files.pythonhosted.org/``网站上下
载。这是个国外的网站，遇到网络情况不好的时候，可能会下载失败，我们可以通过命令，修改p现在软件时的
源。

格式：
``pip install 包名 -i 国内源地址``

示例：
``pip install ipython -i https://pypi.mirrors.ustc.edu.cn/simple/``

就是从中国科技大学ustc)的服务器上下载requests(甚于python的第三方web框架)

国内常用的pip下载源列表：

| 名字         | 国内源地址                                        |
|------------|----------------------------------------------|
| 阿里云        | http://mirrors.aliyun.com/pypi/simple/       |
| 中国科技大学     | https://mirrors.bfsu.edu.cn/pypi/web/simple/ |
| 豆瓣(douban) | https://pypi.doubanio.com/simple/            |
| 清华大学       | https://pypi.tuna.tsinghua.edu.cn/simple/    |
| 中国科学技术大学   | https://mirrors.bfsu.edu.cn/pypi/web/simple/ |

# 变量

变量的格式： 变量名字 = 变量的值

## 数据类型

### Number 数值

    int float

### boolean   布尔
    True,False
### string 字符串

    ""

### list 列表

    [,,,]

### tuple 元组

    (,,,)

### dict 字典

    类似于json对象 {"name": "红浪漫", "age": 18}

