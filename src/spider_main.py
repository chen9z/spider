#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author:yclooper
import os
import requests
from bs4 import BeautifulSoup, SoupStrainer


def down_page_img(page_url, page_count, title):
    print(page_url, page_count, title)
    dir_name=os.path.join("img",title)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    for i in range(1, (int(page_count) + 1)):
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
        img_page_url=page_url+"/"+str(i)
        print(img_page_url)
        img_html = requests.get(img_page_url, headers=headers)

        soup = BeautifulSoup(img_html.text, "lxml")
        img_url = soup.find("div", class_="main-image").find("img").get("src")

        img_cont = requests.get(img_url, headers=headers)

        with open(dir_name + "/" + img_url.split("/")[-1], "wb") as f:
            f.write(img_cont.content)


if __name__ == '__main__':
    url = "http://www.mzitu.com/all"
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
    start_html = requests.get(url, headers=headers)
    strain = SoupStrainer("div", class_="all")
    soup = BeautifulSoup(start_html.text, "lxml", from_encoding="utf-8", parse_only=strain)
    li_node = soup.find_all("li")
    urls = set()
    with open("result.txt", "w", encoding="utf-8") as f:
        for li in li_node:
            a_node = li.find_all("a")
            for a in a_node:
                f.write("%s:%s\n" % (a.get_text(), a.get("href")))
                print("%s:%s" % (a.get_text(), a.get("href")))
                page_url = a.get("href")
                title = a.get_text()
                if page_url not in urls:
                    print(page_url)
                    page_html = requests.get(page_url, headers=headers)
                    img_soup = BeautifulSoup(page_html.text, "lxml")
                    page_count = img_soup.find("div", class_="pagenavi").find_all("span")[-2].get_text()
                    down_page_img(page_url, page_count, title)
                    urls.add(page_url)
    print("爬去完成")