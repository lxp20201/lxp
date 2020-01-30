# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580296507.175095
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/registration/password_reset_done.html'
_template_uri = 'registration/password_reset_done.html'
_source_encoding = 'utf-8'
_exports = []


from django.utils.translation import ugettext as _ 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n<header>\n  <h2>')
        __M_writer(filters.decode.utf8(_("Password reset successful")))
        __M_writer(u'</h2>\n  <hr>\n</header>\n\n<div class="message">\n  <p>')
        __M_writer(filters.decode.utf8(_("We've e-mailed you instructions for setting your password to the e-mail address you submitted. You should be receiving it shortly.")))
        __M_writer(u'</p>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 27, "16": 1, "18": 0, "23": 1, "24": 3, "25": 3, "26": 8, "27": 8}, "uri": "registration/password_reset_done.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/registration/password_reset_done.html"}
__M_END_METADATA
"""
