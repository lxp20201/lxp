# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580211856.242005
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/common/djangoapps/pipeline_mako/templates/mako/js.html'
_template_uri = 'mako/js.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        async = context.get('async', UNDEFINED)
        type = context.get('type', UNDEFINED)
        defer = context.get('defer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<script ')
        if async:
            __M_writer(u'async ')
        if defer:
            __M_writer(u'defer ')
        __M_writer(u'type="')
        __M_writer(filters.decode.utf8(type))
        __M_writer(u'" src="')
        __M_writer(filters.decode.utf8( url ))
        __M_writer(u'" charset="utf-8"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 8, "33": 8, "34": 8, "40": 34, "16": 0, "25": 1, "26": 2, "27": 3, "28": 5, "29": 6, "30": 8, "31": 8}, "uri": "mako/js.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/common/djangoapps/pipeline_mako/templates/mako/js.html"}
__M_END_METADATA
"""
