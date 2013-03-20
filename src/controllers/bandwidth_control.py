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
import datetime   
import hashlib  
import json
  
@route('/widthchart')
class WidthChartHandler(BaseHandler):

    def get(self):
        template_values = {}
        template_values['values'] = None
        self.render_template('/webroot/width.html', **template_values)
        
        
@route('/dashboard')
class DashboardHandler(BaseHandler):

    def get(self):
        template_values = {}
        self.render_template('/webroot/dashboard.html', **template_values) 

        