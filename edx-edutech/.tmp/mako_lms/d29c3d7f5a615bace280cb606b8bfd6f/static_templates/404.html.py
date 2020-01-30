# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580295348.926179
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/static_templates/404.html'
_template_uri = 'static_templates/404.html'
_source_encoding = 'utf-8'
_exports = [u'pagetitle', u'pageheader', u'pagecontent']



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
        page_content = context.get('page_content', UNDEFINED)
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        static = _mako_get_namespace(context, 'static')
        page_header = context.get('page_header', UNDEFINED)
        def pageheader():
            return render_pageheader(context._locals(__M_locals))
        def pagecontent():
            return render_pagecontent(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

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


def render_pagetitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pagetitle():
            return render_pagetitle(context)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(filters.decode.utf8(_("Page Not Found"))))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pageheader(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        page_header = context.get('page_header', UNDEFINED)
        def pageheader():
            return render_pageheader(context)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(filters.decode.utf8(page_header or _("Page not found"))))
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
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_('The page that you were looking for was not found. Go back to the {link_start}homepage{link_end} or let us know about any pages that may have been moved at {email}.')).format(
                    link_start=HTML('<a href="/">'),
                    link_end=HTML('</a>'),
                    email=HTML('<a href="mailto:{email}">{email}</a>').format(email=Text(static.get_tech_support_email_address()))
                    ))))
            __M_writer(u'\n')
        __M_writer(u'            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "28": 2, "34": 1, "48": 1, "49": 2, "50": 6, "51": 7, "56": 9, "61": 14, "66": 27, "72": 9, "78": 9, "84": 14, "91": 14, "97": 17, "105": 17, "106": 18, "107": 19, "108": 19, "109": 19, "110": 20, "111": 21, "112": 21, "117": 25, "118": 27, "124": 118}, "uri": "static_templates/404.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/static_templates/404.html"}
__M_END_METADATA
"""
