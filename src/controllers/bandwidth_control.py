'''
Created on 2013-3-11

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
import datetime,time
import hashlib  
import json
        
        
@route('/dashboard')
class DashboardHandler(BaseHandler):

    def get(self):  
        port = self.get_argument("port", None)
        bandwidths = [bandwidth for bandwidth  in Mongo.db.ui['bandwidths'].find({"port":'18',"type":0}).sort('created_at',-1)[0:11]]
        times = []
        values = []
        now = datetime.datetime.now()
        init_value = bandwidths[10]['value']
        print type(bandwidths)
        bandwidths.reverse()
        i =0
        for bandwidth in bandwidths[1:11]:
#             time.mktime(bandwidth['created_at'].timetuple())
            i  = i+1
            time =  i
            print time
            times.append(time)
            value = bandwidth['value']
            values.append(value-init_value)
            init_value = value        
        template_values = {}
        template_values['times'] = times
        template_values['values'] = values
        template_values['port'] = '18'
        self.render_template("/webroot/dashboard.html", **template_values) 
    
#     def post(self):
#         port = self.get_argument("port", None)
#         bandwidths = [[user2['value'],user2['created_at']] for user2  in Mongo.db.ui['bandwidths'].find({"port":'17'}).sort('created_at',-1)[0:10]]
#         
#         template_values = {}
#         template_values['port'] = bandwidths
#         self.render_template("/webroot/icmp.html", **template_values) 

        