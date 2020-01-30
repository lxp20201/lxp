# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284738.615263
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/common/templates/mathjax_include.html'
_template_uri = u'/mathjax_include.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,disable_fast_preview=True,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,disable_fast_preview=disable_fast_preview)
        mathjax_mode = context.get('mathjax_mode', UNDEFINED)
        Undefined = context.get('Undefined', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        if context.get('load_mathjax', True):
            __M_writer(u'\n')
            if disable_fast_preview:
                __M_writer(u'<script type="text/javascript">\n    // Fast Preview was introduced in 2.5. However, it\n    // causes undesirable flashing/font size changes when\n    // MathJax is used for interactive preview (equation editor).\n    // Setting processSectionDelay to 0 (see below) fully eliminates\n    // fast preview, but to reduce confusion, we are also setting\n    // the option as displayed in the context menu to false.\n    // When upgrading to 2.6, check if this variable name changed.\n    window.MathJax = {\n      menuSettings: {CHTMLpreview: false}\n    };\n</script>\n')
            __M_writer(u'\n')
            if mathjax_mode is not Undefined and mathjax_mode == 'wiki':
                __M_writer(u'<script type="text/x-mathjax-config">\n  MathJax.Hub.Config({\n    tex2jax: {inlineMath: [ [\'$\',\'$\'], ["\\\\(","\\\\)"]],\n              displayMath: [ [\'$$\',\'$$\'], ["\\\\[","\\\\]"]]}\n  });\n</script>\n')
            else:
                __M_writer(u'<script type="text/x-mathjax-config">\n  MathJax.Hub.Config({\n    tex2jax: {\n      inlineMath: [\n        ["\\\\(","\\\\)"],\n        [\'[mathjaxinline]\',\'[/mathjaxinline]\']\n      ],\n      displayMath: [\n        ["\\\\[","\\\\]"],\n        [\'[mathjax]\',\'[/mathjax]\']\n      ]\n    }\n  });\n</script>\n')
            __M_writer(u'<script type="text/x-mathjax-config">\n\n')
            if disable_fast_preview:
                __M_writer(u'  // In order to eliminate all flashing during interactive\n  // preview, it is necessary to set processSectionDelay to 0\n  // (remove delay between input and output phases). This\n  // effectively disables fast preview, regardless of\n  // the fast preview setting as shown in the context menu.\n  MathJax.Hub.processSectionDelay = 0;\n')
            __M_writer(u'\n  MathJax.Hub.signal.Interest(function(message) {\n    if(message[0] === "End Math") {\n        set_mathjax_display_div_settings();\n    }\n  });\n  function set_mathjax_display_div_settings() {\n    $(\'.MathJax_Display\').each(function( index ) {\n      this.setAttribute(\'tabindex\', \'0\');\n      this.setAttribute(\'aria-live\', \'off\');\n      this.removeAttribute(\'role\');\n      this.removeAttribute(\'aria-readonly\');\n    });\n  }\n</script>\n\n<script type="text/javascript">\n    // Activating Mathjax accessibility files\n    window.MathJax = {\n        menuSettings: {\n            collapsible: true,\n            autocollapse: true,\n            explorer: true\n        }\n    };\n</script>\n\n<!-- This must appear after all mathjax-config blocks, so it is after the imports from the other templates.\n     It can\'t be run through static.url because MathJax uses crazy url introspection to do lazy loading of\n     MathJax extension libraries -->\n<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/mathjax@2.7.5/MathJax.js?config=TeX-MML-AM_SVG"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 30, "33": 36, "34": 37, "35": 52, "36": 54, "37": 55, "38": 62, "44": 38, "16": 8, "23": 7, "24": 8, "25": 11, "26": 12, "27": 13, "28": 14, "29": 15, "30": 28, "31": 29}, "uri": "/mathjax_include.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/common/templates/mathjax_include.html"}
__M_END_METADATA
"""
