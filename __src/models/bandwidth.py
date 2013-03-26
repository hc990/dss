'''
Created on 2012/2/22

@author: ishida
'''

from db.mongo import Mongo
from mongokit import *
from tornado import options
import datetime
import hashlib
import hmac
import base64
import re
import json
    

@Mongo.db.connection.register
class Bandwidth(Document):
    structure = {
                 '_id':unicode,
                 'ip':basestring,
                 'values':list
                 }
    use_dot_notation = True
    
    @staticmethod
    def lookup(b_id):
        return Mongo.db.ui['bandwidths'].find_one({'_id' : b_id})
    
    @staticmethod
    def getBandwidths():
        return Mongo.db.ui['bandwidths'].find()
        
    '''
    creates a new user instance. unsaved
    '''
    @staticmethod
    def instance(ip):
        bandwidth = Bandwidth()
        bandwidth.ip = ip    
        bandwidth.values = []
        return bandwidth
    

