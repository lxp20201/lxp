# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284737.998657
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/openedx/features/course_experience/templates/course_experience/course-outline-fragment.html'
_template_uri = 'course_experience/course-outline-fragment.html'
_source_encoding = 'utf-8'
_exports = []



from datetime import date

from django.utils.translation import ugettext as _

from openedx.core.djangolib.markup import HTML, Text


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
        user_timezone = context.get('user_timezone', UNDEFINED)
        blocks = context.get('blocks', UNDEFINED)
        xblock_display_names = context.get('xblock_display_names', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        user_language = context.get('user_language', UNDEFINED)
        gated_content = context.get('gated_content', UNDEFINED)
        enable_links = context.get('enable_links', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')

        course_sections = blocks.get('children')
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['course_sections'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n<main role="main" class="course-outline" id="main" tabindex="-1">\n')
        if course_sections is not None:
            __M_writer(u'        <button class="btn btn-primary"\n                id="expand-collapse-outline-all-button"\n                aria-expanded="false"\n                aria-controls="course-outline-block-tree"\n                >\n          <span class="expand-collapse-outline-all-extra-padding" id="expand-collapse-outline-all-span">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Expand All"))))
            __M_writer(u'</span>\n        </button>\n        <ol class="block-tree accordion"\n            id="course-outline-block-tree"\n            aria-labelledby="expand-collapse-outline-all-button">\n')
            for section in course_sections:
                __M_writer(u'            ')

                section_is_auto_opened = section.get('resume_block') is True
                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['section_is_auto_opened'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                <li class="outline-item section">\n                    <button class="section-name accordion-trigger"\n                            aria-expanded="')
                __M_writer(filters.html_escape(filters.decode.utf8( 'true' if section_is_auto_opened else 'false' )))
                __M_writer(u'"\n                            aria-controls="')
                __M_writer(filters.html_escape(filters.decode.utf8( section['id'] )))
                __M_writer(u'_contents"\n                            id="')
                __M_writer(filters.html_escape(filters.decode.utf8( section['id'] )))
                __M_writer(u'">\n                        <span class="fa fa-chevron-right ')
                __M_writer(filters.html_escape(filters.decode.utf8( 'fa-rotate-90' if section_is_auto_opened else '' )))
                __M_writer(u'" aria-hidden="true"></span>\n                        <h3 class="section-title">')
                __M_writer(filters.html_escape(filters.decode.utf8( section['display_name'] )))
                __M_writer(u'</h3>\n')
                if section.get('complete'):
                    __M_writer(u'                            <span class="complete-checkmark fa fa-check"></span>\n')
                __M_writer(u'                    </button>\n                    <ol class="outline-item accordion-panel ')
                __M_writer(filters.html_escape(filters.decode.utf8( '' if section_is_auto_opened else 'is-hidden' )))
                __M_writer(u'"\n                        id="')
                __M_writer(filters.html_escape(filters.decode.utf8( section['id'] )))
                __M_writer(u'_contents"\n                        aria-labelledby="')
                __M_writer(filters.html_escape(filters.decode.utf8( section['id'] )))
                __M_writer(u'">\n')
                for subsection in section.get('children', []):
                    __M_writer(u'                ')

                    gated_subsection = subsection['id'] in gated_content
                    completed_prereqs = gated_content[subsection['id']]['completed_prereqs'] if gated_subsection else False
                    subsection_is_auto_opened = subsection.get('resume_block') is True
                    
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['completed_prereqs','gated_subsection','subsection_is_auto_opened'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n                      <li class="subsection accordion ')
                    __M_writer(filters.html_escape(filters.decode.utf8( 'current' if subsection.get('resume_block') else '' )))
                    __M_writer(u'">\n')
                    if gated_subsection and not completed_prereqs:
                        __M_writer(u'                                <a href="')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['lms_web_url'] )))
                        __M_writer(u'">\n                                    <button class="subsection-text prerequisite-button"\n                                            id="')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['id'] )))
                        __M_writer(u'">\n                                    <span class="menu-icon icon fa fa-lock"\n                                            aria-hidden="true">\n                                    </span>\n                                    <h4 class="subsection-title">\n                                        ')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['display_name'] )))
                        __M_writer(u'\n                                    </h4>\n                                    <div class="details prerequisite">\n                                        ')
                        __M_writer(filters.html_escape(filters.decode.utf8( _("Prerequisite: ") )))
                        __M_writer(u'\n                                            ')

                        prerequisite_id = gated_content[subsection['id']]['prerequisite']
                        prerequisite_name = xblock_display_names.get(prerequisite_id)
                                                                    
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['prerequisite_name','prerequisite_id'] if __M_key in __M_locals_builtin_stored]))
                        __M_writer(u'\n                                            ')
                        __M_writer(filters.html_escape(filters.decode.utf8( prerequisite_name )))
                        __M_writer(u'\n                                    </div>\n')
                    else:
                        __M_writer(u'                                    <button class="subsection-text accordion-trigger"\n                                            id="')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['id'] )))
                        __M_writer(u'"\n                                            aria-expanded="')
                        __M_writer(filters.html_escape(filters.decode.utf8( 'true' if subsection_is_auto_opened else 'false' )))
                        __M_writer(u'"\n                                            aria-controls="')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['id'] )))
                        __M_writer(u'_contents">\n                                        <span class="fa fa-chevron-right ')
                        __M_writer(filters.html_escape(filters.decode.utf8( 'fa-rotate-90' if subsection_is_auto_opened else '' )))
                        __M_writer(u'"\n                                              aria-hidden="true"></span>\n                                        <h4 class="subsection-title">\n                                            ')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['display_name'] )))
                        __M_writer(u'\n                                        </h4>\n')
                        if subsection.get('complete'):
                            __M_writer(u'                                        <span class="complete-checkmark fa fa-check"></span>\n')
                    __M_writer(u'                                        <div class="details">\n\n')
                    __M_writer(u'                ')

                    if subsection.get('due') is None:
                        # examples: Homework, Lab, etc.
                        data_string = subsection.get('format')
                    else:
                        if 'special_exam_info' in subsection:
                            data_string = _('due {date}')
                        else:
                            data_string = _("{subsection_format} due {{date}}").format(subsection_format=subsection.get('format'))
                    
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['data_string'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
                    if subsection.get('format') or 'special_exam_info' in subsection:
                        __M_writer(u'                                            <span class="subtitle">\n')
                        if 'special_exam' in subsection:
                            __M_writer(u'                                                    <span\n                                                        class="menu-icon icon fa ')
                            __M_writer(filters.html_escape(filters.decode.utf8(subsection['special_exam_info'].get('suggested_icon', 'fa-pencil-square-o'))))
                            __M_writer(u' ')
                            __M_writer(filters.html_escape(filters.decode.utf8(subsection['special_exam_info'].get('status', 'eligible'))))
                            __M_writer(u'"\n                                                        aria-hidden="true"\n                                                    ></span>\n                                                    <span class="subtitle-name">\n                                                        ')
                            __M_writer(filters.html_escape(filters.decode.utf8(subsection['special_exam_info'].get('short_description', ''))))
                            __M_writer(u'\n                                                    </span>\n\n')
                            if not subsection['special_exam_info'].get('in_completed_state', False):
                                __M_writer(u'                                                        <span\n                                                            class="localized-datetime subtitle-name"\n                                                            data-datetime="')
                                __M_writer(filters.html_escape(filters.decode.utf8(subsection.get('due'))))
                                __M_writer(u'"\n                                                            data-string="')
                                __M_writer(filters.html_escape(filters.decode.utf8(data_string)))
                                __M_writer(u'"\n                                                            data-timezone="')
                                __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                                __M_writer(u'"\n                                                            data-language="')
                                __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                                __M_writer(u'"\n                                                        ></span>\n')
                        else:
                            __M_writer(u'                                                    <span\n                                                        class="localized-datetime subtitle-name"\n                                                        data-datetime="')
                            __M_writer(filters.html_escape(filters.decode.utf8(subsection.get('due'))))
                            __M_writer(u'"\n                                                        data-string="')
                            __M_writer(filters.html_escape(filters.decode.utf8(data_string)))
                            __M_writer(u'"\n                                                        data-timezone="')
                            __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                            __M_writer(u'"\n                                                        data-language="')
                            __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                            __M_writer(u'"\n                                                    ></span>\n\n')
                            if subsection.get('graded'):
                                __M_writer(u'                                                        <span class="sr">&nbsp;')
                                __M_writer(filters.html_escape(filters.decode.utf8(_("This content is graded"))))
                                __M_writer(u'</span>\n')
                        __M_writer(u'                                            </span>\n')
                    __M_writer(u'                                        </div> <!-- /details -->\n                                    </button> <!-- /subsection-text -->\n')
                    if gated_subsection and not completed_prereqs:
                        __M_writer(u'                                </a>\n')
                    if not gated_subsection or (gated_subsection and completed_prereqs):
                        __M_writer(u'                                <ol class="outline-item accordion-panel ')
                        __M_writer(filters.html_escape(filters.decode.utf8( '' if subsection_is_auto_opened else 'is-hidden' )))
                        __M_writer(u'"\n                                    id="')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['id'] )))
                        __M_writer(u'_contents"\n                                    aria-labelledby="')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['id'] )))
                        __M_writer(u'"\n                                >\n')
                        for vertical in subsection.get('children', []):
                            __M_writer(u'                                    <li class="vertical outline-item focusable">\n                                        <a class="outline-item focusable"\n')
                            if enable_links:
                                __M_writer(u'                                                href="')
                                __M_writer(filters.html_escape(filters.decode.utf8( vertical['lms_web_url'] )))
                                __M_writer(u'"\n')
                            else:
                                __M_writer(u'                                                aria-disabled="true"\n')
                            __M_writer(u'                                            id="')
                            __M_writer(filters.html_escape(filters.decode.utf8( vertical['id'] )))
                            __M_writer(u'">\n                                            <div class="vertical-details">\n                                              <div class="vertical-title">\n                                                ')
                            __M_writer(filters.html_escape(filters.decode.utf8( vertical['display_name'] )))
                            __M_writer(u'\n                                              </div>\n                                            </div>\n')
                            if vertical.get('complete'):
                                __M_writer(u'                                                <span class="complete-checkmark fa fa-check"></span>\n')
                            __M_writer(u'                                        </a>\n                                    </li>\n')
                        __M_writer(u'                                </ol>\n')
                    __M_writer(u'                            </li>\n')
                __M_writer(u'                    </ol>\n                </li>\n')
            __M_writer(u'        </ol>\n')
        __M_writer(u'</main>\n\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u"\n    DateUtilFactory.transform('.localized-datetime');\n")
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module_async(class_name=u'DateUtilFactory',module_name=u'js/dateutil_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n    new CourseOutline();\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'CourseOutline'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 7, "31": 5, "34": 3, "46": 2, "47": 3, "48": 5, "49": 13, "50": 15, "56": 17, "57": 19, "58": 20, "59": 25, "60": 25, "61": 30, "62": 31, "63": 31, "69": 33, "70": 36, "71": 36, "72": 37, "73": 37, "74": 38, "75": 38, "76": 39, "77": 39, "78": 40, "79": 40, "80": 41, "81": 42, "82": 44, "83": 45, "84": 45, "85": 46, "86": 46, "87": 47, "88": 47, "89": 48, "90": 49, "91": 49, "99": 53, "100": 54, "101": 54, "102": 55, "103": 56, "104": 56, "105": 56, "106": 58, "107": 58, "108": 63, "109": 63, "110": 66, "111": 66, "112": 67, "119": 70, "120": 71, "121": 71, "122": 73, "123": 74, "124": 75, "125": 75, "126": 76, "127": 76, "128": 77, "129": 77, "130": 78, "131": 78, "132": 81, "133": 81, "134": 83, "135": 84, "136": 87, "137": 93, "138": 93, "151": 102, "152": 103, "153": 104, "154": 105, "155": 107, "156": 108, "157": 108, "158": 108, "159": 108, "160": 112, "161": 112, "162": 117, "163": 118, "164": 120, "165": 120, "166": 121, "167": 121, "168": 122, "169": 122, "170": 123, "171": 123, "172": 126, "173": 129, "174": 131, "175": 131, "176": 132, "177": 132, "178": 133, "179": 133, "180": 134, "181": 134, "182": 137, "183": 138, "184": 138, "185": 138, "186": 141, "187": 143, "188": 145, "189": 146, "190": 148, "191": 149, "192": 149, "193": 149, "194": 150, "195": 150, "196": 151, "197": 151, "198": 153, "199": 154, "200": 156, "201": 157, "202": 157, "203": 157, "204": 158, "205": 159, "206": 161, "207": 161, "208": 161, "209": 164, "210": 164, "211": 167, "212": 168, "213": 170, "214": 173, "215": 175, "216": 177, "217": 180, "218": 182, "222": 184, "227": 184, "230": 186, "234": 188, "239": 188, "242": 190, "248": 242}, "uri": "course_experience/course-outline-fragment.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/openedx/features/course_experience/templates/course_experience/course-outline-fragment.html"}
__M_END_METADATA
"""
