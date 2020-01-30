# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284727.353126
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/courseware/course_about.html'
_template_uri = 'custome-theme/lms/templates/courseware/course_about.html'
_source_encoding = 'utf-8'
_exports = [u'course_about_important_dates', u'course_about_reviews_tool', u'course_about_header', u'course_about_details', u'pagetitle', u'js_extra', u'headextra']



from django.utils.translation import ugettext as _, get_language
from django.utils.translation import pgettext
from django.urls import reverse
from courseware.courses import get_course_about_section
from django.conf import settings
from six import text_type
from edxmako.shortcuts import marketing_link
from openedx.core.djangolib.markup import HTML
from openedx.core.lib.courses import course_image_url
from six import string_types


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'../main.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def course_about_reviews_tool():
            return render_course_about_reviews_tool(context._locals(__M_locals))
        def course_about_header():
            return render_course_about_header(context._locals(__M_locals))
        is_shib_course = context.get('is_shib_course', UNDEFINED)
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        course = context.get('course', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        unicode = context.get('unicode', UNDEFINED)
        course_target = context.get('course_target', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        professional_mode = context.get('professional_mode', UNDEFINED)
        can_enroll = context.get('can_enroll', UNDEFINED)
        studio_url = context.get('studio_url', UNDEFINED)
        course_image_urls = context.get('course_image_urls', UNDEFINED)
        invitation_only = context.get('invitation_only', UNDEFINED)
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        reviews_fragment_view = context.get('reviews_fragment_view', UNDEFINED)
        course_price = context.get('course_price', UNDEFINED)
        pre_requisite_courses = context.get('pre_requisite_courses', UNDEFINED)
        can_add_course_to_cart = context.get('can_add_course_to_cart', UNDEFINED)
        active_reg_button = context.get('active_reg_button', UNDEFINED)
        show_courseware_link = context.get('show_courseware_link', UNDEFINED)
        is_course_full = context.get('is_course_full', UNDEFINED)
        registered = context.get('registered', UNDEFINED)
        ecommerce_checkout_link = context.get('ecommerce_checkout_link', UNDEFINED)
        user = context.get('user', UNDEFINED)
        is_cosmetic_price_enabled = context.get('is_cosmetic_price_enabled', UNDEFINED)
        ecommerce_checkout = context.get('ecommerce_checkout', UNDEFINED)
        staff_access = context.get('staff_access', UNDEFINED)
        cart_link = context.get('cart_link', UNDEFINED)
        request = context.get('request', UNDEFINED)
        in_cart = context.get('in_cart', UNDEFINED)
        def course_about_details():
            return render_course_about_details(context._locals(__M_locals))
        reg_then_add_to_cart_link = context.get('reg_then_add_to_cart_link', UNDEFINED)
        def course_about_important_dates():
            return render_course_about_important_dates(context._locals(__M_locals))
        def headextra():
            return render_headextra(context._locals(__M_locals))
        sidebar_html_enabled = context.get('sidebar_html_enabled', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headextra'):
            context['self'].headextra(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer(u'\n\n<section class="course-info">\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'course_about_header'):
            context['self'].course_about_header(**pageargs)
        

        __M_writer(u'\n\n  <div class="container">\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'course_about_details'):
            context['self'].course_about_details(**pageargs)
        

        __M_writer(u'\n\n    <div class="course-sidebar">\n      <div class="course-summary">\n\n        ')
        runtime._include_file(context, u'course_about_sidebar_header.html', _template_uri)
        __M_writer(u'\n\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'course_about_important_dates'):
            context['self'].course_about_important_dates(**pageargs)
        

        __M_writer(u'\n    </div>\n\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'course_about_reviews_tool'):
            context['self'].course_about_reviews_tool(**pageargs)
        

        __M_writer(u'\n\n')
        if get_course_about_section(request, course, "ocw_links"):
            __M_writer(u'      <div class="additional-resources">\n        <header>\n          <h1>')
            __M_writer(filters.decode.utf8(_("Additional Resources")))
            __M_writer(u'</h1>\n      </div>\n\n        <div>\n')
            __M_writer(u'          <h2 class="opencourseware">MITOpenCourseware</h2>\n             ')
            __M_writer(filters.decode.utf8(get_course_about_section(request, course, "ocw_links")))
            __M_writer(u'\n        </div>\n    </div>\n')
        __M_writer(u'\n')
        if sidebar_html_enabled:
            if get_course_about_section(request, course, "about_sidebar_html"):
                __M_writer(u'        <section class="about-sidebar-html">\n          ')
                __M_writer(filters.decode.utf8(get_course_about_section(request, course, "about_sidebar_html")))
                __M_writer(u'\n        </section>\n')
        __M_writer(u'  </div>\n\n  </div>\n</div>\n\n')
        if active_reg_button or is_shib_course:
            __M_writer(u'  <div style="display: none;">\n    <form id="class_enroll_form" method="post" data-remote="true" action="')
            __M_writer(filters.decode.utf8(reverse('change_enrollment')))
            __M_writer(u'">\n      <fieldset class="enroll_fieldset">\n        <legend class="sr">')
            __M_writer(filters.decode.utf8(pgettext("self","Enroll")))
            __M_writer(u'</legend>\n        <input name="course_id" type="hidden" value="')
            __M_writer(filters.html_escape(filters.decode.utf8(course.id )))
            __M_writer(u'">\n        <input name="enrollment_action" type="hidden" value="enroll">\n      </fieldset>\n      <div class="submit">\n        <input name="submit" type="submit" value="')
            __M_writer(filters.decode.utf8(pgettext('self','enroll')))
            __M_writer(u'">\n      </div>\n    </form>\n  </div>\n')
        __M_writer(u'\n')
        runtime._include_file(context, u'../video_modal.html', _template_uri)
        __M_writer(u'\n\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n    DateUtilFactory.transform(iterationKey=".localized_datetime");\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.decode.utf8(static.require_module_async(class_name=u'DateUtilFactory',module_name=u'js/dateutil_factory')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_course_about_important_dates(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        pre_requisite_courses = context.get('pre_requisite_courses', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def course_about_important_dates():
            return render_course_about_important_dates(context)
        course = context.get('course', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        is_cosmetic_price_enabled = context.get('is_cosmetic_price_enabled', UNDEFINED)
        course_price = context.get('course_price', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        can_add_course_to_cart = context.get('can_add_course_to_cart', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n        <ol class="important-dates">\n          <li class="important-dates-item"><span class="icon fa fa-info-circle" aria-hidden="true"></span><p class="important-dates-item-title">')
        __M_writer(filters.decode.utf8(_("Course Number")))
        __M_writer(u'</p><span class="important-dates-item-text course-number">')
        __M_writer(filters.html_escape(filters.decode.utf8(course.display_number_with_default )))
        __M_writer(u'</span></li>\n')
        if not course.start_date_is_still_default:
            __M_writer(u'              ')

            course_start_date = course.advertised_start or course.start
                          
            
            __M_writer(u'\n            <li class="important-dates-item">\n              <span class="icon fa fa-calendar" aria-hidden="true"></span>\n              <p class="important-dates-item-title">')
            __M_writer(filters.decode.utf8(_("Classes Start")))
            __M_writer(u'</p>\n')
            if isinstance(course_start_date, string_types):
                __M_writer(u'                  <span class="important-dates-item-text start-date">')
                __M_writer(filters.decode.utf8(course_start_date))
                __M_writer(u'</span>\n')
            else:
                __M_writer(u'                  ')

                course_date_string = course_start_date.strftime('%Y-%m-%dT%H:%M:%S%z')
                                  
                
                __M_writer(u'\n                  <span class="important-dates-item-text start-date localized_datetime" data-language="')
                __M_writer(filters.decode.utf8(get_language()))
                __M_writer(u'" data-format="shortDate" data-datetime="')
                __M_writer(filters.decode.utf8(course_date_string))
                __M_writer(u'"></span>\n')
            __M_writer(u'            </li>\n')
        if course.end:
            __M_writer(u'                ')

            course_end_date = course.end
                            
            
            __M_writer(u'\n\n            <li class="important-dates-item">\n                <span class="icon fa fa-calendar" aria-hidden="true"></span>\n                <p class="important-dates-item-title">')
            __M_writer(filters.decode.utf8(_("Classes End")))
            __M_writer(u'</p>\n')
            if isinstance(course_end_date, string_types):
                __M_writer(u'                      <span class="important-dates-item-text final-date">')
                __M_writer(filters.decode.utf8(course_end_date))
                __M_writer(u'</span>\n')
            else:
                __M_writer(u'                    ')

                course_date_string = course_end_date.strftime('%Y-%m-%dT%H:%M:%S%z')
                                    
                
                __M_writer(u'\n                    <span class="important-dates-item-text final-date localized_datetime" data-language="')
                __M_writer(filters.decode.utf8(get_language()))
                __M_writer(u'" data-format="shortDate" data-datetime="')
                __M_writer(filters.decode.utf8(course_date_string))
                __M_writer(u'"></span>\n')
            __M_writer(u'            </li>\n')
        __M_writer(u'\n')
        if get_course_about_section(request, course, "effort"):
            __M_writer(u'            <li class="important-dates-item"><span class="icon fa fa-pencil" aria-hidden="true"></span><p class="important-dates-item-title">')
            __M_writer(filters.decode.utf8(_("Estimated Effort")))
            __M_writer(u'</p><span class="important-dates-item-text effort">')
            __M_writer(filters.decode.utf8(get_course_about_section(request, course, "effort")))
            __M_writer(u'</span></li>\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        if course_price and (can_add_course_to_cart or is_cosmetic_price_enabled):
            __M_writer(u'            <li class="important-dates-item">\n              <span class="icon fa fa-money" aria-hidden="true"></span>\n              <p class="important-dates-item-title">')
            __M_writer(filters.decode.utf8(_("Price")))
            __M_writer(u'</p>\n              <span class="important-dates-item-text">')
            __M_writer(filters.decode.utf8(course_price))
            __M_writer(u'</span>\n            </li>\n')
        __M_writer(u'\n')
        if pre_requisite_courses:
            __M_writer(u'          ')
            prc_target = reverse('about_course', args=[unicode(pre_requisite_courses[0]['key'])]) 
            
            __M_writer(u'\n          <li class="prerequisite-course important-dates-item">\n            <span class="icon fa fa-list-ul" aria-hidden="true"></span>\n            <p class="important-dates-item-title">')
            __M_writer(filters.decode.utf8(_("Prerequisites")))
            __M_writer(u'</p>\n')
            __M_writer(u'            <span class="important-dates-item-text pre-requisite"><a href="')
            __M_writer(filters.decode.utf8(prc_target))
            __M_writer(u'">')
            __M_writer(filters.decode.utf8(pre_requisite_courses[0]['display']))
            __M_writer(u'</a></span>\n            <p class="tip">\n            ')
            __M_writer(filters.decode.utf8(_("You must successfully complete {link_start}{prc_display}{link_end} before you begin this course.").format(
              link_start='<a href="{}">'.format(prc_target),
              link_end='</a>',
              prc_display=pre_requisite_courses[0]['display'],
            )))
            __M_writer(u'\n            </p>\n          </li>\n')
        __M_writer(u'\n')
        if get_course_about_section(request, course, "prerequisites"):
            __M_writer(u'            <li class="important-dates-item"><span class="icon fa fa-book" aria-hidden="true"></span><p class="important-dates-item-title">')
            __M_writer(filters.decode.utf8(_("Requirements")))
            __M_writer(u'</p><span class="important-dates-item-text prerequisites">')
            __M_writer(filters.decode.utf8(get_course_about_section(request, course, "prerequisites")))
            __M_writer(u'</span></li>\n')
        __M_writer(u'        </ol>\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_course_about_reviews_tool(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def course_about_reviews_tool():
            return render_course_about_reviews_tool(context)
        reviews_fragment_view = context.get('reviews_fragment_view', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if reviews_fragment_view:
            __M_writer(u'       ')
            __M_writer(filters.decode.utf8(HTML(reviews_fragment_view.body_html())))
            __M_writer(u'\n')
        __M_writer(u'      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_course_about_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        professional_mode = context.get('professional_mode', UNDEFINED)
        cart_link = context.get('cart_link', UNDEFINED)
        show_courseware_link = context.get('show_courseware_link', UNDEFINED)
        can_add_course_to_cart = context.get('can_add_course_to_cart', UNDEFINED)
        course = context.get('course', UNDEFINED)
        def course_about_header():
            return render_course_about_header(context)
        is_course_full = context.get('is_course_full', UNDEFINED)
        can_enroll = context.get('can_enroll', UNDEFINED)
        request = context.get('request', UNDEFINED)
        in_cart = context.get('in_cart', UNDEFINED)
        registered = context.get('registered', UNDEFINED)
        ecommerce_checkout_link = context.get('ecommerce_checkout_link', UNDEFINED)
        invitation_only = context.get('invitation_only', UNDEFINED)
        user = context.get('user', UNDEFINED)
        course_image_urls = context.get('course_image_urls', UNDEFINED)
        course_target = context.get('course_target', UNDEFINED)
        course_price = context.get('course_price', UNDEFINED)
        is_shib_course = context.get('is_shib_course', UNDEFINED)
        reg_then_add_to_cart_link = context.get('reg_then_add_to_cart_link', UNDEFINED)
        ecommerce_checkout = context.get('ecommerce_checkout', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  <header class="course-profile course-profile-promo-box">\n    <div class="holder course-profile-wrapper">\n\n')
        if get_course_about_section(request, course, "video"):
            __M_writer(u'      <a href="#video-modal" class="media" rel="leanModal">\n        <div class="hero">\n          <img src="')
            __M_writer(filters.decode.utf8(course_image_urls['large']))
            __M_writer(u'" alt="" />\n          <div class="play-intro"></div>\n        </div>\n      </a>\n')
        else:
            __M_writer(u'          <img src="')
            __M_writer(filters.decode.utf8(course_image_urls['large']))
            __M_writer(u'" alt="" class="course-profile_img"/>\n')
        __M_writer(u'\n        <section class="intro">\n          <div class="heading-group">\n            <h1>\n              ')
        __M_writer(filters.decode.utf8(course.display_name_with_default_escaped))
        __M_writer(u'\n            </h1>\n            <br />\n            <span>')
        __M_writer(filters.html_escape(filters.decode.utf8(course.display_org_with_default )))
        __M_writer(u'</span>\n          </div>\n\n          <div class="main-cta">\n')
        if user.is_authenticated and registered:
            if show_courseware_link:
                __M_writer(u'              <a href="')
                __M_writer(filters.decode.utf8(course_target))
                __M_writer(u'">\n')
            __M_writer(u'\n            <span class="register disabled">')
            __M_writer(filters.decode.utf8(_("You are enrolled in this course")))
            __M_writer(u'</span>\n\n')
            if show_courseware_link:
                __M_writer(u'              <strong>')
                __M_writer(filters.decode.utf8(_("View Course")))
                __M_writer(u'</strong>\n              </a>\n')
            __M_writer(u'\n')
        elif in_cart:
            __M_writer(u'            <span class="add-to-cart">\n              ')
            __M_writer(filters.decode.utf8(_('This course is in your <a href="{cart_link}">cart</a>.').format(cart_link=cart_link)))
            __M_writer(u'\n            </span>\n')
        elif is_course_full:
            __M_writer(u'            <span class="register disabled">\n              ')
            __M_writer(filters.decode.utf8(_("Course is full")))
            __M_writer(u'\n            </span>\n')
        elif invitation_only and not can_enroll:
            __M_writer(u'            <span class="register disabled">')
            __M_writer(filters.decode.utf8(_("Enrollment in this course is by invitation only")))
            __M_writer(u'</span>\n')
        elif not is_shib_course and not can_enroll:
            __M_writer(u'            <span class="register disabled">')
            __M_writer(filters.decode.utf8(_("Enrollment is Closed")))
            __M_writer(u'</span>\n')
        elif can_add_course_to_cart:
            __M_writer(u'            ')

            if user.is_authenticated:
              reg_href = "#"
              reg_element_id = "add_to_cart_post"
            else:
              reg_href = reg_then_add_to_cart_link
              reg_element_id = "reg_then_add_to_cart"
            
            
            __M_writer(u'\n            ')
            if ecommerce_checkout:
                           reg_href = ecommerce_checkout_link
                           reg_element_id = ""
                       
            
            __M_writer(u'\n            <a href="')
            __M_writer(filters.decode.utf8(reg_href))
            __M_writer(u'" class="add-to-cart" id="')
            __M_writer(filters.decode.utf8(reg_element_id))
            __M_writer(u'">\n              ')
            __M_writer(filters.decode.utf8(_("Add {course_name} to Cart <span>({price} USD)</span>")\
                .format(course_name=course.display_number_with_default, price=course_price)))
            __M_writer(u'\n            </a>\n            <div id="register_error"></div>\n')
        else:
            __M_writer(u'            ')

            if ecommerce_checkout:
              reg_href = ecommerce_checkout_link
            else:
              reg_href="#"
            if professional_mode:
              href_class = "add-to-cart"
            else:
              href_class = "register"
                        
            
            __M_writer(u'\n            <a href="')
            __M_writer(filters.decode.utf8(reg_href))
            __M_writer(u'" class="')
            __M_writer(filters.decode.utf8(href_class))
            __M_writer(u'">\n              ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Enroll in {course_name}").format(course_name=course.display_number_with_default) )))
            __M_writer(u'\n            </a>\n            <div id="register_error"></div>\n')
        __M_writer(u'          </div>\n\n        </section>\n    </div>\n  </header>\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_course_about_details(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        course = context.get('course', UNDEFINED)
        request = context.get('request', UNDEFINED)
        studio_url = context.get('studio_url', UNDEFINED)
        def course_about_details():
            return render_course_about_details(context)
        staff_access = context.get('staff_access', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="details">\n')
        if staff_access and studio_url is not None:
            __M_writer(u'        <div class="wrap-instructor-info studio-view">\n          <a class="instructor-info-action" href="')
            __M_writer(filters.decode.utf8(studio_url))
            __M_writer(u'">')
            __M_writer(filters.decode.utf8(_("View About Page in studio")))
            __M_writer(u'</a>\n        </div>\n')
        __M_writer(u'\n      <div class="inner-wrapper">\n        ')
        __M_writer(filters.decode.utf8(get_course_about_section(request, course, "overview")))
        __M_writer(u'\n      </div>\n    </div>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagetitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pagetitle():
            return render_pagetitle(context)
        course = context.get('course', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(filters.decode.utf8(course.display_name_with_default_escaped))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cart_link = context.get('cart_link', UNDEFINED)
        can_add_course_to_cart = context.get('can_add_course_to_cart', UNDEFINED)
        course = context.get('course', UNDEFINED)
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        reg_then_add_to_cart_link = context.get('reg_then_add_to_cart_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  <script type="text/javascript">\n  (function() {\n    $(".register").click(function(event) {\n      $("#class_enroll_form").submit();\n      event.preventDefault();\n    });\n\n')
        if can_add_course_to_cart:
            __M_writer(u'      add_course_complete_handler = function(jqXHR, textStatus) {\n        if (jqXHR.status == 200) {\n          location.href = "')
            __M_writer(filters.decode.utf8(cart_link))
            __M_writer(u'";\n        }\n        if (jqXHR.status == 400) {\n          $("#register_error")\n            .html(jqXHR.responseText ? jqXHR.responseText : "')
            __M_writer(filters.decode.utf8(_("An error occurred. Please try again later.")))
            __M_writer(u'")\n            .css("display", "block");\n        }\n        else if (jqXHR.status == 403) {\n            location.href = "')
            __M_writer(filters.decode.utf8(reg_then_add_to_cart_link))
            __M_writer(u'";\n        }\n      };\n\n      $("#add_to_cart_post").click(function(event){\n        $.ajax({\n          url: "')
            __M_writer(filters.decode.utf8(reverse('add_course_to_cart', args=[text_type(course.id)])))
            __M_writer(u'",\n          type: "POST",\n          /* Rant: HAD TO USE COMPLETE B/C PROMISE.DONE FOR SOME REASON DOES NOT WORK ON THIS PAGE. */\n          complete: add_course_complete_handler\n        })\n        event.preventDefault();\n      });\n')
        __M_writer(u'\n')
        if settings.FEATURES.get('RESTRICT_ENROLL_BY_REG_METHOD') and course.enrollment_domain:
            __M_writer(u'      ')

            perms_error = _('The currently logged-in user account does not have permission to enroll in this course. '
                            'You may need to {start_logout_tag}log out{end_tag} then try the enroll button again. '
                            'Please visit the {start_help_tag}help page{end_tag} for a possible solution.').format(
                              start_help_tag="<a href='{url}'>".format(url=marketing_link('FAQ')), end_tag='</a>',
                              start_logout_tag="<a href='{url}'>".format(url=reverse('logout'))
                              )
                  
            
            __M_writer(u'\n    $(\'#class_enroll_form\').on(\'ajax:complete\', function(event, xhr) {\n      if(xhr.status == 200) {\n        location.href = "')
            __M_writer(filters.decode.utf8(reverse('dashboard')))
            __M_writer(u'";\n      } else if (xhr.status == 403) {\n        location.href = "')
            __M_writer(filters.decode.utf8(reverse('course-specific-register', args=[text_type(course.id)])))
            __M_writer(u'?course_id=')
            __M_writer(filters.url_escape(filters.decode.utf8(course.id )))
            __M_writer(u'&enrollment_action=enroll";\n      } else if (xhr.status == 400) { //This means the user did not have permission\n        $(\'#register_error\').html("')
            __M_writer(filters.decode.utf8(perms_error))
            __M_writer(u'").css("display", "block");\n      } else {\n        $(\'#register_error\').html(\n            (xhr.responseText ? xhr.responseText : "')
            __M_writer(filters.decode.utf8(_("An error occurred. Please try again later.")))
            __M_writer(u'")\n        ).css("display", "block");\n      }\n    });\n\n')
        else:
            __M_writer(u'\n    $(\'#class_enroll_form\').on(\'ajax:complete\', function(event, xhr) {\n      if(xhr.status == 200) {\n        if (xhr.responseText == "") {\n          location.href = "')
            __M_writer(filters.decode.utf8(reverse('dashboard')))
            __M_writer(u'";\n        }\n        else {\n          location.href = xhr.responseText;\n        }\n      } else if (xhr.status == 403) {\n          location.href = "')
            __M_writer(filters.decode.utf8(reverse('register_user')))
            __M_writer(u'?course_id=')
            __M_writer(filters.url_escape(filters.decode.utf8(course.id )))
            __M_writer(u'&enrollment_action=enroll";\n      } else {\n        $(\'#register_error\').html(\n            (xhr.responseText ? xhr.responseText : "')
            __M_writer(filters.decode.utf8(_("An error occurred. Please try again later.")))
            __M_writer(u'")\n        ).css("display", "block");\n      }\n    });\n\n')
        __M_writer(u'\n  })(this)\n  </script>\n\n  <script src="')
        __M_writer(filters.decode.utf8(static.url('js/course_info.js')))
        __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headextra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headextra():
            return render_headextra(context)
        request = context.get('request', UNDEFINED)
        course = context.get('course', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'  <meta property="og:title" content="')
        __M_writer(filters.decode.utf8(course.display_name_with_default_escaped))
        __M_writer(u'" />\n  <meta property="og:description" content="')
        __M_writer(filters.decode.utf8(get_course_about_section(request, course, 'short_description')))
        __M_writer(u'" />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"512": 86, "513": 86, "514": 92, "515": 92, "516": 92, "517": 92, "518": 95, "519": 95, "520": 101, "521": 105, "522": 105, "16": 2, "536": 16, "537": 19, "538": 19, "539": 19, "540": 20, "541": 20, "547": 541, "36": 1, "42": 0, "90": 1, "91": 13, "92": 15, "97": 21, "102": 106, "107": 108, "112": 203, "117": 219, "118": 224, "119": 224, "124": 302, "129": 310, "130": 313, "131": 314, "132": 316, "133": 316, "134": 321, "135": 322, "136": 322, "137": 326, "138": 327, "139": 328, "140": 329, "141": 330, "142": 330, "143": 334, "144": 342, "145": 343, "146": 344, "147": 344, "148": 346, "149": 346, "150": 347, "151": 347, "152": 351, "153": 351, "154": 356, "155": 357, "156": 357, "160": 359, "165": 359, "168": 361, "174": 226, "188": 226, "189": 228, "190": 228, "191": 228, "192": 228, "193": 229, "194": 230, "195": 230, "199": 232, "200": 235, "201": 235, "202": 236, "203": 237, "204": 237, "205": 237, "206": 238, "207": 239, "208": 239, "212": 241, "213": 242, "214": 242, "215": 242, "216": 242, "217": 244, "218": 248, "219": 249, "220": 249, "224": 251, "225": 255, "226": 255, "227": 256, "228": 257, "229": 257, "230": 257, "231": 258, "232": 259, "233": 259, "237": 261, "238": 262, "239": 262, "240": 262, "241": 262, "242": 264, "243": 266, "244": 267, "245": 268, "246": 268, "247": 268, "248": 268, "249": 268, "250": 270, "251": 272, "252": 273, "253": 274, "254": 276, "255": 276, "256": 277, "257": 277, "258": 280, "259": 281, "260": 282, "261": 282, "263": 282, "264": 285, "265": 285, "266": 287, "267": 287, "268": 287, "269": 287, "270": 287, "271": 289, "276": 293, "277": 297, "278": 298, "279": 299, "280": 299, "281": 299, "282": 299, "283": 299, "284": 301, "290": 305, "297": 305, "298": 307, "299": 308, "300": 308, "301": 308, "302": 310, "308": 112, "333": 112, "334": 116, "335": 117, "336": 119, "337": 119, "338": 123, "339": 124, "340": 124, "341": 124, "342": 126, "343": 130, "344": 130, "345": 133, "346": 133, "347": 137, "348": 138, "349": 139, "350": 139, "351": 139, "352": 141, "353": 142, "354": 142, "355": 144, "356": 145, "357": 145, "358": 145, "359": 148, "360": 149, "361": 150, "362": 151, "363": 151, "364": 153, "365": 154, "366": 155, "367": 155, "368": 157, "369": 158, "370": 158, "371": 158, "372": 162, "373": 163, "374": 163, "375": 163, "376": 164, "377": 165, "378": 165, "387": 172, "388": 173, "393": 176, "394": 177, "395": 177, "396": 177, "397": 177, "398": 178, "400": 179, "401": 182, "402": 183, "403": 183, "414": 192, "415": 193, "416": 193, "417": 193, "418": 193, "419": 194, "420": 194, "421": 198, "427": 207, "437": 207, "438": 209, "439": 210, "440": 211, "441": 211, "442": 211, "443": 211, "444": 214, "445": 216, "446": 216, "452": 108, "459": 108, "528": 16, "465": 23, "476": 23, "477": 31, "478": 32, "479": 34, "480": 34, "481": 38, "482": 38, "483": 42, "484": 42, "485": 48, "486": 48, "487": 56, "488": 58, "489": 59, "490": 59, "499": 66, "500": 69, "501": 69, "502": 71, "503": 71, "504": 71, "505": 71, "506": 73, "507": 73, "508": 76, "509": 76, "510": 81, "511": 82}, "uri": "custome-theme/lms/templates/courseware/course_about.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/courseware/course_about.html"}
__M_END_METADATA
"""
