#! /usr/bin/env python
# -*-coding:utf-8-*-
import os

import requests
from tqdm import tqdm

url = "https://arxiv.org/pdf/2305.13059v2.pdf"
title = "Friendly Neighbors: Contextualized Sequence-to-Sequence Link Prediction".replace(":", "")
BASE_LOCAL = "paper-download/"


def download(title, url, proxies):
    if not os.path.exists(BASE_LOCAL):
        os.mkdir(BASE_LOCAL)

    local = BASE_LOCAL + title + ".pdf"
    response = requests.get(url, stream=True, proxies=proxies)
    # 拿到文件的长度，并把total初始化为0
    total = int(response.headers.get('content-length', 0))
    with open(local, 'wb') as f, tqdm(desc=title, total=total, unit='iB', unit_scale=True,
                                      unit_divisor=1024, ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = f.write(data)
            bar.update(size)


if __name__ == '__main__':
    download(title, url)
