#連線DB
from dbConfig import conn, cur

def getProductsList():
    #拍賣首頁
    sql="SELECT `id_product`, `name`, `num` FROM `products` order by id_product asc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
    
def getCartList():
    sql="SELECT `id_product`, `name`, `buy_num` FROM `cart` order by id_product asc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def getBuyList():
    sql="SELECT `id_product`, `name`, `buy_num` FROM `buy` order by id_product asc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def addNewGood(name,num):
    #新增拍賣品
    sql="insert into products (name,num) values (%s,%s);"
    cur.execute(sql,(name,num))
    conn.commit()
    return True    

def addToCart(name,num):
    #新增cart
    sql="insert into cart (name,buy_num) values (%s,%s);"
    cur.execute(sql,(name,num))
    conn.commit()
    return True   

def UpdateGood(name,num):
    sql="UPDATE `products` SET `num`=%s WHERE `name`=%s;"
    cur.execute(sql,(num,name))
    conn.commit()
    return True    

def buy():
    sql="INSERT buy SELECT * FROM cart;"
    clear="TRUNCATE TABLE cart;"
    cur.execute(sql)
    cur.execute(clear)
    conn.commit()
    return True    

def clearCart():
    sql="TRUNCATE TABLE cart;"
    cur.execute(sql)
    conn.commit()
    return True    

def getProductNum(name):
    sql="SELECT `num` FROM `products` WHERE `name`='%s';"
    cur.execute(sql,(name))
    records = cur.fetchall()
    return records

def clearBuy():
    sql="TRUNCATE TABLE buy;"
    cur.execute(sql)
    conn.commit()
    return True    


'''
def getUserInfo(uid):
    #個人資料
    sql="SELECT `uid`,`uName` FROM `user` where uid = %s"
    cur.execute(sql,(uid,))
    records = cur.fetchall()
    return records

def getHistoryInfo():
    #歷史資料
    sql="SELECT `aid`,`id`,`price` FROM `auctioninfo` where uid = 1"
    cur.execute(sql)
    records = cur.fetchall()
    return records       
    
def bidding(uid,id,bidding):
    #競標
    sql="UPDATE `auctionlist` SET `price`=%s,`uName`= (select uName from user where uid = %s) WHERE id = %s and price < %s;"
    cur.execute(sql,(bidding,uid,id,bidding))
    conn.commit()
    return True

def addAuctionInfo(uid,id,bidding):
    #新增紀錄
    sql="insert into auctioninfo (uid,id,price) values (%s,%s,%s);"
    cur.execute(sql,(uid,id,bidding))
    conn.commit()
    return True    
    
'''