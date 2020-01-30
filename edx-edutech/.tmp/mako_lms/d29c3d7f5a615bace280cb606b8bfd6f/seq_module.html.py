# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284777.065096
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/seq_module.html'
_template_uri = 'seq_module.html'
_source_encoding = 'utf-8'
_exports = []


from django.utils.translation import ugettext as _ 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        prev_url = context.get('prev_url', UNDEFINED)
        save_position = context.get('save_position', UNDEFINED)
        banner_text = context.get('banner_text', UNDEFINED)
        items = context.get('items', UNDEFINED)
        show_completion = context.get('show_completion', UNDEFINED)
        next_url = context.get('next_url', UNDEFINED)
        ajax_url = context.get('ajax_url', UNDEFINED)
        gated_content = context.get('gated_content', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        item_id = context.get('item_id', UNDEFINED)
        position = context.get('position', UNDEFINED)
        element_id = context.get('element_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<div id="sequence_')
        __M_writer(filters.html_escape(filters.decode.utf8(element_id)))
        __M_writer(u'" class="sequence" data-id="')
        __M_writer(filters.html_escape(filters.decode.utf8(item_id)))
        __M_writer(u'"\n     data-position="')
        __M_writer(filters.html_escape(filters.decode.utf8(position)))
        __M_writer(u'" data-ajax-url="')
        __M_writer(filters.html_escape(filters.decode.utf8(ajax_url)))
        __M_writer(u'"\n     data-next-url="')
        __M_writer(filters.html_escape(filters.decode.utf8(next_url)))
        __M_writer(u'" data-prev-url="')
        __M_writer(filters.html_escape(filters.decode.utf8(prev_url)))
        __M_writer(u'"\n     data-save-position="')
        __M_writer(filters.html_escape(filters.decode.utf8('true' if save_position else 'false')))
        __M_writer(u'"\n     data-show-completion="')
        __M_writer(filters.html_escape(filters.decode.utf8('true' if show_completion else 'false')))
        __M_writer(u'"\n>\n')
        if banner_text:
            __M_writer(u'    <div class="pattern-library-shim alert alert-information subsection-header" tabindex="-1">\n      <span class="pattern-library-shim icon alert-icon fa fa-info-circle" aria-hidden="true"></span>\n      <span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Important!'))))
            __M_writer(u'&nbsp;</span>\n      <div class="pattern-library-shim alert-message">\n        <p class="pattern-library-shim alert-copy">\n          ')
            __M_writer(filters.html_escape(filters.decode.utf8(banner_text)))
            __M_writer(u'\n        </p>\n      </div>\n    </div>\n')
        __M_writer(u'\n  <div class="sequence-nav">\n    <button class="sequence-nav-button button-previous">\n      <span class="icon fa fa-chevron-prev" aria-hidden="true"></span>\n      <span class="sequence-nav-button-label">')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Previous'))))
        __M_writer(u'</span>\n    </button>\n    <button class="sequence-nav-button button-next">\n      <span class="sequence-nav-button-label">')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Next'))))
        __M_writer(u'</span>\n      <span class="icon fa fa-chevron-next" aria-hidden="true"></span>\n    </button>\n    <nav class="sequence-list-wrapper" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Sequence'))))
        __M_writer(u'">\n      <ol id="sequence-list" role="tablist">\n')
        if gated_content['gated']:
            __M_writer(u'        <li>\n          <button class="active nav-item tab" title="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Content Locked'))))
            __M_writer(u'" id="tab_0" role="tab" tabindex="-1" aria-selected="true" aria-expanded="true" aria-controls="content_locked" disabled>\n            <span class="icon fa fa-lock" aria-hidden="true"></span>\n          </button>\n        </li>\n')
        else:
            for idx, item in enumerate(items):
                __M_writer(u'        <li role="presentation">\n          <button class="seq_')
                __M_writer(filters.html_escape(filters.decode.utf8(item['type'])))
                __M_writer(u' inactive nav-item tab"\n            role="tab"\n            tabindex="-1"\n            aria-selected="false"\n            aria-expanded="false"\n            aria-controls="seq_content"\n            data-index="')
                __M_writer(filters.html_escape(filters.decode.utf8(idx)))
                __M_writer(u'"\n            data-id="')
                __M_writer(filters.html_escape(filters.decode.utf8(item['id'])))
                __M_writer(u'"\n            data-element="')
                __M_writer(filters.html_escape(filters.decode.utf8(idx+1)))
                __M_writer(u'"\n            data-page-title="')
                __M_writer(filters.html_escape(filters.decode.utf8(item['page_title'])))
                __M_writer(u'"\n            data-path="')
                __M_writer(filters.html_escape(filters.decode.utf8(item['path'])))
                __M_writer(u'"\n            data-graded="')
                __M_writer(filters.html_escape(filters.decode.utf8(item['graded'])))
                __M_writer(u'"\n            id="tab_')
                __M_writer(filters.html_escape(filters.decode.utf8(idx)))
                __M_writer(u'">\n            <span class="icon fa seq_')
                __M_writer(filters.html_escape(filters.decode.utf8(item['type'])))
                __M_writer(u'" aria-hidden="true"></span>\n')
                if 'complete' in item:
                    __M_writer(u'              <span \n                class="fa fa-check-circle check-circle ')
                    __M_writer(filters.html_escape(filters.decode.utf8("is-hidden" if not item['complete'] else "")))
                    __M_writer(u'" \n                style="color:green"\n                aria-hidden="true"\n              ></span>\n')
                __M_writer(u'            <span class="fa fa-fw fa-bookmark bookmark-icon ')
                __M_writer(filters.html_escape(filters.decode.utf8("is-hidden" if not item['bookmarked'] else "bookmarked")))
                __M_writer(u'" aria-hidden="true"></span>\n            <div class="sequence-tooltip sr"><span class="sr">')
                __M_writer(filters.html_escape(filters.decode.utf8(item['type'])))
                __M_writer(u'&nbsp;</span>')
                __M_writer(filters.html_escape(filters.decode.utf8(item['page_title'])))
                __M_writer(u'<span class="sr bookmark-icon-sr">&nbsp;')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Bookmarked") if item['bookmarked'] else "")))
                __M_writer(u'</span></div>\n          </button>\n        </li>\n')
        __M_writer(u'      </ol>\n    </nav>\n  </div>\n')
        if gated_content['gated']:
            __M_writer(u'    ')
            runtime._include_file(context, u'_gated_content.html', _template_uri, prereq_url=gated_content['prereq_url'], prereq_section_name=gated_content['prereq_section_name'], gated_section_name=gated_content['gated_section_name'])
            __M_writer(u'\n')
        else:
            __M_writer(u'  <div class="sr-is-focusable" tabindex="-1"></div>\n\n')
            for idx, item in enumerate(items):
                __M_writer(u'  <div id="seq_contents_')
                __M_writer(filters.html_escape(filters.decode.utf8(idx)))
                __M_writer(u'"\n    aria-labelledby="tab_')
                __M_writer(filters.html_escape(filters.decode.utf8(idx)))
                __M_writer(u'"\n    aria-hidden="true"\n    class="seq_contents tex2jax_ignore asciimath2jax_ignore">\n    ')
                __M_writer(filters.html_escape(filters.decode.utf8(item['content'])))
                __M_writer(u'\n  </div>\n')
            __M_writer(u'  <div id="seq_content" role="tabpanel"></div>\n')
        __M_writer(u'\n  <nav class="sequence-bottom" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Section'))))
        __M_writer(u'">\n    <button class="sequence-nav-button button-previous">\n      <span class="icon fa fa-chevron-prev" aria-hidden="true"></span>\n      <span>')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Previous'))))
        __M_writer(u'</span>\n    </button>\n    <button class="sequence-nav-button button-next">\n      <span>')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Next'))))
        __M_writer(u'</span>\n      <span class="icon fa fa-chevron-next" aria-hidden="true"></span>\n    </button>\n  </nav>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "18": 1, "35": 1, "36": 2, "37": 4, "38": 4, "39": 4, "40": 4, "41": 5, "42": 5, "43": 5, "44": 5, "45": 6, "46": 6, "47": 6, "48": 6, "49": 7, "50": 7, "51": 8, "52": 8, "53": 10, "54": 11, "55": 13, "56": 13, "57": 16, "58": 16, "59": 21, "60": 25, "61": 25, "62": 28, "63": 28, "64": 31, "65": 31, "66": 33, "67": 34, "68": 35, "69": 35, "70": 39, "71": 40, "72": 41, "73": 42, "74": 42, "75": 48, "76": 48, "77": 49, "78": 49, "79": 50, "80": 50, "81": 51, "82": 51, "83": 52, "84": 52, "85": 53, "86": 53, "87": 54, "88": 54, "89": 55, "90": 55, "91": 56, "92": 57, "93": 58, "94": 58, "95": 63, "96": 63, "97": 63, "98": 64, "99": 64, "100": 64, "101": 64, "102": 64, "103": 64, "104": 69, "105": 72, "106": 73, "107": 73, "108": 73, "109": 74, "110": 75, "111": 77, "112": 78, "113": 78, "114": 78, "115": 79, "116": 79, "117": 82, "118": 82, "119": 85, "120": 87, "121": 88, "122": 88, "123": 91, "124": 91, "125": 94, "126": 94, "132": 126}, "uri": "seq_module.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/seq_module.html"}
__M_END_METADATA
"""
