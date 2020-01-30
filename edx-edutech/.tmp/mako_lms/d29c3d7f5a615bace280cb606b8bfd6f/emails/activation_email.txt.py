# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580294264.297929
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/emails/activation_email.txt'
_template_uri = 'emails/activation_email.txt'
_source_encoding = 'utf-8'
_exports = []


from django.utils.translation import ugettext as _ 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        support_url = context.get('support_url', UNDEFINED)
        site = context.get('site', UNDEFINED)
        lms_url = context.get('lms_url', UNDEFINED)
        platform_name = context.get('platform_name', UNDEFINED)
        key = context.get('key', UNDEFINED)
        is_secure = context.get('is_secure', UNDEFINED)
        support_email = context.get('support_email', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(filters.decode.utf8(_("You're almost there! Use the link to activate your account to access engaging, high-quality "
"{platform_name} courses. Note that you will not be able to log back into your account until "
"you have activated it.").format(platform_name=platform_name)))
        __M_writer(u'\n\n')
        if is_secure:
            __M_writer(u'https://')
            __M_writer(filters.decode.utf8( site ))
            __M_writer(u'/activate/')
            __M_writer(filters.decode.utf8( key ))
            __M_writer(u'\n')
        else:
            __M_writer(u'http://')
            __M_writer(filters.decode.utf8( site ))
            __M_writer(u'/activate/')
            __M_writer(filters.decode.utf8( key ))
            __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(filters.decode.utf8(_("Enjoy learning with {platform_name}.").format(platform_name=platform_name)))
        __M_writer(u'\n\n')
        __M_writer(filters.decode.utf8(_("The {platform_name} Team").format(platform_name=platform_name)))
        __M_writer(u'\n\n')
        __M_writer(filters.decode.utf8(_("If you need help, please use our web form at {support_url} or email {support_email}.").format(
  support_url=support_url, support_email=support_email
)))
        __M_writer(u'\n\n')
        __M_writer(filters.decode.utf8(_("This email message was automatically sent by {lms_url} because someone attempted to create an "
"account on {platform_name} using this email address.").format(
  lms_url=lms_url, platform_name=platform_name
)))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "18": 0, "30": 2, "31": 3, "34": 5, "35": 7, "36": 8, "37": 8, "38": 8, "39": 8, "40": 8, "41": 9, "42": 10, "43": 10, "44": 10, "45": 10, "46": 10, "47": 12, "48": 13, "49": 13, "50": 15, "51": 15, "52": 17, "55": 19, "56": 21, "65": 56}, "uri": "emails/activation_email.txt", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/emails/activation_email.txt"}
__M_END_METADATA
"""
