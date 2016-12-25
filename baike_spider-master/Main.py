#coding=utf-8
#Baike_spider Version 1.0.1 By Effortjohn
#https://github.com/effortjohn/baike_spider


from bs4 import BeautifulSoup
import urlparse
import urllib2
import re


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


class Downloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:
            return None
        return response.read()


class Baidu_Parser(object):
#百度百科网页解析器
    def _get_new_urls(self, page_url, soup):
        new_urls = []
        for link in soup.find_all('a', href=re.compile(r"/view/\d+\.htm")):
            new_url = (link.get('href'))
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.append(new_full_url)
        return new_urls
             
    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        #标题代码：<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        #简介代码：<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return 
        soup = BeautifulSoup(html_cont, 'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data


class _360_Parser(object):
#360百科网页解析器：http://baike.so.com/doc/1790119-1892991.html
    def _get_new_urls(self, page_url, soup):
        new_urls = []
        for links in soup.find_all('a', href=re.compile(r"/doc/\d+\.html")):
            new_url = (links.get('href'))
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.append(new_full_url)
        return new_urls
             
    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        #标题代码：<span class="title">Python</span>
        title_node = soup.find('span', class_="title")
        res_data['title'] = title_node.get_text()
        #简介代码：<div class="card_content" id="js-card-content"><p>
        summary_node = soup.find('div', class_="card_content").find('p')
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return 
        soup = BeautifulSoup(html_cont, 'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data


class Outputer(object):
    def __init__(self):
        self.datas=[]

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout=open('result.htm','w')
        fout.write("<html>")
        fout.write("<head>")
        fout.write('<meta charset="utf-8"></meta>')
        fout.write("<title>Crawl Result</title>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write('<h1 style="text-align:center">Crawl Result</h1>')
        fout.write('<table style="border-collapse:collapse;"  border="1">')
        for data in self.datas:
            fout.write("<tr>")
#            fout.write("<td><a href = '%s'>" % data["url"])
#            fout.write("%s</a></td>" % data["title"].encode("utf-8"))
            fout.write("<td><a href='%s'>%s</a></td>" % (data["url"].encode("utf-8"),data["title"].encode("utf-8")))
            fout.write("<td>%s</td>" % data["summary"].encode("utf-8"))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write('<br /><br /><p style="text-align:center">Power By Effortjohn</p>')
        fout.write("</body>")
        fout.write("</html>")


class SpiderMain():
    def craw(self,root_url,times): 
        count=1
        UrlManager.add_new_url(root_url)
        while UrlManager.has_new_url():
            try:
                new_url=UrlManager.get_new_url()
                print "\n%d: crawling %s" %(count,new_url)
                html_cont=Downloader.download(new_url)
                new_urls,new_data=Parser.parse(new_url,html_cont)
                UrlManager.add_new_urls(new_urls)
                Outputer.collect_data(new_data)
                if count==times:
                    break
                count=count+1
            except:
                print "crawl failed" 
        Outputer.output_html()


if __name__=="__main__":
    print "Welcome to baike_spider"
    print "Meun:\n 1. Baidu_Baike\n 2. 360_Baike"
    Parser = input("Please choose crawl type:")
    
    if Parser == 1:
        UrlManager = UrlManager()
        Downloader = Downloader()
        Parser = Baidu_Parser()
        Outputer = Outputer()
        root = raw_input("Enter First Url : http://baike.baidu.com/view/")
        root_url = "http://baike.baidu.com/view/%s" %(root)
        
    elif Parser == 2:
        UrlManager = UrlManager()
        Downloader = Downloader()
        Parser = _360_Parser()
        Outputer = Outputer()
        root = raw_input("Enter First Url : http://baike.so.com/doc/")
        root_url = "http://baike.so.com/doc/%s" %(root)
        
    else:
        wrong = raw_input("Input Wrong.Press Enter to exit.")
        exit()

    times = input("Craw Times : ")
    SpiderMain = SpiderMain()
    SpiderMain.craw(root_url,times)
    print "\nEverything is done. Result is in result.htm ." 