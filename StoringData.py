import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'

def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
        print('输出最后地址1：'+url)
    elif source.startswith('http://'):
        url = source
        print('输出最后地址2：' + url)
    elif source.startswith('https://'):
        url = source
        print('输出最后地址3：' + url)
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http://{}'.format(source)
        print('输出最后地址4：' + url)
    else:
        url = '{}/{}'.format(baseUrl, source)
        print('输出最后地址5：' + url)
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    print('现在开始打印。。。。。。。。')
    print('0:'+absoluteUrl)
    path = absoluteUrl.replace('www.', '')
    print('1:'+path)
    path = path.replace(baseUrl, '')
    print('2:'+path)
    path = downloadDirectory+path
    print('3:'+path)
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.findAll(src=True)

for download in downloadList:
    print('基础地址' + baseUrl + '\n下载地址' + download['src'])
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print('下载文件地址：' + fileUrl + '\n')

        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
        print('-' * 50)
    else:
        print('现在是空',fileUrl)
