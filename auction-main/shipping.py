#!C:\Python311\python.exe
# -*- coding: utf-8 -*-
# 處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import control as ctrl
#連線DB
from dbConfig import conn, cur

print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>清空購物車</title>
<style type="text/css">
body {width:600px; margin:10px auto;}
#content {background-color:DarkOliveGreen; margin:20px; padding:20px; border:2px solid ivory; font-size: 14pt; color:#ff9; line-height:28px}
a {color: yellow}
</style>
</head>
<body>
<div id="content">
""")

records = ctrl.getProductsList()
#print(records)
for (id_product,name,num) in records:
	print(f"<p>ID:{id_product} 名稱:{name} 剩餘數量:{num}</p>")
print("<hr></hr>")
records = ctrl.getBuyList()
for (id_product,name,num) in records:
	print(f"<p>ID:{id_product} 名稱:{name} 待出貨數量:{num}</p>")

print('''<div >
<fieldset>
<form method="post" action="updateGood2.py">
要出貨的商品名字：<input type="text" name='name'><br>
出貨後商品數量：（剩餘數量-待出貨數量）<input type="text" name='num'><br>
<input type="submit"><br>''')

print("</body></html>")



