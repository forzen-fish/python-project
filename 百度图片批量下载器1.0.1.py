"""title"""
import urllib.request
import re

print("请输入你要下载的图片的关键字：")
keyword=input()
keyword=urllib.parse.quote(keyword,safe='/')
print("请输入张数：")
q=input()
q=int(q)
i=0
"""读取网页源码并放到变量html中"""
while q!=i:

    z=0
    URL='http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+str(keyword)+'&pn='+str(z)
    response = urllib.request.urlopen(URL)
    z=int(z)+20
    html=response.read().decode('utf8')
    


    """正则匹配"""
    a=re.findall('"objURL":"(.*?)"',html,re.S)

    """生成一个元组a，格式：【‘...’，‘...’...】，现在对其进行访问"""
    """print(a[0])"""

    """访问成功，注释掉print，开始进行下载"""
    """使用循环"""
    """如果，元组a的长度大于i，停止运行"""
    while q!=i:
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

