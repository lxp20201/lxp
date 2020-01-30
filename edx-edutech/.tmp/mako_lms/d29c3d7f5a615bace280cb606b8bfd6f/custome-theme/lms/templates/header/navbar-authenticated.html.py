# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580283887.032488
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/header/navbar-authenticated.html'
_template_uri = u'custome-theme/lms/templates/header/navbar-authenticated.html'
_source_encoding = 'utf-8'
_exports = []



from django.urls import reverse
from django.utils.translation import ugettext as _
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7fef63142a10', context._clean_inheritance_tokens(), templateuri=u'../main.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fef63142a10')] = ns

    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,online_help_token,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,online_help_token=online_help_token)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fef63142a10')._populate(_import_ns, [u'login_query'])
        marketing_link = _import_ns.get('marketing_link', context.get('marketing_link', UNDEFINED))
        settings = _import_ns.get('settings', context.get('settings', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        show_program_listing = _import_ns.get('show_program_listing', context.get('show_program_listing', UNDEFINED))
        request = _import_ns.get('request', context.get('request', UNDEFINED))
        should_display_shopping_cart_func = _import_ns.get('should_display_shopping_cart_func', context.get('should_display_shopping_cart_func', UNDEFINED))
        course = _import_ns.get('course', context.get('course', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        get_online_help_info = _import_ns.get('get_online_help_info', context.get('get_online_help_info', UNDEFINED))
        static = _mako_get_namespace(context, 'static')
        user = _import_ns.get('user', context.get('user', UNDEFINED))
        show_journal_listing = _import_ns.get('show_journal_listing', context.get('show_journal_listing', UNDEFINED))
        show_dashboard_tabs = _import_ns.get('show_dashboard_tabs', context.get('show_dashboard_tabs', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')

        show_explore_courses = settings.FEATURES.get('COURSES_ARE_BROWSABLE') and not show_program_listing
        show_sysadmin_dashboard = settings.FEATURES.get('ENABLE_SYSADMIN_DASHBOARD','') and user.is_staff
        self.real_user = getattr(user, 'real_user', user)
        
        support_link = configuration_helpers.get_value('SUPPORT_SITE_LINK', settings.SUPPORT_SITE_LINK)
        doc_link = get_online_help_info(online_help_token)['doc_url']
        
        if online_help_token == "instructor":
          help_link = doc_link
        elif support_link:
          help_link = support_link
        else:
          help_link = doc_link
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['show_sysadmin_dashboard','support_link','show_explore_courses','doc_link','help_link'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n<div class="nav-links">\n  <div class="main">\n')
        if show_dashboard_tabs:
            __M_writer(u'      <div class="mobile-nav-item hidden-mobile nav-item nav-tab">\n        <a class="')
            __M_writer(filters.html_escape(filters.decode.utf8('active ' if reverse('dashboard') == request.path else '')))
            __M_writer(u'tab-nav-link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('dashboard'))))
            __M_writer(u'">\n          ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Courses"))))
            __M_writer(u'\n        </a>\n      </div>\n')
            if show_program_listing:
                __M_writer(u'        <div class="mobile-nav-item hidden-mobile nav-item nav-tab">\n          <a class="')
                __M_writer(filters.html_escape(filters.decode.utf8('active ' if reverse('program_listing_view') in request.path else '')))
                __M_writer(u'tab-nav-link" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(reverse('program_listing_view'))))
                __M_writer(u'">\n            ')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Programs"))))
                __M_writer(u'\n          </a>\n        </div>\n')
            if show_journal_listing:
                __M_writer(u'        <div class="mobile-nav-item hidden-mobile nav-item nav-tab">\n          <a class="')
                __M_writer(filters.html_escape(filters.decode.utf8('active ' if reverse('openedx.journals.dashboard') in request.path else '')))
                __M_writer(u'tab-nav-link" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(reverse('openedx.journals.dashboard'))))
                __M_writer(u'">\n            ')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Journals"))))
                __M_writer(u'\n          </a>\n        </div>\n')
            __M_writer(u'      <div class="mobile-nav-item hidden-mobile nav-item nav-tab">\n        <a class="')
            __M_writer(filters.html_escape(filters.decode.utf8('active ' if '/u/' in request.path  else '')))
            __M_writer(u'tab-nav-link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('learner_profile', args=[self.real_user.username]))))
            __M_writer(u'">\n          ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Profile"))))
            __M_writer(u'\n        </a>\n      </div>\n')
        if show_explore_courses:
            __M_writer(u'      <div class="mobile-nav-item hidden-mobile nav-item nav-tab">\n        <a class="tab-nav-link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('COURSES'))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Discover New"))))
            __M_writer(u'</a>\n      </div>\n')
        if show_sysadmin_dashboard:
            __M_writer(u'      <div class="mobile-nav-item hidden-mobile nav-item nav-tab">\n')
            __M_writer(u'        <a class="tab-nav-link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('sysadmin'))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Sysadmin"))))
            __M_writer(u'</a>\n      </div>\n')
        __M_writer(u'  </div>\n  <div class="secondary">\n')
        if should_display_shopping_cart_func() and not (course and static.is_request_in_themed_site()): # see shoppingcart.context_processor.user_has_cart_context_processor
            __M_writer(u'      <div class="mobile-nav-item hidden-mobile nav-item">\n        <a class="shopping-cart" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('shoppingcart.views.show_cart'))))
            __M_writer(u'">\n          <span class="icon fa fa-shopping-cart" aria-hidden="true"></span> ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Shopping Cart"))))
            __M_writer(u'\n        </a>\n      </div>\n')
        __M_writer(u'    <div class="mobile-nav-item hidden-mobile nav-item">\n      <a class="help-link" href="')
        __M_writer(filters.html_escape(filters.decode.utf8(help_link)))
        __M_writer(u'" target="_blank">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Help"))))
        __M_writer(u'</a>\n    </div>\n    ')
        runtime._include_file(context, u'user_dropdown.html', _template_uri)
        __M_writer(u'\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 73, "129": 73, "130": 77, "131": 78, "132": 78, "133": 78, "134": 78, "135": 80, "136": 80, "142": 136, "16": 7, "29": 6, "32": 5, "35": 3, "55": 2, "56": 3, "57": 5, "58": 6, "59": 11, "60": 13, "78": 27, "79": 31, "80": 32, "81": 33, "82": 33, "83": 33, "84": 33, "85": 34, "86": 34, "87": 37, "88": 38, "89": 39, "90": 39, "91": 39, "92": 39, "93": 40, "94": 40, "95": 44, "96": 45, "97": 46, "98": 46, "99": 46, "100": 46, "101": 47, "102": 47, "103": 51, "104": 52, "105": 52, "106": 52, "107": 52, "108": 53, "109": 53, "110": 57, "111": 58, "112": 59, "113": 59, "114": 59, "115": 59, "116": 62, "117": 63, "118": 65, "119": 65, "120": 65, "121": 65, "122": 65, "123": 68, "124": 70, "125": 71, "126": 72, "127": 72}, "uri": "custome-theme/lms/templates/header/navbar-authenticated.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/header/navbar-authenticated.html"}
__M_END_METADATA
"""
