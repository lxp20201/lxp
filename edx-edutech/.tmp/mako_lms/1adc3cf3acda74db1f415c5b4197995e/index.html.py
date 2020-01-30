# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580210684.260407
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = [u'js_extra']



from django.utils.translation import ugettext as _
from django.urls import reverse

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

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'main.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        homepage_overlay_html = context.get('homepage_overlay_html', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        courses_list = context.get('courses_list', UNDEFINED)
        show_signup_immediately = context.get('show_signup_immediately', UNDEFINED)
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        show_homepage_promo_video = context.get('show_homepage_promo_video', UNDEFINED)
        homepage_promo_video_youtube_id = context.get('homepage_promo_video_youtube_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n<main id="main" aria-label="Content" tabindex="-1">\n    <section class="home">\n      <header>\n        <div class="outer-wrapper">\n          <div class="title">\n            <div class="heading-group">\n')
        if homepage_overlay_html:
            __M_writer(u'                ')
            __M_writer(filters.decode.utf8(homepage_overlay_html ))
            __M_writer(u'\n')
        else:
            __M_writer(u'                ')
            runtime._include_file(context, u'index_overlay.html', _template_uri)
            __M_writer(u'\n')
        __M_writer(u'            </div>\n')
        if settings.FEATURES.get('ENABLE_COURSE_DISCOVERY'):
            __M_writer(u'              <div class="course-search">\n                <form method="get" action="/courses">\n                  <label><span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Search for a course"))))
            __M_writer(u'</span>\n                    <input class="search-input" name="search_query" type="text" placeholder="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Search for a course"))))
            __M_writer(u'"></input>\n                  </label>\n                  <button class="search-button" type="submit">\n                    <span class="icon fa fa-search" aria-hidden="true"></span><span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Search"))))
            __M_writer(u'</span>\n                  </button>\n                </form>\n              </div>\n')
        __M_writer(u'\n          </div>\n\n          ')
        runtime._include_file(context, u'index_promo_video.html', _template_uri)
        __M_writer(u'\n        </div>\n\n      </header>\n      ')
        runtime._include_file(context, (courses_list), _template_uri)
        __M_writer(u'\n\n    </section>\n</main>\n\n')
        if show_homepage_promo_video:
            __M_writer(u'  <section id="video-modal" class="modal home-page-video-modal video-modal">\n    <div class="inner-wrapper">\n      <iframe title="YouTube Video" width="640" height="360" src="//www.youtube.com/embed/')
            __M_writer(filters.html_escape(filters.decode.utf8(homepage_promo_video_youtube_id)))
            __M_writer(u'?showinfo=0" frameborder="0" allowfullscreen></iframe>\n    </div>\n  </section>\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n\n')
        if show_signup_immediately is not UNDEFINED:
            __M_writer(u'<script type="text/javascript">\n  $(window).load(function() {$(\'#signup_action\').trigger("click");});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def js_extra():
            return render_js_extra(context)
        __M_writer = context.writer()
        __M_writer(u'\n   <script type="text/javascript">\n      $(window).load(function() {\n         if(getParameterByName(\'next\')) {\n              $(\'#login\').trigger("click");\n         }\n      })\n   </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 4, "30": 3, "36": 1, "49": 1, "50": 2, "51": 3, "52": 9, "53": 17, "54": 18, "55": 18, "56": 18, "57": 19, "58": 20, "59": 20, "60": 20, "61": 22, "62": 23, "63": 24, "64": 26, "65": 26, "66": 27, "67": 27, "68": 30, "69": 30, "70": 35, "71": 38, "72": 38, "73": 42, "74": 42, "75": 47, "76": 48, "77": 50, "78": 50, "79": 54, "84": 63, "85": 65, "86": 68, "92": 55, "98": 55, "104": 98}, "uri": "index.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/index.html"}
__M_END_METADATA
"""
