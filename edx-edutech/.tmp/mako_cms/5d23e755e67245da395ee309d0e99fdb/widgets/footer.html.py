# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580361386.086814
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/widgets/footer.html'
_template_uri = u'widgets/footer.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from django.urls import reverse
from datetime import datetime
from django.conf import settings
import pytz
from cms.djangoapps.contentstore.config.waffle import waffle, ENABLE_ACCESSIBILITY_POLICY_PAGE
from openedx.core.djangolib.markup import HTML, Text


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        is_marketing_link_set = context.get('is_marketing_link_set', UNDEFINED)
        marketing_link = context.get('marketing_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<div class="wrapper-footer wrapper">\n  <footer class="primary" role="contentinfo">\n\n    <div class="footer-content-primary">\n      <div class="colophon">\n        <p>&copy; ')
        __M_writer(filters.html_escape(filters.decode.utf8(datetime.now(pytz.timezone(settings.TIME_ZONE)).year)))
        __M_writer(u' <a data-rel="edx.org" href="')
        __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('ROOT'))))
        __M_writer(u'" rel="external">')
        __M_writer(filters.html_escape(filters.decode.utf8(settings.PLATFORM_NAME)))
        __M_writer(u'</a>.</p>\n      </div>\n\n        <nav class="nav-peripheral" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Policies"))))
        __M_writer(u'">\n          <ol>\n')
        if is_marketing_link_set('TOS'):
            __M_writer(u'              <li class="nav-item nav-peripheral-tos">\n                <a data-rel="edx.org" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('TOS'))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Terms of Service"))))
            __M_writer(u'</a>\n              </li>\n')
        if is_marketing_link_set('PRIVACY'):
            __M_writer(u'              <li class="nav-item nav-peripheral-pp">\n                <a data-rel="edx.org" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('PRIVACY'))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Privacy Policy"))))
            __M_writer(u'</a>\n              </li>\n')
        if waffle().is_enabled(ENABLE_ACCESSIBILITY_POLICY_PAGE):
            __M_writer(u'              <li class="nav-item nav-peripheral-aar">\n                <a data-rel="edx.org" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('accessibility'))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Accessibility Accommodation Request"))))
            __M_writer(u'</a>\n              </li>\n')
        __M_writer(u'            <li class="nav-item">\n              <a data-rel="edx.org" id="lms-link" href="')
        __M_writer(filters.html_escape(filters.decode.utf8(settings.LMS_ROOT_URL)))
        __M_writer(u'">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("LMS"))))
        __M_writer(u'</a>\n            </li>\n          </ol>\n        </nav>\n    </div>\n\n    <div class="footer-content-secondary" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Legal"))))
        __M_writer(u'">\n      <div class="footer-about-copyright">\n')
        __M_writer(u'        <p>\n')
        __M_writer(u'          ')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("edX, Open edX, and the edX and Open edX logos are registered trademarks of {link_start}edX Inc.{link_end}")).format(
            link_start=HTML(u"<a data-rel='edx.org' href='https://www.edx.org/'>"),
            link_end=HTML(u"</a>")
          ))))
        __M_writer(u'\n        </p>\n      </div>\n\n      <div class="footer-about-openedx">\n        <a href="http://open.edx.org" title="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Powered by CintanaTech"))))
        __M_writer(u'">\n          <img alt="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Powered by CintanaTech"))))
        __M_writer(u'" src="(static.url("images/logo.png")">\n        </a>\n      </div>\n    </div>\n  </footer>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "26": 2, "33": 2, "34": 11, "35": 18, "36": 18, "37": 18, "38": 18, "39": 18, "40": 18, "41": 21, "42": 21, "43": 23, "44": 24, "45": 25, "46": 25, "47": 25, "48": 25, "49": 28, "50": 29, "51": 30, "52": 30, "53": 30, "54": 30, "55": 33, "56": 34, "57": 35, "58": 35, "59": 35, "60": 35, "61": 38, "62": 39, "63": 39, "64": 39, "65": 39, "66": 45, "67": 45, "68": 48, "69": 50, "70": 50, "74": 53, "75": 58, "76": 58, "77": 59, "78": 59, "84": 78}, "uri": "widgets/footer.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/widgets/footer.html"}
__M_END_METADATA
"""
