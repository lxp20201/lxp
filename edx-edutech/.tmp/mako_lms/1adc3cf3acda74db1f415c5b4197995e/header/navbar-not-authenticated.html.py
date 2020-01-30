# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580210685.095771
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/header/navbar-not-authenticated.html'
_template_uri = u'header/navbar-not-authenticated.html'
_source_encoding = 'utf-8'
_exports = []



from django.urls import reverse
from django.utils.translation import ugettext as _
from six import text_type


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

    ns = runtime.TemplateNamespace('__anon_0x7f49385f73d0', context._clean_inheritance_tokens(), templateuri=u'../main.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f49385f73d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f49385f73d0')._populate(_import_ns, [u'login_query'])
        marketing_link = _import_ns.get('marketing_link', context.get('marketing_link', UNDEFINED))
        settings = _import_ns.get('settings', context.get('settings', UNDEFINED))
        combined_login_and_register = _import_ns.get('combined_login_and_register', context.get('combined_login_and_register', UNDEFINED))
        course = _import_ns.get('course', context.get('course', UNDEFINED))
        static = _mako_get_namespace(context, 'static')
        login_query = _import_ns.get('login_query', context.get('login_query', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')

        mktg_site_enabled = static.get_value('ENABLE_MKTG_SITE', settings.FEATURES.get('ENABLE_MKTG_SITE', False))
        courses_are_browsable = settings.FEATURES.get('COURSES_ARE_BROWSABLE')
        allows_login = not settings.FEATURES['DISABLE_LOGIN_BUTTON'] and not combined_login_and_register
        can_discover_courses = settings.FEATURES.get('ENABLE_COURSE_DISCOVERY')
        restrict_enroll_for_course = course and settings.FEATURES.get('RESTRICT_ENROLL_BY_REG_METHOD') and course.enrollment_domain
        allow_public_account_creation = static.get_value('ALLOW_PUBLIC_ACCOUNT_CREATION', settings.FEATURES.get('ALLOW_PUBLIC_ACCOUNT_CREATION'))
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['restrict_enroll_for_course','can_discover_courses','mktg_site_enabled','allow_public_account_creation','courses_are_browsable','allows_login'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n<nav class="nav-links" aria-label=')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Supplemental Links"))))
        __M_writer(u'>\n  <div class="main">\n')
        if mktg_site_enabled:
            __M_writer(u'    <div class="mobile-nav-item hidden-mobile nav-item">\n      <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('HOW_IT_WORKS'))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("How it Works"))))
            __M_writer(u'</a>\n    </div>\n')
            if courses_are_browsable:
                __M_writer(u'      <div class="mobile-nav-item hidden-mobile nav-item">\n        <a href="')
                __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('COURSES'))))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Courses"))))
                __M_writer(u'</a>\n      </div>\n')
            __M_writer(u'    <div class="mobile-nav-item hidden-mobile nav-item">\n      <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('SCHOOLS'))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Schools"))))
            __M_writer(u'</a>\n    </div>\n')
        if allows_login:
            if can_discover_courses:
                __M_writer(u'      <div class="mobile-nav-item hidden-mobile nav-item">\n        <a href="/courses">')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Explore courses'))))
                __M_writer(u'</a>\n      </div>\n')
        __M_writer(u'  </div>\n  <div class="secondary">\n    <div>\n')
        if allows_login:
            if restrict_enroll_for_course:
                __M_writer(u'          <div class="mobile-nav-item hidden-mobile nav-item">\n            <a class="register-btn btn" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(reverse('course-specific-register', args=[text_type(course.id)]))))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Register"))))
                __M_writer(u'</a>\n          </div>\n          <div class="mobile-nav-item hidden-mobile nav-item">\n            <a class="sign-in-btn btn" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(reverse('course-specific-login', args=[text_type(course.id)]))))
                __M_writer(filters.html_escape(filters.decode.utf8(login_query())))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Sign in"))))
                __M_writer(u'</a>\n          </div>\n')
            else:
                if allow_public_account_creation:
                    __M_writer(u'            <div class="mobile-nav-item hidden-mobile nav-item">\n              <a class="register-btn btn" href="/register')
                    __M_writer(filters.html_escape(filters.decode.utf8(login_query())))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_("Register"))))
                    __M_writer(u'</a>\n            </div>\n')
                __M_writer(u'          <div class="mobile-nav-item hidden-mobile nav-item">\n            <a class="sign-in-btn btn" href="/login')
                __M_writer(filters.html_escape(filters.decode.utf8(login_query())))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Sign in"))))
                __M_writer(u'</a>\n          </div>\n')
        __M_writer(u'    </div>\n  </div>\n</nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 8, "29": 5, "32": 6, "35": 3, "48": 2, "49": 3, "50": 5, "51": 6, "52": 12, "53": 14, "64": 21, "65": 22, "66": 22, "67": 24, "68": 25, "69": 26, "70": 26, "71": 26, "72": 26, "73": 28, "74": 29, "75": 30, "76": 30, "77": 30, "78": 30, "79": 33, "80": 34, "81": 34, "82": 34, "83": 34, "84": 37, "85": 38, "86": 39, "87": 40, "88": 40, "89": 44, "90": 47, "91": 48, "92": 49, "93": 50, "94": 50, "95": 50, "96": 50, "97": 53, "98": 53, "99": 53, "100": 53, "101": 53, "102": 55, "103": 56, "104": 57, "105": 58, "106": 58, "107": 58, "108": 58, "109": 61, "110": 62, "111": 62, "112": 62, "113": 62, "114": 66, "120": 114}, "uri": "header/navbar-not-authenticated.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/header/navbar-not-authenticated.html"}
__M_END_METADATA
"""
