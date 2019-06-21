#！/usr/bin/env Python3
# -*- coding:UTF-8 -*-

import requests
import time, os, sys
from bs4 import BeautifulSoup

class DownloadNovel(object):
    def __init__ (self, server):
        self.server = server
        # 存放章节名
        self.chapterNames = []
        # 存放章节链接
        self.chapterUrls = []
        # 存放章节数
        self.nums = 0
    def get_download_chapter_url (self):
        # 用于爬取https
        # context = ssl._create_unverified_context()
        # print(context)
        response = requests.get(self.server)
        # print(response.content)
        text = str(response.content, encoding = 'utf-8')
        bf = BeautifulSoup(text, 'html.parser')
        div = bf.find_all('div', class_ = 'volume')

        for i in range(len(div)):
            li = div[i].find_all('li')
            for j in range(len(li)):
                a = li[j].find_all('a')
                html = BeautifulSoup(str(a), 'lxml')
                # print(html)
                # 章节url
                self.chapterUrls.append('https:' + str(html.a.get('href')))
                # 章节名
                self.chapterNames.append(html.a.string)
    def get_contents (self, target):
        # context = ssl._create_unverified_context()
        response = requests.get(target)
        text = str(response.text)
        # bf = BeautifulSoup(text, 'html.parser')
        bf = BeautifulSoup(response.content.decode("utf-8"), "lxml")
        txts = bf.select(".j_readContent p")
        # a = txts[0].select('p')
        # print(a[0])
        # print('-------------------------------')
        # print(txts)
        # print(type(txts))
        # print(txts[0])
        # print(type(txts[0]))
        # print(txts[0].text)
        # print(txts[0])
        # print(type(txts[0]))
        # print(type(txts[0].text))
        # print(type(txts))

        txt_content = ''
        for p in txts:
            # print(type(p.text))
            # print(p.text)
            txt_content = txt_content + p.text +'\n'

        # print(txt_content)
        return txt_content

    def write (self, name, path, txt):
        write_flag = True
        with open(path, 'a', encoding = 'utf-8') as f:
            f.write(name + '\n')
            f.write(txt)
            f.write('\n\n')

# if __name__ == '__main__':
#     dl = DownloadNovel('https://book.qidian.com/info/1015079042#Catalog')
#     dl.get_download_chapter_url()
#     # print(dl.chapterNames)
#     # print(dl.chapterUrls)
#     print('开始下载')
#     for i in range(len(dl.chapterNames)):
#         dl.write(dl.chapterNames[i], 'E:\Program Files\Python37\data\我中了诅咒.txt', dl.get_contents(dl.chapterUrls[i]))
#         print("  已下载:%.3f%%" %  (float(i/len(dl.chapterNames))*100) + '\r')
#         sys.stdout.flush()
#     print('下载完成')

def DownloadOneBook(url,name):
    print('DownLoadBook task %s (%s)...' % (os.path.split(name)[1], os.getpid()))
    start = time.time()
    dl = DownloadNovel(url)
    dl.get_download_chapter_url()
    # print(dl.chapterNames)
    # print(dl.chapterUrls)
    for i in range(len(dl.chapterNames)):
        dl.write(dl.chapterNames[i], name, dl.get_contents(dl.chapterUrls[i]))
        # print("  已下载:%.3f%%" % (float(i / len(dl.chapterNames)) * 100) + '\r')
        sys.stdout.flush()
    end = time.time()
    print('DownLoadBook Task %s runs %0.2f seconds.' % (os.path.split(name)[1], (end - start)))