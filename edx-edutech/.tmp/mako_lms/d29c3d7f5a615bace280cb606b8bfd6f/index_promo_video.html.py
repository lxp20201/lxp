# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580211856.381488
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/index_promo_video.html'
_template_uri = u'index_promo_video.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        show_homepage_promo_video = context.get('show_homepage_promo_video', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if show_homepage_promo_video:
            __M_writer(u'  <a href="#video-modal" class="media" rel="leanModal">\n    <div class="hero">\n      <div class="play-intro"></div>\n    </div>\n  </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 1, "24": 4, "30": 24, "22": 1, "23": 3}, "uri": "index_promo_video.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/index_promo_video.html"}
__M_END_METADATA
"""
