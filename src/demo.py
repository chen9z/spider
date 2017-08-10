#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:yclooper
import os

L=[1,2,3,4,5,6,7,8]

print(L[-1])

url="http://www.mzitu.com/99512/001234.jpg"

print(url.split("/")[-1])

os.makedirs("img/kk")

with open("img/kk/001.txt","w",encoding="utf-8") as f:
    f.write("仲华是个傻子")