# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284629.124042
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/courses_list.html'
_template_uri = 'custome-theme/lms/templates/courses_list.html'
_source_encoding = 'utf-8'
_exports = []


from django.utils.translation import ugettext as _ 

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
        courses = context.get('courses', UNDEFINED)
        homepage_course_max = context.get('homepage_course_max', UNDEFINED)
        marketing_link = context.get('marketing_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n<section class="holder courses-container">\n  <section class="highlighted-courses">\n\n')
        if settings.FEATURES.get('COURSES_ARE_BROWSABLE'):
            __M_writer(u'      <section class="courses">\n        <div class="courses-title">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Our Courses"))))
            __M_writer(u'</div>\n        <ul class="courses-listing">\n')
            for course in courses[:homepage_course_max]:
                __M_writer(u'          <li class="courses-listing-item">\n              ')
                runtime._include_file(context, u'course.html', _template_uri, course=course)
                __M_writer(u'\n          </li>\n')
            __M_writer(u'        </ul>\n      </section>\n')
            if homepage_course_max and len(courses) > homepage_course_max:
                __M_writer(u'      <div class="courses-more">\n        <a class="courses-more-cta" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('COURSES'))))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("View all Courses"))))
                __M_writer(u'</a>\n      </div>\n')
        __M_writer(u'\n  </section>\n</section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "25": 2, "28": 1, "38": 1, "39": 2, "40": 3, "41": 8, "42": 9, "43": 10, "44": 10, "45": 13, "46": 14, "47": 15, "48": 15, "49": 18, "50": 21, "51": 22, "52": 23, "53": 23, "54": 23, "55": 23, "56": 27, "62": 56}, "uri": "custome-theme/lms/templates/courses_list.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/courses_list.html"}
__M_END_METADATA
"""
