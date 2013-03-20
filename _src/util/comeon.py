# -*- coding: utf-8 -*-'''Created on 2012-9-10@author: zongzong'''#coding=utf-8from pysnmp.entity.rfc3413.oneliner import cmdgen, ntforgfrom pysnmp.carrier.asynsock.dispatch import AsynsockDispatcherfrom pysnmp.carrier.asynsock.dgram import udpfrom pyasn1.codec.ber import encoderfrom pysnmp.proto import api    from pysnmp.proto import rfc1902def logger(f, log):    f.write(log)    f.write('\n')def walk(ip, oid, gen='agent', comm='public', ver=1, port=161, Cc=False):    nameList = []    valList = []    communityData = cmdgen.CommunityData(gen, comm, ver,)    snmpTarget = cmdgen.UdpTransportTarget((ip, port))    cmdObj = cmdgen.CommandGenerator()    if Cc:        cmdObj.ignoreNonIncreasingOid = Cc    errorIndication, errorStatus, errorIndex, varBindTable = cmdObj.nextCmd(communityData, snmpTarget, oid)    if errorIndication or errorStatus or errorIndex:        pass    for varBind in varBindTable:        for name, val in varBind:            nameList.append(name.prettyPrint())            valList.append(val.prettyPrint())    return (nameList, valList)def update(ip, oid, gen='agent', comm='public', ver=1, port=161, Cc=False):    verID = api.protoVersion1    pMod = api.protoModules[verID]    errorIndication = ntforg.NotificationOriginator().sendNotification(#    communityData = cmdgen.CommunityData(gen, comm, ver),    cmdgen.UsmUserData('my-user', 'my-authkey', 'my-privkey'),    cmdgen.UdpTransportTarget((ip, 162)),    'trap',    (('SNMPv2-MIB', 'coldStart'),),    ((1, 3, 6, 1, 2, 1, 2, 2, 1, 5, 4), pMod.Integer(10000)))#(ip, oid, gen='agent', comm='public', ver=1, port=161, Cc=False):if __name__ == '__main__':    for i in  walk('192.168.11.253', (1, 3, 6, 1, 2, 1, 2, 2, 1), 'agent', 'jztec'):        print i[118]    update('192.168.11.253', (1, 3, 6, 1, 2, 1, 2, 2, 1), 'agent', 'jztec')#     1.3.6.1.2.1.2.2.1.5.4    for i in  walk('192.168.11.253', (1, 3, 6, 1, 2, 1, 2, 2, 1), 'agent', 'jztec'):        print i[118]        