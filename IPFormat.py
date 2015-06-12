# -*- coding: utf-8 -*-

#点分形式的ip地址转换成十进制形式
def IP2Dec(ip):
    ipStr = ip.split('.')
    #print ipStr
    ipDec = 2**24*int(ipStr[0]) + 2**16*int(ipStr[1]) + 2**8*int(ipStr[2]) + int(ipStr[3])
    return ipDec

#CIDR形式的ip转换成ip段形式
def IPslash2IPseg(ipSlash):
    ipStr1 = ipSlash.split('/')
    ipBegin = IP2Dec(ipStr1[0])
    ipEnd = ipBegin + 2**(32-int(ipStr1[1])) - 1
    return ipBegin,ipEnd,Dec2IP(ipBegin),Dec2IP(ipEnd)

#十进制形式ip转换成点分形式
def Dec2IP(ipDex):
    ipDecInt = int(ipDex)
    ip = str(ipDecInt>>24) + '.' + str(ipDecInt>>16&0x00FF) + '.' + str(ipDecInt>>8&0x000000FF)+ '.' + str(ipDecInt&0x00000000FF)
    return ip
    
#计算cidr形式的ip list中总ip数量
def countip(list2c):
    len1 = len(list2c)
    count = 0 
    for i in xrange(len1):
        IPslash = list2c[i].strip()
        IPlen = int(IPslash2IPseg(IPslash)[1]) - int(IPslash2IPseg(IPslash)[0]) + 1
        #print IPlen
        count += IPlen
    return count
