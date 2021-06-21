# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:01:57 2020

@author: 13775
"""

#豆瓣案例：https://www.douban.com/doulist/3516235/?start=0&sort=seq&sub_type=
#使用正则表达式匹配：<div class="title">[\s\S]*?>([\s\S]*?)</a>[\s\S]*?<span class="rating_nums">([\s\S]*?)</span>[\s\S]*?<div class="abstract">([\s\S]*?)<br />([\s\S]*?)<br />([\s\S]*?)<br />([\s\S]*?)<br />([\s\S]*?)</div>

from bs4 import BeautifulSoup
import re
import basicSpider


def get_html(url):
    """
    获取一页的网页的源码信息
    """
    headers = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0")]
#    proxy = {"123.101.207.22":"9999"}
    html = basicSpider.downloadHtml(url, headers=headers)
    return html

def get_movie_all(html):
    """
    获取当前页面中所有的电影列表信息
    """
    soup = BeautifulSoup(html,"html.parser")
    movie_list = soup.find_all("div", class_='bd doulist-subject')
    return movie_list
    
def get_movie_one(movie):
    """
    获取一部电影的精确信息
    """
    result = ""
    soup = BeautifulSoup(str(movie), "html.parser")
    title = soup.find_all("div", class_='title')
    soup_title = BeautifulSoup(str(title[0]), "html.parser")
    for line in soup_title.stripped_strings:
        result += line
    
    try:
        score = soup.find_all("span", class_='rating_nums')
        score = BeautifulSoup(str(score[0]), "html.parser")
        for line in score.stripped_strings:
            result += "||评分:"
            result += line
    except:
        result += "||评分:0.1"
    
    abstract = soup.find_all("div", class_='abstract')
    abstract_info = BeautifulSoup(str(abstract[0]), "html.parser")
    for line in abstract_info.stripped_strings:
        result += "||"
        result += line
        
    result += '\n'
#    print(result)
    return result

def save_file(movieInfo):
    """
    写文件的操作，这里使用追加的方式
    """
    with open("doubanMovie.txt", "ab") as f:
        f.write(movieInfo.encode("utf-8"))

def crawlMovieInfo(url):
    """
    整个流程的控制：抓取一页的数据，并写入本地文件中
    """
    html = get_html(url)
    movie_list = get_movie_all(html)
    for i in movie_list:
        save_file(get_movie_one(i))
    
    
if __name__ == "__main__":
    url = "https://www.douban.com/doulist/3516235/?start=0&sort=seq&sub_type="
    crawlMovieInfo(url)
    
    # 查找所有的url链接
    html = get_html(url)
    pattern = re.compile('(https://www.douban.com/doulist/3516235/\?start=.*)"')
    itemUrls = re.findall(pattern, html)
#    for i in itemUrls:
        #print(i)
        
    #两步去重操作
    crawl_queue = []     #待爬队列
    crawled_queue = []   #已爬取队列
    for item in itemUrls:
        if item not in crawled_queue:
            crawl_queue.append(item)  #第一步去重，确定这些url不在已爬取队列中
    #第二步去重，对待爬取队列去重
    crawl_queue = list(set(crawl_queue))
    
    #模拟广度优先遍历
    while crawl_queue:  #去待爬取队列中取值，直到待爬取队列为空
        url = crawl_queue.pop(0)  #取出待爬取队列中第一个值
        crawlMovieInfo(url)
        #把已经处理完成的url放入已经爬取的队列中
        crawled_queue.append(url)
