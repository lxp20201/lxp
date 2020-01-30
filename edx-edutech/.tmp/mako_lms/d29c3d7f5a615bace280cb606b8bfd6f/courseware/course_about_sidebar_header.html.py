# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284727.578865
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/courseware/course_about_sidebar_header.html'
_template_uri = u'courseware/course_about_sidebar_header.html'
_source_encoding = 'utf-8'
_exports = []



import urllib

from django.utils.translation import ugettext as _
from django.urls import reverse
from django.conf import settings
from six import text_type


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
        course = context.get('course', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<header>\n')
        if static.get_value('course_about_show_social_links', True):
            __M_writer(u'  <div class="social-sharing">\n    <div class="sharing-message">')
            __M_writer(filters.decode.utf8(_("Share with friends and family!")))
            __M_writer(u'</div>\n')
            __M_writer(u'      ')

            site_domain = static.get_value('site_domain', settings.SITE_NAME)
            site_protocol = 'https' if settings.HTTPS == 'on' else 'http'
            platform_name = static.get_platform_name()
            
            ## Translators: This text will be automatically posted to the student's
            ## Twitter account. {url} should appear at the end of the text.
            tweet_text = _("I just enrolled in {number} {title} through {account}: {url}").format(
                number=course.number,
                title=course.display_name_with_default_escaped,
                account=static.get_value('course_about_twitter_account', settings.PLATFORM_TWITTER_ACCOUNT),
                url=u"{protocol}://{domain}{path}".format(
                    protocol=site_protocol,
                    domain=site_domain,
                    path=urllib.quote_plus(
                        reverse('about_course', args=[text_type(course.id)])
                    )
                )
            ).replace(u" ", u"+")
            tweet_action = u"http://twitter.com/intent/tweet?text={tweet_text}".format(tweet_text=tweet_text)
            
            facebook_link = static.get_value('course_about_facebook_link', settings.PLATFORM_FACEBOOK_ACCOUNT)
            
            email_subject = u"mailto:?subject={subject}&body={body}".format(
                subject=_("Take a course with {platform} online").format(platform=platform_name),
                body=_("I just enrolled in {number} {title} through {platform} {url}").format(
                    number=course.number,
                    title=course.display_name_with_default_escaped,
                    platform=platform_name,
                    url=u"{protocol}://{domain}{path}".format(
                        protocol=site_protocol,
                        domain=site_domain,
                        path=urllib.quote_plus(
                            reverse('about_course', args=[text_type(course.id)]),
                        )
                    )
                )
            ).replace(u" ", u"%20")
                  
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['site_domain','facebook_link','tweet_text','platform_name','email_subject','site_protocol','tweet_action'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n      <a href="')
            __M_writer(filters.decode.utf8(tweet_action))
            __M_writer(u'" class="share">\n        <span class="icon fa fa-twitter" aria-hidden="true"></span><span class="sr">')
            __M_writer(filters.decode.utf8(_("Tweet that you've enrolled in this course")))
            __M_writer(u'</span>\n      </a>\n      <a href="')
            __M_writer(filters.decode.utf8(facebook_link))
            __M_writer(u'" class="share">\n        <span class="icon fa fa-thumbs-up" aria-hidden="true"></span><span class="sr">')
            __M_writer(filters.decode.utf8(_("Post a Facebook message to say you've enrolled in this course")))
            __M_writer(u'</span>\n      </a>\n      <a href="')
            __M_writer(filters.decode.utf8(email_subject))
            __M_writer(u'" class="share">\n        <span class="icon fa fa-envelope" aria-hidden="true"></span><span class="sr">')
            __M_writer(filters.decode.utf8(_("Email someone to say you've enrolled in this course")))
            __M_writer(u'</span>\n      </a>\n  </div>\n')
        __M_writer(u'</header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "32": 1, "35": 0, "42": 1, "43": 9, "44": 12, "45": 13, "46": 14, "47": 14, "48": 18, "49": 18, "91": 56, "92": 57, "93": 57, "94": 58, "95": 58, "96": 60, "97": 60, "98": 61, "99": 61, "100": 63, "101": 63, "102": 64, "103": 64, "104": 68, "110": 104}, "uri": "courseware/course_about_sidebar_header.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/courseware/course_about_sidebar_header.html"}
__M_END_METADATA
"""
