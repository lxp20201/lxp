# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580211856.39723
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/course.html'
_template_uri = u'course.html'
_source_encoding = 'utf-8'
_exports = ['online_help_token']



from django.utils.translation import ugettext as _
from django.urls import reverse
from six import text_type


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,course,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(course=course,pageargs=pageargs)
        static = _mako_get_namespace(context, 'static')
        LANGUAGE_CODE = context.get('LANGUAGE_CODE', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n<article class="course" id="')
        __M_writer(filters.html_escape(filters.decode.utf8(course.id)))
        __M_writer(u'" role="region" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(course.display_name_with_default)))
        __M_writer(u'">\n  <a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(reverse('about_course', args=[text_type(course.id)]))))
        __M_writer(u'">\n    <header class="course-image">\n      <div class="cover-image">\n        <img src="')
        __M_writer(filters.html_escape(filters.decode.utf8(course.course_image_url)))
        __M_writer(u'" alt="')
        __M_writer(filters.html_escape(filters.decode.utf8(course.display_name_with_default)))
        __M_writer(u' ')
        __M_writer(filters.html_escape(filters.decode.utf8(course.display_number_with_default)))
        __M_writer(u'" />\n        <div class="learn-more" aria-hidden="true">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("LEARN MORE"))))
        __M_writer(u'</div>\n      </div>\n    </header>\n    <div class="course-info" aria-hidden="true">\n      <h2 class="course-name">\n        <span class="course-organization">')
        __M_writer(filters.html_escape(filters.decode.utf8(course.display_org_with_default)))
        __M_writer(u'</span>\n        <span class="course-code">')
        __M_writer(filters.html_escape(filters.decode.utf8(course.display_number_with_default)))
        __M_writer(u'</span>\n        <span class="course-title">')
        __M_writer(filters.html_escape(filters.decode.utf8(course.display_name_with_default)))
        __M_writer(u'</span>\n      </h2>\n      ')

        if course.start is not None:
            course_date_string = course.start.strftime('%Y-%m-%dT%H:%M:%S%z')
        else:
            course_date_string = ''
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['course_date_string'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if course.advertised_start is not None:
            __M_writer(u'          <div class="course-date" aria-hidden="true">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Starts"))))
            __M_writer(u': ')
            __M_writer(filters.html_escape(filters.decode.utf8(course.advertised_start)))
            __M_writer(u'</div>\n')
        else:
            __M_writer(u'          <div class="course-date localized_datetime" aria-hidden="true" data-format="shortDate" data-datetime="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_date_string)))
            __M_writer(u'" data-language="')
            __M_writer(filters.html_escape(filters.decode.utf8(LANGUAGE_CODE)))
            __M_writer(u'" data-string="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Starts: {date}"))))
            __M_writer(u'"></div>\n')
        __M_writer(u'    </div>\n    <div class="sr">\n      <ul>\n        <li>')
        __M_writer(filters.html_escape(filters.decode.utf8(course.display_org_with_default)))
        __M_writer(u'</li>\n        <li>')
        __M_writer(filters.html_escape(filters.decode.utf8(course.display_number_with_default)))
        __M_writer(u'</li>\n')
        if course.advertised_start is not None:
            __M_writer(u'            <li>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Starts"))))
            __M_writer(u': <time itemprop="startDate">')
            __M_writer(filters.html_escape(filters.decode.utf8(course.advertised_start)))
            __M_writer(u'</time></li>\n')
        else:
            __M_writer(u'            <li>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Starts"))))
            __M_writer(u': <time class="localized_datetime" itemprop="startDate" data-format="shortDate" data-datetime="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_date_string)))
            __M_writer(u'" data-language="')
            __M_writer(filters.html_escape(filters.decode.utf8(LANGUAGE_CODE)))
            __M_writer(u'"></time></li>\n')
        __M_writer(u'      </ul>\n    </div>\n  </a>\n</article>\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n    DateUtilFactory.transform(iterationKey=".localized_datetime");\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module_async(class_name=u'DateUtilFactory',module_name=u'js/dateutil_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "course" 
        
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 1, "135": 128, "16": 3, "29": 2, "32": 8, "39": 1, "40": 2, "41": 7, "42": 8, "43": 9, "44": 9, "45": 9, "46": 9, "47": 10, "48": 10, "49": 13, "50": 13, "51": 13, "52": 13, "53": 13, "54": 13, "55": 14, "56": 14, "57": 19, "58": 19, "59": 20, "60": 20, "61": 21, "62": 21, "63": 23, "72": 28, "73": 29, "74": 30, "75": 30, "76": 30, "77": 30, "78": 30, "79": 31, "80": 32, "81": 32, "82": 32, "83": 32, "84": 32, "85": 32, "86": 32, "87": 34, "88": 37, "89": 37, "90": 38, "91": 38, "92": 39, "93": 40, "94": 40, "95": 40, "96": 40, "97": 40, "98": 41, "99": 42, "100": 42, "101": 42, "102": 42, "103": 42, "104": 42, "105": 42, "106": 44, "110": 48, "115": 48, "118": 50, "124": 1}, "uri": "course.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/course.html"}
__M_END_METADATA
"""
