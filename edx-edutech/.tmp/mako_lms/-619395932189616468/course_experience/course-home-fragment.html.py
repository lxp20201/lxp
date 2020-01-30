# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284738.434351
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/openedx/features/course_experience/templates/course_experience/course-home-fragment.html'
_template_uri = 'course_experience/course-home-fragment.html'
_source_encoding = 'utf-8'
_exports = [u'content', u'header_extras']



import json

from django.conf import settings
from django.utils.translation import ugettext as _
from django.template.defaultfilters import escapejs
from django.urls import reverse

from django_comment_client.permissions import has_permission
from openedx.core.djangolib.js_utils import dump_js_escaped_json, js_escaped_string
from openedx.core.djangolib.markup import HTML
from openedx.features.course_experience import UNIFIED_COURSE_TAB_FLAG, SHOW_REVIEWS_TOOL_FLAG
from openedx.features.learner_analytics import ENABLE_DASHBOARD_TAB
from openedx.features.portfolio_project import INCLUDE_PORTFOLIO_UPSELL_MODAL


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        resume_course_url = context.get('resume_course_url', UNDEFINED)
        course_home_message_fragment = context.get('course_home_message_fragment', UNDEFINED)
        upgrade_price = context.get('upgrade_price', UNDEFINED)
        upgrade_url = context.get('upgrade_url', UNDEFINED)
        has_goal_permission = context.get('has_goal_permission', UNDEFINED)
        update_message_fragment = context.get('update_message_fragment', UNDEFINED)
        course_tools = context.get('course_tools', UNDEFINED)
        handouts_html = context.get('handouts_html', UNDEFINED)
        course_key = context.get('course_key', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        course = context.get('course', UNDEFINED)
        goal_options = context.get('goal_options', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        course_sock_fragment = context.get('course_sock_fragment', UNDEFINED)
        current_goal = context.get('current_goal', UNDEFINED)
        dates_fragment = context.get('dates_fragment', UNDEFINED)
        course_expiration_fragment = context.get('course_expiration_fragment', UNDEFINED)
        has_visited_course = context.get('has_visited_course', UNDEFINED)
        def header_extras():
            return render_header_extras(context._locals(__M_locals))
        outline_fragment = context.get('outline_fragment', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_extras'):
            context['self'].header_extras(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n\n')
        def ccall(caller):
            def body():
                username = context.get('username', UNDEFINED)
                goal_api_url = context.get('goal_api_url', UNDEFINED)
                __M_writer = context.writer()
                __M_writer(u'\n    new CourseHome({\n        courseRunKey: "')
                __M_writer(js_escaped_string(course_key ))
                __M_writer(u'",\n        resumeCourseLink: ".action-resume-course",\n        courseToolLink: ".course-tool-link",\n        goalApiUrl: "')
                __M_writer(js_escaped_string(goal_api_url ))
                __M_writer(u'",\n        username: "')
                __M_writer(js_escaped_string(username ))
                __M_writer(u'",\n        courseId: "')
                __M_writer(js_escaped_string(course.id ))
                __M_writer(u'",\n    });\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'CourseHome'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u"\n    new CourseEnrollment('.enroll-btn', '")
                __M_writer(js_escaped_string(course_key ))
                __M_writer(u"');\n")
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'Enrollment'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        resume_course_url = context.get('resume_course_url', UNDEFINED)
        course_home_message_fragment = context.get('course_home_message_fragment', UNDEFINED)
        upgrade_url = context.get('upgrade_url', UNDEFINED)
        has_goal_permission = context.get('has_goal_permission', UNDEFINED)
        update_message_fragment = context.get('update_message_fragment', UNDEFINED)
        course_tools = context.get('course_tools', UNDEFINED)
        handouts_html = context.get('handouts_html', UNDEFINED)
        course_key = context.get('course_key', UNDEFINED)
        def content():
            return render_content(context)
        course = context.get('course', UNDEFINED)
        goal_options = context.get('goal_options', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        course_sock_fragment = context.get('course_sock_fragment', UNDEFINED)
        current_goal = context.get('current_goal', UNDEFINED)
        dates_fragment = context.get('dates_fragment', UNDEFINED)
        course_expiration_fragment = context.get('course_expiration_fragment', UNDEFINED)
        has_visited_course = context.get('has_visited_course', UNDEFINED)
        upgrade_price = context.get('upgrade_price', UNDEFINED)
        outline_fragment = context.get('outline_fragment', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div class="course-view page-content-container" id="course-container">\n\n')
        if ENABLE_DASHBOARD_TAB.is_enabled(course_key):
            __M_writer(u'        ')
            __M_writer(filters.html_escape(filters.decode.utf8(static.renderReact(
          component="UpsellExperimentModal",
          id="upsell-modal",
          props={},
        ))))
            __M_writer(u'\n')
        __M_writer(u'\n')
        if INCLUDE_PORTFOLIO_UPSELL_MODAL.is_enabled():
            __M_writer(u'        ')
            __M_writer(filters.html_escape(filters.decode.utf8(static.renderReact(
            component="PortfolioExperimentUpsellModal",
            id="portfolio-experiment-upsell-modal",
            props={}
        ))))
            __M_writer(u'\n')
        __M_writer(u'\n    <header class="page-header has-secondary">\n        <div class="page-header-main">\n            <nav aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Course Outline'))))
        __M_writer(u'" class="sr-is-focusable" tabindex="-1">\n                <h2 class="hd hd-3 page-title">')
        __M_writer(filters.html_escape(filters.decode.utf8(course.display_name_with_default)))
        __M_writer(u'</h2>\n            </nav>\n        </div>\n        <div class="page-header-secondary">\n')
        if settings.FEATURES.get('ENABLE_COURSEWARE_SEARCH'):
            __M_writer(u'                <div class="page-header-search">\n                    <form class="search-form input-group" role="search" action="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('openedx.course_search.course_search_results', args=[course_key]))))
            __M_writer(u'">\n                        <label class="field-label sr-only" for="search" id="search-hint">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Search the course'))))
            __M_writer(u'</label>\n                        <input\n                                class="field-input input-text search-input form-control"\n                                type="search"\n                                name="query"\n                                id="search"\n                                placeholder="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Search the course'))))
            __M_writer(u'"\n                        />\n                        <span class="input-group-btn">\n                            <button class="btn btn-outline-primary search-button" type="submit">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Search'))))
            __M_writer(u'</button>\n                        </span>\n                    </form>\n                </div>\n')
        __M_writer(u'            <div class="form-actions">\n')
        if resume_course_url:
            __M_writer(u'                    <a class="btn btn-primary action-resume-course" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(resume_course_url)))
            __M_writer(u'">\n')
            if has_visited_course:
                __M_writer(u'                            <span data-action-type="resume">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Resume Course"))))
                __M_writer(u'</span>\n')
            else:
                __M_writer(u'                            <span data-action-type="start">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Start Course"))))
                __M_writer(u'</span>\n')
            __M_writer(u'                    </a>\n')
        __M_writer(u'            </div>\n        </div>\n    </header>\n    <div class="page-content">\n        <div class="page-content-main">\n')
        if course_expiration_fragment:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(course_expiration_fragment.content))))
            __M_writer(u'\n')
        if course_home_message_fragment:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(course_home_message_fragment.body_html()))))
            __M_writer(u'\n')
        __M_writer(u'\n')
        if update_message_fragment and UNIFIED_COURSE_TAB_FLAG.is_enabled(course.id):
            __M_writer(u'                <div class="section section-update-message">\n                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(update_message_fragment.body_html()))))
            __M_writer(u'\n                </div>\n')
        __M_writer(u'\n')
        if outline_fragment:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(outline_fragment.body_html()))))
            __M_writer(u'\n')
        __M_writer(u'        </div>\n        <aside class="page-content-secondary course-sidebar">\n')
        if has_goal_permission:
            __M_writer(u'                <div class="section section-goals ')
            __M_writer(filters.html_escape(filters.decode.utf8('' if current_goal else 'hidden')))
            __M_writer(u'">\n                    <div class="current-goal-container">\n                        <label class="title title-label hd-6" for="goal">\n                            <h3 class="hd-6">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Goal: "))))
            __M_writer(u'</h3>\n                        </label>\n                        <h3 class="title hd-6">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Goal: "))))
            __M_writer(u'</h3>\n                        <div class="goal">\n                            <span class="text">')
            __M_writer(filters.html_escape(filters.decode.utf8(goal_options[current_goal.goal_key] if current_goal else "")))
            __M_writer(u'</span>\n                        </div>\n                        <select class="edit-goal-select" id="goal">\n')
            for goal, goal_text in goal_options.items():
                __M_writer(u'                                <option value="')
                __M_writer(filters.html_escape(filters.decode.utf8(goal)))
                __M_writer(u'" ')
                __M_writer(filters.html_escape(filters.decode.utf8("selected" if current_goal and current_goal.goal_key == goal else "")))
                __M_writer(u'>')
                __M_writer(filters.html_escape(filters.decode.utf8(goal_text)))
                __M_writer(u'</option>\n')
            __M_writer(u'                        </select>\n                        <span class="sr sr-update-response-msg" aria-live="polite"></span>\n                        <span class="response-icon" aria-hidden="true"></span>\n                        <span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Edit your course goal:"))))
            __M_writer(u'</span>\n                        <button class="edit-icon">\n                            <span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Edit your course goal:"))))
            __M_writer(u'</span>\n                            <span class="fa fa-pencil" aria-hidden="true"></span>\n                        </button>\n                    </div>\n                </div>\n')
        if course_tools:
            __M_writer(u'                <div class="section section-tools">\n                    <h3 class="hd-6 section-title">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Course Tools"))))
            __M_writer(u'</h3>\n                    <ul class="list-unstyled">\n')
            for course_tool in course_tools:
                __M_writer(u'                            <li class="course-tool">\n                                <a class="course-tool-link" data-analytics-id="')
                __M_writer(filters.html_escape(filters.decode.utf8(course_tool.analytics_id())))
                __M_writer(u'" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(course_tool.url(course_key))))
                __M_writer(u'">\n                                    <span class="icon ')
                __M_writer(filters.html_escape(filters.decode.utf8(course_tool.icon_classes())))
                __M_writer(u'" aria-hidden="true"></span>\n                                    ')
                __M_writer(filters.html_escape(filters.decode.utf8(course_tool.title())))
                __M_writer(u'\n                                </a>\n                            </li>\n')
            __M_writer(u'                    </ul>\n                </div>\n')
        if upgrade_url and upgrade_price:
            __M_writer(u'                <div class="section section-upgrade course-home-sidebar-upgrade">\n                    <h3 class="hd hd-6">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Pursue a verified certificate"))))
            __M_writer(u'</h3>\n                        <img src="https://courses.edx.org/static/images/edx-verified-mini-cert.png" alt="">\n                        <div class="upgrade-container">\n                            <p>\n                                <a class="btn-brand btn-upgrade"\n                                   href="')
            __M_writer(filters.html_escape(filters.decode.utf8(upgrade_url)))
            __M_writer(u'"\n                                   data-creative="sidebarupsell"\n                                   data-position="sidebar-message">\n                                   ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Upgrade ({price})").format(price=upgrade_price))))
            __M_writer(u'\n                                </a>\n                            </p>\n                    <p><button class="btn-link btn-small promo-learn-more">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Learn More'))))
            __M_writer(u'</button></p>\n                        </div>\n                </div>\n')
        if dates_fragment:
            __M_writer(u'                <div class="section section-dates">\n                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(dates_fragment.body_html()))))
            __M_writer(u'\n                </div>\n')
        if handouts_html:
            __M_writer(u'                <div class="section section-handouts">\n                    <h3 class="hd-6 section-title">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Course Handouts"))))
            __M_writer(u'</h3>\n                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(handouts_html))))
            __M_writer(u'\n                </div>\n')
        __M_writer(u'        </aside>\n    </div>\n')
        if course_sock_fragment:
            __M_writer(u'        ')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(course_sock_fragment.body_html()))))
            __M_writer(u'\n')
        __M_writer(u'</div>\n')
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
        __M_writer(u'\n  <link rel="stylesheet" type="text/css" href="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('paragon/static/paragon.min.css'))))
        __M_writer(u'" />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 6, "39": 4, "42": 3, "69": 2, "70": 3, "71": 4, "72": 20, "77": 24, "82": 176, "88": 178, "89": 180, "90": 180, "91": 183, "92": 183, "93": 184, "94": 184, "95": 185, "96": 185, "101": 178, "104": 187, "108": 189, "109": 190, "110": 190, "115": 189, "118": 191, "124": 26, "148": 26, "149": 29, "150": 30, "151": 30, "156": 34, "157": 36, "158": 37, "159": 38, "160": 38, "165": 42, "166": 44, "167": 47, "168": 47, "169": 48, "170": 48, "171": 52, "172": 53, "173": 54, "174": 54, "175": 55, "176": 55, "177": 61, "178": 61, "179": 64, "180": 64, "181": 69, "182": 70, "183": 71, "184": 71, "185": 71, "186": 72, "187": 73, "188": 73, "189": 73, "190": 74, "191": 75, "192": 75, "193": 75, "194": 77, "195": 79, "196": 84, "197": 85, "198": 85, "199": 85, "200": 87, "201": 88, "202": 88, "203": 88, "204": 90, "205": 91, "206": 92, "207": 93, "208": 93, "209": 96, "210": 97, "211": 98, "212": 98, "213": 98, "214": 100, "215": 102, "216": 103, "217": 103, "218": 103, "219": 106, "220": 106, "221": 108, "222": 108, "223": 110, "224": 110, "225": 113, "226": 114, "227": 114, "228": 114, "229": 114, "230": 114, "231": 114, "232": 114, "233": 116, "234": 119, "235": 119, "236": 121, "237": 121, "238": 127, "239": 128, "240": 129, "241": 129, "242": 131, "243": 132, "244": 133, "245": 133, "246": 133, "247": 133, "248": 134, "249": 134, "250": 135, "251": 135, "252": 139, "253": 142, "254": 143, "255": 144, "256": 144, "257": 149, "258": 149, "259": 152, "260": 152, "261": 155, "262": 155, "263": 159, "264": 160, "265": 161, "266": 161, "267": 164, "268": 165, "269": 166, "270": 166, "271": 167, "272": 167, "273": 170, "274": 172, "275": 173, "276": 173, "277": 173, "278": 175, "284": 22, "291": 22, "292": 23, "293": 23, "299": 293}, "uri": "course_experience/course-home-fragment.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/openedx/features/course_experience/templates/course_experience/course-home-fragment.html"}
__M_END_METADATA
"""
