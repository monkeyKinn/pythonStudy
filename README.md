<!-- TOC -->
* [pythonStudy](#pythonstudy)
* [学习爬虫 加油](#-)
  * [2022.10.13开始](#20221013)
* [打卡表](#)
* [日记](#)
  * [2022.10.13](#20221013)
  * [2022.10.17_beforeDawn](#20221017_beforedawn)
  * [2022.10.17_atNight](#20221017_atnight)
  * [2022.10.18](#20221018)
  * [2022.10.19](#20221019)
    * [需要记忆字符串常见操作(需要背下来)](#---)
  * [2022.10.20](#20221020)
  * [2022.10.24_beforeDawn](#20221024_beforedawn)
  * [2022.10.24_atNight](#20221024_atnight)
  * [2022.10.26_beforeDawn](#20221026_beforedawn)
  * [2022.10.26_atNight](#20221026_atnight)
<!-- TOC -->

# pythonStudy

# 学习爬虫 加油
  ## 2022.10.13开始 
  跟着b站[尚硅谷爬虫视频](https://www.bilibili.com/video/BV1Db4y1m7Ho?p=1&vd_source=432ae5430f4b5174f9f12fc5526ad9e3)学习
# 打卡表

| 日期         | 内容                                        | 完成情况 |
|------------|-------------------------------------------|------|
| 2022.10.12 | 手刃个爬虫                                     | √    |
| 2022.10.13 | 基础(注释+变量+变量类型)                            | √    |
| 2022.10.17 | 凌晨-基础(查看数据类型+命名规范+数据类型转换(to (int+float))) | √    |
| 2022.10.17 | 晚上-基础(数据类型转换(to (str+bool)) + (算数+赋值)运算符) | √    |
| 2022.10.18 | 复合赋值+比较运算+逻辑运算+逻辑性能提升+输入+输出               | √    |
| 2022.10.19 | 流程控制语句if-elif-else + for +字符串高级           | √    |
| 2022.10.20 | 列表(增删改查)+元组(查,不能删除)+字典(增改查)               | √    |
| 2022.10.24 | 字典(删+遍历)                                  | √    |
| 2022.10.24 | 函数(的定义+参数+返回值+变量范围)+文件(的打开和关闭+读写)         | √    |
| 2022.10.26 | 文件的序列化和反序列化+异常 + 页面结构(回顾  已经掌握)           | √    |
| 2022.10.26 | 基础xmind总结并上传到resource目录                   | √    |


# 日记

## 2022.10.13

        昨天的b站视频居然是部分的,后面加了微信要资料发现是卖课的,路飞的课,不买也罢.
    准备刷尚硅谷的小白速通 这个就不要钱了 嘻嘻

## 2022.10.17_beforeDawn

        周日,前两天刷怪奇物语了,今天补上,因为命名规范和java的差不多所以看得很快,
    至于去转换的方法,其实也能类比成java的包装类型paseXXX,只不过py更简便(int(),float()),
    
    需要注意的是,float 转换为 int  返回的是小数点前面的数 (取整)

## 2022.10.17_atNight

        学习了数据类型转换(str+bool),
    
    1.转str的时候的区别
    
        将布尔类型转换为字符串,就是本身的字符
    
    2.转bool的时候总结了下
    
      什么情况下为false(9种)
      1.print(bool(0))
    
      2.print(bool(0.0))
    
      3.print(bool(''))
    
      4.print(bool(""))
    
      5.print(bool(【】))
    
      6.print(bool({}))
    
      7.print(bool(()))
    
      8.print(bool(("")))
    
      9.print(bool(('')))
    
    学习了 运算符 具体跟java的差别:

    1.算数运算符
      在py中,+号两端都是字符串才能拼接

      在py中,字符串的乘法是将字符串重复n次
  
    2.赋值运算符
      在py中,可以同时给不同变量名赋相同值:
        a = b = c = 20
  
      在py中,同时赋值多个变量不同的值(用逗号分割):
        a, b, c = 100, 101.1, '1000.2'

## 2022.10.18

    今天没什么难度,复合赋值+比较运算于java一样

    1.逻辑运算+逻辑性能提升
        1.1 在python中 and or not 分别对应 与 或 非
          and 一假即假
          or  一真即真
        1.2 都是短路运算,判断逻辑跟java相差无几
        1.3 性能总结:
          左边恒执行,
            当为true的时候,   and 会执行右边,    or 不会执行右边
            当为false的时候,  and 不会执行右边,  or 会执行右边

    2.输入+输出
      1.1 输出有个格式化
        print('%d,%d' % (变量1,变量2)) 中间由百分号割开,区别于java的逗号
      1.2 输入 input()函数,此函数恒被str类型接受

## 2022.10.19

### 需要记忆字符串常见操作(需要背下来)

| 方法名                                              | 说明                                                                                             |
|--------------------------------------------------|------------------------------------------------------------------------------------------------|
| 获取长度:<br/>len(str)                               | len函数可以获取字符串的长度                                                                                |
| 查找内容:<br/>str.find('需要找的字符')                     | 查找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中第一次出现的开始位置索引值，如果不存在，则返回-1                                       |
| 判断:<br/>str.startswith(''),<br/>str.endswith('') | 判断字符串是不是以谁谁谁开头/结尾   区分大小写                                                                      |
| 计算出现次数:<br/>str.count('需要计算的字符',开始位置,结束位置)       | 返回 str在start和end之间 --> [) 在 str 里面出现的次数  <br/><br/>注意:也可以只有一个参数,即需要找的字符                        |
| 替换内容:<br/>str.replace('旧的字符','新的字符',可选:需要替换的次数)  | 替换字符串中指定的内容，如果指定次数count，则替换不会超过count次                                                          |
| 切割字符串:<br/>str.split('分割的字符')                    | 通过参数的内容切割字符串  返回值是个列表                                                                          |
| 修改大小写:<br/>str.upper(),<br/>str.lower()          | 将字符串中的大小写互换                                                                                    |
| 空格处理:<br/>str.strip()                            | 去空格 (两端的)                                                                                      |
| 字符串拼接:<br/>str.join('字符串')                       | 字符串拼接 把str拼接到'字符串'的每个字符后面 <br/> 举个🌰:<br/> s8 = 'a' <br/><br/>#字a符a串<br/>print(s8.join('字符串')) |

## 2022.10.20
    持续学习第六天,加油.
    一些注意点已经写在[5.数据类型高级-笔记.md]里了,想到了一个复习的方法,周末用思维导图总结一周所学~

## 2022.10.24_beforeDawn
    周末看完了怪奇物语,没有做笔记
    然后回来看了字典的删除和遍历,对应的已经写到笔记上了

## 2022.10.24_atNight
    完成:
    函数(的定义+参数+返回值+变量范围)+文件(的打开和关闭+读写)
    1024节日快乐~

## 2022.10.26_beforeDawn
    完成:
    序列化和反序列化
    明天准备总结一下所学基础,用思维导图的方式

## 2022.10.26_atNight
    完成:
      思维导图总结完成,导出成pdf放在资源目录,方便随时复习
    基础总结:
      有了java基础确实比较简单能够理解,但是截止到今天,只是把爬虫方向的基础学完,py本身还有自己的细节部分,后续精进
    拟精进方式:
      1.把小甲鱼的那本书看完
      2.跟着白嫖的就业班从头学一遍
    拟精进成果物:
      1.继续补充思维导图
