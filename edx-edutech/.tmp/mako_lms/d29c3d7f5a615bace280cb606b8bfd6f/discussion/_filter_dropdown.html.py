# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580296540.401329
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/discussion/_filter_dropdown.html'
_template_uri = u'discussion/_filter_dropdown.html'
_source_encoding = 'utf-8'
_exports = ['render_category', 'render_entry', 'render_dropdown']



from django.utils.translation import ugettext as _
from lms.djangoapps.django_comment_client.constants import TYPE_ENTRY
from openedx.core.djangolib.markup import HTML


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def render_dropdown(map,topic_list):
            return render_render_dropdown(context._locals(__M_locals),map,topic_list)
        category_map = context.get('category_map', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<div class="forum-nav-browse-menu-wrapper" style="display: none" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Discussion topics list"))))
        __M_writer(u'">\n    <form class="forum-nav-browse-filter" autocomplete="off">\n        <label for="forum-nav-browse-filter-input" aria-label=\'')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Filter Topics"))))
        __M_writer(u'\' class="field-label">\n            <span class="field-label-text">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Filter Topics"))))
        __M_writer(u'</span>\n            <input type="text" id="forum-nav-browse-filter-input" role="combobox" aria-expanded="true" aria-owns="discussion_topics_listbox" aria-autocomplete="list" class="forum-nav-browse-filter-input" placeholder="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("filter topics"))))
        __M_writer(u'">\n            <span class="icon fa fa-filter" aria-hidden="true"></span>\n        </label>\n    </form>\n    <ul class="forum-nav-browse-menu" role="listbox" id="discussion_topics_listbox">\n        <li class="forum-nav-browse-menu-item forum-nav-browse-menu-all" role="option" id="all_discussions">\n            <span class="forum-nav-browse-title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("All Discussions"))))
        __M_writer(u'</span>\n        </li>\n        <li class="forum-nav-browse-menu-item forum-nav-browse-menu-following" role="option" id="posts_following">\n            <span class="icon fa fa-star" aria-hidden="true"></span>\n            <span class="forum-nav-browse-title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Posts I'm Following"))))
        __M_writer(u'</span>\n        </li>\n        ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(render_dropdown(category_map, [])))))
        __M_writer(u'\n    </ul>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_category(context,categories,category,topic_list):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_dropdown(map,topic_list):
            return render_render_dropdown(context,map,topic_list)
        __M_writer = context.writer()
        __M_writer(u'\n    <li class="forum-nav-browse-menu-item"\n        id=\'')
        __M_writer(filters.decode.utf8(category ))
        __M_writer(u'\'\n        role="option"\n    >\n        <span class="forum-nav-browse-title">')
        __M_writer(filters.html_escape(filters.decode.utf8(category)))
        __M_writer(u'</span>\n        <ul class="forum-nav-browse-submenu" role="presentation">\n            ')
        topic_list.append(category) 
        
        __M_writer(u'\n            ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(render_dropdown(categories[category], topic_list)))))
        __M_writer(u'\n            ')
        topic_list.remove(category) 
        
        __M_writer(u'\n        </ul>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_entry(context,entries,entry,topic_list):
    __M_caller = context.caller_stack._push_frame()
    try:
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <li\n        class="forum-nav-browse-menu-item"\n        data-discussion-id=\'')
        __M_writer(filters.html_escape(filters.decode.utf8(entries[entry]["id"])))
        __M_writer(u"'\n        id='")
        __M_writer(filters.html_escape(filters.decode.utf8(entries[entry]["id"])))
        __M_writer(u'\'\n        data-divided="')
        __M_writer(filters.html_escape(filters.decode.utf8(str(entries[entry]['is_divided']).lower())))
        __M_writer(u'"\n        role="option"\n    >\n')
        if entry:
            __M_writer(u'        <span class="forum-nav-browse-title">\n')
            if topic_list:
                __M_writer(u'            <span class="sr">\n                ')
                __M_writer(filters.html_escape(filters.decode.utf8(', '.join(topic_list))))
                __M_writer(u',  \n            </span>\n')
            __M_writer(u'        ')
            __M_writer(filters.html_escape(filters.decode.utf8(entry)))
            __M_writer(u'\n        </span>\n')
        __M_writer(u'    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_dropdown(context,map,topic_list):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_category(categories,category,topic_list):
            return render_render_category(context,categories,category,topic_list)
        def render_entry(entries,entry,topic_list):
            return render_render_entry(context,entries,entry,topic_list)
        __M_writer = context.writer()
        __M_writer(u'\n')
        for child, c_type in map["children"]:
            if child in map["entries"] and c_type == TYPE_ENTRY:
                __M_writer(u'            ')
                __M_writer(filters.html_escape(filters.decode.utf8(HTML(render_entry(map["entries"], child, topic_list)))))
                __M_writer(u'\n')
            else:
                __M_writer(u'            ')
                __M_writer(filters.html_escape(filters.decode.utf8(HTML(render_category(map["subcategories"], child, topic_list)))))
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 122, "16": 2, "22": 1, "30": 1, "31": 6, "32": 16, "33": 37, "34": 51, "35": 53, "36": 53, "37": 55, "38": 55, "39": 56, "40": 56, "41": 57, "42": 57, "43": 63, "44": 63, "45": 67, "46": 67, "47": 69, "48": 69, "54": 39, "60": 39, "61": 41, "62": 41, "63": 44, "64": 44, "65": 46, "67": 46, "68": 47, "69": 47, "70": 48, "72": 48, "78": 18, "83": 18, "84": 21, "85": 21, "86": 22, "87": 22, "88": 23, "89": 23, "90": 26, "91": 27, "92": 28, "93": 29, "94": 30, "95": 30, "96": 33, "97": 33, "98": 33, "99": 36, "105": 8, "113": 8, "114": 9, "115": 10, "116": 11, "117": 11, "118": 11, "119": 12, "120": 13, "121": 13, "122": 13}, "uri": "discussion/_filter_dropdown.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/discussion/_filter_dropdown.html"}
__M_END_METADATA
"""
