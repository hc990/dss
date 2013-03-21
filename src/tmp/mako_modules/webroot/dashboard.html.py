# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1363763404.680474
_enable_loop = True
_template_filename = '/home/huangchong/workspace/dashbroad/src/views/webroot/dashboard.html'
_template_uri = '/webroot/dashboard.html'
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
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(u'\n<div class="quick-actions">\n\t\t\t\t<a href="#quickpost" class="modal">\n\t\t\t\t\t<span class="glyph new"></span>\n\t\t\t\t\t\u53c3\u6578\u4fee\u6539\n  </a>\n\n\t\t\t\t<a href="#">\n\t\t\t\t\t<span class="glyph export"></span>\n\t\t\t\t\t\u5c0e\u51faexcel\n  </a>\n\n\t\t\t\t<a href="#" class="disabled">\n\t\t\t\t\t<span class="glyph switch"></span>  \n\t\t\t\t\tTurn off\n  </a>\n\t\t\t</div>\n\n\t\t\t<div class="box column-left">\n\t\t\t\t<div class="box-header">\n\t\t\t\t\t<span class="glyph chart"></span>\n\t\t\t\t\t<h1>\u7528\u91cf\u7d71\u8a08</h1>\n\t\t\t\t</div>\n\n\t\t\t\t<ul class="statistics">\n\t\t\t\t\t<li>\n\t\t\t\t\t\t<a href="#">\n\t\t\t\t\t\t\t<span>1.3k</span>\n\t\t\t\t\t\t\tNew visitors\n      </a>\n\t\t\t\t\t</li>\n\t\t\t\t\t<li>\n\t\t\t\t\t\t<a href="#">\n\t\t\t\t\t\t\t<span>23</span>\n\t\t\t\t\t\t\tReturning visitors\n      </a>\n\t\t\t\t\t</li>\n\t\t\t\t\t<li>\n\t\t\t\t\t\t<a href="#">\n\t\t\t\t\t\t\t<span>16%</span>\n\t\t\t\t\t\t\tBounce rate\n      </a>\n\t\t\t\t\t</li>\n\t\t\t\t\t<li>\n\t\t\t\t\t\t<a href="#">\n\t\t\t\t\t\t\t<span>7%</span>\n\t\t\t\t\t\t\tIncrease since last month\n      </a>\n\t\t\t\t\t</li>\n\t\t\t\t</ul>\n\n\t\t\t\t<div class="action_bar">\n\t\t\t\t\t<!-- <a href="#" class="button small"><span class="glyph export"></span>Export data</a>\n\t\t\t\t\t<a href="#" class="button small"><span class="glyph print"></span>Print statistics</a> -->\n\t\t\t\t</div>\n\t\t\t</div>\n\n\t\t\t<div class="box column-right">\n\t\t\t\t<div class="box-header">\n\t\t\t\t\t<h1>\u7db2\u8def\u72c0\u6cc1</h1>\n\t\t\t\t</div>\n\n\t\t\t\t<table>\n\t\t\t\t\t<tbody>\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<td>Webhosting:</td>\n\t\t\t\t\t\t\t<td><strong>VPS Server 1</strong></td>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<td>Available space:</td>\n\t\t\t\t\t\t\t<td>239/1000 GB used</td>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<td>MySQL databases:</td>\n\t\t\t\t\t\t\t<td class="red">5/5 used</td>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<td>Email accounts:</td>\n\t\t\t\t\t\t\t<td class="red">25/25 used</td>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<td>Ruby version:</td>\n\t\t\t\t\t\t\t<td>1.9.3</td>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<td>Rails version:</td>\n\t\t\t\t\t\t\t<td>3.0.1</td>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t</tbody>\n\t\t\t\t</table>\n\n\t\t\t\t<div class="action_bar">\n\t\t\t\t\t<!-- <a href="#" class="button blue"><span class="glyph plus2"></span>Upgrade plan</a>\n\t\t\t\t\t<a href="#">Cancel subscription</a> -->\n\t\t\t\t</div>\n\t\t\t</div>\n\n\n\n\n\n\t\t\t<div class="box column-left">\n\t\t\t\t<div class="box-header">\n\t\t\t\t\t<h1>Bar Chart</h1>\n\t\t\t\t</div>\n\n\t\t\t\t<div class="box-content">\n\t\t\t\t\t<div id="jflot" style="width: 100%; height: 300px">\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\n\t\t\t</div>\n\t\t\t<script type="text/javascript">\n\t\t\t\tvar dataArray = [];\n\n\t\t\t\tfor (var i = 0; i < 13; i++) {\n\t\t\t\t\tdataArray.push([2000 + i, Math.random() * 11]);\n\t\t\t\t}\n\n\t\t\t\tvar data = [{\n\t\t\t\t\tlabel: "Yearly increase",\n\t\t\t\t\tdata: dataArray\n\t\t\t\t}];\n\n\t\t\t\tvar options = {\n\t\t\t\t\tlegend: {\n\t\t\t\t\t\tshow: true\n\t\t\t\t\t},\n\t\t\t\t\tbars: {\n\t\t\t\t\t\tshow: true\n\t\t\t\t\t},\n\t\t\t\t\tgrid: {\n\t\t\t\t\t\tborderWidth: 0\n\t\t\t\t\t},\n\t\t\t\t\txaxis: {\n\t\t\t\t\t\ttickSize: 1\n\t\t\t\t\t},\n\t\t\t\t\tyaxis: {\n\t\t\t\t\t\ttickSize: 1,\n\t\t\t\t\t\ttickDecimals: 0\n\t\t\t\t\t}\n\t\t\t\t};\n\n\t\t\t\t$(\'document\').ready(function () {\n\t\t\t\t\t$.plot($("#jflot"), data, options);\n\t\t\t\t});\n\t\t\t</script>\n\n\n\n\n\t\t\t<div class="box column-right">\n\t\t\t\t<div class="box-header">\n\t\t\t\t\t<h1>Line Chart</h1>\n\t\t\t\t</div>\n\n\t\t\t\t<div class="box-content">\n\t\t\t\t\t<div id="jflot2" style="width: 100%; height: 300px">\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\n\t\t\t</div>\n\t\t\t<script type="text/javascript">\n\t\t\t\tvar dataArray2 = [];\n\n\t\t\t\tfor (var i = 0; i < 13; i++) {\n\t\t\t\t\tdataArray2.push([2000 + i,  11]);\n\t\t\t\t}\n\n\t\t\t\tvar data2 = [{\n\t\t\t\t\tlabel: "Yearly increase",\n\t\t\t\t\tdata: dataArray2\n\t\t\t\t}];\n\n\t\t\t\tvar options2 = {\n\t\t\t\t\tlegend: {\n\t\t\t\t\t\tshow: true\n\t\t\t\t\t},\n\t\t\t\t\tpoints: {\n\t\t\t\t\t\tshow: true,\n\t\t\t\t\t\tradius: 3\n\t\t\t\t\t},\n\t\t\t\t\tlines: {\n\t\t\t\t\t\tshow: true\n\t\t\t\t\t},\n\t\t\t\t\tgrid: {\n\t\t\t\t\t\tborderWidth: 0\n\t\t\t\t\t},\n\t\t\t\t\txaxis: {\n\t\t\t\t\t\ttickSize: 1\n\t\t\t\t\t},\n\t\t\t\t\tyaxis: {\n\t\t\t\t\t\ttickSize: 1,\n\t\t\t\t\t\ttickDecimals: 0\n\t\t\t\t\t}\n\t\t\t\t};\n\n\t\t\t\t$(\'document\').ready(function () {\n\t\t\t\t\t$.plot($("#jflot2"), data2, options2);\n\t\t\t\t});\n\t\t\t</script>\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


