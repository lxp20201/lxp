# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284776.863576
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/common/templates/xblock_wrapper.html'
_template_uri = 'xblock_wrapper.html'
_source_encoding = 'utf-8'
_exports = []



from openedx.core.djangolib.js_utils import dump_js_escaped_json


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        content = context.get('content', UNDEFINED)
        classes = context.get('classes', UNDEFINED)
        data_attributes = context.get('data_attributes', UNDEFINED)
        js_init_parameters = context.get('js_init_parameters', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div class="')
        __M_writer(filters.decode.utf8(' '.join(classes) ))
        __M_writer(u'" ')
        __M_writer(filters.decode.utf8(data_attributes))
        __M_writer(u'>\n')
        if js_init_parameters:
            __M_writer(u'  <script type="json/xblock-args" class="xblock-json-init-args">\n    ')
            __M_writer(dump_js_escaped_json(js_init_parameters ))
            __M_writer(u'\n  </script>\n')
        __M_writer(u'  ')
        __M_writer(filters.decode.utf8(content))
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 5, "33": 5, "34": 6, "35": 7, "36": 8, "37": 8, "38": 11, "39": 11, "40": 11, "46": 40, "16": 2, "20": 0, "29": 4, "30": 5, "31": 5}, "uri": "xblock_wrapper.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/common/templates/xblock_wrapper.html"}
__M_END_METADATA
"""
