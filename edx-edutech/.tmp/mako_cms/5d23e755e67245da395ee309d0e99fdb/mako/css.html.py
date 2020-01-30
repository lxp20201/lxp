# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580361385.739143
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/common/djangoapps/pipeline_mako/templates/mako/css.html'
_template_uri = 'mako/css.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        media = context.get('media', UNDEFINED)
        charset = context.get('charset', UNDEFINED)
        type = context.get('type', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<link href="')
        __M_writer(filters.decode.utf8(url))
        __M_writer(u'" rel="stylesheet" type="')
        __M_writer(filters.decode.utf8(type))
        __M_writer(u'" ')
        if media:
            __M_writer(u'media="')
            __M_writer(filters.decode.utf8(media))
            __M_writer(u'" ')
        if title:
            __M_writer(u'title="')
            __M_writer(filters.decode.utf8(title))
            __M_writer(u'" ')
        if charset:
            __M_writer(u'charset="')
            __M_writer(filters.decode.utf8(charset))
            __M_writer(u'" ')
        __M_writer(u'/>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 3, "33": 3, "34": 3, "35": 5, "36": 6, "37": 6, "38": 6, "39": 8, "40": 9, "41": 9, "42": 9, "43": 11, "16": 0, "49": 43, "26": 1, "27": 1, "28": 1, "29": 1, "30": 1, "31": 2}, "uri": "mako/css.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/common/djangoapps/pipeline_mako/templates/mako/css.html"}
__M_END_METADATA
"""
