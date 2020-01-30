# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580212376.43051
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/header/navbar-authenticated.html'
_template_uri = u'header/navbar-authenticated.html'
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
    ns = runtime.TemplateNamespace('__anon_0x7f1b4b8b7a50', context._clean_inheritance_tokens(), templateuri=u'../main.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1b4b8b7a50')] = ns

    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,online_help_token,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,online_help_token=online_help_token)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1b4b8b7a50')._populate(_import_ns, [u'login_query'])
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
            __M_writer(u'"\n             aria-current="')
            __M_writer(filters.html_escape(filters.decode.utf8('page' if reverse('dashboard') == request.path else 'false')))
            __M_writer(u'">\n             ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Courses"))))
            __M_writer(u'\n        </a>\n      </div>\n')
            if show_program_listing:
                __M_writer(u'        <div class="mobile-nav-item hidden-mobile nav-item nav-tab">\n          <a class="')
                __M_writer(filters.html_escape(filters.decode.utf8('active ' if reverse('program_listing_view') in request.path else '')))
                __M_writer(u'tab-nav-link" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(reverse('program_listing_view'))))
                __M_writer(u'"\n             aria-current="')
                __M_writer(filters.html_escape(filters.decode.utf8('page' if reverse('program_listing_view') == request.path else 'false')))
                __M_writer(u'">\n             ')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Programs"))))
                __M_writer(u'\n          </a>\n        </div>\n')
            if show_journal_listing:
                __M_writer(u'        <div class="mobile-nav-item hidden-mobile nav-item nav-tab">\n          <a class="')
                __M_writer(filters.html_escape(filters.decode.utf8('active ' if reverse('openedx.journals.dashboard') in request.path else '')))
                __M_writer(u'tab-nav-link" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(reverse('openedx.journals.dashboard'))))
                __M_writer(u'"\n             aria-current="')
                __M_writer(filters.html_escape(filters.decode.utf8('page' if reverse('openedx.journals.dashboard') == request.path else 'false')))
                __M_writer(u'">\n             ')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Journals"))))
                __M_writer(u'\n          </a>\n        </div>\n')
            __M_writer(u'      <div class="mobile-nav-item hidden-mobile nav-item nav-tab">\n          <a class="')
            __M_writer(filters.html_escape(filters.decode.utf8('active ' if '/u/' in request.path  else '')))
            __M_writer(u'tab-nav-link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('learner_profile', args=[self.real_user.username]))))
            __M_writer(u'"\n             aria-current="')
            __M_writer(filters.html_escape(filters.decode.utf8('page' if '/u/' in request.path else 'false')))
            __M_writer(u'">\n             ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Profile"))))
            __M_writer(u'\n          </a>\n      </div>\n')
        if show_explore_courses:
            __M_writer(u'      <div class="mobile-nav-item hidden-mobile nav-item nav-tab">\n          <a class="tab-nav-link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('COURSES'))))
            __M_writer(u'"\n             aria-current="')
            __M_writer(filters.html_escape(filters.decode.utf8('page' if '/courses' in request.path else 'false')))
            __M_writer(u'">\n             ')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Discover New'))))
            __M_writer(u'\n          </a>\n      </div>\n')
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
{"source_encoding": "utf-8", "line_map": {"128": 72, "129": 72, "130": 72, "131": 72, "132": 72, "133": 75, "134": 77, "135": 78, "136": 79, "137": 79, "138": 80, "139": 80, "140": 84, "141": 85, "142": 85, "143": 85, "16": 7, "145": 87, "146": 87, "144": 85, "152": 146, "29": 6, "32": 5, "35": 3, "55": 2, "56": 3, "57": 5, "58": 6, "59": 11, "60": 13, "78": 27, "79": 31, "80": 32, "81": 33, "82": 33, "83": 33, "84": 33, "85": 34, "86": 34, "87": 35, "88": 35, "89": 38, "90": 39, "91": 40, "92": 40, "93": 40, "94": 40, "95": 41, "96": 41, "97": 42, "98": 42, "99": 46, "100": 47, "101": 48, "102": 48, "103": 48, "104": 48, "105": 49, "106": 49, "107": 50, "108": 50, "109": 54, "110": 55, "111": 55, "112": 55, "113": 55, "114": 56, "115": 56, "116": 57, "117": 57, "118": 61, "119": 62, "120": 63, "121": 63, "122": 64, "123": 64, "124": 65, "125": 65, "126": 69, "127": 70}, "uri": "header/navbar-authenticated.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/header/navbar-authenticated.html"}
__M_END_METADATA
"""
