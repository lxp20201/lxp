# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580294266.81303
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/registration/account_activation_sidebar_notice.html'
_template_uri = 'registration/account_activation_sidebar_notice.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        activate_account_message = context.get('activate_account_message', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n<div class="profile-sidebar" role="region" aria-labelledby="account-activation-title">\n  <header class="profile">\n    <h2 id="account-activation-title" class="account-activation-title sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Account Activation Info"))))
        __M_writer(u': </h2>\n  </header>\n  <div class="user-info">\n    <ul>\n      <li class="status status-verification warning" aria-labelledby="status-title" tabindex="-1">\n        <span id="status-title" class="title status-title">\n          <i class="fa fa-exclamation-circle" aria-hidden="true"></i>\n          <span class="sr">Notice</span>\n          ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Activate your account!"))))
        __M_writer(u'\n        </span>\n        <p class="status-note">')
        __M_writer(filters.decode.utf8( activate_account_message ))
        __M_writer(u'</p>\n')
        __M_writer(u'      </li>\n    </ul>\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 16, "33": 18, "34": 18, "35": 22, "41": 35, "16": 2, "21": 1, "27": 1, "28": 5, "29": 8, "30": 8, "31": 16}, "uri": "registration/account_activation_sidebar_notice.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/registration/account_activation_sidebar_notice.html"}
__M_END_METADATA
"""
