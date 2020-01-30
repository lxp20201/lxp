# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580210685.128269
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/index_overlay.html'
_template_uri = u'index_overlay.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<h1>')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_(u"Welcome to {platform_name}")).format(platform_name=settings.PLATFORM_NAME))))
        __M_writer(u'</h1>\n')
        __M_writer(u'<p>')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("It works! Powered by Open edX{registered_trademark}")).format(registered_trademark=HTML("<sup style='font-size: 65%'>&reg;</sup>")))))
        __M_writer(u'</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 10, "33": 10, "39": 33, "16": 3, "21": 1, "27": 1, "28": 6, "29": 8, "30": 8, "31": 10}, "uri": "index_overlay.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/index_overlay.html"}
__M_END_METADATA
"""
