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
    price = input('輸入價格')
    #products.append(name)
    #products.append(price)
    products.append([name,price])
print(products)

#印出清單
for p in products:
    #print(p)
    print (p[0],'價格是',p[1])
    