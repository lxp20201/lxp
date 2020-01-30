# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284734.09132
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/dashboard/_dashboard_course_listing.html'
_template_uri = u'dashboard/_dashboard_course_listing.html'
_source_encoding = 'utf-8'
_exports = []



import urllib

from django.utils.translation import ugettext as _
from django.utils.translation import ungettext
from django.urls import reverse
from course_modes.models import CourseMode
from course_modes.helpers import enrollment_mode_display
from openedx.core.djangolib.js_utils import dump_js_escaped_json, js_escaped_string
from openedx.core.djangolib.markup import HTML, Text
from openedx.features.course_experience import course_home_url_name
from student.helpers import (
  VERIFY_STATUS_NEED_TO_VERIFY,
  VERIFY_STATUS_SUBMITTED,
  VERIFY_STATUS_RESUBMITTED,
  VERIFY_STATUS_APPROVED,
  VERIFY_STATUS_MISSED_DEADLINE,
  VERIFY_STATUS_NEED_TO_REVERIFY,
  DISABLE_UNENROLL_CERT_STATES,
)
from util.course import get_link_for_about_page, get_encoded_course_sharing_utm_params


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,course_overview,enrollment,entitlement,entitlement_session,course_card_index,is_unfulfilled_entitlement,is_fulfilled_entitlement,entitlement_available_sessions,entitlement_expiration_date,entitlement_expired_at,show_courseware_link,cert_status,can_refund_entitlement,can_unenroll,credit_status,show_email_settings,course_mode_info,is_paid_course,is_course_blocked,verification_status,course_requirements,dashboard_index,share_settings,related_programs,display_course_modes_on_dashboard,show_consent_link,enterprise_customer_name,resume_button_url,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(course_overview=course_overview,enterprise_customer_name=enterprise_customer_name,is_course_blocked=is_course_blocked,pageargs=pageargs,course_card_index=course_card_index,is_unfulfilled_entitlement=is_unfulfilled_entitlement,entitlement_session=entitlement_session,can_unenroll=can_unenroll,course_requirements=course_requirements,entitlement=entitlement,related_programs=related_programs,credit_status=credit_status,is_paid_course=is_paid_course,share_settings=share_settings,can_refund_entitlement=can_refund_entitlement,display_course_modes_on_dashboard=display_course_modes_on_dashboard,verification_status=verification_status,resume_button_url=resume_button_url,show_courseware_link=show_courseware_link,entitlement_available_sessions=entitlement_available_sessions,cert_status=cert_status,show_email_settings=show_email_settings,is_fulfilled_entitlement=is_fulfilled_entitlement,show_consent_link=show_consent_link,enrollment=enrollment,entitlement_expired_at=entitlement_expired_at,dashboard_index=dashboard_index,entitlement_expiration_date=entitlement_expiration_date,course_mode_info=course_mode_info)
        user_timezone = context.get('user_timezone', UNDEFINED)
        basestring = context.get('basestring', UNDEFINED)
        course_optouts = context.get('course_optouts', UNDEFINED)
        marketing_link = context.get('marketing_link', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        use_ecommerce_payment_flow = context.get('use_ecommerce_payment_flow', UNDEFINED)
        ecommerce_payment_page = context.get('ecommerce_payment_page', UNDEFINED)
        user_language = context.get('user_language', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        user = context.get('user', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        endif = context.get('endif', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')

        reverify_link = reverse('verify_student_reverify')
        cert_name_short = course_overview.cert_name_short
        if cert_name_short == "":
          cert_name_short = settings.CERT_NAME_SHORT
        
        cert_name_long = course_overview.cert_name_long
        if cert_name_long == "":
          cert_name_long = settings.CERT_NAME_LONG
        billing_email = settings.PAYMENT_SUPPORT_EMAIL
        
        is_course_expired = hasattr(show_courseware_link, 'error_code') and show_courseware_link.error_code == 'audit_expired'
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['billing_email','cert_name_long','cert_name_short','reverify_link','is_course_expired'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<li class="course-item">\n')
        if display_course_modes_on_dashboard:
            __M_writer(u'    ')

            course_verified_certs = enrollment_mode_display(
                enrollment.mode,
                verification_status.get('status'),
                course_overview.id
            )
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['course_verified_certs'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n    ')

            mode_class = course_verified_certs.get('display_mode', '')
            if mode_class:
                mode_class = ' ' + mode_class ;
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mode_class'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        else:
            __M_writer(u'    ')
            mode_class = '' 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mode_class'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        __M_writer(u'      <div class="course-container"\n')
        if getattr(course_overview, 'language'):
            __M_writer(u'          lang="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_overview.language)))
            __M_writer(u'"\n')
        __M_writer(u'      >\n<article class="course')
        __M_writer(filters.html_escape(filters.decode.utf8(mode_class)))
        __M_writer(u'" aria-labelledby="course-title-')
        __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
        __M_writer(u'" id="course-card-')
        __M_writer(filters.html_escape(filters.decode.utf8(course_card_index)))
        __M_writer(u'">\n  ')
        course_target = reverse(course_home_url_name(course_overview.id), args=[unicode(course_overview.id)]) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['course_target'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n  <section class="details" aria-labelledby="details-heading-')
        __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
        __M_writer(u'">\n      <h2 class="hd hd-2 sr" id="details-heading-')
        __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
        __M_writer(u'">')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Course details'))))
        __M_writer(u'</h2>\n    <div class="wrapper-course-image" aria-hidden="true">\n')
        if show_courseware_link and not is_unfulfilled_entitlement:
            if not is_course_blocked and not is_course_expired:
                __M_writer(u'            <a href="')
                __M_writer(filters.html_escape(filters.decode.utf8(course_target)))
                __M_writer(u'" data-course-key="')
                __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
                __M_writer(u'" class="cover course-target-link" tabindex="-1">\n              <img src="')
                __M_writer(filters.html_escape(filters.decode.utf8(course_overview.image_urls['small'])))
                __M_writer(u'" class="course-image" alt="')
                __M_writer(filters.html_escape(filters.decode.utf8(_('{course_number} {course_name} Home Page').format(course_number=course_overview.number, course_name=course_overview.display_name_with_default))))
                __M_writer(u'" />\n            </a>\n')
            else:
                __M_writer(u'            <a class="fade-cover">\n              <img src="')
                __M_writer(filters.html_escape(filters.decode.utf8(course_overview.image_urls['small'])))
                __M_writer(u'" class="course-image" alt="')
                __M_writer(filters.html_escape(filters.decode.utf8(_('{course_number} {course_name} Cover Image').format(course_number=course_overview.number, course_name=course_overview.display_name_with_default))))
                __M_writer(u'" />\n            </a>\n')
        else:
            __M_writer(u'        <a class="cover">\n          <img src="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_overview.image_urls['small'])))
            __M_writer(u'" class="course-image" alt="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('{course_number} {course_name} Cover Image').format(course_number=course_overview.number, course_name=course_overview.display_name_with_default))))
            __M_writer(u'" />\n        </a>\n')
        if display_course_modes_on_dashboard and course_verified_certs.get('display_mode') != 'audit':
            __M_writer(u'        <span class="sts-enrollment" title="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_verified_certs.get('enrollment_title'))))
            __M_writer(u'">\n          <span class="label">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Enrolled as: "))))
            __M_writer(u'</span>\n')
            if course_verified_certs.get('show_image'):
                __M_writer(u'              <img class="deco-graphic" src="')
                __M_writer(filters.html_escape(filters.decode.utf8(static.url('images/verified-ribbon.png'))))
                __M_writer(u'" alt="')
                __M_writer(filters.html_escape(filters.decode.utf8(course_verified_certs.get('image_alt'))))
                __M_writer(u'" />\n')
            __M_writer(u'          <div class="sts-enrollment-value">')
            __M_writer(filters.html_escape(filters.decode.utf8(course_verified_certs.get('enrollment_value'))))
            __M_writer(u'</div>\n        </span>\n')
        __M_writer(u'    </div>\n      <div class="wrapper-course-details">\n        <h3 class="course-title" id="course-title-')
        __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
        __M_writer(u'">\n')
        if show_courseware_link and not is_unfulfilled_entitlement:
            if not is_course_blocked and not is_course_expired:
                __M_writer(u'              <a data-course-key="')
                __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
                __M_writer(u'" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(course_target)))
                __M_writer(u'" class="course-target-link">')
                __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_name_with_default)))
                __M_writer(u'</a>\n')
            else:
                __M_writer(u'              <a class="disable-look" data-course-key="')
                __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_name_with_default)))
                __M_writer(u'</a>\n')
        else:
            __M_writer(u'            <span>')
            __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_name_with_default)))
            __M_writer(u'</span>\n')
        __M_writer(u'        </h3>\n        <div class="course-info">\n          <span class="info-university">')
        __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_org_with_default)))
        __M_writer(u' - </span>\n          <span class="info-course-id">')
        __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_number_with_default)))
        __M_writer(u'</span>\n          ')

        if course_overview.start_date_is_still_default:
            container_string = _("Coming Soon")
            course_date = None
        else:
            format = 'shortDate'
            if course_overview.has_ended():
                container_string = _("Ended - {date}")
                course_date = course_overview.end
            elif course_overview.has_started():
                container_string = _("Started - {date}")
                course_date = course_overview.dashboard_start_display
            elif course_overview.starts_within(days=5):
                container_string = _("Starts - {date}")
                course_date = course_overview.dashboard_start_display
                format = 'defaultFormat'
            else: ## hasn't started yet
                container_string = _("Starts - {date}")
                course_date = course_overview.dashboard_start_display
            endif
        endif
                  
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['container_string','course_date','format'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n            <span class="info-date-block-container">\n')
        if not is_unfulfilled_entitlement and is_course_expired:
            __M_writer(u'                  <span class="info-date-block" data-course-key="')
            __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
            __M_writer(u'">\n                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(show_courseware_link.user_message)))
            __M_writer(u'\n                    <span class="sr">\n                      &nbsp;')
            __M_writer(filters.html_escape(filters.decode.utf8(_('for {course_display_name}').format(course_display_name=course_overview.display_name_with_default))))
            __M_writer(u'\n                    </span>\n                  </span>\n')
        elif is_unfulfilled_entitlement:
            __M_writer(u'                    <span class="info-date-block" aria-live="polite">\n                        <span class="icon fa fa-warning" aria-hidden="true"></span>\n')
            if not entitlement_expired_at:
                if entitlement_expiration_date:
                    __M_writer(u'                                ')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('You must select a session by {expiration_date} to access the course.').format(expiration_date=entitlement_expiration_date))))
                    __M_writer(u'\n')
                else:
                    __M_writer(u'                                ')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('You must select a session to access the course.'))))
                    __M_writer(u'\n')
            __M_writer(u'                    </span>\n')
        else:
            if isinstance(course_date, basestring):
                __M_writer(u'                        <span class="info-date-block">')
                __M_writer(filters.html_escape(filters.decode.utf8(container_string.format(date=course_date))))
                __M_writer(u'</span>\n')
            elif course_date is not None:
                __M_writer(u'                        <span class="info-date-block localized-datetime" data-language="')
                __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                __M_writer(u'" data-timezone="')
                __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                __M_writer(u'" data-datetime="')
                __M_writer(filters.html_escape(filters.decode.utf8(course_date.strftime('%Y-%m-%dT%H:%M:%S%z'))))
                __M_writer(u'" data-format=')
                __M_writer(filters.html_escape(filters.decode.utf8(format)))
                __M_writer(u' data-string="')
                __M_writer(filters.html_escape(filters.decode.utf8(container_string)))
                __M_writer(u'"></span>\n')
        if entitlement:
            if not entitlement_expired_at:
                __M_writer(u'                        <button class="change-session btn-link ')
                __M_writer(filters.html_escape(filters.decode.utf8('hidden' if is_unfulfilled_entitlement else '')))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Change or Leave Session'))))
                __M_writer(u'</button>\n')
        __M_writer(u'            </span>\n')
        if entitlement and not is_unfulfilled_entitlement and entitlement_expiration_date:
            __M_writer(u'                <div class="info-expires-at">\n                        <span class="msg-icon fa fa-warning" aria-hidden="true"></span>\n')
            if entitlement_expired_at:
                __M_writer(u'                            ')
                __M_writer(filters.html_escape(filters.decode.utf8(_('You can no longer change sessions.'))))
                __M_writer(u'\n')
            else:
                __M_writer(u'                            ')
                __M_writer(filters.html_escape(filters.decode.utf8(_('You can change sessions until {entitlement_expiration_date}.').format(entitlement_expiration_date=entitlement_expiration_date))))
                __M_writer(u'\n')
            __M_writer(u'                </div>\n')
        __M_writer(u'        </div>\n        <div class="wrapper-course-actions">\n          <div class="course-actions">\n')
        if (show_courseware_link or is_unfulfilled_entitlement) and not is_course_expired:
            if course_overview.has_ended():
                if not is_course_blocked:
                    __M_writer(u'                  <a href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_target)))
                    __M_writer(u'" class="enter-course archived course-target-link" data-course-key="')
                    __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('View Archived Course'))))
                    __M_writer(u'<span class="sr">&nbsp;')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_name_with_default)))
                    __M_writer(u'</span></a>\n')
                else:
                    __M_writer(u'                  <a class="enter-course-blocked archived course-target-link" data-course-key="')
                    __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('View Archived Course'))))
                    __M_writer(u'<span class="sr">&nbsp;')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_name_with_default)))
                    __M_writer(u'</span></a>\n')
                __M_writer(u'\n')
            else:
                if resume_button_url != '':
                    __M_writer(u'                  <a href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(resume_button_url)))
                    __M_writer(u'"\n                     class="course-target-link enter-course ')
                    __M_writer(filters.html_escape(filters.decode.utf8('hidden' if is_unfulfilled_entitlement else '')))
                    __M_writer(u'"\n                     data-course-key="')
                    __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
                    __M_writer(u'">\n                    ')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Resume Course'))))
                    __M_writer(u'\n                    <span class="sr">\n                      &nbsp;')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_name_with_default)))
                    __M_writer(u'\n                    </span>\n                  </a>\n')
                elif not is_course_blocked:
                    __M_writer(u'                  <a href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_target)))
                    __M_writer(u'"\n                     class="course-target-link enter-course ')
                    __M_writer(filters.html_escape(filters.decode.utf8('hidden' if is_unfulfilled_entitlement else '')))
                    __M_writer(u'"\n                     data-course-key="')
                    __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
                    __M_writer(u'">\n                    ')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('View Course'))))
                    __M_writer(u'\n                    <span class="sr">\n                      &nbsp;')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_name_with_default)))
                    __M_writer(u'\n                    </span>\n                  </a>\n')
                else:
                    __M_writer(u'                  <a class="enter-course-blocked"\n                     data-course-key="')
                    __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
                    __M_writer(u'">\n                    ')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('View Course'))))
                    __M_writer(u'\n                    <span class="sr">\n                      &nbsp;')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_name_with_default)))
                    __M_writer(u'\n                    </span>\n                  </a>\n')
        __M_writer(u'\n')
        if show_courseware_link or course_overview.has_social_sharing_url() or course_overview.has_marketing_url():
            __M_writer(u'\n')
            if share_settings:
                __M_writer(u'                    ')

                share_url = get_link_for_about_page(course_overview)
                encoded_utm_parameters = get_encoded_course_sharing_utm_params()
                share_window_name = 'shareWindow'
                share_window_config = 'toolbar=no, location=no, status=no, menubar=no, scrollbars=yes, resizable=yes, width=640, height=480'
                                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['encoded_utm_parameters','share_window_name','share_window_config','share_url'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                if share_settings.get('DASHBOARD_FACEBOOK', False):
                    __M_writer(u'                        ')

                    facebook_share_url = "{url}?{utm_params}".format(url=share_url.encode('utf-8'), utm_params=encoded_utm_parameters['facebook'])
                    share_text = _("I'm taking {course_name} online with {facebook_brand}. Check it out!").format(course_name=course_overview.display_name_with_default, facebook_brand=share_settings.get('FACEBOOK_BRAND', 'edX.org'))
                    query_params = urllib.urlencode((('u', facebook_share_url), ('quote', share_text.encode('utf-8')),))
                    facebook_url = 'https://www.facebook.com/sharer/sharer.php?{query}'.format(query=query_params)
                    share_msg = _("Share {course_name} on Facebook").format(course_name=course_overview.display_name_with_default)
                                            
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['query_params','facebook_url','share_text','facebook_share_url','share_msg'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n                        <a\n                          data-tooltip="')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Share on Facebook'))))
                    __M_writer(u'"\n                          data-trigger="focus hover"\n                          class="action action-facebook"\n                          href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(facebook_url)))
                    __M_writer(u'"\n                          target="_blank"\n                          title="')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Share on Facebook'))))
                    __M_writer(u'"\n                          data-course-id="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.id)))
                    __M_writer(u'"\n                          onclick="window.open(\'')
                    __M_writer(filters.html_escape(filters.decode.utf8(facebook_url)))
                    __M_writer(u"', '")
                    __M_writer(filters.html_escape(filters.decode.utf8(share_window_name)))
                    __M_writer(u"', '")
                    __M_writer(filters.html_escape(filters.decode.utf8(share_window_config)))
                    __M_writer(u'\'); return false;">\n                          <span class="sr">')
                    __M_writer(filters.html_escape(filters.decode.utf8(share_msg)))
                    __M_writer(u'</span>\n                          <span class="fa fa-facebook" aria-hidden="true"></span>\n                        </a>\n')
                if share_settings.get('DASHBOARD_TWITTER', False):
                    __M_writer(u'                        ')

                    twitter_share_url = "{url}?{utm_params}".format(url=share_url.encode('utf-8'), utm_params=encoded_utm_parameters['twitter'])
                    default_share_text = _("I'm taking {course_name} online with {twitter_brand}. Check it out!").format(course_name=course_overview.display_name_with_default, twitter_brand=share_settings.get('TWITTER_BRAND', '@edxonline'))
                    share_text = urllib.quote_plus(share_settings.get('DASHBOARD_TWITTER_TEXT', default_share_text.encode('utf-8')))
                    twitter_url = 'https://twitter.com/intent/tweet?text=' + share_text + '%20' + urllib.quote_plus(twitter_share_url)
                    share_msg = _("Share {course_name} on Twitter").format(course_name=course_overview.display_name_with_default)
                                            
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['twitter_url','share_msg','share_text','default_share_text','twitter_share_url'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n                        <a\n                          data-tooltip="')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Share on Twitter'))))
                    __M_writer(u'"\n                          data-trigger="focus hover"\n                          class="action action-twitter"\n                          href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(twitter_url)))
                    __M_writer(u'"\n                          target="_blank"\n                          title="')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Share on Twitter'))))
                    __M_writer(u'"\n                          data-course-id="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.id)))
                    __M_writer(u'"\n                          onclick="window.open(\'')
                    __M_writer(filters.html_escape(filters.decode.utf8(twitter_url)))
                    __M_writer(u"', '")
                    __M_writer(filters.html_escape(filters.decode.utf8(share_window_name)))
                    __M_writer(u"', '")
                    __M_writer(filters.html_escape(filters.decode.utf8(share_window_config)))
                    __M_writer(u'\'); return false;">\n                          <span class="sr">')
                    __M_writer(filters.html_escape(filters.decode.utf8(share_msg)))
                    __M_writer(u'</span>\n                          <span class="fa fa-twitter" aria-hidden="true"></span>\n                        </a>\n')
        __M_writer(u'\n')
        if entitlement and (can_refund_entitlement or show_email_settings):
            __M_writer(u'                ')
            runtime._include_file(context, u'_dashboard_entitlement_actions.html', _template_uri, course_overview=course_overview,entitlement=entitlement,dashboard_index=dashboard_index, can_refund_entitlement=can_refund_entitlement, show_email_settings=show_email_settings)
            __M_writer(u'\n')
        elif not entitlement:
            __M_writer(u'                <div class="wrapper-action-more" data-course-key="')
            __M_writer(filters.html_escape(filters.decode.utf8(enrollment.course_id)))
            __M_writer(u'">\n                  <button type="button" class="action action-more" id="actions-dropdown-link-')
            __M_writer(filters.html_escape(filters.decode.utf8(dashboard_index)))
            __M_writer(u'" aria-haspopup="true" aria-expanded="false" aria-controls="actions-dropdown-')
            __M_writer(filters.html_escape(filters.decode.utf8(dashboard_index)))
            __M_writer(u'" data-course-number="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_overview.number)))
            __M_writer(u'" data-course-name="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_name_with_default)))
            __M_writer(u'" data-dashboard-index="')
            __M_writer(filters.html_escape(filters.decode.utf8(dashboard_index)))
            __M_writer(u'">\n                    <span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Course options for'))))
            __M_writer(u'</span>\n                    <span class="sr">&nbsp;\n                      ')
            __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_name_with_default)))
            __M_writer(u'\n                    </span>\n                    <span class="fa fa-cog" aria-hidden="true"></span>\n                  </button>\n                  <div class="actions-dropdown" id="actions-dropdown-')
            __M_writer(filters.html_escape(filters.decode.utf8(dashboard_index)))
            __M_writer(u'" tabindex="-1">\n                    <ul class="actions-dropdown-list" id="actions-dropdown-list-')
            __M_writer(filters.html_escape(filters.decode.utf8(dashboard_index)))
            __M_writer(u'" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Available Actions'))))
            __M_writer(u'" role="menu">\n')
            if can_unenroll:
                __M_writer(u'                        <li class="actions-item" id="actions-item-unenroll-')
                __M_writer(filters.html_escape(filters.decode.utf8(dashboard_index)))
                __M_writer(u'" role="menuitem">\n                          ')
                course_refund_url = reverse('course_run_refund_status', args=[unicode(course_overview.id)]) 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['course_refund_url'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                if not is_course_blocked:
                    __M_writer(u'                              <a href="#unenroll-modal" class="action action-unenroll" rel="leanModal"\n                                 data-course-id="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.id)))
                    __M_writer(u'"\n                                 data-course-number="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.number)))
                    __M_writer(u'"\n                                 data-course-name="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_name_with_default)))
                    __M_writer(u'"\n                                 data-dashboard-index="')
                    __M_writer(filters.html_escape(filters.decode.utf8(dashboard_index)))
                    __M_writer(u'"\n                                 data-course-refund-url="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_refund_url)))
                    __M_writer(u'"\n                                 data-course-is-paid-course="')
                    __M_writer(filters.html_escape(filters.decode.utf8(is_paid_course)))
                    __M_writer(u'"\n                                 data-course-cert-name-long="')
                    __M_writer(filters.html_escape(filters.decode.utf8(cert_name_long)))
                    __M_writer(u'"\n                                 data-course-enrollment-mode="')
                    __M_writer(filters.html_escape(filters.decode.utf8(enrollment.mode)))
                    __M_writer(u'">\n                                ')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Unenroll'))))
                    __M_writer(u'\n                              </a>\n')
                else:
                    __M_writer(u'                              <a class="action action-unenroll is-disabled"\n                                 data-course-id="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.id)))
                    __M_writer(u'"\n                                 data-course-number="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.number)))
                    __M_writer(u'"\n                                 data-course-name="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.display_name_with_default)))
                    __M_writer(u'"\n                                 data-dashboard-index="')
                    __M_writer(filters.html_escape(filters.decode.utf8(dashboard_index)))
                    __M_writer(u'"\n                                 data-course-refund-url="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_refund_url)))
                    __M_writer(u'"\n                                 data-course-is-paid-course="')
                    __M_writer(filters.html_escape(filters.decode.utf8(is_paid_course)))
                    __M_writer(u'"\n                                 data-course-cert-name-long="')
                    __M_writer(filters.html_escape(filters.decode.utf8(cert_name_long)))
                    __M_writer(u'"\n                                 data-course-enrollment-mode="')
                    __M_writer(filters.html_escape(filters.decode.utf8(enrollment.mode)))
                    __M_writer(u'">\n                                ')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Unenroll'))))
                    __M_writer(u'\n                              </a>\n')
                __M_writer(u'                        </li>\n')
            __M_writer(u'                      <li class="actions-item" id="actions-item-email-settings-')
            __M_writer(filters.html_escape(filters.decode.utf8(dashboard_index)))
            __M_writer(u'" role="menuitem">\n')
            if show_email_settings:
                if not is_course_blocked:
                    __M_writer(u'                            <a href="#email-settings-modal" class="action action-email-settings" rel="leanModal" data-course-id="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.id)))
                    __M_writer(u'" data-course-number="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.number)))
                    __M_writer(u'" data-dashboard-index="')
                    __M_writer(filters.html_escape(filters.decode.utf8(dashboard_index)))
                    __M_writer(u'" data-optout="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.id in course_optouts)))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Email Settings'))))
                    __M_writer(u'</a>\n')
                else:
                    __M_writer(u'                            <a class="action action-email-settings is-disabled" data-course-id="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.id)))
                    __M_writer(u'" data-course-number="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.number)))
                    __M_writer(u'" data-dashboard-index="')
                    __M_writer(filters.html_escape(filters.decode.utf8(dashboard_index)))
                    __M_writer(u'" data-optout="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.id in course_optouts)))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Email Settings'))))
                    __M_writer(u'</a>\n')
            __M_writer(u'                      </li>\n                    </ul>\n                  </div>\n                </div>\n')
        __M_writer(u'          </div>\n        </div>\n      </div>\n  </section>\n  <footer class="wrapper-messages-primary">\n    <div class="messages-list">\n\n')
        if entitlement and not entitlement_expired_at:
            __M_writer(u'        <div class="course-entitlement-selection-container ')
            __M_writer(filters.html_escape(filters.decode.utf8('' if is_unfulfilled_entitlement else 'hidden')))
            __M_writer(u'"></div>\n        ')
            def ccall(caller):
                def body():
                    str = context.get('str', UNDEFINED)
                    __M_writer = context.writer()
                    __M_writer(u"\n          EntitlementFactory({\n              el: '")
                    __M_writer(js_escaped_string( '#course-card-' + str(course_card_index) + ' .course-entitlement-selection-container' ))
                    __M_writer(u"',\n              triggerOpenBtn: '")
                    __M_writer(js_escaped_string( '#course-card-' + str(course_card_index) + ' .change-session' ))
                    __M_writer(u"',\n              courseCardMessages: '")
                    __M_writer(js_escaped_string( '#course-card-' + str(course_card_index) + ' .messages-list > .message' ))
                    __M_writer(u"',\n              courseTitleLink: '")
                    __M_writer(js_escaped_string( '#course-card-' + str(course_card_index) + ' .course-title a' ))
                    __M_writer(u"',\n              courseImageLink: '")
                    __M_writer(js_escaped_string( '#course-card-' + str(course_card_index) + ' .wrapper-course-image > a' ))
                    __M_writer(u"',\n              dateDisplayField: '")
                    __M_writer(js_escaped_string( '#course-card-' + str(course_card_index) + ' .info-date-block' ))
                    __M_writer(u"',\n              policyMsg: '")
                    __M_writer(js_escaped_string( '#course-card-' + str(course_card_index) + ' .info-expires-at' ))
                    __M_writer(u"',\n              enterCourseBtn: '")
                    __M_writer(js_escaped_string( '#course-card-' + str(course_card_index) + ' .enter-course' ))
                    __M_writer(u"',\n              availableSessions: '")
                    __M_writer(dump_js_escaped_json( entitlement_available_sessions ))
                    __M_writer(u"',\n              entitlementUUID: '")
                    __M_writer(js_escaped_string( entitlement.course_uuid ))
                    __M_writer(u"',\n              currentSessionId: '")
                    __M_writer(js_escaped_string( entitlement_session.course_id if entitlement_session else "" ))
                    __M_writer(u"',\n              enrollUrl: '")
                    __M_writer(js_escaped_string( reverse('entitlements_api:v1:enrollments', args=[str(entitlement.uuid)]) ))
                    __M_writer(u"',\n              courseHomeUrl: '")
                    __M_writer(js_escaped_string( course_target ))
                    __M_writer(u"',\n              expiredAt: '")
                    __M_writer(js_escaped_string( entitlement.expired_at_datetime ))
                    __M_writer(u"',\n              daysUntilExpiration: '")
                    __M_writer(js_escaped_string( entitlement.get_days_until_expiration() ))
                    __M_writer(u"'\n          });\n        ")
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'EntitlementFactory'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        __M_writer(u'\n')
        if related_programs:
            __M_writer(u'        <div class="message message-related-programs is-shown">\n          <span class="related-programs-preface" tabindex="0">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Related Programs'))))
            __M_writer(u':</span>\n          <ul>\n')
            for program in related_programs:
                __M_writer(u'            <li>\n              <span class="category-icon ')
                __M_writer(filters.html_escape(filters.decode.utf8(program['type'].lower())))
                __M_writer(u'-icon" aria-hidden="true"></span>\n              <span><a href="')
                __M_writer(filters.html_escape(filters.decode.utf8(program['detail_url'])))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(u'{title} {type}'.format(title=program['title'], type=program['type']))))
                __M_writer(u'</a></span>\n            </li>\n')
            __M_writer(u'          </ul>\n        </div>\n')
        __M_writer(u'\n')
        if cert_status:
            __M_writer(u'        ')
            runtime._include_file(context, u'_dashboard_certificate_information.html', _template_uri, cert_status=cert_status,course_overview=course_overview, enrollment=enrollment, reverify_link=reverify_link)
            __M_writer(u'\n')
        __M_writer(u'\n')
        if credit_status is not None:
            __M_writer(u'        ')
            runtime._include_file(context, u'_dashboard_credit_info.html', _template_uri, credit_status=credit_status)
            __M_writer(u'\n')
        __M_writer(u'\n')
        if is_course_blocked and entitlement:
            __M_writer(u'        <p id="block-course-msg" class="course-block">\n          ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("You can no longer access this course because payment has not yet been received. You can contact the account holder to request payment, or you can unenroll from this course"))))
            __M_writer(u'\n        </p>\n')
        elif is_course_blocked:
            __M_writer(u'        <p id="block-course-msg" class="course-block">\n          ')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_("You can no longer access this course because payment has not yet been received. "
              "You can {contact_link_start}contact the account holder{contact_link_end} "
              "to request payment, or you can "
              "{unenroll_link_start}unenroll{unenroll_link_end} "
              "from this course")).format(
            contact_link_start=HTML('<button type="button">'),
            contact_link_end=HTML('</button>'),
            unenroll_link_start=HTML(
              '<a id="unregister_block_course" rel="leanModal" '
              'data-course-id="{course_id}" data-course-number="{course_number}" data-course-name="{course_name}" '
              'href="#unenroll-modal">'
            ).format(
              course_id=course_overview.id,
              course_number=course_overview.number,
              course_name=course_overview.display_name_with_default,
            ),
            unenroll_link_end=HTML('</a>'),
          ))))
            __M_writer(u'\n        </p>\n')
        else:
            if show_consent_link:
                __M_writer(u'          ')
                runtime._include_file(context, u'_dashboard_show_consent.html', _template_uri, course_overview=course_overview, course_target=course_target, enrollment=enrollment, enterprise_customer_name=enterprise_customer_name)
                __M_writer(u'\n')
            __M_writer(u'\n')
            if verification_status.get('should_display') and verification_status.get('status') in [VERIFY_STATUS_NEED_TO_VERIFY, VERIFY_STATUS_SUBMITTED, VERIFY_STATUS_RESUBMITTED, VERIFY_STATUS_APPROVED, VERIFY_STATUS_NEED_TO_REVERIFY]:
                __M_writer(u'          <div class="message message-status wrapper-message-primary is-shown">\n')
                if verification_status['status'] == VERIFY_STATUS_NEED_TO_VERIFY:
                    __M_writer(u'              <div class="verification-reminder">\n')
                    if verification_status['days_until_deadline'] is not None:
                        __M_writer(u'                  <h4 class="message-title">')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('Verification not yet complete.'))))
                        __M_writer(u'</h4>\n                  <p class="message-copy">')
                        __M_writer(filters.html_escape(filters.decode.utf8(ungettext(
                    'You only have {days} day left to verify for this course.',
                    'You only have {days} days left to verify for this course.',
                    verification_status['days_until_deadline']
                  ).format(days=verification_status['days_until_deadline']))))
                        __M_writer(u'</p>\n')
                    else:
                        __M_writer(u'                  <h4 class="message-title">')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('Almost there!'))))
                        __M_writer(u'</h4>\n                  <p class="message-copy">')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('You still need to verify for this course.'))))
                        __M_writer(u'</p>\n')
                    __M_writer(u'              </div>\n              <div class="verification-cta">\n                <a href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(reverse('verify_student_verify_now', kwargs={'course_id': unicode(course_overview.id)}))))
                    __M_writer(u'" class="btn" data-course-id="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.id)))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Verify Now'))))
                    __M_writer(u'</a>\n              </div>\n')
                elif verification_status['status'] == VERIFY_STATUS_SUBMITTED:
                    __M_writer(u'              <h4 class="message-title">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('You have submitted your verification information.'))))
                    __M_writer(u'</h4>\n              <p class="message-copy">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('You will see a message on your dashboard when the verification process is complete (usually within 1-2 days).'))))
                    __M_writer(u'</p>\n')
                elif verification_status['status'] == VERIFY_STATUS_RESUBMITTED:
                    __M_writer(u'              <h4 class="message-title">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Your current verification will expire soon!'))))
                    __M_writer(u'</h4>\n              <p class="message-copy">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('You have submitted your reverification information. You will see a message on your dashboard when the verification process is complete (usually within 1-2 days).'))))
                    __M_writer(u'</p>\n')
                elif verification_status['status'] == VERIFY_STATUS_APPROVED:
                    __M_writer(u'              <h4 class="message-title">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('You have successfully verified your ID with edX'))))
                    __M_writer(u'</h4>\n')
                    if verification_status.get('verification_good_until') is not None:
                        __M_writer(u'                <p class="message-copy">')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('Your current verification is effective until {date}.').format(date=verification_status['verification_good_until']))))
                        __M_writer(u'\n')
                elif verification_status['status'] == VERIFY_STATUS_NEED_TO_REVERIFY:
                    __M_writer(u'              <h4 class="message-title">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Your current verification will expire soon.'))))
                    __M_writer(u'</h4>\n')
                    __M_writer(u'              <p class="message-copy">')
                    __M_writer(filters.html_escape(filters.decode.utf8(Text(_('Your current verification will expire in {days} days. {start_link}Re-verify your identity now{end_link} using a webcam and a government-issued photo ID.')).format(
                  start_link=HTML('<a href="{href}">').format(href=reverse('verify_student_reverify')),
                  end_link=HTML('</a>'),
                  days=settings.VERIFY_STUDENT.get("EXPIRING_SOON_WINDOW")
                ))))
                    __M_writer(u'\n              </p>\n')
                __M_writer(u'          </div>\n')
            __M_writer(u'\n')
            if course_mode_info and course_mode_info['show_upsell'] and not entitlement:
                __M_writer(u'          <div class="message message-upsell has-actions is-shown">\n            <div class="wrapper-extended">\n              <p class="message-copy" align="justify">\n                <b class="message-copy-bold">\n                  ')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Pursue a {cert_name_long} to highlight the knowledge and skills you gain in this course.").format(cert_name_long=cert_name_long))))
                __M_writer(u'\n                </b><br>\n                  ')
                __M_writer(filters.html_escape(filters.decode.utf8(Text(_("It's official. It's easily shareable. "
                      "It's a proven motivator to complete the course. {line_break}"
                      "{link_start}Learn more about the verified {cert_name_long}{link_end}.")).format(
                        line_break=HTML('<br>'),
                        link_start=HTML('<a href="{}" class="verified-info" data-course-key="{}">').format(
                          marketing_link('WHAT_IS_VERIFIED_CERT'),
                          enrollment.course_id
                        ),
                        link_end=HTML('</a>'),
                        cert_name_long=cert_name_long
                      ))))
                __M_writer(u'\n              </p>\n              <div class="action-upgrade-container">\n')
                if use_ecommerce_payment_flow and course_mode_info['verified_sku']:
                    __M_writer(u'                  <a class="action action-upgrade" href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(ecommerce_payment_page)))
                    __M_writer(u'?sku=')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_mode_info['verified_sku'])))
                    __M_writer(u'">\n')
                else:
                    __M_writer(u'                  <a class="action action-upgrade" href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(reverse('verify_student_upgrade_and_verify', kwargs={'course_id': unicode(course_overview.id)}))))
                    __M_writer(u'" data-course-id="')
                    __M_writer(filters.html_escape(filters.decode.utf8(course_overview.id)))
                    __M_writer(u'" data-user="')
                    __M_writer(filters.html_escape(filters.decode.utf8(user.username)))
                    __M_writer(u'">\n')
                __M_writer(u'                    <span class="action-upgrade-icon" aria-hidden="true"></span>\n                  <span class="wrapper-copy">\n                    <span class="copy" id="upgrade-to-verified">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Upgrade to Verified"))))
                __M_writer(u'</span>\n                      <span class="sr">&nbsp;')
                __M_writer(filters.html_escape(filters.decode.utf8(_(course_overview.display_name_with_default))))
                __M_writer(u'</span>\n                  </span>\n                </a>\n              </div>\n            </div>\n          </div>\n')
        __M_writer(u'\n')
        if course_requirements:
            __M_writer(u'        ')
            prc_target = reverse('about_course', args=[unicode(course_requirements['courses'][0]['key'])]) 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['prc_target'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n        <div class="prerequisites">\n          <p class="tip">\n            ')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_("You must successfully complete {link_start}{prc_display}{link_end} before you begin this course.")).format(
                link_start=HTML('<a href="{}">').format(prc_target),
                link_end=HTML('</a>'),
                prc_display=course_requirements['courses'][0]['display'],
              ))))
            __M_writer(u'\n          </p>\n        </div>\n')
        __M_writer(u'    </div>\n  </footer>\n</article>\n</div>\n</li>\n<script>\n           $( document ).ready(function() {\n\n               if("')
        __M_writer(dump_js_escaped_json(is_course_blocked ))
        __M_writer(u'" == \'true\'){\n                   $( "#unregister_block_course" ).click(function() {\n                       $(\'.disable-look-unregister\').click();\n                   });\n               }\n           });\n</script>\n\n')
        if share_settings.get('DASHBOARD_FACEBOOK', False) and share_settings.get('DASHBOARD_TWITTER', False):
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    __M_writer(u'\n        CourseSharingEvents("')
                    __M_writer(js_escaped_string(course_overview.id ))
                    __M_writer(u'");\n    ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.require_module_async(class_name=u'CourseSharingEvents',module_name=u'js/course_sharing/course_sharing_events'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n    DateUtilFactory.transform(iterationKey=".localized-datetime");\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module_async(class_name=u'DateUtilFactory',module_name=u'js/dateutil_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "46": 40, "49": 1, "69": 1, "70": 24, "71": 26, "87": 38, "88": 40, "89": 43, "90": 44, "91": 44, "101": 50, "102": 51, "110": 55, "111": 56, "112": 57, "113": 57, "117": 57, "118": 59, "119": 60, "120": 61, "121": 61, "122": 61, "123": 63, "124": 64, "125": 64, "126": 64, "127": 64, "128": 64, "129": 64, "130": 65, "134": 65, "135": 66, "136": 66, "137": 67, "138": 67, "139": 67, "140": 67, "141": 69, "142": 70, "143": 71, "144": 71, "145": 71, "146": 71, "147": 71, "148": 72, "149": 72, "150": 72, "151": 72, "152": 74, "153": 75, "154": 76, "155": 76, "156": 76, "157": 76, "158": 79, "159": 80, "160": 81, "161": 81, "162": 81, "163": 81, "164": 84, "165": 85, "166": 85, "167": 85, "168": 86, "169": 86, "170": 87, "171": 88, "172": 88, "173": 88, "174": 88, "175": 88, "176": 90, "177": 90, "178": 90, "179": 93, "180": 95, "181": 95, "182": 96, "183": 97, "184": 98, "185": 98, "186": 98, "187": 98, "188": 98, "189": 98, "190": 98, "191": 99, "192": 100, "193": 100, "194": 100, "195": 100, "196": 100, "197": 102, "198": 103, "199": 103, "200": 103, "201": 105, "202": 107, "203": 107, "204": 108, "205": 108, "206": 109, "231": 130, "232": 133, "233": 134, "234": 134, "235": 134, "236": 135, "237": 135, "238": 137, "239": 137, "240": 140, "241": 141, "242": 143, "243": 144, "244": 145, "245": 145, "246": 145, "247": 146, "248": 147, "249": 147, "250": 147, "251": 150, "252": 151, "253": 152, "254": 153, "255": 153, "256": 153, "257": 154, "258": 155, "259": 155, "260": 155, "261": 155, "262": 155, "263": 155, "264": 155, "265": 155, "266": 155, "267": 155, "268": 155, "269": 158, "270": 159, "271": 160, "272": 160, "273": 160, "274": 160, "275": 160, "276": 163, "277": 164, "278": 165, "279": 167, "280": 168, "281": 168, "282": 168, "283": 169, "284": 170, "285": 170, "286": 170, "287": 172, "288": 174, "289": 177, "290": 178, "291": 179, "292": 180, "293": 180, "294": 180, "295": 180, "296": 180, "297": 180, "298": 180, "299": 180, "300": 180, "301": 181, "302": 182, "303": 182, "304": 182, "305": 182, "306": 182, "307": 182, "308": 182, "309": 184, "310": 185, "311": 186, "312": 187, "313": 187, "314": 187, "315": 188, "316": 188, "317": 189, "318": 189, "319": 190, "320": 190, "321": 192, "322": 192, "323": 195, "324": 196, "325": 196, "326": 196, "327": 197, "328": 197, "329": 198, "330": 198, "331": 199, "332": 199, "333": 201, "334": 201, "335": 204, "336": 205, "337": 206, "338": 206, "339": 207, "340": 207, "341": 209, "342": 209, "343": 215, "344": 216, "345": 217, "346": 218, "347": 219, "348": 219, "357": 224, "358": 225, "359": 226, "360": 226, "370": 232, "371": 234, "372": 234, "373": 237, "374": 237, "375": 239, "376": 239, "377": 240, "378": 240, "379": 241, "380": 241, "381": 241, "382": 241, "383": 241, "384": 241, "385": 242, "386": 242, "387": 246, "388": 247, "389": 247, "399": 253, "400": 255, "401": 255, "402": 258, "403": 258, "404": 260, "405": 260, "406": 261, "407": 261, "408": 262, "409": 262, "410": 262, "411": 262, "412": 262, "413": 262, "414": 263, "415": 263, "416": 269, "417": 273, "418": 274, "419": 274, "420": 274, "421": 275, "422": 276, "423": 276, "424": 276, "425": 277, "426": 277, "427": 277, "428": 277, "429": 277, "430": 277, "431": 277, "432": 277, "433": 277, "434": 277, "435": 278, "436": 278, "437": 280, "438": 280, "439": 284, "440": 284, "441": 285, "442": 285, "443": 285, "444": 285, "445": 286, "446": 287, "447": 287, "448": 287, "449": 288, "453": 288, "454": 289, "455": 290, "456": 291, "457": 291, "458": 292, "459": 292, "460": 293, "461": 293, "462": 294, "463": 294, "464": 295, "465": 295, "466": 296, "467": 296, "468": 297, "469": 297, "470": 298, "471": 298, "472": 299, "473": 299, "474": 301, "475": 302, "476": 303, "477": 303, "478": 304, "479": 304, "480": 305, "481": 305, "482": 306, "483": 306, "484": 307, "485": 307, "486": 308, "487": 308, "488": 309, "489": 309, "490": 310, "491": 310, "492": 311, "493": 311, "494": 314, "495": 316, "496": 316, "497": 316, "498": 317, "499": 318, "500": 319, "501": 319, "502": 319, "503": 319, "504": 319, "505": 319, "506": 319, "507": 319, "508": 319, "509": 319, "510": 319, "511": 320, "512": 321, "513": 321, "514": 321, "515": 321, "516": 321, "517": 321, "518": 321, "519": 321, "520": 321, "521": 321, "522": 321, "523": 324, "524": 329, "525": 336, "526": 337, "527": 337, "528": 337, "533": 338, "534": 340, "535": 340, "536": 341, "537": 341, "538": 342, "539": 342, "540": 343, "541": 343, "542": 344, "543": 344, "544": 345, "545": 345, "546": 346, "547": 346, "548": 347, "549": 347, "550": 348, "551": 348, "552": 349, "553": 349, "554": 350, "555": 350, "556": 351, "557": 351, "558": 352, "559": 352, "560": 353, "561": 353, "562": 354, "563": 354, "568": 338, "571": 356, "572": 358, "573": 359, "574": 360, "575": 361, "576": 361, "577": 363, "578": 364, "579": 365, "580": 365, "581": 366, "582": 366, "583": 366, "584": 366, "585": 369, "586": 372, "587": 373, "588": 374, "589": 374, "590": 374, "591": 376, "592": 377, "593": 378, "594": 378, "595": 378, "596": 380, "597": 381, "598": 382, "599": 383, "600": 383, "601": 385, "602": 386, "603": 387, "621": 404, "622": 406, "623": 407, "624": 408, "625": 408, "626": 408, "627": 410, "628": 411, "629": 412, "630": 413, "631": 414, "632": 415, "633": 416, "634": 416, "635": 416, "636": 417, "641": 421, "642": 422, "643": 423, "644": 423, "645": 423, "646": 424, "647": 424, "648": 426, "649": 428, "650": 428, "651": 428, "652": 428, "653": 428, "654": 428, "655": 430, "656": 431, "657": 431, "658": 431, "659": 432, "660": 432, "661": 433, "662": 434, "663": 434, "664": 434, "665": 435, "666": 435, "667": 436, "668": 437, "669": 437, "670": 437, "671": 438, "672": 439, "673": 439, "674": 439, "675": 441, "676": 442, "677": 442, "678": 442, "679": 445, "680": 445, "685": 449, "686": 452, "687": 454, "688": 455, "689": 456, "690": 460, "691": 460, "692": 462, "703": 472, "704": 475, "705": 476, "706": 476, "707": 476, "708": 476, "709": 476, "710": 477, "711": 478, "712": 478, "713": 478, "714": 478, "715": 478, "716": 478, "717": 478, "718": 480, "719": 482, "720": 482, "721": 483, "722": 483, "723": 491, "724": 492, "725": 494, "726": 494, "730": 494, "731": 497, "736": 501, "737": 505, "738": 513, "739": 513, "740": 521, "741": 522, "745": 522, "746": 523, "747": 523, "752": 522, "755": 524, "756": 526, "760": 527, "765": 527, "768": 529, "774": 768}, "uri": "dashboard/_dashboard_course_listing.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/dashboard/_dashboard_course_listing.html"}
__M_END_METADATA
"""
