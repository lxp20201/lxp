# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580296540.474941
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/djangoapps/discussion/templates/discussion/discussion_board_js.template'
_template_uri = 'discussion/discussion_board_js.template'
_source_encoding = 'utf-8'
_exports = []



from openedx.core.djangolib.js_utils import dump_js_escaped_json, js_escaped_string


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        root_url = context.get('root_url', UNDEFINED)
        annotated_content_info = context.get('annotated_content_info', UNDEFINED)
        course_settings = context.get('course_settings', UNDEFINED)
        roles = context.get('roles', UNDEFINED)
        thread_pages = context.get('thread_pages', UNDEFINED)
        is_commentable_divided = context.get('is_commentable_divided', UNDEFINED)
        sort_preference = context.get('sort_preference', UNDEFINED)
        user_info = context.get('user_info', UNDEFINED)
        threads = context.get('threads', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        discussion_default_topic_id = context.get('discussion_default_topic_id', UNDEFINED)
        course = context.get('course', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u"\n\n(function (require, define) {\n    var registerDiscussionClass = function(moduleName, modulePath) {\n        define(\n            modulePath,\n            [],\n            function() {\n                var discussionClass = window[moduleName];\n                if (!discussionClass) {\n                  throw new Error('Discussion class not loaded: ' + moduleName);\n                }\n                return discussionClass;\n            }\n        );\n    }\n\n")
        __M_writer(u'    ')

        discussion_classes = [
            ['Discussion', 'common/js/discussion/discussion'],
            ['Content', 'common/js/discussion/content'],
            ['DiscussionModuleView', 'common/js/discussion/discussion_module_view'],
            ['DiscussionThreadView', 'common/js/discussion/views/discussion_thread_view'],
            ['DiscussionThreadListView', 'common/js/discussion/views/discussion_thread_list_view'],
            ['DiscussionThreadProfileView', 'common/js/discussion/views/discussion_thread_profile_view'],
            ['DiscussionUtil', 'common/js/discussion/utils'],
            ['DiscussionCourseSettings', 'common/js/discussion/models/discussion_course_settings'],
            ['DiscussionUser', 'common/js/discussion/models/discussion_user'],
            ['NewPostView', 'common/js/discussion/views/new_post_view'],
        ]
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['discussion_classes'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        for discussion_class_info in discussion_classes:
            __M_writer(u"        registerDiscussionClass(\n            '")
            __M_writer(js_escaped_string(discussion_class_info[0] ))
            __M_writer(u"',\n            '")
            __M_writer(js_escaped_string(discussion_class_info[1] ))
            __M_writer(u"'\n        );\n")
        __M_writer(u'\n')
        __M_writer(u"    $(function() {\n        require(['discussion/js/discussion_board_factory'], function (DiscussionBoardFactory) {\n            DiscussionBoardFactory({\n                courseId: '")
        __M_writer(js_escaped_string(unicode(course.id) ))
        __M_writer(u'\',\n                $el: $(".discussion-board"),\n                rootUrl: \'')
        __M_writer(js_escaped_string(root_url ))
        __M_writer(u"',\n                userInfo: ")
        __M_writer(dump_js_escaped_json(user_info ))
        __M_writer(u',\n                roles: ')
        __M_writer(dump_js_escaped_json(roles ))
        __M_writer(u",\n                sortPreference: '")
        __M_writer(js_escaped_string(sort_preference ))
        __M_writer(u"',\n                threads: ")
        __M_writer(dump_js_escaped_json(threads ))
        __M_writer(u",\n                threadPages: '")
        __M_writer(js_escaped_string(thread_pages ))
        __M_writer(u"',\n                contentInfo: ")
        __M_writer(dump_js_escaped_json(annotated_content_info ))
        __M_writer(u",\n                courseName: '")
        __M_writer(js_escaped_string(course.display_name_with_default ))
        __M_writer(u"',\n                courseSettings: ")
        __M_writer(dump_js_escaped_json(course_settings ))
        __M_writer(u',\n                isCommentableDivided: ')
        __M_writer(dump_js_escaped_json(is_commentable_divided ))
        __M_writer(u",\n                defaultTopicId: '")
        __M_writer(js_escaped_string(discussion_default_topic_id ))
        __M_writer(u"'\n            });\n        });\n    });\n}).call(this, require || RequireJS.require, define || RequireJS.define);\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "20": 0, "37": 2, "38": 5, "39": 23, "40": 23, "57": 36, "58": 38, "59": 39, "60": 40, "61": 40, "62": 41, "63": 41, "64": 44, "65": 46, "66": 49, "67": 49, "68": 51, "69": 51, "70": 52, "71": 52, "72": 53, "73": 53, "74": 54, "75": 54, "76": 55, "77": 55, "78": 56, "79": 56, "80": 57, "81": 57, "82": 58, "83": 58, "84": 59, "85": 59, "86": 60, "87": 60, "88": 61, "89": 61, "95": 89}, "uri": "discussion/discussion_board_js.template", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/djangoapps/discussion/templates/discussion/discussion_board_js.template"}
__M_END_METADATA
"""
