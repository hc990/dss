# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1364197151.115804
_enable_loop = True
_template_filename = '/home/huangchong/workspace/dashbroad/src/views/webroot/dashboard.html'
_template_uri = '/webroot/dashboard.html'
_source_encoding = 'utf-8'
from views.filters import Cycler,Filters
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
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        values = context.get('values', UNDEFINED)
        port = context.get('port', UNDEFINED)
        times = context.get('times', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(u'\n\t\t\t<div class="box column-left">\n\t\t\t\t<div class="box-header">\n\t\t\t\t\t<h1>Line Chart</h1>\n\t\t\t\t</div>\n\t\t\t\t<div class="box-content">\n\t\t\t\t\t<div id="jflot2" style="width: 100%; height: 300px">\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\n\t\t\t</div>\n\t\t\t<script type="text/javascript">\n\t\t\t\tvar dataArray2 = [];\n\t\t\t\tvar times = ')
        # SOURCE LINE 19
        __M_writer(unicode(times))
        __M_writer(u'\n\t\t\t\tvar values = ')
        # SOURCE LINE 20
        __M_writer(unicode(values))
        __M_writer(u' \n\t\t\t\tfor (var i = 0; i < 5 ; i++) {  \n\t\t\t\t\tdataArray2.push([times[i],values[i]]);\n\t\t\t\t}\n\t\t\t\tvar data2 = [{\n\t\t\t\t\tlabel: "\u6d41\u91cf\u5206\u65f6\u6570\u636e \u7aef\u53e3:"+')
        # SOURCE LINE 25
        __M_writer(unicode(port))
        __M_writer(u',\n\t\t\t\t\tdata: dataArray2\n\t\t\t\t}];\n\n\t\t\t\tvar options2 = {\n\t\t\t\t\tlegend: {\n\t\t\t\t\t\tshow: true\n\t\t\t\t\t},\n\t\t\t\t\tpoints: {\n\t\t\t\t\t\tshow: true,\n\t\t\t\t\t\tradius: 3\n\t\t\t\t\t},\n\t\t\t\t\tlines: {\n\t\t\t\t\t\tshow: true\n\t\t\t\t\t},\n\t\t\t\t\tgrid: {\n\t\t\t\t\t\tborderWidth: 0\n\t\t\t\t\t},\n\t\t\t\t\txaxis: {\n\t\t\t\t\t\ttickSize: 1\n\t\t\t\t\t},\n\t\t\t\t\tyaxis: {\n\t\t\t\t\t\ttickSize: 1,\n\t\t\t\t\t\ttickDecimals: 0\n\t\t\t\t\t}\n\t\t\t\t};\n\n\t\t\t\t$(\'document\').ready(function () {\n\t\t\t\t\t$.plot($("#jflot2"), data2, options2);\n\t\t\t\t});\n\t\t\t</script>\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


