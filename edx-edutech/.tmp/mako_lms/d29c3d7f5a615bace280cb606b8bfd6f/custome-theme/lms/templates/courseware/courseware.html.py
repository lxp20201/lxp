# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284777.14387
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/courseware/courseware.html'
_template_uri = 'custome-theme/lms/templates/courseware/courseware.html'
_source_encoding = 'utf-8'
_exports = ['course_name', u'bodyclass', u'title', 'online_help_token', u'js_extra', u'headextra', u'header_extras']



import waffle

from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext as _

from edxnotes.helpers import is_feature_enabled as is_edxnotes_enabled
from openedx.core.djangolib.js_utils import js_escaped_string
from openedx.core.djangolib.markup import HTML
from openedx.features.course_experience import course_home_page_title, COURSE_OUTLINE_PAGE_FLAG


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
    return runtime._inherit_from(context, u'/main.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        disable_accordion = context.get('disable_accordion', UNDEFINED)
        int = context.get('int', UNDEFINED)
        course = context.get('course', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        unicode = context.get('unicode', UNDEFINED)
        default_tab = context.get('default_tab', UNDEFINED)
        def course_name():
            return render_course_name(context._locals(__M_locals))
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        section = context.get('section', UNDEFINED)
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        getattr = context.get('getattr', UNDEFINED)
        language_preference = context.get('language_preference', UNDEFINED)
        entrance_exam_passed = context.get('entrance_exam_passed', UNDEFINED)
        fragment = context.get('fragment', UNDEFINED)
        sequence_title = context.get('sequence_title', UNDEFINED)
        staff_access = context.get('staff_access', UNDEFINED)
        chapter = context.get('chapter', UNDEFINED)
        section_title = context.get('section_title', UNDEFINED)
        accordion = context.get('accordion', UNDEFINED)
        request = context.get('request', UNDEFINED)
        course_url = context.get('course_url', UNDEFINED)
        entrance_exam_current_score = context.get('entrance_exam_current_score', UNDEFINED)
        course_sock_fragment = context.get('course_sock_fragment', UNDEFINED)
        def headextra():
            return render_headextra(context._locals(__M_locals))
        def header_extras():
            return render_header_extras(context._locals(__M_locals))
        round = context.get('round', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        include_special_exams = settings.FEATURES.get('ENABLE_SPECIAL_EXAMS', False) and (course.enable_proctored_exams or course.enable_timed_exams)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['include_special_exams'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_extras'):
            context['self'].header_extras(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headextra'):
            context['self'].headextra(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n\n<div class="message-banner" aria-live="polite"></div>\n\n')
        if default_tab:
            runtime._include_file(context, u'/courseware/course_navigation.html', _template_uri)
            __M_writer(u'\n')
        else:
            runtime._include_file(context, u'/courseware/course_navigation.html', _template_uri, active_page='courseware')
            __M_writer(u'\n')
        __M_writer(u'\n<div class="container"\n')
        if getattr(course, 'language'):
            __M_writer(u'lang="')
            __M_writer(filters.html_escape(filters.decode.utf8(course.language)))
            __M_writer(u'"\n')
        __M_writer(u'>\n<div class="course-wrapper" role="presentation">\n\n')
        if disable_accordion is UNDEFINED or not disable_accordion:
            __M_writer(u'    <div class="course-index">\n\n        <div class="wrapper-course-modes">\n\n            <div class="courseware-bookmarks-button">\n                <a class="bookmarks-list-button" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('openedx.course_bookmarks.home', args=[course.id]))))
            __M_writer(u'">\n                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Bookmarks"))))
            __M_writer(u'\n                </a>\n            </div>\n\n')
            if settings.FEATURES.get('ENABLE_COURSEWARE_SEARCH'):
                __M_writer(u'            <div id="courseware-search-bar" class="search-bar courseware-search-bar" role="search" aria-label="Course">\n                <form class="search-form">\n                    <label for="course-search-input" class="sr">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Course Search"))))
                __M_writer(u'</label>\n                    <div class="search-field-wrapper">\n                        <input id="course-search-input" type="text" class="search-field"/>\n                        <button type="submit" class="search-button">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Search"))))
                __M_writer(u'</button>\n                        <button type="button" class="cancel-button" title="')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Clear search'))))
                __M_writer(u'">\n                            <span class="icon fa fa-remove" aria-hidden="true"></span>\n                        </button>\n                    </div>\n                </form>\n            </div>\n')
            __M_writer(u'\n        </div>\n\n        <div class="accordion">\n            <nav class="course-navigation" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Course'))))
            __M_writer(u'">\n')
            if accordion.strip():
                __M_writer(u'                ')
                __M_writer(filters.html_escape(filters.decode.utf8(HTML(accordion))))
                __M_writer(u'\n')
            else:
                __M_writer(u'                <div class="chapter">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("No content has been added to this course"))))
                __M_writer(u'</div>\n')
            __M_writer(u'            </nav>\n        </div>\n\n    </div>\n')
        __M_writer(u'    <section class="course-content" id="course-content">\n        <header class="page-header has-secondary">\n            <div class="page-header-main">\n                <nav aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Course'))))
        __M_writer(u'" class="sr-is-focusable" tabindex="-1">\n                    <div class="has-breadcrumbs">\n                        <div class="breadcrumbs">\n')
        if COURSE_OUTLINE_PAGE_FLAG.is_enabled(course.id):
            __M_writer(u'                            <span class="nav-item nav-item-course">\n                                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(course_home_page_title(course))))
            __M_writer(u'</a>\n                                </span>\n                            <span class="icon fa fa-angle-right" aria-hidden="true"></span>\n')
        if chapter:
            __M_writer(u'                            <span class="nav-item nav-item-chapter" data-course-position="')
            __M_writer(filters.html_escape(filters.decode.utf8(course.position)))
            __M_writer(u'" data-chapter-position="')
            __M_writer(filters.html_escape(filters.decode.utf8(chapter.position)))
            __M_writer(u'">\n                                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_url)))
            __M_writer(u'#')
            __M_writer(filters.html_escape(filters.decode.utf8(unicode(chapter.location))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(chapter.display_name_with_default)))
            __M_writer(u'</a>\n                                </span>\n                            <span class="icon fa fa-angle-right" aria-hidden="true"></span>\n')
        if section:
            __M_writer(u'                            <span class="nav-item nav-item-section">\n                                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_url)))
            __M_writer(u'#')
            __M_writer(filters.html_escape(filters.decode.utf8(unicode(section.location))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(section.display_name_with_default)))
            __M_writer(u'</a>\n                                </span>\n                            <span class="icon fa fa-angle-right" aria-hidden="true"></span>\n')
        __M_writer(u'                            <span class="nav-item nav-item-sequence">')
        __M_writer(filters.html_escape(filters.decode.utf8(sequence_title)))
        __M_writer(u'</span>\n                        </div>\n                        <i class="fullscreen-button fs-expand" aria-hidden="true" id="fullscreen">\n                            <svg>\n                                <use xlink:href="#ico-fs-expand"></use>\n                            </svg>\n                        </i>\n                    </div>\n                </nav>\n            </div>\n        </header>\n\n        <main id="main" tabindex="-1" aria-label="Content">\n')
        if getattr(course, 'entrance_exam_enabled') and \
            getattr(course, 'entrance_exam_minimum_score_pct') and \
            entrance_exam_current_score is not UNDEFINED:
            if not entrance_exam_passed:
                __M_writer(u'            <p class="sequential-status-message">\n                ')
                __M_writer(filters.html_escape(filters.decode.utf8(_('To access course materials, you must score {required_score}% or higher on this \
                exam. Your current score is {current_score}%.').format(
                required_score=int(round(course.entrance_exam_minimum_score_pct * 100)),
                current_score=int(round(entrance_exam_current_score * 100))
                ))))
                __M_writer(u'\n            </p>\n            <script type="text/javascript">\n                $(document).ajaxSuccess(function(event, xhr, settings) {\n                    if (settings.url.indexOf("xmodule_handler/problem_check") > -1) {\n                        var data = JSON.parse(xhr.responseText);\n                        if (data.entrance_exam_passed){\n                            location.reload();\n                        }\n                    }\n                });\n            </script>\n')
            else:
                __M_writer(u'            <p class="sequential-status-message">\n                ')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Your score is {current_score}%. You have passed the entrance exam.').format(
                current_score=int(round(entrance_exam_current_score * 100))
                ))))
                __M_writer(u'\n            </p>\n')
        __M_writer(u'\n            ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(fragment.body_html()))))
        __M_writer(u'\n        </main>\n    </section>\n\n    <section class="courseware-results-wrapper">\n        <div id="loading-message" aria-live="polite" aria-relevant="all"></div>\n        <div id="error-message" aria-live="polite"></div>\n        <div class="courseware-results search-results" data-course-id="')
        __M_writer(filters.html_escape(filters.decode.utf8(course.id)))
        __M_writer(u'" data-lang-code="')
        __M_writer(filters.html_escape(filters.decode.utf8(language_preference)))
        __M_writer(u'"></div>\n    </section>\n\n</div>\n')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(course_sock_fragment.body_html()))))
        __M_writer(u'\n</div>\n<div class="container-footer">\n')
        if settings.FEATURES.get("LICENSING", False):
            __M_writer(u'    <div class="course-license">\n')
            if getattr(course, "license", None):
                __M_writer(u'        ')
                runtime._include_file(context, u'../license.html', _template_uri, license=course.license)
                __M_writer(u'\n')
            else:
                __M_writer(u'        ')
                runtime._include_file(context, u'../license.html', _template_uri, license='all-rights-reserved')
                __M_writer(u'\n')
            __M_writer(u'    </div>\n')
        __M_writer(u'</div>\n')
        if course.show_calculator or is_edxnotes_enabled(course, request.user):
            __M_writer(u'<nav class="nav-utilities ')
            __M_writer(filters.html_escape(filters.decode.utf8("has-utility-calculator" if course.show_calculator else "")))
            __M_writer(u'" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Course Utilities'))))
            __M_writer(u'">\n')
            if is_edxnotes_enabled(course, request.user):
                runtime._include_file(context, u'/edxnotes/toggle_notes.html', _template_uri, course=course)
                __M_writer(u'\n')
            __M_writer(u'\n')
            if course.show_calculator:
                runtime._include_file(context, u'/calculator/toggle_calculator.html', _template_uri)
                __M_writer(u'\n')
            __M_writer(u'</nav>\n')
        __M_writer(u'\n<script src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/fullscreenButton.js'))))
        __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_course_name(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        course = context.get('course', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        return _("{course_number} Courseware").format(course_number=course.display_number_with_default) 
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        course = context.get('course', UNDEFINED)
        def bodyclass():
            return render_bodyclass(context)
        __M_writer = context.writer()
        __M_writer(u'view-in-course view-courseware courseware ')
        __M_writer(filters.html_escape(filters.decode.utf8(course.css_class or '')))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        static = _mako_get_namespace(context, 'static')
        section_title = context.get('section_title', UNDEFINED)
        def course_name():
            return render_course_name(context)
        sequence_title = context.get('sequence_title', UNDEFINED)
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer(u'\n<title data-base-title="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.get_page_title_breadcrumbs(section_title, course_name()))))
        __M_writer(u'">\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(static.get_page_title_breadcrumbs(sequence_title, section_title, course_name()))))
        __M_writer(u'\n</title>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "courseware" 
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        fragment = context.get('fragment', UNDEFINED)
        request = context.get('request', UNDEFINED)
        course = context.get('course', UNDEFINED)
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        staff_access = context.get('staff_access', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('common/js/vendor/jquery.scrollTo.js'))))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/flot/jquery.flot.js'))))
        __M_writer(u'"></script>\n\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.js(group=u'courseware'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        runtime._include_file(context, u'/mathjax_include.html', _template_uri, disable_fast_preview=True)
        __M_writer(u'\n\n')
        if settings.FEATURES.get('ENABLE_COURSEWARE_SEARCH'):
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    __M_writer(u"\nvar courseId = $('.courseware-results').data('courseId');\nCourseSearchFactory({\ncourseId: courseId,\nsearchHeader: $('.search-bar')\n});\n")
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'CourseSearchFactory',module_name=u'course_search/js/course_search_factory'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\nCoursewareFactory();\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'CoursewareFactory',module_name=u'js/courseware/courseware_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n')
        if staff_access:
            runtime._include_file(context, u'xqa_interface.html', _template_uri)
            __M_writer(u'\n')
        __M_writer(u'\n<script type="text/javascript">\n    var $$course_id = "')
        __M_writer(js_escaped_string(course.id ))
        __M_writer(u'";\n</script>\n\n')
        if not request.user.is_authenticated:
            __M_writer(u'<script type="text/javascript">\n    // Disable discussions\n    $(\'.xblock-student_view-discussion button.discussion-show\').attr(\'disabled\', true);\n\n    // Insert message informing user discussions are only available to logged in users.\n    $(\'.discussion-module\')\n</script>\n')
        __M_writer(u'\n')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(fragment.foot_html()))))
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headextra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        fragment = context.get('fragment', UNDEFINED)
        def headextra():
            return render_headextra(context)
        static = _mako_get_namespace(context, 'static')
        request = context.get('request', UNDEFINED)
        course = context.get('course', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-course-vendor'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-course'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        if is_edxnotes_enabled(course, request.user):
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-student-notes'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        __M_writer(u'\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/jquery.autocomplete.js'))))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/src/tooltip_manager.js'))))
        __M_writer(u'"></script>\n\n<link href="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('css/vendor/jquery.autocomplete.css'))))
        __M_writer(u'" rel="stylesheet" type="text/css">\n')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(fragment.head_html()))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_extras(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        include_special_exams = context.get('include_special_exams', UNDEFINED)
        def header_extras():
            return render_header_extras(context)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        for template_name in ["image-modal"]:
            __M_writer(u'<script type="text/template" id="')
            __M_writer(filters.html_escape(filters.decode.utf8(template_name)))
            __M_writer(u'-tpl">\n    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.include(path=u'common/templates/' + (template_name) + u'.underscore'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n</script>\n')
        __M_writer(u'\n')
        if include_special_exams is not UNDEFINED and include_special_exams:
            for template_name in ["proctored-exam-status"]:
                __M_writer(u'<script type="text/template" id="')
                __M_writer(filters.html_escape(filters.decode.utf8(template_name)))
                __M_writer(u'-tpl">\n    ')
                def ccall(caller):
                    def body():
                        __M_writer = context.writer()
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    __M_writer(filters.html_escape(filters.decode.utf8(static.include(path=u'courseware/' + (template_name) + u'.underscore'))))
                finally:
                    context.caller_stack.nextcaller = None
                __M_writer(u'\n</script>\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 5, "36": 3, "42": 1, "80": 1, "81": 2, "82": 3, "83": 4, "84": 16, "85": 17, "91": 19, "92": 22, "97": 24, "102": 30, "107": 48, "112": 63, "117": 106, "118": 110, "119": 111, "120": 111, "121": 112, "122": 113, "123": 113, "124": 115, "125": 117, "126": 118, "127": 118, "128": 118, "129": 120, "130": 123, "131": 124, "132": 129, "133": 129, "134": 130, "135": 130, "136": 134, "137": 135, "138": 137, "139": 137, "140": 140, "141": 140, "142": 141, "143": 141, "144": 148, "145": 152, "146": 152, "147": 153, "148": 154, "149": 154, "150": 154, "151": 155, "152": 156, "153": 156, "154": 156, "155": 158, "156": 163, "157": 166, "158": 166, "159": 169, "160": 170, "161": 171, "162": 171, "163": 171, "164": 171, "165": 175, "166": 176, "167": 176, "168": 176, "169": 176, "170": 176, "171": 177, "172": 177, "173": 177, "174": 177, "175": 177, "176": 177, "177": 181, "178": 182, "179": 183, "180": 183, "181": 183, "182": 183, "183": 183, "184": 183, "185": 187, "186": 187, "187": 187, "188": 200, "191": 203, "192": 204, "193": 205, "198": 209, "199": 221, "200": 222, "201": 223, "204": 225, "205": 229, "206": 230, "207": 230, "208": 237, "209": 237, "210": 237, "211": 237, "212": 241, "213": 241, "214": 244, "215": 245, "216": 246, "217": 247, "218": 247, "219": 247, "220": 248, "221": 250, "222": 250, "223": 250, "224": 252, "225": 254, "226": 255, "227": 256, "228": 256, "229": 256, "230": 256, "231": 256, "232": 258, "233": 259, "234": 259, "235": 261, "236": 263, "237": 264, "238": 264, "239": 266, "240": 268, "241": 269, "242": 269, "248": 20, "253": 20, "254": 21, "256": 21, "262": 24, "269": 24, "270": 24, "276": 26, "287": 26, "288": 27, "289": 27, "290": 28, "291": 28, "297": 4, "301": 4, "308": 65, "319": 65, "320": 66, "321": 66, "322": 67, "323": 67, "331": 69, "334": 69, "335": 70, "336": 70, "337": 72, "341": 73, "346": 73, "349": 79, "350": 81, "354": 82, "359": 82, "362": 84, "363": 86, "364": 87, "365": 87, "366": 89, "367": 91, "368": 91, "369": 94, "370": 95, "371": 103, "372": 104, "373": 104, "379": 50, "389": 50, "397": 51, "400": 51, "408": 52, "411": 52, "412": 54, "420": 55, "423": 55, "424": 57, "425": 58, "426": 58, "427": 59, "428": 59, "429": 61, "430": 61, "431": 62, "432": 62, "438": 32, "446": 32, "447": 34, "448": 35, "449": 35, "450": 35, "458": 36, "461": 36, "462": 39, "463": 40, "464": 41, "465": 42, "466": 42, "467": 42, "475": 43, "478": 43, "479": 47, "485": 479}, "uri": "custome-theme/lms/templates/courseware/courseware.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/courseware/courseware.html"}
__M_END_METADATA
"""
