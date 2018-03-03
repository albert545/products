# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 13:02:53 2018

@author: albert-w10
"""

products = []
while True:
    name = input('輸入商品名稱:')
    if name == 'q':
        break
    products.append(name)
print(products)

    