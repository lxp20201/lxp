# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580212376.465845
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/learner_dashboard/_dashboard_navigation_courses.html'
_template_uri = u'learner_dashboard/_dashboard_navigation_courses.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<header class="wrapper-header-courses">\n  <h2 class="header-courses">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("My Courses"))))
        __M_writer(u'</h2>\n</header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"34": 28, "16": 2, "20": 1, "25": 1, "26": 4, "27": 7, "28": 7}, "uri": "learner_dashboard/_dashboard_navigation_courses.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/learner_dashboard/_dashboard_navigation_courses.html"}
__M_END_METADATA
"""
