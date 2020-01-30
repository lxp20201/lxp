# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580361385.714706
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/base.html'
_template_uri = u'base.html'
_source_encoding = 'utf-8'
_exports = [u'bodyclass', u'title', u'jsextra', u'view_notes', u'content', u'page_alert', u'header_extras', u'page_bundle', u'modal_placeholder', u'requirejs']


main_css = "style-main-v1" 


from django.utils.translation import ugettext as _

from openedx.core.djangoapps.util.user_messages import PageLevelMessages
from openedx.core.djangolib.js_utils import (
    dump_js_escaped_json, js_escaped_string
)
from openedx.core.djangolib.markup import HTML
from openedx.core.release import RELEASE_LINE


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
        def requirejs():
            return render_requirejs(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        EDX_ROOT_URL = context.get('EDX_ROOT_URL', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        LANGUAGE_CODE = context.get('LANGUAGE_CODE', UNDEFINED)
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        context_library = context.get('context_library', UNDEFINED)
        def jsextra():
            return render_jsextra(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        getattr = context.get('getattr', UNDEFINED)
        uses_bootstrap = context.get('uses_bootstrap', UNDEFINED)
        def view_notes():
            return render_view_notes(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        context_course = context.get('context_course', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        list = context.get('list', UNDEFINED)
        def page_bundle():
            return render_page_bundle(context._locals(__M_locals))
        def page_alert():
            return render_page_alert(context._locals(__M_locals))
        def header_extras():
            return render_header_extras(context._locals(__M_locals))
        def modal_placeholder():
            return render_modal_placeholder(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n<!doctype html>\n<!--[if lte IE 9]><html class="ie9 lte9" lang="')
        __M_writer(filters.html_escape(filters.decode.utf8(LANGUAGE_CODE)))
        __M_writer(u'"><![endif]-->\n<!--[if !IE]><<!--><html lang="')
        __M_writer(filters.html_escape(filters.decode.utf8(LANGUAGE_CODE)))
        __M_writer(u'"><!--<![endif]-->\n  <head dir="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.dir_rtl())))
        __M_writer(u'">\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n    <meta name="openedx-release-line" content="')
        __M_writer(filters.html_escape(filters.decode.utf8(RELEASE_LINE)))
        __M_writer(u'" />\n    <title>\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(u' |\n')
        if context_course:
            __M_writer(u'        ')
            ctx_loc = context_course.location 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ctx_loc'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n        ')
            __M_writer(filters.html_escape(filters.decode.utf8(context_course.display_name_with_default)))
            __M_writer(u' |\n')
        elif context_library:
            __M_writer(u'        ')
            __M_writer(filters.html_escape(filters.decode.utf8(context_library.display_name_with_default)))
            __M_writer(u' |\n')
        __M_writer(u'        ')
        __M_writer(filters.html_escape(filters.decode.utf8(settings.STUDIO_NAME)))
        __M_writer(u'\n    </title>\n\n    ')

        jsi18n_path = "js/i18n/{language}/djangojs.js".format(language=LANGUAGE_CODE)
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['jsi18n_path'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if getattr(settings, 'CAPTURE_CONSOLE_LOG', False):
            __M_writer(u'        <script type="text/javascript">\n            var oldOnError = window.onerror;\n            window.localStorage.setItem(\'console_log_capture\', JSON.stringify([]));\n\n            window.onerror = function (message, url, lineno, colno, error) {\n                if (oldOnError) {\n                    oldOnError.apply(this, arguments);\n                }\n\n                var messages = JSON.parse(window.localStorage.getItem(\'console_log_capture\'));\n                messages.push([message, url, lineno, colno, (error || {}).stack]);\n                window.localStorage.setItem(\'console_log_capture\', JSON.stringify(messages));\n            }\n        </script>\n')
        __M_writer(u'\n    <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url(jsi18n_path))))
        __M_writer(u'"></script>\n    <meta name="viewport" content="width=device-width,initial-scale=1">\n    <meta name="path_prefix" content="')
        __M_writer(filters.html_escape(filters.decode.utf8(EDX_ROOT_URL)))
        __M_writer(u'">\n\n    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-vendor'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-vendor-tinymce-content'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-vendor-tinymce-skin'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n')
        if uses_bootstrap:
            __M_writer(u'      <link rel="stylesheet" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(static.url(self.attr.main_css))))
            __M_writer(u'" type="text/css" media="all" />\n')
        else:
            __M_writer(u'      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=(self.attr.main_css)))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        __M_writer(u'\n    ')
        runtime._include_file(context, u'widgets/segment-io.html', _template_uri)
        __M_writer(u'\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_extras'):
            context['self'].header_extras(**pageargs)
        

        __M_writer(u'\n  </head>\n\n  <body class="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.dir_rtl())))
        __M_writer(u' ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u' lang_')
        __M_writer(filters.html_escape(filters.decode.utf8(LANGUAGE_CODE)))
        __M_writer(u'">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'view_notes'):
            context['self'].view_notes(**pageargs)
        

        __M_writer(u'\n\n    <a class="nav-skip" href="#main">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Skip to main content"))))
        __M_writer(u'</a>\n\n    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.js(group=u'base_vendor'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'commons'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n    <script type="text/javascript">\n      window.baseUrl = "')
        __M_writer(js_escaped_string(settings.STATIC_URL ))
        __M_writer(u'";\n      require.config({\n          baseUrl: window.baseUrl\n      });\n    </script>\n\n    <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url("cms/js/require-config.js"))))
        __M_writer(u'"></script>\n\n    <!-- view -->\n    <div class="wrapper wrapper-view" dir="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.dir_rtl())))
        __M_writer(u'">\n      ')
        online_help_token = self.online_help_token() if hasattr(self, 'online_help_token') else None 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['online_help_token'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n      ')
        runtime._include_file(context, u'widgets/header.html', _template_uri, online_help_token=online_help_token)
        __M_writer(u'\n\n      ')

        banner_messages = list(PageLevelMessages.user_messages(request))
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['banner_messages'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if banner_messages:
            __M_writer(u'        <div class="page-banner">\n          <div class="user-messages">\n')
            for message in banner_messages:
                __M_writer(u'              <div class="alert ')
                __M_writer(filters.html_escape(filters.decode.utf8(message.css_class)))
                __M_writer(u'" role="alert">\n                <span class="icon icon-alert fa ')
                __M_writer(filters.html_escape(filters.decode.utf8(message.icon_class)))
                __M_writer(u'" aria-hidden="true"></span>\n                ')
                __M_writer(filters.html_escape(filters.decode.utf8(HTML(message.message_html))))
                __M_writer(u'\n              </div>\n')
            __M_writer(u'          </div>\n        </div>\n')
        __M_writer(u'\n      <div id="page-alert">\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_alert'):
            context['self'].page_alert(**pageargs)
        

        __M_writer(u'\n      </div>\n\n      <main id="main" aria-label="Content" tabindex="-1">\n        <div id="content">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n        </div>\n      </main>\n\n')
        if user.is_authenticated:
            __M_writer(u'        ')
            runtime._include_file(context, u'widgets/sock.html', _template_uri, online_help_token=online_help_token)
            __M_writer(u'\n')
        __M_writer(u'      ')
        runtime._include_file(context, u'widgets/footer.html', _template_uri)
        __M_writer(u'\n\n      <div id="page-notification"></div>\n    </div>\n\n    <div id="page-prompt"></div>\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'modal_placeholder'):
            context['self'].modal_placeholder(**pageargs)
        

        __M_writer(u'\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'jsextra'):
            context['self'].jsextra(**pageargs)
        

        __M_writer(u'\n\n')
        if context_course:
            __M_writer(u'      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'js/factories/context_course'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n      <script type="text/javascript">\n        window.course = new ContextCourse({\n          id: "')
            __M_writer(js_escaped_string(context_course.id ))
            __M_writer(u'",\n          name: "')
            __M_writer(js_escaped_string(context_course.display_name_with_default ))
            __M_writer(u'",\n          url_name: "')
            __M_writer(js_escaped_string(context_course.location.block_id ))
            __M_writer(u'",\n          org: "')
            __M_writer(js_escaped_string(context_course.location.org ))
            __M_writer(u'",\n          num: "')
            __M_writer(js_escaped_string(context_course.location.course ))
            __M_writer(u'",\n          display_course_number: "')
            __M_writer(js_escaped_string(context_course.display_coursenumber ))
            __M_writer(u'",\n          revision: "')
            __M_writer(js_escaped_string(context_course.location.branch ))
            __M_writer(u'",\n          self_paced: ')
            __M_writer(dump_js_escaped_json( context_course.self_paced ))
            __M_writer(u'\n        });\n      </script>\n')
        if user.is_authenticated:
            __M_writer(u'      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'js/sock'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        __M_writer(u'    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_bundle'):
            context['self'].page_bundle(**pageargs)
        

        __M_writer(u'\n    ')
        runtime._include_file(context, u'widgets/segment-io-footer.html', _template_uri)
        __M_writer(u'\n    <div class="modal-cover"></div>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyclass():
            return render_bodyclass(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_jsextra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def jsextra():
            return render_jsextra(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_view_notes(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def view_notes():
            return render_view_notes(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_alert(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_alert():
            return render_page_alert(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_extras(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_extras():
            return render_header_extras(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_bundle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def requirejs():
            return render_requirejs(context)
        def page_bundle():
            return render_page_bundle(context)
        __M_writer = context.writer()
        __M_writer(u'\n      <script type="text/javascript">\n      require([\'js/factories/base\'], function () {\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'requirejs'):
            context['self'].requirejs(**pageargs)
        

        __M_writer(u'\n      });\n      </script>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_modal_placeholder(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def modal_placeholder():
            return render_modal_placeholder(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_requirejs(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def requirejs():
            return render_requirejs(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 6, "18": 10, "36": 9, "39": 21, "77": 3, "78": 6, "79": 9, "80": 19, "81": 21, "82": 23, "83": 23, "84": 24, "85": 24, "86": 25, "87": 25, "88": 28, "89": 28, "94": 30, "95": 31, "96": 32, "97": 32, "101": 32, "102": 33, "103": 33, "104": 34, "105": 35, "106": 35, "107": 35, "108": 37, "109": 37, "110": 37, "111": 40, "117": 42, "118": 44, "119": 45, "120": 60, "121": 61, "122": 61, "123": 63, "124": 63, "132": 65, "135": 65, "143": 66, "146": 66, "154": 67, "157": 67, "158": 69, "159": 70, "160": 70, "161": 70, "162": 71, "163": 72, "171": 72, "174": 72, "175": 74, "176": 75, "177": 75, "182": 77, "183": 80, "184": 80, "189": 80, "190": 80, "191": 80, "196": 81, "197": 83, "198": 83, "206": 85, "209": 85, "217": 87, "220": 87, "221": 90, "222": 90, "223": 96, "224": 96, "225": 99, "226": 99, "227": 100, "231": 100, "232": 101, "233": 101, "234": 103, "240": 105, "241": 107, "242": 108, "243": 110, "244": 111, "245": 111, "246": 111, "247": 112, "248": 112, "249": 113, "250": 113, "251": 116, "252": 119, "257": 121, "262": 126, "263": 130, "264": 131, "265": 131, "266": 131, "267": 133, "268": 133, "269": 133, "274": 140, "279": 142, "280": 144, "281": 145, "289": 145, "292": 145, "293": 148, "294": 148, "295": 149, "296": 149, "297": 150, "298": 150, "299": 151, "300": 151, "301": 152, "302": 152, "303": 153, "304": 153, "305": 154, "306": 154, "307": 155, "308": 155, "309": 159, "310": 160, "318": 160, "321": 160, "322": 162, "327": 168, "328": 169, "329": 169, "335": 80, "346": 30, "357": 142, "368": 81, "379": 126, "390": 121, "401": 77, "412": 162, "420": 162, "425": 165, "431": 140, "442": 165, "453": 442}, "uri": "base.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/base.html"}
__M_END_METADATA
"""
