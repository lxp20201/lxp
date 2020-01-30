# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580210685.138934
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/courses_list.html'
_template_uri = 'courses_list.html'
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
        journal_info = context.get('journal_info', UNDEFINED)
        homepage_course_max = context.get('homepage_course_max', UNDEFINED)
        marketing_link = context.get('marketing_link', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        len = context.get('len', UNDEFINED)
        courses = context.get('courses', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n<section class="courses-container">\n  <section class="highlighted-courses">\n\n')
        if settings.FEATURES.get('COURSES_ARE_BROWSABLE'):
            __M_writer(u'      <section class="courses">\n        <ul class="journal-list">\n')
            for bundle in journal_info.get('journal_bundles'):
                __M_writer(u'          <li class="courses-listing-item">\n            ')
                runtime._include_file(context, u'journals/bundle_card.html', _template_uri, bundle=bundle)
                __M_writer(u'\n          </li>\n')
            __M_writer(u'        </ul>\n        <ul class="journal-list">\n')
            for journal in journal_info.get('journals'):
                __M_writer(u'          <li class="courses-listing-item">\n              ')
                runtime._include_file(context, u'journals/journal_card.html', _template_uri, journal=journal)
                __M_writer(u'\n          </li>\n')
            __M_writer(u'        </ul>\n        <ul class="courses-listing">\n')
            for course in courses[:homepage_course_max]:
                __M_writer(u'          <li class="courses-listing-item">\n              ')
                runtime._include_file(context, u'course.html', _template_uri, course=course)
                __M_writer(u'\n          </li>\n')
            __M_writer(u'        </ul>\n      </section>\n')
            if homepage_course_max and len(courses) > homepage_course_max:
                __M_writer(u'      <div class="courses-more">\n        <a class="courses-more-cta" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('COURSES'))))
                __M_writer(u'"> ')
                __M_writer(filters.html_escape(filters.decode.utf8(_("View all Courses"))))
                __M_writer(u' </a>\n      </div>\n')
        __M_writer(u'\n  </section>\n</section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "25": 2, "28": 1, "39": 1, "40": 2, "41": 3, "42": 8, "43": 9, "44": 11, "45": 12, "46": 13, "47": 13, "48": 16, "49": 18, "50": 19, "51": 20, "52": 20, "53": 23, "54": 26, "55": 27, "56": 28, "57": 28, "58": 31, "59": 34, "60": 35, "61": 36, "62": 36, "63": 36, "64": 36, "65": 40, "71": 65}, "uri": "courses_list.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/courses_list.html"}
__M_END_METADATA
"""
