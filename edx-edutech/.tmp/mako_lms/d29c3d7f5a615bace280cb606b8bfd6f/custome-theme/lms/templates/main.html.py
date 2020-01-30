# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580283886.903599
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/main.html'
_template_uri = u'custome-theme/lms/templates/main.html'
_source_encoding = 'utf-8'
_exports = [u'head_extra', u'bodyclass', u'js_overrides', u'footer_extra', u'title', 'pagetitle', u'js_extra', u'marketing_hero', u'bodyextra', u'headextra', 'login_query']


main_css = "style-main-v1" 


from branding import api as branding_api
from django.urls import reverse
from django.utils.http import urlquote_plus
from django.utils.translation import ugettext as _
from django.utils.translation import get_language_bidi
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from openedx.core.djangolib.js_utils import dump_js_escaped_json, js_escaped_string
from openedx.core.release import RELEASE_LINE
from pipeline_mako import render_require_js_path_overrides



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
        disable_window_wrap = context.get('disable_window_wrap', UNDEFINED)
        disable_courseware_js = context.get('disable_courseware_js', UNDEFINED)
        EDX_ROOT_URL = context.get('EDX_ROOT_URL', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        unicode = context.get('unicode', UNDEFINED)
        LANGUAGE_CODE = context.get('LANGUAGE_CODE', UNDEFINED)
        disable_footer = context.get('disable_footer', UNDEFINED)
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        def js_overrides():
            return render_js_overrides(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        def marketing_hero():
            return render_marketing_hero(context._locals(__M_locals))
        uses_bootstrap = context.get('uses_bootstrap', UNDEFINED)
        def footer_extra():
            return render_footer_extra(context._locals(__M_locals))
        def headextra():
            return render_headextra(context._locals(__M_locals))
        uses_pattern_library = context.get('uses_pattern_library', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        def head_extra():
            return render_head_extra(context._locals(__M_locals))
        def bodyextra():
            return render_bodyextra(context._locals(__M_locals))
        disable_header = context.get('disable_header', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        is_from_mobile_app = context.get('is_from_mobile_app', UNDEFINED)
        allow_iframing = context.get('allow_iframing', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n')
        online_help_token = self.online_help_token() if hasattr(self, 'online_help_token') else None 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['online_help_token'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n<!DOCTYPE html>\n<!--[if lte IE 9]><html class="ie ie9 lte9" lang="')
        __M_writer(filters.decode.utf8(LANGUAGE_CODE))
        __M_writer(u'"><![endif]-->\n<!--[if !IE]><!--><html lang="')
        __M_writer(filters.decode.utf8(LANGUAGE_CODE))
        __M_writer(u'"><!--<![endif]-->\n<head dir="')
        __M_writer(filters.decode.utf8(static.dir_rtl()))
        __M_writer(u'">\n    <meta charset="UTF-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(u'\n\n')
        if not allow_iframing:
            __M_writer(u'      <script type="text/javascript">\n        /* immediately break out of an iframe if coming from the marketing website */\n        (function(window) {\n          if (window.location !== window.top.location) {\n            window.top.location = window.location;\n          }\n        })(this);\n      </script>\n')
        __M_writer(u'\n  ')

        jsi18n_path = "js/i18n/{language}/djangojs.js".format(language=LANGUAGE_CODE)
        ie11_fix_path = "js/ie11_find_array.js"
          
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['jsi18n_path','ie11_fix_path'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if getattr(settings, 'CAPTURE_CONSOLE_LOG', False):
            __M_writer(u'    <script type="text/javascript">\n      var oldOnError = window.onerror;\n      window.localStorage.setItem(\'console_log_capture\', JSON.stringify([]));\n\n      window.onerror = function (message, url, lineno, colno, error) {\n        if (oldOnError) {\n          oldOnError.apply(this, arguments);\n        }\n\n        var messages = JSON.parse(window.localStorage.getItem(\'console_log_capture\'));\n        messages.push([message, url, lineno, colno, (error || {}).stack]);\n        window.localStorage.setItem(\'console_log_capture\', JSON.stringify(messages));\n      }\n    </script>\n')
        __M_writer(u'  <script type="text/javascript" src="')
        __M_writer(filters.decode.utf8(static.url(jsi18n_path)))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.decode.utf8(static.url(ie11_fix_path)))
        __M_writer(u'"></script>\n\n  <link rel="icon" type="image/x-icon" href="')
        __M_writer(filters.decode.utf8(static.url(static.get_value('favicon_path', settings.FAVICON_PATH))))
        __M_writer(u'" />\n\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.decode.utf8(static.css(group=u'style-vendor')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        if '/' in self.attr.main_css:
            if get_language_bidi():
                __M_writer(u'      ')

                rtl_css_file = self.attr.main_css.replace('.css', '-rtl.css')
                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['rtl_css_file'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n      <link rel="stylesheet" href="')
                __M_writer(filters.decode.utf8(unicode(static.url(rtl_css_file))))
                __M_writer(u'" type="text/css" media="all" />\n')
            else:
                __M_writer(u'      <link rel="stylesheet" href="')
                __M_writer(filters.decode.utf8(static.url(self.attr.main_css)))
                __M_writer(u'" type="text/css" media="all" />\n')
        else:
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.decode.utf8(static.css(group=(self.attr.main_css))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        __M_writer(u'\n')
        if disable_courseware_js or uses_pattern_library:
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.decode.utf8(static.js(group=u'base_vendor')))
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
                __M_writer(filters.decode.utf8(static.js(group=u'base_application')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        else:
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.decode.utf8(static.js(group=u'main_vendor')))
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
                __M_writer(filters.decode.utf8(static.js(group=u'application')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.decode.utf8(static.webpack(entry=u'commons')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n')
        if uses_bootstrap:
            __M_writer(u'    <script type="text/javascript" src="')
            __M_writer(filters.decode.utf8(static.url('common/js/vendor/bootstrap.bundle.js')))
            __M_writer(u'"></script>\n')
        __M_writer(u'\n  <script>\n    window.baseUrl = "')
        __M_writer(js_escaped_string(settings.STATIC_URL ))
        __M_writer(u'";\n    (function (require) {\n      require.config({\n          baseUrl: window.baseUrl\n      });\n    }).call(this, require || RequireJS.require);\n  </script>\n  <script type="text/javascript" src="')
        __M_writer(filters.decode.utf8(static.url("lms/js/require-config.js")))
        __M_writer(u'"></script>\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_overrides'):
            context['self'].js_overrides(**pageargs)
        

        __M_writer(u'\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headextra'):
            context['self'].headextra(**pageargs)
        

        __M_writer(u'\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_extra'):
            context['self'].head_extra(**pageargs)
        

        __M_writer(u'\n\n    <link rel="stylesheet" type="text/css" href="/static/')
        __M_writer(filters.decode.utf8(settings.FEATURES.get('MARVEL_YELLOW_DEFAULT_HAWTHORN_SITE_THEME', settings.DEFAULT_SITE_THEME)))
        __M_writer(u'/css/custom.css"></link>\n\n  ')
        runtime._include_file(context, u'/courseware/experiments.html', _template_uri)
        __M_writer(u'\n  ')
        runtime._include_file(context, u'user_metadata.html', _template_uri)
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.decode.utf8(static.optional_include_mako(is_theming_enabled=u'True',file=u'head-extra.html')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n  ')
        runtime._include_file(context, u'widgets/optimizely.html', _template_uri)
        __M_writer(u'\n  ')
        runtime._include_file(context, u'widgets/segment-io.html', _template_uri)
        __M_writer(u'\n\n  <meta name="path_prefix" content="')
        __M_writer(filters.decode.utf8(EDX_ROOT_URL))
        __M_writer(u'">\n  \n  ')
        google_site_verification_id = configuration_helpers.get_value('GOOGLE_SITE_VERIFICATION_ID', settings.GOOGLE_SITE_VERIFICATION_ID) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['google_site_verification_id'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if google_site_verification_id:
            __M_writer(u'    <meta name="google-site-verification" content="')
            __M_writer(filters.decode.utf8(google_site_verification_id))
            __M_writer(u'" />\n')
        __M_writer(u'\n  <meta name="openedx-release-line" content="')
        __M_writer(filters.decode.utf8(RELEASE_LINE))
        __M_writer(u'" />\n\n')
        ga_acct = static.get_value("GOOGLE_ANALYTICS_ACCOUNT", settings.GOOGLE_ANALYTICS_ACCOUNT) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ga_acct'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if ga_acct:
            __M_writer(u'    <script type="text/javascript">\n    var _gaq = _gaq || [];\n    _gaq.push([\'_setAccount\', \'')
            __M_writer(js_escaped_string(ga_acct ))
            __M_writer(u"']);\n    _gaq.push(['_trackPageview']);\n\n    (function() {\n      var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;\n      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';\n      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);\n    })();\n    </script>\n")
        __M_writer(u'\n')
        branch_key = static.get_value("BRANCH_IO_KEY", settings.BRANCH_IO_KEY) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['branch_key'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if branch_key and not is_from_mobile_app:
            __M_writer(u'    <script type="text/javascript">\n        (function(b,r,a,n,c,h,_,s,d,k){if(!b[n]||!b[n]._q){for(;s<_.length;)c(h,_[s++]);d=r.createElement(a);d.async=1;d.src="https://cdn.branch.io/branch-latest.min.js";k=r.getElementsByTagName(a)[0];k.parentNode.insertBefore(d,k);b[n]=h}})(window,document,"script","branch",function(b,r){b[r]=function(){b._q.push([r,arguments])}},{_q:[],_v:1},"addListener applyCode banner closeBanner creditHistory credits data deepview deepviewCta first getCode init link logout redeem referrals removeListener sendSMS setBranchViewData setIdentity track validateCode".split(" "), 0);\n        branch.init(\'')
            __M_writer(js_escaped_string(branch_key ))
            __M_writer(u"');\n    </script>\n")
        __M_writer(u'\n</head>\n\n<body class="')
        __M_writer(filters.decode.utf8(static.dir_rtl()))
        __M_writer(u' ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u' lang_')
        __M_writer(filters.decode.utf8(LANGUAGE_CODE))
        __M_writer(u'">\n\n<svg style="display: none">\n    <symbol viewBox="0 0 1536 1536" id="ico-fs-expand">\n        <path d="M1283 413L928 768l355 355 144-144q29-31 70-14 39 17 39 59v448q0 26-19 45t-45 19h-448q-42 0-59-40-17-39 14-69l144-144-355-355-355 355 144 144q31 30 14 69-17 40-59 40H64q-26 0-45-19t-19-45v-448q0-42 40-59 39-17 69 14l144 144 355-355-355-355-144 144q-19 19-45 19-12 0-24-5-40-17-40-59V64q0-26 19-45T64 0h448q42 0 59 40 17 39-14 69L413 253l355 355 355-355-144-144q-31-30-14-69 17-40 59-40h448q26 0 45 19t19 45v448q0 42-39 59-13 5-25 5-26 0-45-19z" />\n    </symbol>\n    <symbol viewBox="0 0 1536 1536" id="ico-fs-shrink">\n        <path d="M768 832v448q0 26-19 45t-45 19-45-19l-144-144-332 332q-10 10-23 10t-23-10L23 1399q-10-10-10-23t10-23l332-332-144-144q-19-19-19-45t19-45 45-19h448q26 0 45 19t19 45zm755-672q0 13-10 23l-332 332 144 144q19 19 19 45t-19 45-45 19H832q-26 0-45-19t-19-45V256q0-26 19-45t45-19 45 19l144 144 332-332q10-10 23-10t23 10l114 114q10 10 10 23z" />\n    </symbol>\n    <symbol viewBox="0 0 35 35" id="ico-linkedin">\n        <title>linkedin</title>\n        <path d="M17.5 0C7.8 0 0 7.8 0 17.5S7.8 35 17.5 35 35 27.2 35 17.5C35 7.8 27.2 0 17.5 0zM13.1 26H8.8V10.7h4.4V26zM11.1 9.7c-1.1 0-2-0.9-2-2.1s0.9-2.1 2.1-2.1c1.1 0 2.1 0.9 2.1 2.1C13.1 8.8 12.2 9.7 11.1 9.7zM28.4 26h-4.4V16.5c0-1.1-0.3-1.9-1.7-1.9 -2.3 0-2.7 1.9-2.7 1.9v9.5h-4.4V10.7h4.4v1.5c0.6-0.5 2.2-1.5 4.4-1.5 1.4 0 4.4 0.8 4.4 6V26z" />\n    </symbol>\n    <symbol viewBox="0 0 35 35" id="ico-behance">\n        <title>behance</title>\n        <path d="M14.1 13.9c0-1.7-1.1-1.7-1.1-1.7h-0.6H8.3v3.5h4.3C13.4 15.8 14.1 15.5 14.1 13.9z" class="a" />\n        <path d="M13 18.2H8.3v4.2h4.4c0.7 0 1.9-0.2 1.9-2.1C14.6 18.2 13 18.2 13 18.2z" class="a" />\n        <path d="M24.8 15.8c-2.5 0-2.8 2.4-2.8 2.4h5.2C27.2 18.2 27.2 15.8 24.8 15.8z" class="a" />\n        <path d="M17.5 0C7.8 0 0 7.8 0 17.5S7.8 35 17.5 35 35 27.2 35 17.5 27.2 0 17.5 0zM21.3 10.3h6.6v2h-6.5V10.3zM18 20.6c0 4.8-5 4.7-5 4.7H8.3 8.2 4.7V9.4h3.5 0.1 4.6c2.5 0 4.5 1.4 4.5 4.2s-2.4 3-2.4 3C18.2 16.6 18 20.6 18 20.6zM24.8 23.1c2.6 0 2.5-1.7 2.5-1.7h2.8c0 4.5-5.4 4.2-5.4 4.2 -6.5 0-6.1-6.1-6.1-6.1s0-6.1 6.1-6.1c6.4 0 5.5 6.9 5.5 6.9H22C22 23.3 24.8 23.1 24.8 23.1z" class="a" />\n    </symbol>\n    <symbol viewBox="0 0 35 35" id="ico-facebook">\n        <title>facebook</title>\n        <path d="M17.5 0C7.8 0 0 7.8 0 17.5S7.8 35 17.5 35 35 27.2 35 17.5C35 7.8 27.2 0 17.5 0zM23.6 9.6h-2.2c-0.8 0-1.4 0.2-1.6 0.5 -0.3 0.3-0.4 0.9-0.4 1.5v2.7h4.2l-0.5 4.2h-3.6v10.8h-4.3V18.5h-3.6V14.3h3.6v-3.1c0-1.8 0.5-3.1 1.5-4.1 1-1 2.3-1.5 3.9-1.5 1.4 0 2.5 0.1 3.2 0.2C23.6 5.9 23.6 9.6 23.6 9.6z" />\n    </symbol>\n    <symbol viewBox="0 0 35 35" id="ico-instagram">\n        <title>instagram</title>\n        <path d="M17.5 21c1.9 0 3.5-1.6 3.5-3.5 0-0.8-0.2-1.5-0.7-2 -0.6-0.9-1.7-1.5-2.8-1.5s-2.2 0.6-2.8 1.5c-0.4 0.6-0.7 1.3-0.7 2C14 19.4 15.6 21 17.5 21z" class="a" />\n        <polygon points="25.2 13.2 25.2 10.3 25.2 9.8 24.7 9.8 21.8 9.9 21.8 13.2 " class="a" />\n        <path d="M17.5 0C7.9 0 0 7.9 0 17.5S7.9 35 17.5 35 35 27.1 35 17.5 27.2 0 17.5 0zM27.5 15.5v8.1c0 2.1-1.7 3.8-3.8 3.8H11.4c-2.1 0-3.8-1.7-3.8-3.8v-8.1 -4.1c0-2.1 1.7-3.8 3.8-3.8h12.2c2.1 0 3.8 1.7 3.8 3.8L27.5 15.5 27.5 15.5z" class="a" />\n        <path d="M22.9 17.5c0 3-2.4 5.4-5.4 5.4s-5.4-2.4-5.4-5.4c0-0.7 0.1-1.4 0.4-2H9.5v8.1c0 1.1 0.9 1.9 1.9 1.9h12.2c1.1 0 1.9-0.9 1.9-1.9v-8.1h-3C22.8 16.1 22.9 16.8 22.9 17.5z" class="a" />\n    </symbol>\n    <symbol viewBox="0 0 35 35" id="ico-odnoklassniki">\n        <title>odnoklassniki</title>\n        <path d="M17.5 14.5c1.7 0 3-1.3 3-3s-1.3-3-3-3c-1.7 0-3 1.4-3 3C14.5 13.2 15.8 14.5 17.5 14.5z" class="a" />\n        <path d="M17.5 0C7.8 0 0 7.8 0 17.5S7.8 35 17.5 35 35 27.2 35 17.5 27.2 0 17.5 0zM17.5 5.3c3.4 0 6.1 2.8 6.1 6.2 0 3.4-2.8 6.1-6.2 6.1 -3.4 0-6.1-2.8-6.1-6.2C11.4 8.1 14.1 5.3 17.5 5.3zM24.4 20.1c-0.8 0.8-1.7 1.3-2.7 1.7 -1 0.4-2 0.6-3 0.7 0.2 0.2 0.2 0.3 0.3 0.4 1.4 1.4 2.8 2.8 4.2 4.2 0.5 0.5 0.6 1.1 0.3 1.6 -0.3 0.6-0.9 1-1.6 1 -0.4 0-0.7-0.2-1-0.5 -1.1-1.1-2.1-2.1-3.2-3.2 -0.3-0.3-0.4-0.3-0.7 0 -1.1 1.1-2.1 2.2-3.2 3.2 -0.5 0.5-1.1 0.6-1.6 0.3 -0.6-0.3-1-0.9-1-1.5 0-0.4 0.2-0.7 0.5-1 1.4-1.4 2.8-2.8 4.2-4.2 0.1-0.1 0.2-0.2 0.3-0.3 -1.9-0.2-3.6-0.7-5-1.8 -0.2-0.1-0.4-0.3-0.5-0.4 -0.6-0.6-0.7-1.3-0.2-2 0.4-0.6 1.2-0.8 1.9-0.4 0.1 0.1 0.3 0.2 0.4 0.2 2.7 1.9 6.4 1.9 9.2 0.1 0.3-0.2 0.6-0.4 0.9-0.5 0.7-0.2 1.3 0.1 1.6 0.6C24.9 18.9 24.9 19.6 24.4 20.1z" class="a" />\n    </symbol>\n    <symbol viewBox="0 0 35 35" id="ico-twitter">\n        <title>twitter</title>\n        <path d="M17.5 0C7.8 0 0 7.8 0 17.5S7.8 35 17.5 35 35 27.2 35 17.5C35 7.8 27.2 0 17.5 0zM26.2 13.6l0 0.6c0 5.7-4.3 12.3-12.3 12.3 -2.4 0-4.7-0.7-6.6-1.9 0.3 0 0.7 0.1 1 0.1 2 0 3.9-0.7 5.4-1.8 -1.9 0-3.5-1.3-4-3 0.3 0.1 0.5 0.1 0.8 0.1 0.4 0 0.8 0 1.1-0.1 -2-0.4-3.5-2.1-3.5-4.2v-0.1c0.6 0.3 1.2 0.5 2 0.5 -1.2-0.8-1.9-2.1-1.9-3.6 0-0.8 0.2-1.5 0.6-2.2 2.1 2.6 5.3 4.3 8.9 4.5 -0.1-0.3-0.1-0.6-0.1-1 0-2.4 1.9-4.3 4.3-4.3 1.2 0 2.4 0.5 3.1 1.4 1-0.2 1.9-0.6 2.7-1 -0.3 1-1 1.9-1.9 2.4 0.9-0.1 1.7-0.3 2.5-0.7C27.8 12.2 27 13 26.2 13.6z" />\n    </symbol>\n    <symbol viewBox="0 0 35 35" id="ico-vimeo">\n        <title>vimeo</title>\n        <path d="M17.5 0C7.8 0 0 7.8 0 17.5S7.8 35 17.5 35 35 27.2 35 17.5 27.2 0 17.5 0zM29.9 11.7c-0.1 2.4-1.8 5.7-5.1 9.9 -3.4 4.4-6.2 6.6-8.5 6.6 -1.4 0-2.7-1.3-3.7-4 -0.7-2.4-1.3-4.9-2-7.3 -0.7-2.7-1.5-4-2.4-4 -0.2 0-0.8 0.4-1.9 1.2l-1.2-1.5c1.2-1.1 2.4-2.1 3.6-3.2 1.6-1.4 2.9-2.1 3.7-2.2 1.9-0.2 3.1 1.1 3.6 4 0.5 3 0.8 4.9 1 5.7 0.6 2.5 1.2 3.8 1.8 3.8 0.5 0 1.3-0.8 2.3-2.5 1-1.6 1.6-2.9 1.7-3.7 0.1-1.4-0.4-2.1-1.7-2.1 -0.6 0-1.2 0.1-1.8 0.4 1.2-4 3.5-5.9 7-5.8C28.8 6.9 30 8.5 29.9 11.7z" />\n    </symbol>\n    <symbol viewBox="0 0 35 35" id="ico-vk">\n        <title>vk</title>\n        <path d="M17.5 0C7.8 0 0 7.8 0 17.5S7.8 35 17.5 35 35 27.2 35 17.5 27.2 0 17.5 0zM26.4 19.4c0.8 0.8 1.7 1.5 2.4 2.4 0.3 0.4 0.6 0.8 0.9 1.2 0.3 0.6 0 1.4-0.5 1.4l-3.6 0c-0.9 0.1-1.7-0.3-2.3-0.9 -0.5-0.5-1-1-1.4-1.6 -0.2-0.2-0.4-0.4-0.6-0.6 -0.5-0.3-0.9-0.2-1.2 0.3 -0.3 0.5-0.4 1.1-0.4 1.7 0 0.8-0.3 1.1-1.1 1.1 -1.8 0.1-3.5-0.2-5.1-1.1 -1.4-0.8-2.5-1.9-3.5-3.2 -1.9-2.5-3.3-5.3-4.5-8.1 -0.3-0.6-0.1-1 0.6-1 1.2 0 2.3 0 3.5 0 0.5 0 0.8 0.3 1 0.7 0.6 1.6 1.4 3 2.4 4.4 0.3 0.4 0.5 0.7 0.9 1 0.4 0.3 0.7 0.2 0.9-0.3 0.1-0.3 0.2-0.6 0.2-0.9 0.1-1.1 0.1-2.2-0.1-3.2 -0.1-0.7-0.5-1.1-1.2-1.2 -0.3-0.1-0.3-0.2-0.1-0.4 0.3-0.3 0.6-0.5 1.1-0.5l4.1 0c0.6 0.1 0.8 0.4 0.9 1.1l0 4.5c0 0.2 0.1 1 0.6 1.1 0.4 0.1 0.6-0.2 0.8-0.4 1-1 1.7-2.2 2.3-3.5 0.3-0.6 0.5-1.1 0.7-1.7 0.2-0.4 0.4-0.6 0.9-0.6l3.9 0c0.1 0 0.2 0 0.3 0 0.7 0.1 0.8 0.4 0.6 1 -0.3 1-0.9 1.8-1.5 2.7 -0.7 0.9-1.3 1.8-2 2.7C25.6 18.3 25.6 18.7 26.4 19.4z" />\n    </symbol>\n    <symbol viewBox="0 0 35 35" id="ico-youtube">\n        <title>youtube</title>\n        <path d="M15.2 24.5c0 0.3 0 0.5 0 0.6 0 0.2 0 0.2-0.1 0.3 0 0.2-0.2 0.3-0.4 0.4 -0.2 0.1-0.3 0-0.5-0.3 0 0 0-0.1 0-0.3 0-0.2 0-0.4 0-0.6l0-3.8h-1.4l0 3.8c0 0.3 0 0.5 0 0.7s0 0.4 0 0.5c0 0.2 0 0.3 0.1 0.5 0 0.2 0.1 0.3 0.3 0.5 0.2 0.1 0.4 0.2 0.6 0.2 0.2 0 0.4 0 0.7-0.1 0.2-0.1 0.4-0.2 0.6-0.3 0.2-0.1 0.3-0.3 0.4-0.4l0 0.8L16.7 26.8v-6.1h-1.4L15.2 24.5 15.2 24.5z" class="a" />\n        <path d="M20.1 20.5c-0.3 0-0.7 0.2-1.2 0.5V18.6h-1.4v8.2l1.2 0 0.1-0.5c0.4 0.3 0.7 0.5 1 0.6 0.3 0.1 0.6 0 0.8-0.1 0.2-0.1 0.4-0.3 0.5-0.6 0.1-0.3 0.2-0.6 0.2-1v-3.2c0-0.6-0.2-1-0.6-1.3C20.5 20.5 20.3 20.5 20.1 20.5zM20.2 25.3c0 0.1-0.1 0.2-0.2 0.3 -0.1 0.1-0.3 0.1-0.4 0.1 -0.2 0-0.3 0-0.4-0.1 -0.1-0.1-0.2-0.2-0.2-0.3v-3.6c0-0.1 0.1-0.2 0.2-0.3 0.1-0.1 0.3-0.1 0.4-0.1 0.2 0 0.3 0 0.4 0.1 0.1 0.1 0.2 0.2 0.2 0.3V25.3z" class="a" />\n        <polygon points="13.2 18.6 8.6 18.6 8.6 19.6 10.1 19.6 10.1 26.8 11.5 26.8 11.5 19.6 13.2 19.6 " class="a" />\n        <path d="M17.5 0C7.8 0 0 7.8 0 17.5S7.8 35 17.5 35 35 27.2 35 17.5C35 7.8 27.2 0 17.5 0zM20 12.7V8.5h1.3v4.9c0 0.1 0 0.2 0.1 0.3 0.1 0.1 0.2 0.1 0.4 0.1 0.1 0 0.3 0 0.4-0.1 0.1-0.1 0.2-0.2 0.2-0.3V8.5h1.2v6.3h-1.6l0-0.5c-0.1 0.2-0.3 0.4-0.4 0.5 -0.2 0.1-0.3 0.2-0.5 0.2 -0.2 0-0.4-0.1-0.6-0.2 -0.1-0.1-0.3-0.2-0.4-0.4 0-0.1-0.1-0.2-0.1-0.3 0-0.1 0-0.2 0-0.3 0-0.1 0-0.2 0-0.4L20 12.7 20 12.7zM16.1 8.6c0.3-0.2 0.6-0.3 1.1-0.3 0.4 0 0.7 0.1 1 0.2 0.3 0.1 0.5 0.3 0.6 0.5 0.1 0.2 0.2 0.4 0.3 0.6 0.1 0.3 0.1 0.6 0.1 1v1.6c0 0.6 0 1-0.1 1.3 0 0.2-0.1 0.5-0.3 0.8 -0.2 0.3-0.4 0.4-0.6 0.5 -0.3 0.1-0.6 0.2-0.9 0.2 -0.3 0-0.7 0-0.9-0.2 -0.3-0.1-0.5-0.2-0.6-0.4 -0.1-0.2-0.2-0.4-0.3-0.7 -0.1-0.3-0.1-0.7-0.1-1.3 0 0 0-1.7 0-1.7 0-0.6 0.1-1 0.2-1.4C15.6 9 15.8 8.7 16.1 8.6zM11.9 6l0.9 3.1 0.9-3.1h1.7l-1.8 4.2v4.8H12.2v-4.8l-1.9-4.2H11.9zM27.8 26c0 0.4-0.1 0.8-0.3 1.2 -0.2 0.4-0.4 0.7-0.7 0.9 -0.3 0.3-0.7 0.5-1.1 0.6 -0.4 0.2-0.8 0.2-1.3 0.2H10.6c-0.5 0-0.9-0.1-1.3-0.2 -0.4-0.2-0.8-0.4-1.1-0.6 -0.3-0.3-0.6-0.6-0.7-0.9 -0.2-0.4-0.3-0.7-0.3-1.2v-6.8c0-0.4 0.1-0.8 0.3-1.2 0.2-0.4 0.4-0.7 0.7-0.9 0.3-0.3 0.7-0.5 1.1-0.6 0.4-0.2 0.8-0.2 1.3-0.2H24.4c0.5 0 0.9 0.1 1.3 0.2s0.8 0.4 1.1 0.6c0.3 0.3 0.6 0.6 0.7 0.9 0.2 0.4 0.3 0.7 0.3 1.2V26z" class="a" />\n        <path d="M17.2 13.9c0.2 0 0.3-0.1 0.4-0.2 0.1-0.1 0.2-0.3 0.2-0.4V9.9c0-0.2-0.1-0.3-0.2-0.5 -0.1-0.1-0.3-0.2-0.4-0.2 -0.2 0-0.3 0.1-0.4 0.2 -0.1 0.1-0.2 0.3-0.2 0.5v3.4c0 0.2 0.1 0.3 0.2 0.4C16.9 13.9 17.1 13.9 17.2 13.9z" class="a" />\n        <path d="M24.7 24.7v0.2 0.5c0 0.2-0.1 0.3-0.2 0.4 -0.1 0.1-0.3 0.1-0.4 0.1h-0.2c-0.2 0-0.3 0-0.4-0.1 -0.1-0.1-0.2-0.2-0.2-0.4v-0.1 -0.6 -0.8h2.5v-0.8c0-0.3 0-0.6 0-0.9 0-0.3 0-0.5-0.1-0.7 0-0.3-0.2-0.5-0.4-0.7 -0.2-0.2-0.5-0.3-0.7-0.3 -0.3-0.1-0.6-0.1-0.9 0 -0.3 0-0.5 0.1-0.8 0.3 -0.3 0.2-0.5 0.4-0.6 0.8 -0.1 0.3-0.2 0.8-0.2 1.3v1.9c0 0.8 0.2 1.4 0.6 1.7 0.4 0.3 0.8 0.5 1.2 0.5 0 0 0.1 0 0.1 0 0.5 0 0.9-0.2 1.3-0.6 0.3-0.3 0.4-0.6 0.4-1.1 0-0.1 0-0.3-0.1-0.5H24.7v0h0V24.7zM23.3 22.1c0-0.2 0.1-0.3 0.2-0.4 0.1-0.1 0.3-0.2 0.4-0.2h0.1c0.2 0 0.3 0.1 0.5 0.2 0.1 0.1 0.2 0.2 0.2 0.4l0 0.8h-1.4L23.3 22.1z" class="a" />\n    </symbol>\n    <symbol viewBox="0 0 78.1 16" style="enable-background:new 0 0 78.1 16;" id="logo-edx" class="test">\n        <title>logo-edx</title>\n\n        <g>\n            <g>\n                <path class="st0" fill="#fff" d="M14,15.8v-12h3.2c0.7,0,1.3,0,1.7,0.1c0.5,0.1,1,0.3,1.4,0.5C20.7,4.6,21,5,21.2,5.5c0.2,0.5,0.3,1,0.3,1.5\n\t\t\tc0,1-0.3,1.8-0.9,2.4c-0.6,0.7-1.7,1-3.3,1h-1.8v5.4H14z M15.5,9.1h1.9c1,0,1.6-0.2,2-0.5C19.8,8.2,20,7.7,20,7\n\t\t\tc0-0.5-0.1-0.9-0.4-1.2c-0.2-0.3-0.5-0.6-0.9-0.7c-0.2-0.1-0.7-0.1-1.4-0.1h-1.8V9.1z"/>\n                <path class="st0" fill="#fff" d="M23.3,15.8v-12h7.6v1.3h-6.1v3.8h5.8v1.3h-5.8v4.3h6.3v1.3H23.3z"/>\n                <path class="st0" fill="#fff" d="M33,15.8v-12h1.5l6.7,9.6V3.8h1.4v12h-1.5l-6.7-9.7v9.7H33z"/>\n                <g>\n                    <path class="st0" fill="#fff" d="M10.5,5.2c1.2,1.2,1.8,2.7,1.8,4.5s-0.6,3.2-1.8,4.5C9.3,15.4,7.9,16,6.2,16c-1.7,0-3.2-0.6-4.4-1.8\n\t\t\t\tC0.6,12.9,0,11.4,0,9.7s0.6-3.2,1.8-4.5C3,4,4.5,3.4,6.2,3.4C7.9,3.4,9.3,4,10.5,5.2z M6.2,5C4.9,5,3.8,5.5,2.9,6.4\n\t\t\t\tC2,7.3,1.6,8.4,1.6,9.7C1.6,11,2,12.1,2.9,13c0.9,0.9,2,1.4,3.2,1.4c1.3,0,2.4-0.5,3.3-1.4c0.9-0.9,1.3-2,1.3-3.3\n\t\t\t\tc0-1.3-0.4-2.4-1.3-3.3C8.5,5.5,7.4,5,6.2,5z"/>\n                </g>\n            </g>\n            <path class="st1" fill="#fff" d="M63.6,0c0,0.8,0,2.5,0,2.5l1.3,0c0,0,0.2,0.2,0.3,0.3c0,0,0,0,0,0c0,3.3,0,6.5,0,9.8c0,0,0,0,0,0\n\t\tc-0.1,0.2-0.3,0.4-0.4,0.5c-0.4,0-0.8,0-1.2,0c0,0.9,0,1.7,0,2.6c-0.3,0-0.6,0-0.9,0c0-0.4,0-0.7,0-1.1c-0.8,0.5-1.8,1-3,1.1\n\t\tc-0.3,0-0.5,0-0.8,0c-1.9-0.2-3.1-0.9-4.1-2c0,0,0,0,0,0c0.5-0.5,0.8-1.1,1.1-1.7c-0.7,0-1.5,0-2.2,0c0,0,0,0,0,0\n\t\tc-0.2-0.4-0.3-0.9-0.4-1.4c0,0,0,0,0,0c0.8,0,1.7,0,2.6,0c0,0,0,0,0,0c0.5,1.5,1.9,2.8,4,2.5c1.5-0.2,2.8-1.5,2.9-3.2\n\t\tc0.1-1.3-0.3-2.1-1-2.8c-0.5-0.5-1.2-1-2.1-1c-1.8-0.1-2.8,0.8-3.4,1.9c0,0,0,0,0,0c-0.3-1-0.7-1.8-1.3-2.4c0,0,0,0,0,0\n\t\tc0.8-0.9,2-1.7,3.6-1.9c1.7-0.3,3.3,0.3,4.3,1c0-0.7,0-1.4,0-2.1c-0.5,0-1.1,0-1.6,0c0-0.8,0-1.7,0-2.5C61.8,0,62.7,0,63.6,0z"/>\n            <path class="st2" fill="#fff" d="M63.6,0c0.5,0,1.1,0,1.6,0c0,0.9,0,1.9,0,2.8c-0.1-0.1-0.3-0.3-0.3-0.3l-1.3,0C63.6,2.5,63.6,0.8,63.6,0z"/>\n            <path class="st3" fill="#fff" d="M65.1,0c1.5,0,3.1,0,4.6,0c0,0.8,0,1.6,0,2.5c-0.5,0-1,0-1.4,0c0.8,1,1.7,2.1,2.5,3.1c0.8-1,1.7-2,2.5-3.1\n\t\tc0,0,0,0,0,0c-0.5,0-0.9,0-1.4,0c0-0.8,0-1.6,0-2.5c2.1,0,4.1,0,6.2,0c0,0.8,0,1.6,0,2.5c-0.4,0-0.9,0-1.3,0\n\t\tC75.4,4.2,74,6,72.6,7.7c1.4,1.8,2.9,3.6,4.4,5.4c0.4,0,0.8,0,1.2,0c0,0.9,0,1.7,0,2.6c-2.1,0-4.1,0-6.2,0c0-0.9,0-1.7,0-2.6\n\t\tc0.5,0,1,0,1.5,0c-0.8-1.1-1.8-2.2-2.6-3.3c-0.9,1.1-1.8,2.2-2.7,3.3c0.5,0,1,0,1.6,0c0,0.9,0,1.7,0,2.6c-0.9,0-1.8,0-2.7,0\n\t\tc0-0.8,0-1.7,0-2.5c-0.6,0-1.3,0-1.9,0c0-0.2,0-0.3,0-0.5c0,0,0,0,0,0c1.3-1.6,2.7-3.3,4-4.9c-1.3-1.7-2.6-3.3-4-4.9c0,0,0,0,0,0\n\t\tC65.1,1.9,65.1,0.9,65.1,0z"/>\n            <path class="st4" fill="#fff" d="M68.4,2.5c0.4,0,0.9,0,1.4,0C69.3,2.5,68.8,2.5,68.4,2.5z"/>\n            <path class="st4" fill="#fff" d="M72,2.5c0.5,0,0.9,0,1.4,0c0,0,0,0,0,0C72.9,2.5,72.4,2.5,72,2.5z"/>\n            <path class="st4" fill="#fff" d="M76.8,2.5c0.4,0,0.9,0,1.3,0C77.7,2.5,77.3,2.5,76.8,2.5z"/>\n            <path class="st4" fill="#fff" d="M50.1,3.5c0.1,0,0.4,0,0.5,0C50.4,3.5,50.2,3.5,50.1,3.5z"/>\n            <path class="st1" fill="#fff" d="M46.2,5.1c1-0.8,2.1-1.5,3.9-1.6c0.2,0,0.3,0,0.5,0c1.7,0.1,2.8,0.7,3.8,1.6c0.1,0.1,0.2,0.2,0.3,0.3\n\t\tc0,0,0.1,0.1,0.1,0.1c0,0,0,0,0,0c-0.6,0.6-1.1,1.4-1.4,2.4c0,0,0,0,0,0c-0.6-1-1.4-1.8-2.9-1.9c-0.1,0-0.2,0-0.3,0\n\t\tc-1,0-1.6,0.4-2.2,0.9c-0.1,0.1-0.2,0.2-0.3,0.3c-0.3,0.4-0.6,0.8-0.7,1.3c2.1,0,4.2,0,6.3,0c-0.1,0.6-0.1,1.4,0,2c0,0,0,0,0,0\n\t\tc-2.1,0-4.2,0-6.3,0c0.4,1.2,1.2,2.1,2.4,2.4c1.3,0.4,2.5-0.1,3.2-0.8c0.1-0.1,0.3-0.2,0.3-0.3c0.2,0,0.5,0,0.7,0c0,0,0,0,0,0\n\t\tc0.3,0.7,0.7,1.2,1.1,1.7c0,0,0,0,0,0c-1,1-2.2,1.8-4.1,2c-0.2,0-0.4,0-0.6,0c-1.7-0.1-3.1-0.8-4-1.8c-0.9-0.9-1.7-2.3-1.8-4\n\t\tc0-0.2,0-0.3,0-0.5c0.1-1.7,0.7-2.9,1.6-3.9C46,5.4,46.1,5.3,46.2,5.1z"/>\n            <path class="st2" fill="#fff" d="M54.7,5.5c0.6,0.7,1,1.4,1.3,2.4c-0.4,0.6-0.5,1.8-0.3,2.6c-0.9,0-1.7,0-2.6,0c-0.1-0.6-0.1-1.4,0-2\n\t\tc0.1,0,0.3,0,0.4,0c0-0.2-0.1-0.4-0.2-0.6C53.7,7,54.1,6.1,54.7,5.5z"/>\n            <path class="st4" fill="#fff" d="M53.3,7.9C53.4,7.9,53.4,7.9,53.3,7.9c0.1,0.2,0.2,0.4,0.3,0.6c-0.1,0-0.3,0-0.4,0C53.3,8.3,53.3,8.1,53.3,7.9\n\t\tz"/>\n            <path class="st5" fill="#fff" d="M56,7.9C56,7.9,56,7.9,56,7.9c0.2,0.8,0.3,1.8,0.1,2.6c-0.1,0-0.3,0-0.4,0c0,0,0,0,0,0\n\t\tC55.5,9.7,55.7,8.6,56,7.9z"/>\n            <path class="st2" fill="#fff" d="M53.6,12c0.7,0,1.5,0,2.2,0c-0.3,0.7-0.6,1.3-1.1,1.7C54.3,13.2,53.9,12.6,53.6,12z"/>\n            <path class="st2" fill="#fff" d="M65.1,12.6c0,0.2,0,0.3,0,0.5c0.6,0,1.3,0,1.9,0c0,0.8,0,1.7,0,2.5c-1.2,0-2.3,0-3.5,0c0-0.9,0-1.7,0-2.6\n\t\tc0.4,0,0.8,0,1.2,0C64.9,13,65,12.8,65.1,12.6z"/>\n            <path class="st4" fill="#fff" d="M54.4,5.1c0.1,0.1,0.2,0.2,0.3,0.3C54.5,5.3,54.4,5.2,54.4,5.1z"/>\n            <path class="st4" fill="#fff" d="M47.6,7.2C47.7,7.1,47.8,7,47.9,7C47.8,7.1,47.8,7.2,47.6,7.2z"/>\n        </g>\n\n    </symbol>\n    <symbol viewBox="0 0 100 100" id="logo-raccoon">\n        <path d="M68.6 10.2v12.6L57.3 20.3h0L50 20.3v0l-7.2 0h0l-11.3 2.5V10.2L12.8 28.9 0.9 40.7l0 0 9.2 9.2 13.5 13.5 9.3 9.3L50 89.8v0l17.1-17.1 9.3-9.3 13.4-13.5 9.2-9.2 -11.8-11.9L68.6 10.2zM64.3 71.8l0 0L50 66.7v0l-14.3 5.2 0 0 -9.7-9.8 9.6-5.9L50 53v0l14.4 3.1 9.6 5.9L64.3 71.8zM95.3 40.7l-7.5 7.6h0l-9.5-7.5 -9.6-3.9 -7.9 3.9L50 46V45.9l-10.7-5.2 -7.9-3.9 -9.6 3.9 -9.5 7.5 0 0 -7.5-7.6 0 0 12.6-12.6 11.6-11.6 0 9.9 0.1 0 14.7-3.6 0 0H50v0h6.4l14.7 3.6 0.1 0 0-9.9L82.7 28.1l12.6 12.6V40.7z" fill="#FFF" />\n    </symbol>\n</svg>\n\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.decode.utf8(static.optional_include_mako(is_theming_enabled=u'True',file=u'body-initial.html')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n<div id="page-prompt"></div>\n')
        if not disable_window_wrap:
            __M_writer(u'  <div class="window-wrap" dir="')
            __M_writer(filters.decode.utf8(static.dir_rtl()))
            __M_writer(u'">\n')
        __M_writer(u'    <a class="nav-skip sr-only sr-only-focusable" href="#main">')
        __M_writer(filters.decode.utf8(_("Skip to main content")))
        __M_writer(u'</a>\n\n')
        if not disable_header:
            __M_writer(u'        ')
            runtime._include_file(context, (static.get_template_path('header.html')), _template_uri, online_help_token=online_help_token)
            __M_writer(u'\n        ')
            runtime._include_file(context, u'/preview_menu.html', _template_uri)
            __M_writer(u'\n')
        __M_writer(u'\n    ')
        runtime._include_file(context, u'/page_banner.html', _template_uri)
        __M_writer(u'\n\n    <div class="marketing-hero">')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'marketing_hero'):
            context['self'].marketing_hero(**pageargs)
        

        __M_writer(u'</div>\n\n    <div class="content-wrapper main-container" id="content">\n      ')
        __M_writer(filters.decode.utf8(self.body()))
        __M_writer(u'\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyextra'):
            context['self'].bodyextra(**pageargs)
        

        __M_writer(u'\n    </div>\n\n')
        if not disable_footer:
            __M_writer(u'        ')
            runtime._include_file(context, (static.get_template_path('footer.html')), _template_uri)
            __M_writer(u'\n')
        __M_writer(u'\n')
        if not disable_window_wrap:
            __M_writer(u'  </div>\n')
        __M_writer(u'\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer_extra'):
            context['self'].footer_extra(**pageargs)
        

        __M_writer(u'\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n\n  ')
        runtime._include_file(context, u'widgets/segment-io-footer.html', _template_uri)
        __M_writer(u'\n  <script type="text/javascript" src="')
        __M_writer(filters.decode.utf8(static.url('js/vendor/noreferrer.js')))
        __M_writer(u'" charset="utf-8"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.decode.utf8(static.url('js/utils/navigation.js')))
        __M_writer(u'" charset="utf-8"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.decode.utf8(static.url('js/header/header.js')))
        __M_writer(u'"></script>\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.decode.utf8(static.optional_include_mako(is_theming_enabled=u'True',file=u'body-extra.html')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n</body>\n</html>\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head_extra():
            return render_head_extra(context)
        __M_writer = context.writer()
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


def render_js_overrides(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        def js_overrides():
            return render_js_overrides(context)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(filters.decode.utf8(render_require_js_path_overrides(settings.REQUIRE_JS_PATH_OVERRIDES) ))
        __M_writer(u'\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer_extra():
            return render_footer_extra(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer(u'\n      <title>\n       ')
        __M_writer(filters.decode.utf8(static.get_page_title_breadcrumbs(self.pagetitle())))
        __M_writer(u'\n      </title>\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagetitle(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def js_extra():
            return render_js_extra(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_marketing_hero(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def marketing_hero():
            return render_marketing_hero(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyextra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyextra():
            return render_bodyextra(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headextra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headextra():
            return render_headextra(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login_query(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        login_redirect_url = context.get('login_redirect_url', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(filters.decode.utf8(
  u"?next={next}".format(
    next=urlquote_plus(login_redirect_url if login_redirect_url else request.path)
  ) if (login_redirect_url or request) else ""
))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"517": 329, "527": 517, "16": 10, "18": 15, "38": 13, "41": 0, "80": 2, "81": 7, "82": 10, "83": 13, "84": 14, "88": 14, "89": 26, "90": 28, "91": 28, "92": 29, "93": 29, "94": 30, "95": 30, "96": 39, "97": 41, "102": 46, "103": 48, "104": 49, "105": 58, "106": 59, "113": 62, "114": 64, "115": 65, "116": 80, "117": 80, "118": 80, "119": 81, "120": 81, "121": 83, "122": 83, "130": 85, "133": 85, "134": 86, "135": 87, "136": 88, "137": 88, "143": 90, "144": 91, "145": 91, "146": 92, "147": 93, "148": 93, "149": 93, "150": 95, "151": 96, "159": 96, "162": 96, "163": 98, "164": 99, "165": 100, "173": 100, "176": 100, "184": 101, "187": 101, "188": 102, "189": 103, "197": 103, "200": 103, "208": 104, "211": 104, "212": 106, "220": 107, "223": 107, "224": 109, "225": 111, "226": 111, "227": 111, "228": 113, "229": 115, "230": 115, "231": 122, "232": 122, "237": 125, "242": 127, "247": 128, "248": 130, "249": 130, "250": 132, "251": 132, "252": 133, "253": 133, "261": 134, "264": 134, "265": 136, "266": 136, "267": 137, "268": 137, "269": 139, "270": 139, "271": 141, "275": 141, "276": 142, "277": 143, "278": 143, "279": 143, "280": 145, "281": 146, "282": 146, "283": 148, "287": 148, "288": 149, "289": 150, "290": 152, "291": 152, "292": 162, "293": 163, "297": 163, "298": 164, "299": 165, "300": 167, "301": 167, "302": 170, "303": 173, "304": 173, "309": 173, "310": 173, "311": 173, "319": 289, "322": 289, "323": 291, "324": 292, "325": 292, "326": 292, "327": 294, "328": 294, "329": 294, "330": 296, "331": 297, "332": 297, "333": 297, "334": 298, "335": 298, "336": 300, "337": 301, "338": 301, "343": 303, "344": 306, "345": 306, "350": 307, "351": 310, "352": 311, "353": 311, "354": 311, "355": 313, "356": 314, "357": 315, "358": 317, "363": 318, "368": 319, "369": 321, "370": 321, "371": 322, "372": 322, "373": 323, "374": 323, "375": 324, "376": 324, "384": 325, "387": 325, "388": 333, "394": 128, "405": 173, "416": 123, "423": 123, "424": 124, "425": 124, "431": 318, "442": 42, "450": 42, "451": 44, "452": 44, "458": 41, "467": 319, "478": 303, "489": 307, "500": 127, "511": 329}, "uri": "custome-theme/lms/templates/main.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/main.html"}
__M_END_METADATA
"""
