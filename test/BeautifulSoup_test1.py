import requests
from bs4 import BeautifulSoup
from test import pachong
import os
from multiprocessing import Pool
import pandas
import time

if __name__=='__main__':

    start = time.time()

    headers={
            'UserAgent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
            }

    total=[]
    for i in range(1,2):
        url='https://www.qidian.com/rank/yuepiao?chn=0&page=%s'% str(i)
        print(url)
        res=requests.get(url,headers=headers)
        soup=BeautifulSoup(res.text,'html.parser')
        书名s=soup.select('#rank-view-list > div > ul > li > div.book-mid-info > h4 > a')
        作者s=soup.select('#rank-view-list > div > ul > li > div.book-mid-info > p.author > a.name')
        类型s=soup.select('#rank-view-list > div > ul > li > div.book-mid-info > p.author > a:nth-of-type(2)')
        简介s=soup.select('#rank-view-list > div > ul > li > div.book-mid-info > p.intro')
        最新章节s=soup.select('#rank-view-list > div > ul > li > div.book-mid-info > p.update > a')
        链接s=soup.select('#rank-view-list > div > ul > li > div.book-mid-info > h4 > a')

        for 书名,作者,类型,简介,最新章节,链接 in zip(书名s,作者s,类型s,简介s,最新章节s,链接s):
            data={'书名':书名.get_text().strip(),\
            '作者':作者.get_text().strip(),\
            '类型':类型.get_text().strip(),\
            '简介':简介.get_text().strip(),\
            '最新章节':最新章节.get_text().strip(),\
            '链接':链接['href'].strip()}
            total.append(data)

    # print(total)

    deal1=pandas.DataFrame(total)
    # print(deal1)
    xls_file = 'E:\Program Files\Python37\data\qidian.xls'
    if os.path.exists(xls_file):
        os.remove(xls_file)
    deal1.to_excel(xls_file)
    #创建进程池
    p = Pool(10)
    for book in total:

        bookName = book['书名']
        p.apply_async(pachong.DownloadOneBook, args=('https:'+book['链接']+'#Catalog','E:\Program Files\Python37\data\\'+ bookName +'.txt'))
        # print('Child process will start.')
        # p.start()
        # # p.join() # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
        # print('Child process end.')
    print('Waiting for all subprocesses done...')
    p.close()
    # 对Pool对象调用join()方法会等待所有子进程执行完毕，
    # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    p.join()
    print('All subprocesses done.')
    end = time.time()
    print('DownLoadAllBook Task runs  %0.2f seconds.' %  (end - start))
