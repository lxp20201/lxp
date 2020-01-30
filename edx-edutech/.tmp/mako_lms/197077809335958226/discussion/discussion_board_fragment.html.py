# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580296540.382679
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/djangoapps/discussion/templates/discussion/discussion_board_fragment.html'
_template_uri = 'discussion/discussion_board_fragment.html'
_source_encoding = 'utf-8'
_exports = []



import json
from django.utils.translation import ugettext as _
from django.template.defaultfilters import escapejs
from django.urls import reverse

from django_comment_client.permissions import has_permission
from openedx.core.djangolib.js_utils import dump_js_escaped_json, js_escaped_string
from openedx.core.djangolib.markup import HTML


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
        can_create_subcomment = context.get('can_create_subcomment', UNDEFINED)
        sort_preference = context.get('sort_preference', UNDEFINED)
        course = context.get('course', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        can_create_comment = context.get('can_create_comment', UNDEFINED)
        flag_moderator = context.get('flag_moderator', UNDEFINED)
        user_group_id = context.get('user_group_id', UNDEFINED)
        course_expiration_fragment = context.get('course_expiration_fragment', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<section class="discussion discussion-board page-content-container" id="discussion-container"\n         data-course-id="')
        __M_writer(filters.html_escape(filters.decode.utf8(course.id)))
        __M_writer(u'"\n         data-user-create-comment="')
        __M_writer(filters.html_escape(filters.decode.utf8(json.dumps(can_create_comment))))
        __M_writer(u'"\n         data-user-create-subcomment="')
        __M_writer(filters.html_escape(filters.decode.utf8(json.dumps(can_create_subcomment))))
        __M_writer(u'"\n         data-read-only="false"\n         data-sort-preference="')
        __M_writer(filters.html_escape(filters.decode.utf8(sort_preference)))
        __M_writer(u'"\n         data-flag-moderator="')
        __M_writer(filters.html_escape(filters.decode.utf8(json.dumps(flag_moderator))))
        __M_writer(u'"\n         data-user-group-id="')
        __M_writer(filters.html_escape(filters.decode.utf8(user_group_id)))
        __M_writer(u'">\n    <header class="page-header has-secondary">\n')
        __M_writer(u'        <div class="page-header-main">\n            <nav aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Discussions'))))
        __M_writer(u'" class="sr-is-focusable" tabindex="-1">\n                <div class="has-breadcrumbs"></div>\n            </nav>\n        </div>\n        <div class="page-header-secondary">\n')
        if has_permission(user, 'create_thread', course.id):
            __M_writer(u'            <div class="forum-actions">\n                <button class="btn btn-outline-primary btn-small new-post-btn">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Add a Post"))))
            __M_writer(u'</button>\n            </div>\n')
        __M_writer(u'            <div class="forum-search"></div>\n        </div>\n    </header>\n')
        if course_expiration_fragment:
            __M_writer(u'        ')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(course_expiration_fragment.content))))
            __M_writer(u'\n')
        __M_writer(u'    <div class="page-content"\n')
        if getattr(course, 'language'):
            __M_writer(u'        lang="')
            __M_writer(filters.html_escape(filters.decode.utf8(course.language)))
            __M_writer(u'"\n')
        __M_writer(u'    >\n        <div class="discussion-body">\n            <main id="main" class="discussion-column" aria-label="Content" tabindex="-1">\n                <article class="new-post-article is-hidden" style="display: none" tabindex="-1" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("New topic form"))))
        __M_writer(u'"></article>\n                <div class="forum-content"></div>\n            </main>\n            <aside class="forum-nav" role="complementary" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Discussion thread list"))))
        __M_writer(u'">\n                ')
        runtime._include_file(context, u'_filter_dropdown.html', _template_uri)
        __M_writer(u'\n                <div class="discussion-thread-list-container"></div>\n            </aside>\n        </div>\n    </div>\n</section>\n\n')
        runtime._include_file(context, u'_underscore_templates.html', _template_uri)
        __M_writer(u'\n')
        runtime._include_file(context, u'_thread_list_template.html', _template_uri)
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 7, "34": 3, "37": 5, "51": 2, "52": 3, "53": 5, "54": 16, "55": 19, "56": 19, "57": 20, "58": 20, "59": 21, "60": 21, "61": 23, "62": 23, "63": 24, "64": 24, "65": 25, "66": 25, "67": 28, "68": 29, "69": 29, "70": 35, "71": 36, "72": 37, "73": 37, "74": 41, "75": 44, "76": 45, "77": 45, "78": 45, "79": 47, "80": 48, "81": 49, "82": 49, "83": 49, "84": 51, "85": 54, "86": 54, "87": 57, "88": 57, "89": 58, "90": 58, "91": 65, "92": 65, "93": 66, "94": 66, "100": 94}, "uri": "discussion/discussion_board_fragment.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/djangoapps/discussion/templates/discussion/discussion_board_fragment.html"}
__M_END_METADATA
"""
