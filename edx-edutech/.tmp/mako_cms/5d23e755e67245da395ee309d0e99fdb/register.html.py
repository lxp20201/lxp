# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580361432.887504
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/register.html'
_template_uri = 'register.html'
_source_encoding = 'utf-8'
_exports = [u'content', u'requirejs', u'bodyclass', 'online_help_token', u'title']



from django.utils.translation import ugettext as _
from django.urls import reverse


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        settings = context.get('settings', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def requirejs():
            return render_requirejs(context._locals(__M_locals))
        marketing_link = context.get('marketing_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'requirejs'):
            context['self'].requirejs(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        marketing_link = context.get('marketing_link', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n<div class="wrapper-content wrapper">\n  <section class="content">\n    <header>\n      <h1 class="title title-1">')
        __M_writer(filters.decode.utf8(_("Sign Up for {studio_name}").format(studio_name=settings.STUDIO_NAME)))
        __M_writer(u'</h1>\n      <a href="')
        __M_writer(filters.decode.utf8(reverse('login')))
        __M_writer(u'" class="action action-signin">')
        __M_writer(filters.decode.utf8(_("Already have a {studio_name} Account? Sign in").format(studio_name=settings.STUDIO_SHORT_NAME)))
        __M_writer(u'</a>\n    </header>\n\n    <p class="introduction">')
        __M_writer(filters.decode.utf8(_("Ready to start creating online courses? Sign up below and start creating your first {platform_name} course today.").format(platform_name=settings.PLATFORM_NAME)))
        __M_writer(u'</p>\n\n    <article class="content-primary" role="main">\n      <form id="register_form" method="post">\n        <div id="register_error" name="register_error" class="message message-status message-status error">\n        </div>\n\n        <fieldset>\n          <legend class="sr">')
        __M_writer(filters.decode.utf8(_("Required Information to Sign Up for {studio_name}").format(studio_name=settings.STUDIO_NAME)))
        __M_writer(u'</legend>\n\n          <ol class="list-input">\n            <li class="field text required" id="field-email">\n              <label for="email">')
        __M_writer(filters.decode.utf8(_("E-mail")))
        __M_writer(u'</label>\n')
        __M_writer(u'              <input id="email" type="email" name="email" placeholder="')
        __M_writer(filters.decode.utf8(_("example: username@domain.com")))
        __M_writer(u'" />\n            </li>\n\n            <li class="field text required" id="field-name">\n              <label for="name">')
        __M_writer(filters.decode.utf8(_("Full Name")))
        __M_writer(u'</label>\n')
        __M_writer(u'              <input id="name" type="text" name="name" placeholder="')
        __M_writer(filters.decode.utf8(_("example: Jane Doe")))
        __M_writer(u'" />\n            </li>\n\n            <li class="field text required" id="field-username">\n              <label for="username">')
        __M_writer(filters.decode.utf8(_("Public Username")))
        __M_writer(u'</label>\n')
        __M_writer(u'              <input id="username" type="text" name="username" placeholder="')
        __M_writer(filters.decode.utf8(_("example: JaneDoe")))
        __M_writer(u'" />\n              <span class="tip tip-stacked">')
        __M_writer(filters.decode.utf8(_("This will be used in public discussions with your courses and in our edX101 support forums")))
        __M_writer(u'</span>\n            </li>\n\n            <li class="field text required" id="field-password">\n              <label for="password">')
        __M_writer(filters.decode.utf8(_("Password")))
        __M_writer(u'</label>\n              <input id="password" type="password" name="password" />\n              <span id="password_error" class="tip tip-error hidden" role="alert"></span>\n            </li>\n\n            <li class="field-group">\n              <div class="field text" id="field-location">\n                <label for="location">')
        __M_writer(filters.decode.utf8(_("Your Location")))
        __M_writer(u'</label>\n                <input class="short" id="location" type="text" name="location" />\n              </div>\n\n              <div class="field text" id="field-language">\n                <label for="language">')
        __M_writer(filters.decode.utf8(_("Preferred Language")))
        __M_writer(u'</label>\n                <input class="short" id="language" type="text" name="language" />\n              </div>\n            </li>\n\n            <li class="field checkbox required" id="field-tos">\n              <input id="tos" name="terms_of_service" type="checkbox" value="true" />\n              <label for="tos">\n                ')
        __M_writer(filters.decode.utf8(_("I agree to the {a_start} Terms of Service {a_end}").format(a_start='<a data-rel="edx.org" href="{}">'.format(marketing_link('TOS')), a_end="</a>")))
        __M_writer(u'\n              </label>\n            </li>\n          </ol>\n        </fieldset>\n\n        <div class="form-actions">\n          <button type="submit" id="submit" name="submit" class="action action-primary">')
        __M_writer(filters.decode.utf8(_("Create My Account &amp; Start Authoring Courses")))
        __M_writer(u'</button>\n        </div>\n\n        <!-- no honor code for CMS, but need it because we\'re using the lms student object -->\n        <input name="honor_code" type="checkbox" value="true" checked="true" hidden="true">\n      </form>\n    </article>\n\n    <aside class="content-supplementary" role="complementary">\n      <h2 class="sr">')
        __M_writer(filters.decode.utf8(_("Common {studio_name} Questions").format(studio_name=settings.STUDIO_SHORT_NAME)))
        __M_writer(u'</h2>\n\n      <div class="bit">\n        <h3 class="title-3">')
        __M_writer(filters.decode.utf8(_("Who is {studio_name} for?").format(studio_name=settings.STUDIO_SHORT_NAME)))
        __M_writer(u'</h3>\n        <p>')
        __M_writer(filters.decode.utf8(_("{studio_name} is for anyone that wants to create online courses that leverage the global {platform_name} platform. Our users are often faculty members, teaching assistants and course staff, and members of instructional technology groups.").format(
          studio_name=settings.STUDIO_SHORT_NAME, platform_name=settings.PLATFORM_NAME,
        )))
        __M_writer(u'</p>\n      </div>\n\n      <div class="bit">\n        <h3 class="title-3">')
        __M_writer(filters.decode.utf8(_("How technically savvy do I need to be to create courses in {studio_name}?").format(studio_name=settings.STUDIO_SHORT_NAME)))
        __M_writer(u'</h3>\n        <p>')
        __M_writer(filters.decode.utf8(_("{studio_name} is designed to be easy to use by almost anyone familiar with common web-based authoring environments (Wordpress, Moodle, etc.). No programming knowledge is required, but for some of the more advanced features, a technical background would be helpful. As always, we are here to help, so don't hesitate to dive right in.").format(
          studio_name=settings.STUDIO_SHORT_NAME,
        )))
        __M_writer(u'</p>\n      </div>\n\n      <div class="bit">\n        <h3 class="title-3">')
        __M_writer(filters.decode.utf8(_("I've never authored a course online before. Is there help?")))
        __M_writer(u'</h3>\n        <p>')
        __M_writer(filters.decode.utf8(_("Absolutely. We have created an online course, edX101, that describes some best practices: from filming video, creating exercises, to the basics of running an online course. Additionally, we're always here to help, just drop us a note.")))
        __M_writer(u'</p>\n      </div>\n    </aside>\n  </section>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_requirejs(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def requirejs():
            return render_requirejs(context)
        __M_writer = context.writer()
        __M_writer(u'\n    require(["js/factories/register"], function (RegisterFactory) {\n        RegisterFactory();\n    });\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyclass():
            return render_bodyclass(context)
        __M_writer = context.writer()
        __M_writer(u'not-signedin view-signup')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "register" 
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer(filters.decode.utf8(_("Sign Up")))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 93, "129": 97, "130": 97, "131": 98, "134": 100, "135": 104, "136": 104, "137": 105, "138": 105, "16": 3, "144": 112, "150": 112, "156": 9, "32": 0, "162": 9, "168": 2, "172": 2, "47": 1, "48": 2, "49": 6, "179": 8, "54": 8, "185": 8, "59": 9, "191": 185, "64": 110, "69": 116, "75": 11, "83": 11, "84": 16, "85": 16, "86": 17, "87": 17, "88": 17, "89": 17, "90": 20, "91": 20, "92": 28, "93": 28, "94": 32, "95": 32, "96": 34, "97": 34, "98": 34, "99": 38, "100": 38, "101": 40, "102": 40, "103": 40, "104": 44, "105": 44, "106": 46, "107": 46, "108": 46, "109": 47, "110": 47, "111": 51, "112": 51, "113": 58, "114": 58, "115": 63, "116": 63, "117": 71, "118": 71, "119": 78, "120": 78, "121": 87, "122": 87, "123": 90, "124": 90, "125": 91}, "uri": "register.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/register.html"}
__M_END_METADATA
"""
