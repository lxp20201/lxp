# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580305006.405663
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/static_templates/server-error.html'
_template_uri = 'static_templates/server-error.html'
_source_encoding = 'utf-8'
_exports = [u'pageheader', u'pagecontent']



from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'../main.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        page_header = context.get('page_header', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        page_content = context.get('page_content', UNDEFINED)
        def pageheader():
            return render_pageheader(context._locals(__M_locals))
        def pagecontent():
            return render_pagecontent(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n<main id="main" aria-label="Content" tabindex="-1">\n    <section class="outside-app">\n        <h1>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pageheader'):
            context['self'].pageheader(**pageargs)
        

        __M_writer(u'\n        </h1>\n        <p>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagecontent'):
            context['self'].pagecontent(**pageargs)
        

        __M_writer(u'\n        </p>\n    </section>\n</main>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pageheader(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        page_header = context.get('page_header', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        def pageheader():
            return render_pageheader(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if page_header:
            __M_writer(u'                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(page_header)))
            __M_writer(u'\n')
        else:
            __M_writer(u'                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_(u"There has been a 500 error on the {platform_name} servers")).format(
                    platform_name=HTML("<em>{platform_name}</em>").format(platform_name=Text(static.get_platform_name()))
                    ))))
            __M_writer(u'\n')
        __M_writer(u'            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagecontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        page_content = context.get('page_content', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        def pagecontent():
            return render_pagecontent(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if page_content:
            __M_writer(u'                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(page_content)))
            __M_writer(u'\n')
        else:
            __M_writer(u'                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_('Please wait a few seconds and then reload the page. If the problem persists, please email us at {email}.')).format(
                    email=HTML('<a href="mailto:{email}">{email}</a>').format(
                    email=Text(static.get_tech_support_email_address())
                    )
                    ))))
            __M_writer(u'\n')
        __M_writer(u'            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "28": 2, "34": 1, "46": 1, "47": 2, "48": 6, "49": 7, "54": 20, "59": 33, "65": 12, "73": 12, "74": 13, "75": 14, "76": 14, "77": 14, "78": 15, "79": 16, "80": 16, "83": 18, "84": 20, "90": 23, "98": 23, "99": 24, "100": 25, "101": 25, "102": 25, "103": 26, "104": 27, "105": 27, "110": 31, "111": 33, "117": 111}, "uri": "static_templates/server-error.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/static_templates/server-error.html"}
__M_END_METADATA
"""
