# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580296243.874504
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/footer.html'
_template_uri = u'custome-theme/lms/templates/footer.html'
_source_encoding = 'utf-8'
_exports = []



from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from branding.api import get_footer


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
        include_dependencies = context.get('include_dependencies', UNDEFINED)
        is_secure = context.get('is_secure', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        bidi = context.get('bidi', UNDEFINED)
        footer_css_urls = context.get('footer_css_urls', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        footer = get_footer(is_secure=is_secure) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['footer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n\n<div class="wrapper wrapper-footer">\n\n  <div class="footer_section footer_section-contact-us">\n    <div class="footer_section-holder">\n      <span class="footer_text">If you have some questions please contact us</span>\n      <a class="footer_btn__contact" href="/contact">Contact us</a>\n    </div>\n  </div>\n\n  <footer id="footer-openedx" class="grid-container"\n')
        if bidi:
            __M_writer(u'      dir=')
            __M_writer(filters.html_escape(filters.decode.utf8(bidi)))
            __M_writer(u'\n')
        __M_writer(u'  >\n    <div class="colophon">\n      <div class="footer-nav-wrapper">\n        <div class="footer-col">\n          <div class="footer-title">About the CintanaTech</div>\n          <ul>\n            <li><a href="https://cintanatech.com/" target="_blank">CintanaTech</a></li>\n            <li><a href="https://cintanatech.com/" target="_blank">About Us</a></li>\n            <li><a href="https://cintanatech.com/" target="_blank">eDX Services</a></li>\n            <li><a href="https://cintanatech.com/" target="_blank">Blog</a></li>\n          </ul>\n        </div>\n\n        <div class="footer-col">\n          <div class="footer-title">courses</div>\n          <ul>\n            <li><a href="https://cintanatech.com/" target="_blank">Create Course Now</a></li>\n            <li><a href="https://cintanatech.com/en/about-us/" target="_blank">About Us</a></li>\n            <li><a href="https://cintanatech.com/#our_services" target="_blank">eDX Services</a></li>\n            <li><a href="https://cintanatech.com/en/blog/" target="_blank">Blog</a></li>\n          </ul>\n        </div>\n\n        <div class="footer-col">\n          <div class="footer-title">Contact us</div>\n          <ul>\n            <li><a href="/contact">Contact Us</a></li>\n            <li><a href="https://cintanatech.com/" target="_blank">Help</a></li>\n          </ul>\n        </div>\n      </div>\n\n      <div class="footer_section">\n        <div class="footer_copyright-holder">\n          \xa9 2020 CintanaTech. All Rights Reserved\n          <a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(footer['openedx_link']['url'])))
        __M_writer(u'">\n            <img src="')
        __M_writer(filters.html_escape(filters.decode.utf8(footer['openedx_link']['image'])))
        __M_writer(u'" alt="')
        __M_writer(filters.html_escape(filters.decode.utf8(footer['openedx_link']['title'])))
        __M_writer(u'" width="140" />\n          </a>\n        </div>\n      </div>\n\n    </div>\n  </footer>\n</div>\n')
        if include_dependencies:
            __M_writer(u'  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.js(group=u'base_vendor'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-vendor'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n  ')
            runtime._include_file(context, u'widgets/segment-io.html', _template_uri)
            __M_writer(u'\n  ')
            runtime._include_file(context, u'widgets/segment-io-footer.html', _template_uri)
            __M_writer(u'\n')
        if footer_css_urls:
            for url in footer_css_urls:
                __M_writer(u'    <link rel="stylesheet" type="text/css" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(url)))
                __M_writer(u'"></link>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "29": 9, "32": 2, "42": 2, "43": 7, "44": 8, "48": 8, "49": 9, "50": 24, "51": 25, "52": 25, "53": 25, "54": 27, "55": 62, "56": 62, "57": 63, "58": 63, "59": 63, "60": 63, "61": 71, "62": 72, "70": 72, "73": 72, "81": 73, "84": 73, "85": 74, "86": 74, "87": 75, "88": 75, "89": 77, "90": 78, "91": 79, "92": 79, "93": 79, "99": 93}, "uri": "custome-theme/lms/templates/footer.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/footer.html"}
__M_END_METADATA
"""
