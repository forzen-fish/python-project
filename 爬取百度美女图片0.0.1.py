"""title"""
import urllib.request
import re

""""读取网页源码并放到变量html中"""
response = urllib.request.urlopen("http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1555823104869_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&f=3&oq=%E5%9B%BE%E7%89%87&rsp=0")
html = response.read()
html = html.decode("utf-8")


"""正则匹配"""
a=re.findall('"objURL":"(.*?)"',html,re.S)

"""生成一个元组a，格式：【‘...’，‘...’...】，现在对其进行访问"""
"""print(a[0])"""

"""访问成功，注释掉print，开始进行下载"""
"""使用循环"""
"""如果，元组a的长度大于i，停止运行"""
i=0
while len(a)>i:
    try:
        url=a[i]
        print(url)
        response = urllib.request.urlopen(url)
        pict=response.read()
        with open(str(i)+".jpg",'wb')as f:
            f.write(pict)
        i=i+1
    except:
        i=i+1
        url=a[i]
        print(url)
        response = urllib.request.urlopen(url)
        pict=response.read()
        with open(str(i)+".jpg",'wb')as f:
            f.write(pict)
        i=i+1
print("当前网站第一页图片已下载完毕")
