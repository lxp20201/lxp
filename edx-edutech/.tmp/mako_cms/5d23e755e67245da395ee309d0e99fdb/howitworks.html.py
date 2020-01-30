# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580361385.65219
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/howitworks.html'
_template_uri = 'howitworks.html'
_source_encoding = 'utf-8'
_exports = [u'content', u'bodyclass', 'online_help_token', u'title']



from django.urls import reverse
from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        settings = context.get('settings', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
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
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        static = _mako_get_namespace(context, 'static')
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n<div class="wrapper-content-header wrapper">\n  <section class="content content-header">\n    <header>\n      <h1><span class="wrapper-text-welcome">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Welcome to {studio_name}").format(
          studio_name=settings.STUDIO_NAME
      ))))
        __M_writer(u'</span></h1>\n      <p class="tagline">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("{studio_name} helps manage your online courses, so you can focus on teaching them").format(
        studio_name=settings.STUDIO_SHORT_NAME
      ))))
        __M_writer(u'</p>\n    </header>\n  </section>\n</div>\n\n<div class="wrapper-content-features wrapper">\n  <section class="content content-features">\n    <header>\n      <h2 class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("{studio_name}'s Many Features").format(studio_name=settings.STUDIO_SHORT_NAME))))
        __M_writer(u'</h2>\n    </header>\n\n    <ol class="list-features">\n      <li class="feature">\n        <figure class="img zoom">\n          <a rel="modal" href="#hiw-feature1">\n            <img src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url("images/thumb-hiw-feature1.png"))))
        __M_writer(u'" alt="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('{studio_name} Helps You Keep Your Courses Organized').format(studio_name=settings.STUDIO_SHORT_NAME))))
        __M_writer(u'" />\n            <figcaption class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("{studio_name} Helps You Keep Your Courses Organized").format(studio_name=settings.STUDIO_NAME))))
        __M_writer(u'</figcaption>\n            <span class="action-zoom">\n              <span class="icon fa fa-search-plus" aria-hidden="true"></span><span class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Enlarge image"))))
        __M_writer(u'</span>\n            </span>\n          </a>\n        </figure>\n\n        <div class="copy">\n          <h3>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Keeping Your Course Organized"))))
        __M_writer(u'</h3>\n          <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("The backbone of your course is how it is organized. {studio_name} offers an {strong_start}Outline{strong_end} editor, providing a simple hierarchy and easy drag and drop to help you and your students stay organized.")).format(
                  studio_name=settings.STUDIO_SHORT_NAME,
                  strong_start=HTML('<strong>'),
                  strong_end=HTML('</strong>')
              ))))
        __M_writer(u'</p>\n\n          <ul class="list-proofpoints">\n            <li class="proofpoint">\n              <h4 class="title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Simple Organization For Content"))))
        __M_writer(u'</h4>\n              <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("{studio_name} uses a simple hierarchy of {strong_start}sections{strong_end} and {strong_start}subsections{strong_end} to organize your content.")).format(
                    studio_name=settings.STUDIO_SHORT_NAME,
                    strong_start=HTML('<strong>'),
                    strong_end=HTML('</strong>')
                  ))))
        __M_writer(u'</p>\n            </li>\n\n            <li class="proofpoint">\n              <h4 class="title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Change Your Mind Anytime"))))
        __M_writer(u'</h4>\n              <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Draft your outline and build content anywhere. Simple drag and drop tools let you reorganize quickly."))))
        __M_writer(u'</p>\n            </li>\n\n            <li class="proofpoint">\n              <h4 class="title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Go A Week Or A Semester At A Time"))))
        __M_writer(u'</h4>\n              <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("Build and release {strong_start}sections{strong_end} to your students incrementally. You don't have to have it all done at once.")).format(
                    strong_start=HTML('<strong>'),
                    strong_end=HTML('</strong>')
                  ))))
        __M_writer(u'</p>\n            </li>\n          </ul>\n        </div>\n      </li>\n\n      <li class="feature">\n        <figure class="img zoom">\n        <a rel="modal" href="#hiw-feature2">\n          <img src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url("images/thumb-hiw-feature2.png"))))
        __M_writer(u'" alt="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Learning is More than Just Lectures'))))
        __M_writer(u'" />\n          <figcaption class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Learning is More than Just Lectures"))))
        __M_writer(u'</figcaption>\n          <span class="action-zoom">\n            <span class="icon fa fa-search-plus" aria-hidden="true"></span><span class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Enlarge image"))))
        __M_writer(u'</span>\n          </span>\n        </a>\n        </figure>\n\n        <div class="copy">\n          <h3>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Learning is More than Just Lectures"))))
        __M_writer(u'</h3>\n          <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("{studio_name} lets you weave your content together in a way that reinforces learning. Insert videos, discussions, and a wide variety of exercises with just a few clicks.").format(studio_name=settings.STUDIO_SHORT_NAME))))
        __M_writer(u' </p>\n\n          <ul class="list-proofpoints">\n            <li class="proofpoint">\n              <h4 class="title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Create Learning Pathways"))))
        __M_writer(u'</h4>\n              <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Help your students understand one concept at a time with multimedia, HTML, and exercises."))))
        __M_writer(u'</p>\n            </li>\n\n            <li class="proofpoint">\n              <h4 class="title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Work Visually, Organize Quickly"))))
        __M_writer(u'</h4>\n              <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Work visually and see exactly what your students will see. Reorganize all your content with drag and drop."))))
        __M_writer(u'</p>\n            </li>\n\n            <li class="proofpoint">\n              <h4 class="title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("A Broad Library of Problem Types"))))
        __M_writer(u'</h4>\n              <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("It's more than just multiple choice. {studio_name} supports more than a dozen types of problems to challenge your learners.").format(studio_name=settings.STUDIO_SHORT_NAME))))
        __M_writer(u'</p>\n            </li>\n          </ul>\n        </div>\n      </li>\n\n      <li class="feature">\n        <figure class="img zoom">\n          <a rel="modal" href="#hiw-feature3">\n            <img src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url("images/thumb-hiw-feature3.png"))))
        __M_writer(u'" alt="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('{studio_name} Gives You Simple, Fast, and Incremental Publishing. With Friends.').format(studio_name=settings.STUDIO_SHORT_NAME))))
        __M_writer(u'" />\n            <figcaption class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("{studio_name} Gives You Simple, Fast, and Incremental Publishing. With Friends.").format(studio_name=settings.STUDIO_SHORT_NAME))))
        __M_writer(u'</figcaption>\n            <span class="action-zoom">\n              <span class="icon fa fa-search-plus" aria-hidden="true"></span><span class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Enlarge image"))))
        __M_writer(u'</span>\n            </span>\n          </a>\n        </figure>\n\n        <div class="copy">\n          <h3>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Simple, Fast, and Incremental Publishing. With Friends."))))
        __M_writer(u'</h3>\n          <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("{studio_name} works like web applications you already know, yet understands how you build curriculum. Instant publishing to the web when you want it, incremental release when it makes sense. And with co-authors, you can have a whole team building a course, together.").format(studio_name=settings.STUDIO_SHORT_NAME))))
        __M_writer(u'</p>\n\n          <ul class="list-proofpoints">\n            <li class="proofpoint">\n              <h4 class="title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Instant Changes"))))
        __M_writer(u'</h4>\n              <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Caught a bug? No problem. When you want, your changes go live when you click Save."))))
        __M_writer(u'</p>\n            </li>\n\n            <li class="proofpoint">\n              <h4 class="title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Release-On Date Publishing"))))
        __M_writer(u'</h4>\n              <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("When you've finished a {strong_start}section{strong_end}, pick when you want it to go live and {studio_name} takes care of the rest. Build your course incrementally.")).format(
                      studio_name=settings.STUDIO_SHORT_NAME,
                      strong_start=HTML('<strong>'),
                      strong_end=HTML('</strong>')
                  ))))
        __M_writer(u'</p>\n            </li>\n\n            <li class="proofpoint">\n              <h4 class="title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Work in Teams"))))
        __M_writer(u'</h4>\n              <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Co-authors have full access to all the same authoring tools. Make your course better through a team effort."))))
        __M_writer(u'</p>\n            </li>\n          </ul>\n        </div>\n      </li>\n    </ol>\n  </section>\n</div>\n\n<div class="wrapper-content-cta wrapper">\n  <section class="content content-cta">\n    <header>\n      <h2 class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Sign Up for {studio_name} Today!").format(studio_name=settings.STUDIO_SHORT_NAME))))
        __M_writer(u'</h2>\n    </header>\n\n    <ul class="list-actions">\n      <li class="action-item">\n        <a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(reverse('signup'))))
        __M_writer(u'" class="action action-primary">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Sign Up & Start Making Your {platform_name} Course").format(platform_name=settings.PLATFORM_NAME))))
        __M_writer(u'</a>\n      </li>\n      <li class="action-item">\n        <a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(reverse('login'))))
        __M_writer(u'" class="action action-secondary">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Already have a {studio_name} Account? Sign In").format(studio_name=settings.STUDIO_SHORT_NAME))))
        __M_writer(u'</a>\n      </li>\n    </ul>\n  </section>\n</div>\n\n<div class="content-modal" id="hiw-feature1">\n  <h3 class="title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Outlining Your Course"))))
        __M_writer(u'</h3>\n  <figure>\n    <img src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url("images/hiw-feature1.png"))))
        __M_writer(u'" alt="" />\n    <figcaption class="description">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Simple two-level outline to organize your course. Drag and drop, and see your course at a glance."))))
        __M_writer(u'</figcaption>\n  </figure>\n\n  <a href="" rel="view" class="action action-modal-close">\n    <span class="icon fa fa-times-circle" aria-hidden="true"></span>\n    <span class="label">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("close modal"))))
        __M_writer(u'</span>\n  </a>\n</div>\n\n<div class="content-modal" id="hiw-feature2">\n  <h3 class="title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("More than Just Lectures"))))
        __M_writer(u'</h3>\n  <figure>\n    <img src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url("images/hiw-feature2.png"))))
        __M_writer(u'" alt="" />\n    <figcaption class="description">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Quickly create videos, text snippets, inline discussions, and a variety of problem types."))))
        __M_writer(u'</figcaption>\n  </figure>\n\n  <a href="" rel="view" class="action action-modal-close">\n    <span class="icon fa fa-times-circle" aria-hidden="true"></span>\n    <span class="label">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("close modal"))))
        __M_writer(u'</span>\n  </a>\n</div>\n\n<div class="content-modal" id="hiw-feature3">\n  <h3 class="title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Publishing on Date"))))
        __M_writer(u'</h3>\n  <figure>\n    <img src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url("images/hiw-feature3.png"))))
        __M_writer(u'" alt="" />\n    <figcaption class="description">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Simply set the date of a section or subsection, and {studio_name} will publish it to your students for you.").format(studio_name=settings.STUDIO_SHORT_NAME))))
        __M_writer(u'</figcaption>\n  </figure>\n\n  <a href="" rel="view" class="action action-modal-close">\n    <span class="icon fa fa-times-circle" aria-hidden="true"></span>\n    <span class="label">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("close modal"))))
        __M_writer(u'</span>\n  </a>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyclass():
            return render_bodyclass(context)
        __M_writer = context.writer()
        __M_writer(u'not-signedin index view-howitworks')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "welcome" 
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(filters.decode.utf8(_("Welcome"))))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 5, "29": 4, "35": 1, "48": 1, "49": 2, "50": 3, "51": 4, "52": 9, "57": 11, "62": 12, "67": 211, "73": 14, "81": 14, "82": 19, "85": 21, "86": 22, "89": 24, "90": 32, "91": 32, "92": 39, "93": 39, "94": 39, "95": 39, "96": 40, "97": 40, "98": 42, "99": 42, "100": 48, "101": 48, "102": 49, "107": 53, "108": 57, "109": 57, "110": 58, "115": 62, "116": 66, "117": 66, "118": 67, "119": 67, "120": 71, "121": 71, "122": 72, "126": 75, "127": 84, "128": 84, "129": 84, "130": 84, "131": 85, "132": 85, "133": 87, "134": 87, "135": 93, "136": 93, "137": 94, "138": 94, "139": 98, "140": 98, "141": 99, "142": 99, "143": 103, "144": 103, "145": 104, "146": 104, "147": 108, "148": 108, "149": 109, "150": 109, "151": 118, "152": 118, "153": 118, "154": 118, "155": 119, "156": 119, "157": 121, "158": 121, "159": 127, "160": 127, "161": 128, "162": 128, "163": 132, "164": 132, "165": 133, "166": 133, "167": 137, "168": 137, "169": 138, "174": 142, "175": 146, "176": 146, "177": 147, "178": 147, "179": 159, "180": 159, "181": 164, "182": 164, "183": 164, "184": 164, "185": 167, "186": 167, "187": 167, "188": 167, "189": 174, "190": 174, "191": 176, "192": 176, "193": 177, "194": 177, "195": 182, "196": 182, "197": 187, "198": 187, "199": 189, "200": 189, "201": 190, "202": 190, "203": 195, "204": 195, "205": 200, "206": 200, "207": 202, "208": 202, "209": 203, "210": 203, "211": 208, "212": 208, "218": 12, "224": 12, "230": 3, "234": 3, "241": 11, "247": 11, "253": 247}, "uri": "howitworks.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/howitworks.html"}
__M_END_METADATA
"""
