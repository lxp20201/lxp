# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284727.592055
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/video_modal.html'
_template_uri = u'courseware/../video_modal.html'
_source_encoding = 'utf-8'
_exports = []



from courseware.courses import get_course_about_section


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
        course = context.get('course', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<div id="video-modal" class="modal video-modal">\n  <div class="inner-wrapper">\n    ')
        __M_writer(filters.decode.utf8(get_course_about_section(request, course, "video")))
        __M_writer(u'\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"37": 3, "38": 4, "39": 8, "40": 8, "46": 40, "16": 1, "27": 4, "30": 0}, "uri": "courseware/../video_modal.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/video_modal.html"}
__M_END_METADATA
"""
