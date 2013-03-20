# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1363156189.625
_enable_loop = True
_template_filename = 'E:\\workspacePY\\dashbroad\\src/views/account/login.html'
_template_uri = '/account/login.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['body']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!DOCTYPE html>\r\n<html xmlns="http://www.w3.org/1999/xhtml"> \r\n')
        # SOURCE LINE 37
        __M_writer(u' \r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'  \r\n<head> \r\n\t<meta http-equiv="Content-type" content="text/html; charset=utf-8" /> \r\n\t<title>Login | </title> \r\n\t<link rel="stylesheet" href="/static/css/reset.css" type="text/css" media="screen" title="no title" />\r\n\t<link rel="stylesheet" href="/static/css/text.css" type="text/css" media="screen" title="no title" />\r\n\t<link rel="stylesheet" href="/static/css/form.css" type="text/css" media="screen" title="no title" />\r\n\t<link rel="stylesheet" href="/static/css/buttons.css" type="text/css" media="screen" title="no title" />\r\n\t<link rel="stylesheet" href="/static/css/login.css" type="text/css" media="screen" title="no title" />\r\n</head> \r\n\r\n<div id="login">\r\n\t<h1></h1>  \r\n\t<div id="login_panel">\r\n\t\t<form action="./login" method="post" accept-charset="utf-8">\t\t\r\n\t\t\t<div class="login_fields">\r\n\t\t\t\t<div class="field">\r\n\t\t\t\t\t<label for="email">Email</label>\r\n\t\t\t\t\t<input type="text" name="email" value="" id="email" tabindex="1" placeholder="email@example.com" />\t\t\r\n\t\t\t\t</div>\r\n\t\t\t\t\r\n\t\t\t\t<div class="field">\r\n\t\t\t\t\t<label for="password">Password <small><a href="javascript:;">Forgot Password?</a></small></label>\r\n\t\t\t\t\t<input type="password" name="password" value="" id="password" tabindex="2" placeholder="password" />\t\t\t\r\n\t\t\t\t</div>\r\n\t\t\t</div> <!-- .login_fields -->\r\n\t\t\t\r\n\t\t\t<div class="login_actions">\r\n\t\t\t\t<button type="submit" class="btn btn-orange" tabindex="3">Login</button>\r\n\t\t\t</div>\r\n\t\t</form>\r\n\t</div> <!-- #login_panel -->\t\t\r\n</div> <!-- #login -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


