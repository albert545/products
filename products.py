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
    price = int(price)  #若p 轉成 int 則 下方p[1] str+int 會出錯
    #products.append(name)
    #products.append(price)
    products.append([name,price])
print(products)

#印出清單
for p in products:
    #print(p)
    print (p[0],'價格是',p[1])
    
#寫入檔案 *.txt 可改成 *.csv ',' 是要給EXCEL 區隔
    
#with open('products.txt','w') as f:
with open('products.csv','w') as f:
    f.write('商品,價格\n') #加入欄位名稱
    for p in products:        
        f.write(p[0] + ',' + str(p[1]) + '\n') #p[1] 改為str .casting
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    