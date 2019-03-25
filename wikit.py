# -*- coding:UTF-8 -*-
import requests
import sys
from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find(id='mw-content-text')
    #重定向和歧义页面待完成

    arr_para = []
    children = content.find_all('p')
    for child in children:
        arr_para.append("  " + child.text.strip() + '\n')

    print(''.join(arr_para))


if __name__ == '__main__':
    proxies = {
        'http': 'socks5://127.0.0.1:1080',
        'https': 'socks5://127.0.0.1:1080'
    }

    key = sys.argv[1]
    url = "https://zh.wikipedia.org/wiki/" + key
    target = requests.get(url, proxies=proxies)
    parse_html(target.text)
