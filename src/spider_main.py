#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author:yclooper
import requests
from bs4 import BeautifulSoup,SoupStrainer

if __name__ == '__main__':
    url = "http://www.mzitu.com/all"
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
    start_html = requests.get(url, headers=headers)
    strain=SoupStrainer("div",class_="all")
    soup = BeautifulSoup(start_html.text, "lxml", from_encoding="utf-8",parse_only=strain)
    li_node = soup.find_all("li")
    urls=set()
    with open("result.txt", "w") as f:
        for li in li_node:
            a_node = li.find_all("a")
            for a in a_node:
                f.write("%s:%s\n" % (a.get_text(), a.get("href")))
                print("%s:%s" % (a.get_text(), a.get("href")))
