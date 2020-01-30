# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580211856.294892
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/themes/red-theme/lms/templates/header.html'
_template_uri = 'red-theme/lms/templates/header.html'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,online_help_token,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,online_help_token=online_help_token)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u"<!--\nTo override this page, add a header.html file in the following\nlocation: {your_theme}/lms/templates/header/header.html.html.\n\nIf you do not wish to override the header, you can simply delete\nthis file from your theme's repository.\n-->\n")
        __M_writer(u'\n')
        __M_writer(u'\n')
        runtime._include_file(context, (static.get_template_path(relative_path='header/header.html')), _template_uri, online_help_token=online_help_token)
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 2, "33": 9, "34": 10, "35": 11, "36": 11, "42": 36, "23": 10, "26": 9}, "uri": "red-theme/lms/templates/header.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/themes/red-theme/lms/templates/header.html"}
__M_END_METADATA
"""
