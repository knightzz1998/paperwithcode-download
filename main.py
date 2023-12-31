#! /usr/bin/env python
# -*-coding:utf-8-*-
import asyncio

import requests
from lxml import etree

from newbing_test import init, get_ask
from translate import translate_word
from download_file import download
from docx_write import write_doc

BASE_URL = "https://paperswithcode.com/tasklist/link-prediction/latest"
# https://paperswithcode.com/task/link-prediction/latest?page={}&q=Link%20Prediction

proxies = {
    'http': 'http://localhost:4780',
    'https': 'http://localhost:4780'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


def get_data(page=1, question="Link Prediction", result=[]):
    data = {"page": page, "q": question}
    BASE_URL.format()
    response = requests.get(BASE_URL, params=data, proxies=proxies)
    content = response.text
    parse_html = etree.HTML(content)
    titles = parse_html.xpath(
        "//div[@class='infinite-container text-center']/div/div/div/div[2]/div/div[1]/h1/a/text()")
    links = parse_html.xpath("//div[@class='infinite-container text-center']/div/div/div/div[2]/div/div[1]/h1/a/@href")
    prefix = "https://paperswithcode.com"

    # 初始化 NewBing
    bot = asyncio.run(init())
    count = 0
    for title, link in zip(titles, links):
        paper_url = prefix + link
        # print(result[k])
        content = requests.get(paper_url, proxies=proxies).content
        paper_html = etree.HTML(content)
        abstract = paper_html.xpath("//div[@class='paper-abstract']/div/div/p/text()")[0].replace("\n            ", "")
        pdf_url = paper_html.xpath("//div[@class='paper-abstract']/div/div/a[1]/@href")[0]
        code_url = paper_html.xpath("//*[@id='implementations-short-list']/div/div[1]/div/a/@href")[0]
        # print(abstract)
        # print(pdf_url)
        # print(code_url)
        zh_abstract = translate_word(abstract, proxies)
        summarize = asyncio.run(get_ask(pdf_url))
        count += 1
        if count > 25:
            asyncio.run(bot.reset())
        # zh_abstract = abstract
        res = {'title': title, 'abstract': abstract,
               'summarize': summarize,
               'zh_abstract': zh_abstract,
               'paper_url': paper_url,
               'pdf_url': pdf_url,
               'code_url': code_url}
        # download(k, pdf_url)
        result.append(res)
        print(title)
        # 下载文件
        download(title, pdf_url, proxies)


if __name__ == '__main__':
    result = []
    for page in range(1, 10):
        get_data(page=page, result=result)
    write_doc(result, '链路预测论文整理.docx')
