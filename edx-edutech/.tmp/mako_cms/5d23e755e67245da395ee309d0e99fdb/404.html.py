# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580361387.041672
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/404.html'
_template_uri = '404.html'
_source_encoding = 'utf-8'
_exports = [u'content', u'bodyclass', u'title']



from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text


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
    return runtime._inherit_from(context, u'base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        settings = context.get('settings', UNDEFINED)
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u'\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div class="wrapper-content wrapper">\n  <section class="content">\n    <header>\n      <h1 class="title title-1">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Page not found"))))
        __M_writer(u'</h1>\n    </header>\n    <article class="content-primary" role="main">\n      <p>\n      ')
        __M_writer(filters.html_escape(filters.decode.utf8(_('The page that you were looking for was not found.'))))
        __M_writer(u'\n      ')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_('Go back to the {homepage} or let us know about any pages that may have been moved at {email}.')).format(
        homepage=HTML('<a href="/">homepage</a>'),
        email=HTML('<a href="mailto:{address}">{address}</a>').format(
          address=Text(settings.TECH_SUPPORT_EMAIL)
        )
      ))))
        __M_writer(u'\n      </p>\n    </article>\n  </section>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyclass():
            return render_bodyclass(context)
        __M_writer = context.writer()
        __M_writer(u'view-util util-404')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(filters.decode.utf8(_("Page Not Found"))))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 1, "97": 8, "67": 11, "103": 7, "109": 7, "76": 15, "74": 11, "75": 15, "44": 1, "45": 5, "46": 6, "77": 19, "16": 2, "115": 109, "91": 8, "51": 7, "78": 19, "56": 8, "79": 20, "61": 30, "85": 25}, "uri": "404.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/404.html"}
__M_END_METADATA
"""
