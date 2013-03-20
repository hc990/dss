# -*- coding: utf-8 -*-'''Created on 2012-3-19@author: zongzong'''from core.basehandler import BaseHandlerfrom db.mongo import Mongofrom tornado.web import authenticatedfrom views.decorators import routefrom views.decorators import role_requiredfrom models.user import Userfrom models.product import Productfrom models.exchange import Exchangefrom views.paginator import Paginator  import datetime@route('/manage')class ManagerHandler(BaseHandler):           @authenticated       @role_required('/manage')    def post(self):             cname = self.get_argument("cname", '')        oname = self.current_user['_id']        status = self.get_argument("status", None)        #page info        page = self.get_argument('page', 1)        page = page if page >= 1 else 1        #get the document count param        count = self.get_argument('count', 10)        count = count if count >= 1 else 10        template_values = {}        if status is not None and status != '':            products = Product.getProducts(cname, status, oname)            template_values['status'] = status        else:            products = Product.getAllProducts(cname, oname)            template_values['status'] = ''        #create a Paginator object        paginator = Paginator(products, page, count, len(products))        template_values['cname'] = cname        template_values['paginator'] = paginator        self.render_template('/site/manage.html', **template_values)    @authenticated   #   @role_required('/manage')    def get(self):        oname = self.get_current_user()['_id']        products = Product.getOperatorProducts(oname)        #page info        page = self.get_argument('page', 1)        page = page if page >= 1 else 1        #get the document count param        count = self.get_argument('count', 10)        count = count if count >= 1 else 10        paginator = Paginator(products, page, count, len(products))        template_values = {}        template_values['cname'] = ''        template_values['status'] = ''        template_values['paginator'] = paginator        self.render_template('/site/manage.html', **template_values)        @route('/custorm_add')class AddCustormHandler(BaseHandler):        @authenticated    @role_required('/custorm_add')    def get(self):        template_values = {}        template_values['next'] = self.get_argument('next', '/')        oname = self.current_user['_id']        template_values['exchanges'] = Exchange.get_active_exchanges(oname, 1)        self.render_template('/site/custorm_add.html', **template_values)        @authenticated    @role_required('/custorm_add')    def post(self):          oname = self.get_username()        address = self.get_argument("address", None)        phonenum = self.get_argument("phonenum", None)          cname = self.get_argument("cname", None)        vlan = self.get_argument("vlan", '')        begin_at = datetime.datetime.strptime(self.get_argument("begin_at", None),"%m/%d/%Y %H:%M")        suspended_at = datetime.datetime.strptime(self.get_argument("suspended_at", None),"%m/%d/%Y %H:%M")        continue_to = self.get_argument("continue_to", None)         # email for custorm add         email = self.get_argument("email", '')                        e_id = self.get_argument("e_id", None)            port = self.get_argument("port", '')                   ctype = self.get_argument("type", None)        price = self.get_argument("price", None)           Product.insert(oname, 1, cname, e_id, vlan, port, begin_at, suspended_at, continue_to, ctype, address, phonenum, price, email)             #/*signup for cusormer**/        user = User.lookup(cname)          if not user:            from util import password_util              from util import mail_util               password = password_util.pass_gen(15,)              mail_util.sent_mail("", '%s, %s' % (cname,password) \            , cname, email)                   user = User.instance(cname, password, 3)               Mongo.db.ui['users'].insert(user)            self.redirect("/manage")          @route('/custorm_mod')  class ModifiedCustormHandler(BaseHandler):        @authenticated    @role_required('/custorm_mod')    def get(self):        _cid = self.get_argument("name", None)        status = self.get_argument("status", None)        percent = self.get_argument("percent", None)        begin_at = datetime.datetime.strptime(self.get_argument("begin_at", None),"%m/%d/%Y %H:%M")        suspended_at = datetime.datetime.strptime(self.get_argument("suspended_at", None) ,"%m/%d/%Y %H:%M")        Product.update(status, percent, begin_at, suspended_at)          custormers = Product.getAllProducts()        template_values = {}        template_values['products'] = custormers        self.render_template('/site/manage.html', **template_values)        @route('/custorm_del')class DelCustormHandler(BaseHandler):    def post(self):        _cid = self.get_argument("c_id", None)          Product.updateProduct(_cid, 0)          self.finish("finished")        @route('/custorm_active')class ActiveCustormHandler(BaseHandler):    def post(self):        _cid = self.get_argument("c_id", None)        Product.updateProduct(_cid, 1)          self.finish("finished")                                        