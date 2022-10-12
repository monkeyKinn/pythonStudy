# 爬虫：通过编写程序来获取到互联网上的资源
# 百度
# 需求：用程序模拟浏览器，输入一个网址，从该网址中获取到资源或者内容
# python搞定以上需求，特别简单

# 打开 URL url，它可以是字符串或 Request 对象
from urllib.request import urlopen

url = "http://www.baidu.com"
# 获取相应
resp = urlopen(url)

# 控制台打印内容
# print(resp.read().decode("utf-8"))

# 创建一个文件 mode=w是 打开写入，首先截断文件 , encode是用于对文件进行解码或编码的编码名称
with open("mybaidu.html", mode="w", encoding="utf-8") as f:
    # 写入读取到网页的源代码
    f.write(resp.read().decode("utf-8"))
print("over")
