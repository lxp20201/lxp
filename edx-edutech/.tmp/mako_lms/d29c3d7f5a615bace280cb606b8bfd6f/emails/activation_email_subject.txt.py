# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580294264.287915
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/emails/activation_email_subject.txt'
_template_uri = 'emails/activation_email_subject.txt'
_source_encoding = 'utf-8'
_exports = []


from django.utils.translation import ugettext as _ 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        platform_name = context.get('platform_name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(filters.decode.utf8(_("Action Required: Activate your {platform_name} account").format(platform_name=platform_name)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 26, "16": 2, "18": 0, "24": 2, "25": 3, "26": 3}, "uri": "emails/activation_email_subject.txt", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/emails/activation_email_subject.txt"}
__M_END_METADATA
"""
