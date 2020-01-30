# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580211867.810493
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/student_account/login_and_register.html'
_template_uri = 'student_account/login_and_register.html'
_source_encoding = 'utf-8'
_exports = [u'pagetitle', u'js_extra', u'header_extras']



import json
from django.utils.translation import ugettext as _
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from openedx.core.djangolib.js_utils import dump_js_escaped_json


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'/static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'../main.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        static = _mako_get_namespace(context, 'static')
        def header_extras():
            return render_header_extras(context._locals(__M_locals))
        enable_enterprise_sidebar = context.get('enable_enterprise_sidebar', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_extras'):
            context['self'].header_extras(**pageargs)
        

        __M_writer(u'\n<div class="section-bkg-wrapper">\n    <main id="main" aria-label="Content" tabindex="-1">\n        <div id="content-container" class="login-register-content">\n')
        if enable_enterprise_sidebar:
            __M_writer(u'                ')
            runtime._include_file(context, u'enterprise_sidebar.html', _template_uri)
            __M_writer(u'\n                ')

            border_class = 'border-left'
                            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['border_class'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        else:
            __M_writer(u'                ')

            border_class = ''
                            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['border_class'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        __M_writer(u'            <div id="login-and-registration-container" class="login-register ')
        __M_writer(filters.html_escape(filters.decode.utf8(border_class)))
        __M_writer(u'"></div>\n        </div>\n    </main>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagetitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pagetitle():
            return render_pagetitle(context)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(filters.decode.utf8(_("Sign in or Register"))))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        def ccall(caller):
            def body():
                data = context.get('data', UNDEFINED)
                __M_writer = context.writer()
                __M_writer(u'\n        var options = ')
                __M_writer(dump_js_escaped_json(data ))
                __M_writer(u";\n        LogistrationFactory(options);\n        if ('newrelic' in window) {\n            newrelic.finished();\n            // Because of a New Relic bug, the finished() event doesn't show up\n            // in Insights, so we have to make a new PageAction that is basically\n            // the same thing. We still want newrelic.finished() for session\n            // traces though.\n            newrelic.addPageAction('xfinished');\n        }\n    ")
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'LogistrationFactory',module_name=u'js/student_account/logistration_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        if configuration_helpers.get_value('DISPLAY_TOS_IN_MODAL_ON_REGISTRATION_PAGE', False):
            __M_writer(u'    <script type="text/javascript" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/student_account/tos_modal.js'))))
            __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_extras(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_extras():
            return render_header_extras(context)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n')
        for template_name in ["account", "access", "form_field", "login", "register", "institution_login", "institution_register", "password_reset", "account_recovery", "hinted_login"]:
            __M_writer(u'        <script type="text/template" id="')
            __M_writer(filters.html_escape(filters.decode.utf8(template_name)))
            __M_writer(u'-tpl">\n            ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.include(path=u'student_account/' + (template_name) + u'.underscore'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n        </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"130": 26, "131": 27, "132": 28, "133": 28, "134": 28, "140": 32, "16": 2, "147": 32, "148": 33, "149": 34, "150": 34, "151": 34, "30": 8, "159": 35, "162": 35, "36": 1, "168": 162, "49": 1, "50": 7, "51": 8, "52": 10, "57": 12, "62": 30, "67": 38, "68": 42, "69": 43, "70": 43, "71": 43, "72": 44, "78": 46, "79": 47, "80": 48, "81": 48, "87": 50, "88": 52, "89": 52, "90": 52, "96": 12, "102": 12, "108": 14, "115": 14, "120": 15, "121": 16, "122": 16, "127": 15}, "uri": "student_account/login_and_register.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/student_account/login_and_register.html"}
__M_END_METADATA
"""
