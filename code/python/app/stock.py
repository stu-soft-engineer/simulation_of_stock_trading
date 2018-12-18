#! usr/bin/python3
# -*- coding: utf-8 -*-


def getStockDM(stockID):
    # 获取股票是sh还是sz
    i = {5: 'sh', 6: 'sh', 9: 'sz', 0: 'sz', 1: 'sz', 2: 'sz', 3: 'sz'}
    h = int(int(stockID)/100000)
    try:
        dm = i[h]
    except:
        return None
    else:
        return dm


def getPrice(stockID):
    return 1.0
