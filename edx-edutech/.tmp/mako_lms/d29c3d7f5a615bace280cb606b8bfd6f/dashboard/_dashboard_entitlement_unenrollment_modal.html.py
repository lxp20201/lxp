# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580212376.471105
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/dashboard/_dashboard_entitlement_unenrollment_modal.html'
_template_uri = u'dashboard/_dashboard_entitlement_unenrollment_modal.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<div id="entitlement-unenrollment-modal" class="entitlement-unenrollment-modal js-entitlement-unenrollment-modal js-modal" aria-hidden="true">\n  <div class="entitlement-unenrollment-modal-inner-wrapper" role="dialog" aria-modal="true" aria-labelledby="entitlement-unenrollment-modal-title" aria-live="polite">\n    <button class="entitlement-unenrollment-modal-close-btn js-entitlement-unenrollment-modal-close-btn">\n      <span class="icon fa fa-remove" aria-hidden="true"></span>\n      <span class="sr">\n')
        __M_writer(u'        ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Close"))))
        __M_writer(u'\n      </span>\n    </button>\n\n    <header class="entitlement-unenrollment-modal-header">\n      <h2 id="entitlement-unenrollment-modal-title">\n        <span class=\'js-entitlement-unenrollment-modal-header-text\'></span>\n        <span class="sr">,\n')
        __M_writer(u'          ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("window open"))))
        __M_writer(u'\n        </span>\n      </h2>\n      <hr/>\n    </header>\n    <div class="entitlement-unenrollment-modal-error-text js-entitlement-unenrollment-modal-error-text"></div>\n    <div class="entitlement-unenrollment-modal-submit-wrapper">\n      <button class="entitlement-unenrollment-modal-submit js-entitlement-unenrollment-modal-submit">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Unenroll"))))
        __M_writer(u'</button>\n    </div>\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 22, "33": 29, "34": 29, "40": 34, "16": 3, "20": 1, "25": 1, "26": 5, "27": 13, "28": 13, "29": 13, "30": 22, "31": 22}, "uri": "dashboard/_dashboard_entitlement_unenrollment_modal.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/dashboard/_dashboard_entitlement_unenrollment_modal.html"}
__M_END_METADATA
"""
