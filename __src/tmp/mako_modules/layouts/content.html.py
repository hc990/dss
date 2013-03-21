# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1363856514.668531
_enable_loop = True
_template_filename = u'/home/huangchong/workspace/dashbroad/src/views/layouts/content.html'
_template_uri = u'/layouts/content.html'
_source_encoding = 'utf-8'
from views.filters import Cycler,Filters
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
    return runtime._inherit_from(context, u'/layouts/base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_content():
            __M_caller = context.caller_stack._push_frame()
            try:
                next = context.get('next', UNDEFINED)
                __M_writer = context.writer()
                # SOURCE LINE 47
                __M_writer(u'\n\t\t\t\t\t')
                # SOURCE LINE 48
                __M_writer(unicode(next.body()))
                __M_writer(u'\n\t\t\t\t')
                return ''
            finally:
                context.caller_stack._pop_frame()
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n\t<!-- Primary navigation -->\n\t<nav id="primary">\n\t\t<ul>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../syslog"><span class="glyph dashboard"></span>syslog\u67e5\u8be2</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../dashboard"><span class="glyph pencil"></span>\u6d41\u91cf\u67e5\u8be2</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../icmp"><span class="glyph eye"></span>\u8fde\u901a\u67e5\u8be2</a>\n\t\t\t\t\t\t\t</li>\n                            <li>\n\t\t\t\t\t\t\t\t<a href="../pwdchange"><span class="glyph pencil"></span>\u5bc6\u7801\u91cd\u7f6e</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t<li class="bottom">\n\t\t\t\t<a href="/logout">\n\t\t\t\t\t<span class="glyph quit"></span>\n\t\t\t\t\t\u9000\u51fa\u7cfb\u7edf\n          </a>\n\t\t\t</li>\n\t\t</ul>\n\t</nav>\n\t<!-- Secondary navigation -->\n\t<nav id="secondary" style="width:10px; overflow:hidden;">\n\t\t<ul>\n\t\t\t<li><a href="../charts/linechart.html">Line chart</a></li>\n\t\t\t<li><a href="../charts/barchart.html">Bar chart</a></li>\n\t\t\t<li><a href="../charts/realtime.html">Realtime chart</a></li>\n\t\t\t<li><a href="../charts/piechart.html">Pie chart</a></li>\n\t\t</ul>\n\n\t\t<div id="notifications">\n\t\t\t<ul>\n\t\t\t</ul>\n\t\t</div>\n\t</nav>\n\t\n\t<section id="maincontainer">\n\t\t<div id="main" class="container_12">\n\t\t')
        # SOURCE LINE 46
        runtime._include_file(context, u'/shared/header.html', _template_uri)
        __M_writer(u'\n\t\t\t\t')
        # SOURCE LINE 49
        __M_writer(u'\n\t\t\t\t')
        # SOURCE LINE 50
        __M_writer(unicode(body_content()))
        __M_writer(u'\n\t\t</div>\n\t</section>\n\n\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


