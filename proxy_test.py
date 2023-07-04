#! /usr/bin/env python
# -*-coding:utf-8-*-

import requests

proxies = {
    'http': 'http://localhost:4780',
    'https': 'http://localhost:4780'
}
BASE_URL = "https://paperswithcode.com/tasklist/link-prediction/latest"
data = {"page": 1, "q": "Link Prediction"}
url = 'https://paperswithcode.com/task/link-prediction/latest?page=2&q=Link%20Prediction'
response = requests.get(BASE_URL, params=data, proxies=proxies)

print(response.text)
