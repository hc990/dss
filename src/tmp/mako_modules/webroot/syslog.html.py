# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1363851927.408578
_enable_loop = True
_template_filename = '/home/huangchong/workspace/dashbroad/src/views/webroot/syslog.html'
_template_uri = '/webroot/syslog.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['body']


# SOURCE LINE 4
import time 

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
        # SOURCE LINE 53
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        paginator = context.get('paginator', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n<div class="box">\n\t<div class="box-header">\n\t\t<h1>syslog</h1>\n\t</div>\n\t<div class="box-content">\n\t<table id="product" class="table table-hover">\n\t\t\t<thead>\n\t\t\t\t<tr>\n\t\t\t\t\t<th align="center">\u7f16\u53f7</th>\n\t\t\t\t    <th align="center">syslog</th>\n\t\t\t\t</tr>\n\t\t\t</thead>\n\t\t\t<tbody>\n\t\t\t    ')
        # SOURCE LINE 18
        i=1 
        
        __M_writer(u'\n')
        # SOURCE LINE 19
        for c in paginator.page:
            # SOURCE LINE 20
            __M_writer(u'\t\t\t\t<tr style="cursor:pointer">\n\t\t\t\t    <td align="center" >')
            # SOURCE LINE 21
            __M_writer(unicode(i))
            __M_writer(u'</td>\n\t\t\t\t    ')
            # SOURCE LINE 22
            i=i+1 
            
            __M_writer(u'\n\t\t\t\t\t<td>')
            # SOURCE LINE 23
            __M_writer(unicode(c))
            __M_writer(u'</td>  \n\t\t\t\t</tr>\n')
        # SOURCE LINE 26
        __M_writer(u'\t\t        </tbody>\n\t\t    <tfoot>\n\t\t        <tr id="ui-detail-row" >\n\t\t        \t<td colspan="10">\n\t\t        \t\t<table id="ui-detail-content">\t\t        \t\t\t\n\t\t        \t\t</table>\n\t\t        \t</td>\n\t\t        </tr>\n\t\t\t</tfoot>\n\t</table>\n\t<div>\t\n\t\t\t\u7b2c ')
        # SOURCE LINE 37
        __M_writer(unicode(paginator.current_page))
        __M_writer(u' \u9875  \uff5c \u5171 ')
        __M_writer(unicode(paginator.page_count))
        __M_writer(u'\u9875   \n\t\t\t<!-- if there is a previous page print a back link -->\n')
        # SOURCE LINE 39
        if paginator.has_previous:
            # SOURCE LINE 40
            __M_writer(u'                  <a href="')
            __M_writer(unicode(paginator.previous_page_link(request)))
            __M_writer(u'"><< back</a>\n')
        # SOURCE LINE 42
        __M_writer(u'            <!-- if there is a previous and a next page print a divider -->\n')
        # SOURCE LINE 43
        if paginator.has_previous and paginator.has_next:
            # SOURCE LINE 44
            __M_writer(u'                  | \n')
        # SOURCE LINE 46
        __M_writer(u'            <!-- if there is a next page print a next link -->\n')
        # SOURCE LINE 47
        if paginator.has_next:
            # SOURCE LINE 48
            __M_writer(u'                    <a href="')
            __M_writer(unicode(paginator.next_page_link(request)))
            __M_writer(u'">next >></a>\n')
        # SOURCE LINE 50
        __M_writer(u'\t</div>\n</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


