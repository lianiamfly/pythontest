from bs4 import BeautifulSoup
soup = BeautifulSoup('example.html', 'html.parser') #加载我们的html文件#
soup.find('div') # 找到 div 标签


li = soup.find_all('li') # 找到所有 li 标签
'[<li>首页</li>, <li>新闻</li>, <li>影视</li>]'

for i in li:
    print(i.text)    #获取每个 li 标签的内容
