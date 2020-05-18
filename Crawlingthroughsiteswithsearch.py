class Content:

    def __init__(self,topic,url,title,body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body


    def print(self):
        print('New article found for topic:{}'.format(self.topic))
        print('Url:{}'.format(self.url))
        print('Title:{}'.format(self.title))
        print('Body:\n{}'.format(self.body))

class Website:

    def __init__(self,name,url,searchUrl,resultListing,resultUrl,absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag

import requests
from bs4 import BeautifulSoup

class Crawler:

    def getPage(self,url):
        try:
            req=requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text,'html.parser')


    def safeGet(self,pageObj,selector):
        childObj=pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''

    def search(self,topic,site):
        bs=self.getPage(site.searchUrl+topic)
        print('带参数的地址：'+site.searchUrl+topic)

        searchResults = bs.select(site.resultListing)
        print('结果列表：'+site.resultListing)

        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs['href']

            print('查询【0】的绝对地址：'+str(site.absoluteUrl))

            if (site.absoluteUrl):
                print('绝对地址：'+url)
                bs=self.getPage(url)

            else:
                print('相对地址：'+site.url+url)
                bs=self.getPage(site.url+url)

            if bs is None:
                print('Something was wrong with that page or url,skipping')
                return

            title=self.safeGet(bs,site.titleTag)
            body=self.safeGet(bs,site.bodyTag)

            if title!='' and body!='':
                content=Content(topic,title,body,url)
                content.print()

crawler=Crawler()
#self,name,url,searchUrl,resultListing,resultUrl,absoluteUrl, titleTag, bodyTag
siteData = [
    ['O\'Reilly Media', 'http://oreilly.com','https://ssearch.oreilly.com/?q=','article.product-result', 'p.title a', True, 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com', 'http://www.reuters.com/search/news?blob=', 'div.search-result-content','h3.search-result-title a', False, 'h1', 'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu','https://www.brookings.edu/search/?s=','div.list-content article', 'h4.title a', True, 'h1', 'div.post-body']
]
sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2],row[3], row[4], row[5], row[6], row[7]))

topics = ['python', 'data science']
for topic in topics:
    print('GETTING INFO ABOUT: ' + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)
