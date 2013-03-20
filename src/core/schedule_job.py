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
30min start the job
'''
    
def job_function():    
    print " [x] Requesting"
    print 'set_bandwidth_job start at ', datetime.datetime.now()
    
    
def job_bandwidth(id):
    values = []
    logging.basicConfig() 
    cg = cmdgen.CommandGenerator() 
    comm_data = cmdgen.CommunityData('jztec', 'jztec',) 
    transport = cmdgen.UdpTransportTarget(('192.168.11.253', 161))
    variables = (1, 3, 6, 1, 2, 1, 2, 2, 1, 10) 
    errIndication, errStatus, errIndex, results = cg.nextCmd(comm_data, transport, variables)  
    for result in results:
        for name,val in result:
            a = name[10:]
            print a 
            c = {'port':str(a),'created_at':None,'value':val.prettyPrint()}
            print c
            Mongo.db.ui['bandwidths'].update({"_id":id}, {'$push':{'values':[{'port':a,'created_at':datetime.datetime.now(),'value':val.prettyPrint()}]}} )   
             
#     variables = (1, 3, 6, 1, 2, 1, 2, 2, 1, 16) 
#     errIndication, errStatus, errIndex, results = cg.nextCmd(comm_data, transport, variables) 
#     for result in results:
#         for name,val in result:
#             ports.append(name[10:])
#             values.append(int(val.prettyPrint()))
     
   
     
    
def dss_jobs(id):
    Mongo.create(host='localhost', port=27017)
    id = Mongo.db.ui['bandwidths'].insert({'ip':'192.168.11.253'})
    sche = JzScheduler()
    sche.add_interval_job(job_bandwidth,seconds=5,args=[id])
    sche.start()



if __name__ == '__main__':
    dss_jobs(id)