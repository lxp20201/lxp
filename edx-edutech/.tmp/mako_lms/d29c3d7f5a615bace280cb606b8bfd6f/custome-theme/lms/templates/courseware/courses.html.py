# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284720.111402
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/courseware/courses.html'
_template_uri = 'custome-theme/lms/templates/courseware/courses.html'
_source_encoding = 'utf-8'
_exports = [u'pagetitle', u'header_extras']



import json
from django.utils.translation import ugettext as _
from openedx.core.djangolib.js_utils import dump_js_escaped_json


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
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
        courses = context.get('courses', UNDEFINED)
        def header_extras():
            return render_header_extras(context._locals(__M_locals))
        static = _mako_get_namespace(context, 'static')
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')

        course_discovery_enabled = settings.FEATURES.get('ENABLE_COURSE_DISCOVERY')
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['course_discovery_enabled'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        if course_discovery_enabled:
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_extras'):
                context['self'].header_extras(**pageargs)
            

            __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer(u'\n\n<main id="main" aria-label="Content" tabindex="-1">\n    <section class="find-courses">\n      <section class="courses-container holder">\n')
        if course_discovery_enabled:
            __M_writer(u'        <div id="discovery-form" role="search" aria-label="course" class="wrapper-search-context">\n          <div id="discovery-message" class="search-status-label"></div>\n          <form class="wrapper-search-input">\n            <label for="discovery-input" class="sr">')
            __M_writer(filters.decode.utf8(_("Search for a course")))
            __M_writer(u'</label>\n            <input id="discovery-input" class="discovery-input" placeholder="')
            __M_writer(filters.decode.utf8(_('Search for a course')))
            __M_writer(u'" type="text"/>\n            <button type="submit" class="button postfix discovery-submit" title="')
            __M_writer(filters.decode.utf8(_('Search')))
            __M_writer(u'">\n              <span class="icon fa fa-search" aria-hidden="true"></span>\n              <div aria-live="polite" aria-relevant="all">\n                <div id="loading-indicator" class="loading-spinner hidden">\n                  <span class="icon fa fa-spinner fa-spin" aria-hidden="true"></span>\n                  <span class="sr">')
            __M_writer(filters.decode.utf8(_("Loading")))
            __M_writer(u'</span>\n                </div>\n              </div>\n            </button>\n          </form>\n        </div>\n\n        <div id="filter-bar" class="filters hide-phone is-collapsed">\n        </div>\n')
        __M_writer(u'\n        <div class="courses')
        __M_writer(filters.decode.utf8('' if course_discovery_enabled else ' no-course-discovery'))
        __M_writer(u'" role="region" aria-label="')
        __M_writer(filters.decode.utf8(_('List of Courses')))
        __M_writer(u'">\n          <ul class="courses-listing">\n')
        for course in courses:
            __M_writer(u'            <li class="courses-listing-item">\n              ')
            runtime._include_file(context, u'../course.html', _template_uri, course=course)
            __M_writer(u'\n            </li>\n')
        __M_writer(u'          </ul>\n        </div>\n\n\n')
        if course_discovery_enabled:
            __M_writer(u'        <aside aria-label="')
            __M_writer(filters.decode.utf8(_('Refine Your Search')))
            __M_writer(u'" class="search-facets phone-menu">\n          <h2 class="header-search-facets">')
            __M_writer(filters.decode.utf8(_("Refine Your Search")))
            __M_writer(u'</h2>\n          <section class="search-facets-lists">\n          </section>\n        </aside>\n')
        __M_writer(u'\n      </section>\n    </section>\n</main>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagetitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pagetitle():
            return render_pagetitle(context)
        __M_writer = context.writer()
        __M_writer(filters.decode.utf8(_("Courses")))
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
        for template_name in ["course_card", "filter_bar", "filter", "facet", "facet_option"]:
            __M_writer(u'  <script type="text/template" id="')
            __M_writer(filters.decode.utf8(template_name))
            __M_writer(u'-tpl">\n      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.decode.utf8(static.include(path=u'discovery/' + (template_name) + u'.underscore')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n  </script>\n')
        __M_writer(u'  ')
        def ccall(caller):
            def body():
                user_timezone = context.get('user_timezone', UNDEFINED)
                course_discovery_meanings = context.get('course_discovery_meanings', UNDEFINED)
                user_language = context.get('user_language', UNDEFINED)
                __M_writer = context.writer()
                __M_writer(u'\n    DiscoveryFactory(\n      ')
                __M_writer(dump_js_escaped_json(course_discovery_meanings ))
                __M_writer(u',\n      getParameterByName(\'search_query\'),\n      "')
                __M_writer(filters.decode.utf8(user_language))
                __M_writer(u'",\n      "')
                __M_writer(filters.decode.utf8(user_timezone))
                __M_writer(u'"\n    );\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.decode.utf8(static.require_module(class_name=u'DiscoveryFactory',module_name=u'js/discovery/discovery_factory')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"132": 17, "135": 17, "136": 20, "143": 20, "16": 1, "145": 22, "146": 24, "147": 24, "148": 25, "149": 25, "154": 20, "29": 11, "35": 0, "163": 157, "47": 5, "48": 6, "49": 7, "55": 9, "56": 11, "57": 13, "62": 28, "63": 30, "68": 31, "69": 36, "70": 37, "71": 40, "72": 40, "73": 41, "74": 41, "75": 42, "76": 42, "77": 47, "78": 47, "79": 57, "80": 58, "81": 58, "82": 58, "83": 58, "84": 60, "85": 61, "86": 62, "87": 62, "88": 65, "89": 69, "90": 70, "91": 70, "92": 70, "93": 71, "94": 71, "95": 76, "144": 22, "101": 31, "107": 31, "157": 27, "113": 14, "120": 14, "121": 15, "122": 16, "123": 16, "124": 16}, "uri": "custome-theme/lms/templates/courseware/courses.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/courseware/courses.html"}
__M_END_METADATA
"""
