# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580211856.163809
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/common/djangoapps/pipeline_mako/templates/static_content.html'
_template_uri = u'static_content.html'
_source_encoding = 'utf-8'
_exports = ['get_page_title_breadcrumbs', 'is_request_in_themed_site', 'marketing_link', 'get_platform_name', 'url', 'get_tech_support_email_address', 'get_value', 'studiofrontend', 'optional_include_mako', 'js', 'get_contact_email_address', 'webpack', 'dir_rtl', 'renderReact', 'require_module', 'require_module_async', 'include', 'get_template_path', 'css', 'certificate_asset_url']



import logging
import json
from django.contrib.staticfiles.storage import staticfiles_storage
from pipeline_mako import compressed_css, compressed_js
from pipeline_mako.helpers.studiofrontend import load_sfe_i18n_messages
from django.utils.translation import get_language_bidi
from mako.exceptions import TemplateLookupException
from edxmako.shortcuts import marketing_link

from openedx.core.djangolib.js_utils import js_escaped_string, dump_js_escaped_json
from openedx.core.djangolib.markup import HTML
from openedx.core.djangoapps.site_configuration.helpers import (
  page_title_breadcrumbs,
  get_value,
)

from openedx.core.djangoapps.theming.helpers import (
  get_template_path,
  is_request_in_themed_site,
)
from lms.djangoapps.certificates.api import get_asset_url_by_slug
from webpack_loader.templatetags.webpack_loader import render_bundle
logger = logging.getLogger(__name__)


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_page_title_breadcrumbs(context,*args):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        return page_title_breadcrumbs(*args)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_is_request_in_themed_site(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        return is_request_in_themed_site()
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_marketing_link(context,name):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        link = marketing_link(name)
        return "/" if link == "#" else link
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_platform_name(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()

        return get_value('platform_name', settings.PLATFORM_NAME)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_url(context,file,raw=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        try:
            url = staticfiles_storage.url(file)
        except:
            url = file
        ## HTML-escaping must be handled by caller
        
        
        __M_writer(filters.decode.utf8(url ))
        __M_writer(filters.html_escape(filters.decode.utf8("?raw" if raw else "")))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_tech_support_email_address(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()

        return get_value('email_from_address', settings.TECH_SUPPORT_EMAIL)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_value(context,val_name,default=None,**kwargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        return get_value(val_name, default=default, **kwargs)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_studiofrontend(context,entry):
    __M_caller = context.caller_stack._push_frame()
    try:
        def url(file,raw=False):
            return render_url(context,file,raw)
        capture = context.get('capture', UNDEFINED)
        caller = context.get('caller', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(u'\n    ')

        body = capture(caller.body)
        body_dict = json.loads(body)
        locale = body_dict['lang']
        
        messages = load_sfe_i18n_messages(locale)
            
        
        __M_writer(u'\n    <script type="application/json" id="SFE_i18n_data">\n      {\n        "locale": "')
        __M_writer(filters.decode.utf8( locale ))
        __M_writer(u'",\n        "messages": ')
        __M_writer(filters.decode.utf8( messages ))
        __M_writer(u'\n      }\n    </script>\n    <script type="application/javascript" id=\'courseContext\'>\n        var studioContext = ')
        __M_writer(filters.decode.utf8( body ))
        __M_writer(u';\n    </script>\n    <div id="root" class="SFE"></div>\n')
        if settings.STUDIO_FRONTEND_CONTAINER_URL:
            __M_writer(u'        <script type="text/javascript" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(settings.STUDIO_FRONTEND_CONTAINER_URL)))
            __M_writer(u'/')
            __M_writer(filters.html_escape(filters.decode.utf8(entry)))
            __M_writer(u'.js"></script>\n')
        else:
            __M_writer(u'        <script type="text/javascript" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(url('common/js/vendor/runtime.min.js'))))
            __M_writer(u'"></script>\n        <script type="text/javascript" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(url('common/js/vendor/common.min.js'))))
            __M_writer(u'"></script>\n        <script type="text/javascript" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(url('common/js/vendor/{}.min.js'.format(entry)))))
            __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_optional_include_mako(context,file,is_theming_enabled=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()

# http://stackoverflow.com/q/21219531
        if is_theming_enabled:
            file = get_template_path(file)
        try:
            tmpl = self.get_template(file)
        except TemplateLookupException:
            pass
        else:
            tmpl.render_context(context)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context,group):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if settings.PIPELINE_ENABLED:
            __M_writer(u'    ')
            __M_writer(filters.decode.utf8(compressed_js(group) ))
            __M_writer(u'\n')
        else:
            for filename in settings.PIPELINE_JS[group]['source_filenames']:
                __M_writer(u'      <script type="text/javascript" src="')
                __M_writer(filters.html_escape(filters.decode.utf8(staticfiles_storage.url(filename.replace('.coffee', '.js')))))
                __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_contact_email_address(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()

        return get_value('email_from_address', settings.CONTACT_EMAIL)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_webpack(context,entry,extension=None,config='DEFAULT',attrs=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        capture = context.get('capture', UNDEFINED)
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(u'\n    ')

        body = capture(caller.body)
            
        
        __M_writer(u'\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(render_bundle(entry, extension=None, config='DEFAULT', attrs=attrs)))))
        __M_writer(u'\n')
        if body:
            __M_writer(u'      <script type="text/javascript">\n        ')
            __M_writer(filters.decode.utf8(body ))
            __M_writer(u'\n      </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_dir_rtl(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        return 'rtl' if get_language_bidi() else 'ltr'
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_renderReact(context,component,id,props={}):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(u'\n\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(render_bundle(component)))))
        __M_writer(u'\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(render_bundle('ReactRenderer')))))
        __M_writer(u'\n\n    <div id="')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'"></div>\n    <script type="text/javascript">\n      var c;\n      try { c = ')
        __M_writer(filters.decode.utf8(component ))
        __M_writer(u"; } catch (e) { c = null; }\n      new ReactRenderer({\n        component: c,\n        selector: '#")
        __M_writer(filters.decode.utf8(id ))
        __M_writer(u"',\n        componentName: '")
        __M_writer(js_escaped_string(component ))
        __M_writer(u"',\n        props: ")
        __M_writer(dump_js_escaped_json(props ))
        __M_writer(u'\n      });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_require_module(context,module_name,class_name):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(u'\n')
        if not settings.REQUIRE_DEBUG:
            __M_writer(u'      <script type="text/javascript" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(staticfiles_storage.url(module_name + '.js') + '?raw')))
            __M_writer(u'"></script>\n')
        __M_writer(u'    <script type="text/javascript">\n        (function (require) {\n            require([\'')
        __M_writer(js_escaped_string(module_name ))
        __M_writer(u"'], function (")
        __M_writer(filters.decode.utf8(class_name ))
        __M_writer(u') {\n                ')
        __M_writer(filters.decode.utf8(caller.body() ))
        __M_writer(u'\n            });\n        }).call(this, require || RequireJS.require);\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_require_module_async(context,module_name,class_name):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  ')
        __M_writer(u'\n  <script type="text/javascript">\n    (function (require) {\n')
        if settings.REQUIRE_DEBUG:
            __M_writer(u"          (function (require) {\n              require(['")
            __M_writer(js_escaped_string(module_name ))
            __M_writer(u"'], function (")
            __M_writer(filters.decode.utf8(class_name ))
            __M_writer(u') {\n                  ')
            __M_writer(filters.decode.utf8(caller.body() ))
            __M_writer(u'\n              });\n          }).call(this, require || RequireJS.require);\n')
        else:
            __M_writer(u"        require(['")
            __M_writer(js_escaped_string(staticfiles_storage.url(module_name + ".js") + "?raw" ))
            __M_writer(u"'], function () {\n          require(['")
            __M_writer(js_escaped_string(module_name ))
            __M_writer(u"'], function (")
            __M_writer(filters.decode.utf8(class_name ))
            __M_writer(u') {\n            ')
            __M_writer(filters.decode.utf8(caller.body() ))
            __M_writer(u'\n          });\n        });\n')
        __M_writer(u'    }).call(this, require || RequireJS.require);\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_include(context,path):
    __M_caller = context.caller_stack._push_frame()
    try:
        list = context.get('list', UNDEFINED)
        __M_writer = context.writer()

        from django.conf import settings
        from django.template.engine import Engine
        from django.template.loaders.filesystem import Loader
        from openedx.core.djangoapps.theming.helpers import get_current_theme
        dirs = settings.DEFAULT_TEMPLATE_ENGINE['DIRS']
        theme = get_current_theme()
        if theme:
            dirs = list(dirs)
            dirs.insert(0, theme.path / 'templates')
        engine = Engine(dirs=dirs)
        source, template_path = Loader(engine).load_template_source(path)
        
        
        __M_writer(filters.decode.utf8(source ))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_template_path(context,relative_path,**kwargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        return get_template_path(relative_path, **kwargs)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context,group,raw=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  ')

        rtl_group = '{}-rtl'.format(group)
        
        if get_language_bidi() and rtl_group in settings.PIPELINE_CSS:
          group = rtl_group
          
        
        __M_writer(u'\n\n')
        if settings.PIPELINE_ENABLED:
            __M_writer(u'    ')
            __M_writer(filters.decode.utf8(compressed_css(group, raw=raw) ))
            __M_writer(u'\n')
        else:
            for filename in settings.PIPELINE_CSS[group]['source_filenames']:
                __M_writer(u'      <link rel="stylesheet" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(staticfiles_storage.url(filename.replace('.scss', '.css')))))
                __M_writer(filters.html_escape(filters.decode.utf8("?raw" if raw else "")))
                __M_writer(u'" type="text/css" media="all" / >\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_certificate_asset_url(context,slug):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        try:
            url = get_asset_url_by_slug(slug)
        except:
            url = ''
        ## HTML-escaping must be handled by caller
        
        
        __M_writer(filters.decode.utf8(url ))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "42": 1, "47": 1, "48": 26, "49": 31, "50": 39, "51": 47, "52": 64, "53": 74, "54": 83, "55": 97, "56": 128, "57": 144, "58": 171, "59": 189, "60": 218, "61": 230, "62": 235, "63": 239, "64": 243, "65": 247, "66": 251, "67": 255, "68": 259, "74": 233, "78": 233, "87": 249, "91": 249, "100": 28, "104": 28, "114": 237, "119": 237, "128": 33, "132": 33, "140": 39, "141": 39, "147": 253, "152": 253, "161": 241, "165": 241, "174": 99, "183": 99, "184": 103, "185": 104, "193": 110, "194": 113, "195": 113, "196": 114, "197": 114, "198": 118, "199": 118, "200": 121, "201": 122, "202": 122, "203": 122, "204": 122, "205": 122, "206": 123, "207": 124, "208": 124, "209": 124, "210": 125, "211": 125, "212": 126, "213": 126, "219": 220, "224": 220, "241": 66, "246": 66, "247": 67, "248": 68, "249": 68, "250": 68, "251": 69, "252": 70, "253": 71, "254": 71, "255": 71, "261": 257, "266": 257, "275": 130, "281": 130, "282": 134, "283": 135, "287": 137, "288": 138, "289": 138, "290": 139, "291": 140, "292": 141, "293": 141, "299": 81, "303": 81, "312": 146, "316": 146, "317": 155, "318": 157, "319": 157, "320": 158, "321": 158, "322": 160, "323": 160, "324": 163, "325": 163, "326": 166, "327": 166, "328": 167, "329": 167, "330": 168, "331": 168, "337": 173, "343": 173, "344": 178, "345": 179, "346": 180, "347": 180, "348": 180, "349": 182, "350": 184, "351": 184, "352": 184, "353": 184, "354": 185, "355": 185, "361": 191, "367": 191, "368": 196, "369": 199, "370": 200, "371": 201, "372": 201, "373": 201, "374": 201, "375": 202, "376": 202, "377": 205, "378": 210, "379": 210, "380": 210, "381": 211, "382": 211, "383": 211, "384": 211, "385": 212, "386": 212, "387": 216, "393": 85, "398": 85, "412": 97, "418": 245, "422": 245, "431": 49, "436": 49, "437": 50, "444": 55, "445": 57, "446": 58, "447": 58, "448": 58, "449": 59, "450": 60, "451": 61, "452": 61, "453": 61, "454": 61, "460": 41, "464": 41, "472": 47, "478": 472}, "uri": "static_content.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/common/djangoapps/pipeline_mako/templates/static_content.html"}
__M_END_METADATA
"""
