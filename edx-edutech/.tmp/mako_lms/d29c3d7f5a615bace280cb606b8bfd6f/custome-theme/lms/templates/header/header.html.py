# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580296465.528049
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/header/header.html'
_template_uri = 'custome-theme/lms/templates/header/header.html'
_source_encoding = 'utf-8'
_exports = [u'js_extra', u'navigation_top', u'navigation_other_global_links', u'navigation_global_links_authenticated']



from django.urls import reverse
from django.utils.translation import ugettext as _

from lms.djangoapps.ccx.overrides import get_current_ccx
from openedx.core.djangolib.markup import HTML, Text

# App that handles subdomain specific branding
from branding import api as branding_api
from openedx.core.djangoapps.lang_pref.api import header_language_selector_is_enabled, released_languages



def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

    ns = runtime.TemplateNamespace('__anon_0x7f8feee166d0', context._clean_inheritance_tokens(), templateuri=u'../main.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8feee166d0')] = ns

def render_body(context,online_help_token,use_cookie_banner=False,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(use_cookie_banner=use_cookie_banner,pageargs=pageargs,online_help_token=online_help_token)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8feee166d0')._populate(_import_ns, [u'login_query'])
        csrf_token = _import_ns.get('csrf_token', context.get('csrf_token', UNDEFINED))
        marketing_link = _import_ns.get('marketing_link', context.get('marketing_link', UNDEFINED))
        settings = _import_ns.get('settings', context.get('settings', UNDEFINED))
        request = _import_ns.get('request', context.get('request', UNDEFINED))
        show_program_listing = _import_ns.get('show_program_listing', context.get('show_program_listing', UNDEFINED))
        def navigation_top():
            return render_navigation_top(context._locals(__M_locals))
        def navigation_other_global_links():
            return render_navigation_other_global_links(context._locals(__M_locals))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        course = _import_ns.get('course', context.get('course', UNDEFINED))
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        static = _mako_get_namespace(context, 'static')
        user = _import_ns.get('user', context.get('user', UNDEFINED))
        LANGUAGE_CODE = _import_ns.get('LANGUAGE_CODE', context.get('LANGUAGE_CODE', UNDEFINED))
        uses_pattern_library = _import_ns.get('uses_pattern_library', context.get('uses_pattern_library', UNDEFINED))
        def navigation_global_links_authenticated():
            return render_navigation_global_links_authenticated(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navigation_top'):
            context['self'].navigation_top(**pageargs)
        

        __M_writer(u'\n\n')
        if uses_pattern_library:
            __M_writer(u'    ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
                context['self'].js_extra(**pageargs)
            

            __M_writer(u'\n')
        __M_writer(u'\n<header class="global-header theme-header ')
        __M_writer(filters.html_escape(filters.decode.utf8('slim' if course else '')))
        __M_writer(u'">\n    <div class="theme-header-info">\n        <div class="theme-header-info_contact">\n            <span class="theme-header-info_text">Have any question?</span>\n            <span class="theme-header-info_phone"><i class="fa fa-phone" aria-hidden="true"></i> +1 857 4533328</span>\n            <a class="theme-header-info_mail" href="mailto:cintanatech@gmail.com"><i class="fa fa-envelope" aria-hidden="true"></i>cintanatech@gmail.com</a>\n        </div>\n        <div class="theme-header-info_social">\n            <span class="theme-header-info_text">Find us in social network</span>\n            <ul class="social-list">\n                <li class="social-list_item"><a class="social-list_link" href="https://twitter.com/raccoongangcom" target="_blank"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>\n                <li class="social-list_item"><a class="social-list_link" href="https://www.facebook.com/raccoongangco" target="_blank"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>\n                <li class="social-list_item"><a class="social-list_link" href="https://www.linkedin.com/company/raccoon-gang" target="_blank"><i class="fa fa-linkedin" aria-hidden="true"></i></a></li>\n            </ul>\n        </div>\n    </div>\n    <div class="holder">\n')
        if use_cookie_banner:
            __M_writer(u'            ')
            __M_writer(filters.html_escape(filters.decode.utf8(static.renderReact(
                component="CookiePolicyBanner",
                id="cookie-policy-banner",
                props={}
            ))))
            __M_writer(u'\n')
        __M_writer(u'        <div class="main-header">\n            ')
        runtime._include_file(context, u'navbar-logo-header.html', _template_uri, online_help_token=online_help_token)
        __M_writer(u'\n')
        if user.is_authenticated:
            __M_writer(u'                ')
            runtime._include_file(context, u'navbar-authenticated.html', _template_uri, online_help_token=online_help_token)
            __M_writer(u'\n')
        else:
            __M_writer(u'                ')
            runtime._include_file(context, u'navbar-not-authenticated.html', _template_uri, online_help_token=online_help_token)
            __M_writer(u'\n')
        __M_writer(u'        </div>\n        <div class="mobile-menu hidden" aria-label=')
        __M_writer(filters.html_escape(filters.decode.utf8(_("More Options"))))
        __M_writer(u' role="menu" id="mobile-menu"></div>\n    </div>\n\n    <div class="theme-main-nav">\n        <div class="theme-main-nav_opener">\n            <span class="line"></span>\n            <span class="line"></span>\n            <span class="line"></span>\n            <span class="line"></span>\n        </div>\n        <div class="theme-main-nav_logo">\n            <a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('ROOT'))))
        __M_writer(u'">\n          <span class="theme-nav-wrapper_logo-holder theme-nav-wrapper_logo-holder_small">\n              <img src="/static/')
        __M_writer(filters.html_escape(filters.decode.utf8(settings.FEATURES.get('MARVEL_YELLOW_DEFAULT_HAWTHORN_SITE_THEME', settings.DEFAULT_SITE_THEME))))
        __M_writer(u'/images/logo.png" alt="logo">\n          </span>\n            </a>\n        </div>\n        <nav class="theme-main-nav_holder">\n            <ul class="theme-main-nav_list">\n                <li class="theme-main-nav_item"><a href="/about" class="theme-main-nav_link">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("About The CintanaTech"))))
        __M_writer(u'</a></li>\n                <li class="theme-main-nav_item"><a href="/blog" class="theme-main-nav_link">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Blog"))))
        __M_writer(u'</a></li>\n                <li class="theme-main-nav_item"><a href="/contact" class="theme-main-nav_link">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Contact Us"))))
        __M_writer(u'</a></li>\n')
        if user.is_authenticated():
            __M_writer(u'                ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'navigation_global_links_authenticated'):
                context['self'].navigation_global_links_authenticated(**pageargs)
            

            __M_writer(u'\n')
        else:
            __M_writer(u'            ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'navigation_other_global_links'):
                context['self'].navigation_other_global_links(**pageargs)
            

            __M_writer(u'\n')
        __M_writer(u'        </ul>\n        </nav>\n    </div>\n</header>\n\n<script>\n    $(".theme-main-nav_opener").on("click", function open(){\n        if ($(this).parent().hasClass("theme-main-nav__open")){\n            $(this).parent().removeClass("theme-main-nav__open");\n        } else {\n            $(this).parent().addClass("theme-main-nav__open");\n        }\n    });\n</script>\n\n')
        if course:
            __M_writer(u'<!--[if lte IE 9]>\n<div class="ie-banner" aria-hidden="true">')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_('{begin_strong}Warning:{end_strong} Your browser is not fully supported. We strongly recommend using {chrome_link} or {ff_link}.')).format(
    begin_strong=HTML('<strong>'),
    end_strong=HTML('</strong>'),
    chrome_link=HTML('<a href="https://www.google.com/chrome" target="_blank">Chrome</a>'),
    ff_link=HTML('<a href="http://www.mozilla.org/firefox" target="_blank">Firefox</a>'),
))))
            __M_writer(u'</div>\n<![endif]-->\n')
        __M_writer(u'\n')
        if settings.FEATURES.get('ENABLE_COOKIE_CONSENT', False):
            __M_writer(u'  ')
            runtime._include_file(context, u'../widgets/cookie-consent.html', _template_uri)
            __M_writer(u'\n')
        __M_writer(u'\n')
        if header_language_selector_is_enabled():
            __M_writer(u'    ')
            languages = released_languages() 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['languages'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            if len(languages) > 1:
                __M_writer(u'        <form action="/i18n/setlang/" method="post" class="settings-language-form" id="language-settings-form">\n            <input type="hidden" id="csrf_token" name="csrfmiddlewaretoken" value="')
                __M_writer(filters.html_escape(filters.decode.utf8(csrf_token)))
                __M_writer(u'">\n')
                if user.is_authenticated:
                    __M_writer(u'                <input title="preference api" type="hidden" class="url-endpoint" value="')
                    __M_writer(filters.html_escape(filters.decode.utf8(reverse('preferences_api', kwargs={'username': user.username}))))
                    __M_writer(u'" data-user-is-authenticated="true">\n')
                else:
                    __M_writer(u'                <input title="session update url" type="hidden" class="url-endpoint" value="')
                    __M_writer(filters.html_escape(filters.decode.utf8(reverse('session_language'))))
                    __M_writer(u'" data-user-is-authenticated="false">\n')
                __M_writer(u'            <label><span class="sr">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Choose Language"))))
                __M_writer(u'</span>\n            <select class="input select language-selector" id="settings-language-value" name="language">\n')
                for language in languages:
                    if language[0] == LANGUAGE_CODE:
                        __M_writer(u'                        <option value="')
                        __M_writer(filters.html_escape(filters.decode.utf8(language[0])))
                        __M_writer(u'" selected="selected">')
                        __M_writer(filters.html_escape(filters.decode.utf8(language[1])))
                        __M_writer(u'</option>\n')
                    else:
                        __M_writer(u'                        <option value="')
                        __M_writer(filters.html_escape(filters.decode.utf8(language[0])))
                        __M_writer(u'" >')
                        __M_writer(filters.html_escape(filters.decode.utf8(language[1])))
                        __M_writer(u'</option>\n')
                __M_writer(u'            </select>\n            </label>\n        </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8feee166d0')._populate(_import_ns, [u'login_query'])
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n    HeaderFactory();\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'HeaderFactory',module_name=u'js/header_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navigation_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8feee166d0')._populate(_import_ns, [u'login_query'])
        def navigation_top():
            return render_navigation_top(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navigation_other_global_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8feee166d0')._populate(_import_ns, [u'login_query'])
        def navigation_other_global_links():
            return render_navigation_other_global_links(context)
        settings = _import_ns.get('settings', context.get('settings', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if not settings.FEATURES['DISABLE_LOGIN_BUTTON']:
            if settings.FEATURES.get('ENABLE_COURSE_DISCOVERY'):
                __M_writer(u'            <li class="theme-main-nav_item">\n                <a class="theme-main-nav_link" href="/courses">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Explore Courses"))))
                __M_writer(u'</a>\n            </li>\n')
        __M_writer(u'        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navigation_global_links_authenticated(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8feee166d0')._populate(_import_ns, [u'login_query'])
        marketing_link = _import_ns.get('marketing_link', context.get('marketing_link', UNDEFINED))
        settings = _import_ns.get('settings', context.get('settings', UNDEFINED))
        show_program_listing = _import_ns.get('show_program_listing', context.get('show_program_listing', UNDEFINED))
        request = _import_ns.get('request', context.get('request', UNDEFINED))
        user = _import_ns.get('user', context.get('user', UNDEFINED))
        def navigation_global_links_authenticated():
            return render_navigation_global_links_authenticated(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if settings.FEATURES.get('COURSES_ARE_BROWSABLE') and not show_program_listing:
            __M_writer(u'                <li class="theme-main-nav_item">\n                    <a class="theme-main-nav_link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('COURSES'))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Explore Courses"))))
            __M_writer(u'</a>\n                </li>\n')
        if show_program_listing:
            __M_writer(u'                <li class="theme-main-nav_item">\n                    <a class="')
            __M_writer(filters.html_escape(filters.decode.utf8('active ' if reverse('dashboard') == request.path else '')))
            __M_writer(u'theme-main-nav_link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('dashboard'))))
            __M_writer(u'">\n                        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Courses"))))
            __M_writer(u'\n                    </a>\n                </li>\n                <li class="theme-main-nav_item">\n                    <a class="')
            __M_writer(filters.html_escape(filters.decode.utf8('active ' if reverse('program_listing_view') in request.path else '')))
            __M_writer(u'theme-main-nav_link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('program_listing_view'))))
            __M_writer(u'">\n                        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Programs"))))
            __M_writer(u'\n                    </a>\n                </li>\n')
        if settings.FEATURES.get('ENABLE_SYSADMIN_DASHBOARD','') and user.is_staff:
            __M_writer(u'                <li class="theme-main-nav_item">\n')
            __M_writer(u'                    <a class="theme-main-nav_link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('sysadmin'))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Sysadmin"))))
            __M_writer(u'</a>\n                </li>\n')
        __M_writer(u'            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 7, "36": 5, "39": 6, "42": 3, "68": 2, "69": 3, "70": 5, "71": 6, "72": 18, "77": 21, "78": 24, "79": 25, "84": 29, "85": 31, "86": 32, "87": 32, "88": 49, "89": 50, "90": 50, "95": 54, "96": 56, "97": 57, "98": 57, "99": 58, "100": 59, "101": 59, "102": 59, "103": 60, "104": 61, "105": 61, "106": 61, "107": 63, "108": 64, "109": 64, "110": 75, "111": 75, "112": 77, "113": 77, "114": 83, "115": 83, "116": 84, "117": 84, "118": 85, "119": 85, "120": 86, "121": 87, "126": 111, "127": 112, "128": 113, "133": 121, "134": 123, "135": 138, "136": 139, "137": 140, "143": 145, "144": 148, "145": 149, "146": 150, "147": 150, "148": 150, "149": 152, "150": 153, "151": 154, "152": 154, "156": 154, "157": 155, "158": 156, "159": 157, "160": 157, "161": 158, "162": 159, "163": 159, "164": 159, "165": 160, "166": 161, "167": 161, "168": 161, "169": 163, "170": 163, "171": 163, "172": 165, "173": 166, "174": 167, "175": 167, "176": 167, "177": 167, "178": 167, "179": 168, "180": 169, "181": 169, "182": 169, "183": 169, "184": 169, "185": 172, "191": 25, "200": 25, "204": 26, "209": 26, "212": 28, "218": 21, "231": 113, "240": 113, "241": 114, "242": 115, "243": 116, "244": 117, "245": 117, "246": 121, "252": 87, "265": 87, "266": 88, "267": 89, "268": 90, "269": 90, "270": 90, "271": 90, "272": 93, "273": 94, "274": 95, "275": 95, "276": 95, "277": 95, "278": 96, "279": 96, "280": 100, "281": 100, "282": 100, "283": 100, "284": 101, "285": 101, "286": 105, "287": 106, "288": 108, "289": 108, "290": 108, "291": 108, "292": 108, "293": 111, "299": 293}, "uri": "custome-theme/lms/templates/header/header.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/header/header.html"}
__M_END_METADATA
"""
