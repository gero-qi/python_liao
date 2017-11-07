from twisted.web.client import getPage
from twisted.internet import reactor

links = ['http://www.verycd.com/topics/%d/' % i for i in range(5420, 5430)]


def parse_page(data, url):
    print
    len(data), url


def fetch_error(error, url):
    print
    error.getErrorMessage(), url


# 批量抓取链接
for url in links:
    getPage(url, timeout=5) \
        .addCallback(parse_page, url) \  # 成功则调用parse_page方法
    .addErrback(fetch_error, url)  # 失败则调用fetch_error方法

reactor.callLater(5, reactor.stop)  # 5秒钟后通知reactor结束程序
reactor.run()