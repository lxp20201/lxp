# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580361385.756552
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/widgets/segment-io.html'
_template_uri = u'widgets/segment-io.html'
_source_encoding = 'utf-8'
_exports = []


from openedx.core.djangolib.js_utils import js_escaped_string 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        context_course = context.get('context_course', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if context_course:

            locator = context_course.id
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['locator'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        __M_writer(u'\n')
        if settings.CMS_SEGMENT_KEY:
            __M_writer(u'<!-- begin Segment -->\n<script type="text/javascript">\n  // if inside course, inject the course location into the JS namespace\n')
            if context_course:
                __M_writer(u'      var course_location_analytics = "')
                __M_writer(js_escaped_string( locator ))
                __M_writer(u'";\n')
            __M_writer(u'\n  // Asynchronously load Segment\'s analytics.js library\n  !function(){var analytics=window.analytics=window.analytics||[];if(!analytics.initialize)if(analytics.invoked)window.console&&console.error&&console.error("Segment snippet included twice.");else{analytics.invoked=!0;analytics.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","reset","group","track","ready","alias","page","once","off","on"];analytics.factory=function(t){return function(){var e=Array.prototype.slice.call(arguments);e.unshift(t);analytics.push(e);return analytics}};for(var t=0;t<analytics.methods.length;t++){var e=analytics.methods[t];analytics[e]=analytics.factory(e)}analytics.load=function(t){var e=document.createElement("script");e.type="text/javascript";e.async=!0;e.src=("https:"===document.location.protocol?"https://":"http://")+"cdn.segment.com/analytics.js/v1/"+t+"/analytics.min.js";var n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(e,n)};analytics.SNIPPET_VERSION="3.1.0";\n  analytics.load("')
            __M_writer(js_escaped_string( settings.CMS_SEGMENT_KEY ))
            __M_writer(u'");\n  analytics.page();\n  }}();\n  // Note: user tracking moved to segment-io-footer.html\n</script>\n<!-- end Segment -->\n')
        else:
            __M_writer(u'<!-- dummy Segment -->\n<script type="text/javascript">\n')
            if context_course:
                __M_writer(u'  var course_location_analytics = "')
                __M_writer(js_escaped_string( locator ))
                __M_writer(u'";\n')
            __M_writer(u'  var analytics = {\n    "track": function() {}\n  };\n</script>\n<!-- end dummy Segment -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "18": 1, "25": 1, "26": 2, "27": 4, "28": 5, "34": 7, "35": 9, "36": 10, "37": 11, "38": 14, "39": 15, "40": 15, "41": 15, "42": 17, "43": 20, "44": 20, "45": 26, "46": 27, "47": 29, "48": 30, "49": 30, "50": 30, "51": 32, "57": 51}, "uri": "widgets/segment-io.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/widgets/segment-io.html"}
__M_END_METADATA
"""
