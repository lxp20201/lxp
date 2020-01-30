# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580212381.881524
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/themes/red-theme/lms/templates/footer.html'
_template_uri = u'footer.html'
_source_encoding = 'utf-8'
_exports = []



from django.urls import reverse
from django.utils.translation import ugettext as _
from django.conf import settings

from datetime import datetime
import pytz

from openedx.core.djangoapps.lang_pref.api import footer_language_selector_is_enabled
from openedx.core.djangolib.markup import HTML, Text


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        static = _mako_get_namespace(context, 'static')
        marketing_link = context.get('marketing_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n<div class="wrapper wrapper-footer">\n  <footer>\n    <!-- This is super-ugly, don\'t use it! -->\n    <div class="colophon">\n      <nav class="nav-colophon" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('About'))))
        __M_writer(u'">\n      <ol>\n          <li class="nav-colophon-01">\n          <a id="about" href="')
        __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('ABOUT'))))
        __M_writer(u'">\n              ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("About"))))
        __M_writer(u'\n          </a>\n          </li>\n')
        if marketing_link('JOBS') and marketing_link('JOBS') != '#':
            __M_writer(u'            <li class="nav-colophon-02">\n              <a id="jobs" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('JOBS'))))
            __M_writer(u'">\n                ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Jobs"))))
            __M_writer(u'\n              </a>\n            </li>\n')
        if marketing_link('NEWS') and marketing_link('NEWS') != '#':
            __M_writer(u'            <li class="nav-colophon-03">\n              <a id="news" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('NEWS'))))
            __M_writer(u'">\n                ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("News"))))
            __M_writer(u'\n              </a>\n            </li>\n')
        __M_writer(u'          <li class="nav-colophon-04">\n          <a id="faq" href="')
        __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('FAQ'))))
        __M_writer(u'">\n              ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("FAQ"))))
        __M_writer(u'\n          </a>\n          </li>\n          <li class="nav-colophon-05">\n          <a id="contact" href="')
        __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('CONTACT'))))
        __M_writer(u'">\n              ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Contact"))))
        __M_writer(u'\n          </a>\n          </li>\n      </ol>\n      </nav>\n\n')
        if context.get('include_language_selector', footer_language_selector_is_enabled()):
            __M_writer(u'          ')
            runtime._include_file(context, (static.get_template_path('widgets/footer-language-selector.html')), _template_uri)
            __M_writer(u'\n')
        __M_writer(u'\n      <div class="wrapper-logo">\n        <p>\n          <a href="/">\n')
        __M_writer(u'            <img alt="organization logo placeholder" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url("images/logo.png"))))
        __M_writer(u'">\n          </a>\n        </p>\n      </div>\n\n      <p class="copyright">&copy; ')
        __M_writer(filters.html_escape(filters.decode.utf8(datetime.now(pytz.timezone(settings.TIME_ZONE)).year)))
        __M_writer(u' ')
        __M_writer(filters.html_escape(filters.decode.utf8(static.get_platform_name())))
        __M_writer(u'.</p>\n\n')
        __M_writer(u'      <p class="copyright">\n')
        __M_writer(u'        ')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("edX, Open edX, and the edX and Open edX logos are registered trademarks of {link_start}edX Inc.{link_end}")).format(
            link_start=HTML(u"<a href='https://www.edx.org/'>"),
            link_end=HTML(u"</a>")
        ))))
        __M_writer(u'\n      </p>\n      <nav class="nav-legal" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Legal'))))
        __M_writer(u'">\n        <ul>\n')
        if marketing_link('HONOR') and marketing_link('HONOR') != '#':
            __M_writer(u'          <li class="nav-legal-01">\n            ')

            tos_link = HTML(u"<a href='{}'>").format(marketing_link('TOS'))
            honor_link = HTML(u"<a href='{}'>").format(marketing_link('HONOR'))
                        
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['honor_link','tos_link'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n            ')
            __M_writer(filters.html_escape(filters.decode.utf8(
              Text(_("{tos_link_start}Terms of Service{tos_link_end} and {honor_link_start}Honor Code{honor_link_end}")).format(
                tos_link_start=tos_link,
                tos_link_end=HTML("</a>"),
                honor_link_start=honor_link,
                honor_link_end=HTML("</a>"),
              )
            )))
            __M_writer(u'\n          </li>\n')
        else:
            __M_writer(u'          <li class="nav-legal-01">\n            <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('TOS'))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Terms of Service"))))
            __M_writer(u'</a>\n          </li>\n')
        __M_writer(u'          <li class="nav-legal-02">\n            <a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('PRIVACY'))))
        __M_writer(u'">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Privacy Policy"))))
        __M_writer(u'</a>\n          </li>\n        </ul>\n      </nav>\n    </div>\n\n')
        __M_writer(u'    <div class="footer-about-openedx">\n      <p>\n        <a href="http://openedx.org/">\n')
        __M_writer(u'          <img src="(static.url("images/logo.png")" alt="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Powered by Open edX'))))
        __M_writer(u'" width="140" />\n')
        __M_writer(u'        </a>\n      </p>\n    </div>\n  </footer>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 113, "129": 113, "130": 118, "136": 130, "16": 4, "35": 3, "38": 2, "45": 2, "46": 3, "47": 14, "48": 20, "49": 20, "50": 23, "51": 23, "52": 24, "53": 24, "54": 27, "55": 28, "56": 29, "57": 29, "58": 30, "59": 30, "60": 34, "61": 35, "62": 36, "63": 36, "64": 37, "65": 37, "66": 41, "67": 42, "68": 42, "69": 43, "70": 43, "71": 47, "72": 47, "73": 48, "74": 48, "75": 54, "76": 55, "77": 55, "78": 55, "79": 57, "80": 63, "81": 63, "82": 63, "83": 68, "84": 68, "85": 68, "86": 68, "87": 71, "88": 73, "89": 73, "93": 76, "94": 78, "95": 78, "96": 80, "97": 81, "98": 82, "105": 85, "106": 86, "114": 93, "115": 95, "116": 96, "117": 97, "118": 97, "119": 97, "120": 97, "121": 100, "122": 101, "123": 101, "124": 101, "125": 101, "126": 108, "127": 113}, "uri": "footer.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/themes/red-theme/lms/templates/footer.html"}
__M_END_METADATA
"""
