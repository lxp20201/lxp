# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284656.235698
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/static_templates/about.html'
_template_uri = 'static_templates/about.html'
_source_encoding = 'utf-8'
_exports = [u'pagetitle', u'pageheader', u'pagecontent']


from django.utils.translation import ugettext as _ 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'../main.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        page_header = context.get('page_header', UNDEFINED)
        page_content = context.get('page_content', UNDEFINED)
        def pageheader():
            return render_pageheader(context._locals(__M_locals))
        def pagecontent():
            return render_pagecontent(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer(u'\n\n<main id="main" aria-label="Content" tabindex="-1">\n    <section class="container about">\n        <h1>\n            ')
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
        __M_writer(filters.html_escape(filters.decode.utf8(_("About"))))
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
        __M_writer(filters.html_escape(filters.decode.utf8(page_header or _("About"))))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagecontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        page_content = context.get('page_content', UNDEFINED)
        def pagecontent():
            return render_pagecontent(context)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(filters.decode.utf8(page_content or _("This page left intentionally blank. Feel free to add your own content."))))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"65": 5, "97": 13, "71": 5, "103": 97, "42": 1, "43": 2, "44": 3, "77": 10, "16": 2, "49": 5, "84": 10, "54": 10, "90": 13, "59": 13, "29": 1}, "uri": "static_templates/about.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/static_templates/about.html"}
__M_END_METADATA
"""
