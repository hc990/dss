'''
Created on 2013-3-18

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
import datetime,hashlib,json
from views.paginator import Paginator

@route('/syslog')
class SyslogHandler(BaseHandler):

    def get(self):
        template_values = {}
        s = []
        with open('/var/log/firewall/log.log') as f:
            for a in f:
                s.append(a)
        #page info
        k = list(reversed(s))
        page = self.get_argument('page', 1)
        page = page if page >= 1 else 1    
        #get the document count param
        count = self.get_argument('count', 10)
        count = count if count >= 1 else 10
        paginator = Paginator(k, page, count, len(k))
        template_values['paginator'] = paginator
        self.render_template('/webroot/syslog.html', **template_values)
