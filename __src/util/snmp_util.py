# -*- coding: utf-8 -*-
'''
Created on 2013-3-20

@author: huangchong
'''
from core.basehandler import BaseHandler
from db.mongo import Mongo
from pyasn1.codec.ber import encoder
from pysnmp.carrier.asynsock.dgram import udp
from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import api, rfc1902
from pysnmp.proto.rfc1902 import Gauge32
from tornado.web import authenticated
from views.decorators import role_required, route
from views.paginator import Paginator
import datetime
import hashlib
import json



def getTrunk(ip,port,agent,communication):
    macAddr = []
    macList = []
    portList = []
    macStrList = []
    linkPort = []
    oid1 = (1,3,6,1,2,1,4,22,1,2)#ARP表oid
    oid2 = (1,3,6,1,2,1,17,4,3,1,2)#mac端口对应表lid

    
    gen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBinds = gen.nextCmd(
        cmdgen.CommunityData(agent, communication,1),
        cmdgen.UdpTransportTarget((ip,port)),
        oid1,
        )
    #获取ARP表里的mac地址
    for varBind in varBinds:
        for name,val in varBind:
            macAddr.append(val.prettyPrint(0))
            print val.prettyPrint(0)
    
    gen.ignoreNonIncreasingOid = True#让oid可以非递增
    errorIndication, errorStatus, errorIndex, varBinds = gen.nextCmd(
        cmdgen.CommunityData(agent, communication,1),
        cmdgen.UdpTransportTarget((ip,port)),
        oid2,
        )
    #获取mac端口对应关系
    for varBind in varBinds:
        for name,val in varBind:
            macList.append(name[-6:])
            portList.append(val.prettyPrint())
            print name,val
    #将十进制mac地址转化为16进制的字符串
    for item in macList:
        temp = ''
        for part in item:
            temp += str(hex(int(part)))[2:]
        temp = '0x' + temp
        macStrList.append(temp)
    for item in macAddr:#获取端口号
        if item in macStrList:
            index = macStrList.index(item)
            linkPort.append(portList[index])
    #去除列表中的重复元素
    linkPort = {}.fromkeys(linkPort).keys()#linkPort = list(set(linkPort))
    return linkPort


if __name__ == '__main__':
    print getTrunk('192.168.11.253',161,'jztec','jztec')
