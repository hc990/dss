'''
Created on 2012-11-8

@author: huangchong
'''
from config import options_setup
from core.scheduler import JzScheduler
from db.mongo import Mongo
from pysnmp.entity.rfc3413.oneliner import cmdgen
from tornado.options import define, options, options
import datetime
import json
import json
import logging
import string
import uuid

'''  
cron jobs 
'''
def job_function():    
    print '[x] Requesting'
    print 'set_bandwidth_job start at ', datetime.datetime.now()
        
def job_bandwidth():
    created_at = datetime.datetime.now()
    values = []
    logging.basicConfig()
    cg = cmdgen.CommandGenerator()
    Mongo.create(host='localhost', port=27017)
    created_at = datetime.datetime.now()
    comm_data = cmdgen.CommunityData('jztec', 'jztec',)   
    transport = cmdgen.UdpTransportTarget(('192.168.11.253', 161))
    variables = (1, 3, 6, 1, 2, 1, 2, 2, 1, 10) 
    errIndication, errStatus, errIndex, results = cg.nextCmd(comm_data, transport, variables) 
    for result in results:
        for name,val in result:
            Mongo.db.ui['bandwidths'].insert({'ip':'192.168.11.253','port': str(name[10:]),'type':0,'created_at':created_at,"value":int(val.prettyPrint())}) 
    variables = (1, 3, 6, 1, 2, 1, 2, 2, 1, 16) 
    errIndication, errStatus, errIndex, results = cg.nextCmd(comm_data, transport, variables) 
    for result in results:
        for name,val in result:
            Mongo.db.ui['bandwidths'].insert({'ip':'192.168.11.253','port': str(name[10:]),'type':1,'created_at':created_at,"value":int(val.prettyPrint())})

def dss_jobs():  
    sche = JzScheduler()
    sche.add_interval_job(job_bandwidth,seconds=5)
    sche.start()

if __name__ == '__main__':
    dss_jobs()