# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1347440164.968
_enable_loop = True
_template_filename = 'E:\\workspacePY\\let\\src/views/site/index.html'
_template_uri = '/site/index.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['body']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/layouts/content.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<div id="page-header">\n\t<div class="title">\n\t\t\u6b22\u8fce\u4f7f\u7528\uff01\n\t</div>\n\t<div class="subtitle">\n\t\tversion 1.0\t\n\t</div>\n</div>\n<div class="form" style="margin:0 auto 0 auto;width: 250px;">\n\t<div class="title">\n\t\t\u8bf7\u767b\u9646\n\t</div>\n\t<form action="/login" method="post"> \n\t\t<input type="hidden" name="next" value="')
        # SOURCE LINE 17
        __M_writer(unicode(next))
        __M_writer(u'" /> \n\t\t<div class="field">\n\t\t\t<label for="username" class="label">\n\t\t\t\t\u7528\u6237\u540d\n\t\t\t</label>\n\t\t\t<div class="input">\n\t\t\t\t<input type="text" id="username" name="username"/>\n\t\t\t</div>\n\t\t</div>\n\t\t\n\t\t<div class="field">\n\t\t\t<label for="password" class="label">\n\t\t\t\t\u5bc6\u7801\n\t\t\t</label>\n\t\t\t<div class="input">\n\t\t\t\t<input type="password" id="password" name="password"/>\n\t\t\t</div>\n\t\t</div>\n\t\t\n\t\t<div class="field">\n\t\t\t<label for="keep_logged_in"><input type="checkbox" name="keep_logged_in" id="keep_logged_in" /> keep me logged in</label>\n\t\t</div> \n\t\t\n\t\t<div class="buttons">\n\t\t\t<input type="submit" value="Login" class="button"   />\n\t\t</div>\n\t</form>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


