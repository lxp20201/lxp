# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284727.25349
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/openedx/features/course_experience/templates/course_experience/course_reviews_modules/coursetalk-reviews-fragment.html'
_template_uri = 'course_experience/course_reviews_modules/coursetalk-reviews-fragment.html'
_source_encoding = 'utf-8'
_exports = []



from django.conf import settings
from openedx.core.djangolib.js_utils import js_escaped_string
from openedx.features.course_experience import SHOW_REVIEWS_TOOL_FLAG


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        course = context.get('course', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        platform_key = context.get('platform_key', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        if SHOW_REVIEWS_TOOL_FLAG.is_enabled(course.id):
            __M_writer(u'    <div class="coursetalk-read-reviews">\n        <span class="fa fa-spinner fa-spin" aria-hidden="true"></span>\n')
            __M_writer(u'        <div id="ct-custom-read-review-widget" data-provider="')
            __M_writer(filters.html_escape(filters.decode.utf8(platform_key)))
            __M_writer(u'" data-course="')
            __M_writer(filters.html_escape(filters.decode.utf8(course.id)))
            __M_writer(u'"></div>\n    </div>\n')
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n    new CourseTalkReviews({\n        toggleButton: \'.toggle-read-write-reviews\',\n        loadIcon: \'.coursetalk-read-reviews .fa.fa-spinner\',\n        readSrc: "')
                __M_writer(js_escaped_string(settings.COURSE_TALK_READ_ONLY_SOURCE ))
                __M_writer(u'",\n        writeSrc: "')
                __M_writer(js_escaped_string(settings.COURSE_TALK_WRITE_ONLY_SOURCE ))
                __M_writer(u'"\n    });\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'CourseTalkReviews'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 7, "29": 5, "32": 3, "40": 2, "41": 3, "42": 5, "43": 11, "44": 13, "45": 14, "46": 17, "47": 17, "48": 17, "49": 17, "50": 17, "51": 20, "55": 21, "56": 25, "57": 25, "58": 26, "59": 26, "64": 21, "67": 28, "73": 67}, "uri": "course_experience/course_reviews_modules/coursetalk-reviews-fragment.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/openedx/features/course_experience/templates/course_experience/course_reviews_modules/coursetalk-reviews-fragment.html"}
__M_END_METADATA
"""
