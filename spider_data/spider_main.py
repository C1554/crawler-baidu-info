#coding:utf8
from spider_data import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        #initialize object
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()



    def craw(self, root_url):
        count=1
        #add root_url into url manager
        self.urls.add_new_url(root_url)
        #when url manager has new url,execute under method
        while self.urls.has_new_url():
            try:
                #get crawed url
                new_url=self.urls.get_new_url()
                print 'craw %d : %s' %(count,new_url)
                #underload url pageweb
                html_cont=self.downloader.download(new_url)
                #parser url pageweb ,get new urls and data
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                #add url,attention:here urls and up url are different,up url is single,below url is plural and batch
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count==1000:
                    break
                count = count +1
            except:
                print 'craw failed'
        self.outputer.output_html()


if __name__=="__main__":
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)
    