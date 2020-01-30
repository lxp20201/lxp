# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580283886.821412
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/dashboard.html'
_template_uri = 'custome-theme/lms/templates/dashboard.html'
_source_encoding = 'utf-8'
_exports = [u'pagetitle', u'header_extras', u'bodyclass', 'online_help_token', u'js_extra']



import pytz
from datetime import datetime, timedelta
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.template import RequestContext
from entitlements.models import CourseEntitlement
from third_party_auth import pipeline
from util.date_utils import strftime_localized
from opaque_keys.edx.keys import CourseKey
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from openedx.core.djangolib.js_utils import dump_js_escaped_json, js_escaped_string
from openedx.core.djangolib.markup import HTML, Text

from student.models import CourseEnrollment


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
    return runtime._inherit_from(context, u'main.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        enterprise_customer_name = context.get('enterprise_customer_name', UNDEFINED)
        enrollment_message = context.get('enrollment_message', UNDEFINED)
        display_sidebar_account_activation_message = context.get('display_sidebar_account_activation_message', UNDEFINED)
        block_courses = context.get('block_courses', UNDEFINED)
        course_enrollments = context.get('course_enrollments', UNDEFINED)
        banner_account_activation_message = context.get('banner_account_activation_message', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        unicode = context.get('unicode', UNDEFINED)
        resume_button_urls = context.get('resume_button_urls', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        redirect_message = context.get('redirect_message', UNDEFINED)
        show_email_settings_for = context.get('show_email_settings_for', UNDEFINED)
        empty_dashboard_message = context.get('empty_dashboard_message', UNDEFINED)
        unfulfilled_entitlement_pseudo_sessions = context.get('unfulfilled_entitlement_pseudo_sessions', UNDEFINED)
        errored_courses = context.get('errored_courses', UNDEFINED)
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        credit_statuses = context.get('credit_statuses', UNDEFINED)
        display_course_modes_on_dashboard = context.get('display_course_modes_on_dashboard', UNDEFINED)
        account_activation_messages = context.get('account_activation_messages', UNDEFINED)
        staff_access = context.get('staff_access', UNDEFINED)
        marketing_link = context.get('marketing_link', UNDEFINED)
        display_dashboard_courses = context.get('display_dashboard_courses', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        course_entitlement_available_sessions = context.get('course_entitlement_available_sessions', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        consent_required_courses = context.get('consent_required_courses', UNDEFINED)
        all_course_modes = context.get('all_course_modes', UNDEFINED)
        user = context.get('user', UNDEFINED)
        activate_account_message = context.get('activate_account_message', UNDEFINED)
        courses_requirements_not_met = context.get('courses_requirements_not_met', UNDEFINED)
        order_history_list = context.get('order_history_list', UNDEFINED)
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        display_sidebar_on_dashboard = context.get('display_sidebar_on_dashboard', UNDEFINED)
        cert_statuses = context.get('cert_statuses', UNDEFINED)
        unfulfilled_entitlement = context.get('unfulfilled_entitlement', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        enterprise_message = context.get('enterprise_message', UNDEFINED)
        show_courseware_links_for = context.get('show_courseware_links_for', UNDEFINED)
        str = context.get('str', UNDEFINED)
        verification_status_by_course = context.get('verification_status_by_course', UNDEFINED)
        course_entitlements = context.get('course_entitlements', UNDEFINED)
        def header_extras():
            return render_header_extras(context._locals(__M_locals))
        inverted_programs = context.get('inverted_programs', UNDEFINED)
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        enrolled_courses_either_paid = context.get('enrolled_courses_either_paid', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')

        cert_name_short = settings.CERT_NAME_SHORT
        cert_name_long = settings.CERT_NAME_LONG
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['cert_name_long','cert_name_short'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_extras'):
            context['self'].header_extras(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n\n<div class="dashboard-notifications" tabindex="-1">\n\n')
        if banner_account_activation_message:
            __M_writer(u'        <div class="dashboard-banner">\n            ')
            __M_writer(filters.decode.utf8(banner_account_activation_message ))
            __M_writer(u'\n        </div>\n')
        __M_writer(u'\n')
        if enrollment_message:
            __M_writer(u'        <div class="dashboard-banner">\n            ')
            __M_writer(filters.decode.utf8(enrollment_message ))
            __M_writer(u'\n        </div>\n')
        __M_writer(u'\n')
        if enterprise_message:
            __M_writer(u'        <div class="dashboard-banner">\n            ')
            __M_writer(filters.decode.utf8( enterprise_message ))
            __M_writer(u'\n        </div>\n')
        __M_writer(u'\n')
        if account_activation_messages:
            __M_writer(u'      <div class="activation-message-container">\n')
            for account_activation_message in account_activation_messages:
                __M_writer(u'          <div class="account-activation ')
                __M_writer(filters.html_escape(filters.decode.utf8(account_activation_message.tags)))
                __M_writer(u'" role="alert" aria-label="Account Activation Message" tabindex="-1">\n            <div class="message-copy" >\n              ')
                __M_writer(filters.decode.utf8( account_activation_message ))
                __M_writer(u'\n            </div>\n          </div>\n')
            __M_writer(u'      </div>\n')
        __M_writer(u'\n</div>\n\n<main id="main" aria-label="Content" tabindex="-1">\n    <div class="dashboard holder" id="dashboard-main">\n      <div class="main-container">\n        <div class="my-courses" id="my-courses">\n')
        if display_dashboard_courses:
            __M_writer(u'          ')
            runtime._include_file(context, u'learner_dashboard/_dashboard_navigation_courses.html', _template_uri)
            __M_writer(u'\n')
        __M_writer(u'\n')
        if len(course_entitlements + course_enrollments) > 0:
            __M_writer(u'            <ul class="listing-courses">\n            ')

            share_settings = configuration_helpers.get_value(
                'SOCIAL_SHARING_SETTINGS',
                getattr(settings, 'SOCIAL_SHARING_SETTINGS', {})
            )
                        
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['share_settings'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            for dashboard_index, enrollment in enumerate(course_entitlements + course_enrollments):
                __M_writer(u'              ')

                # Check if the course run is an entitlement and if it has an associated session
                entitlement = enrollment if isinstance(enrollment, CourseEntitlement) else None
                entitlement_session = entitlement.enrollment_course_run if entitlement else None
                entitlement_days_until_expiration = entitlement.get_days_until_expiration() if entitlement else None
                entitlement_expiration = datetime.now(tz=pytz.UTC) + timedelta(days=entitlement_days_until_expiration) if (entitlement and entitlement_days_until_expiration < settings.ENTITLEMENT_EXPIRED_ALERT_PERIOD) else None
                entitlement_expiration_date = strftime_localized(entitlement_expiration, 'SHORT_DATE') if entitlement and entitlement_expiration else None
                entitlement_expired_at = strftime_localized(entitlement.expired_at_datetime, 'SHORT_DATE') if entitlement and entitlement.expired_at_datetime else None
                
                is_fulfilled_entitlement = True if entitlement and entitlement_session else False
                is_unfulfilled_entitlement = True if entitlement and not entitlement_session else False
                
                entitlement_available_sessions = []
                if entitlement:
                  # Grab the available, enrollable sessions for a given entitlement and scrape them for relevant attributes
                  entitlement_available_sessions = [{
                    'session_id': course['key'],
                    'enrollment_end': course['enrollment_end'],
                    'pacing_type': course['pacing_type'],
                    'advertised_start': CourseOverview.get_from_id(CourseKey.from_string(course['key'])).advertised_start,
                    'start': CourseOverview.get_from_id(CourseKey.from_string(course['key'])).start,
                    'end': CourseOverview.get_from_id(CourseKey.from_string(course['key'])).end,
                    } for course in course_entitlement_available_sessions[str(entitlement.uuid)]]
                  if is_fulfilled_entitlement:
                    # If the user has a fulfilled entitlement, pass through the entitlements CourseEnrollment object
                    enrollment = entitlement_session
                  else:
                    # If the user has an unfulfilled entitlement, pass through a bare CourseEnrollment object to populate card with metadata
                    pseudo_session = unfulfilled_entitlement_pseudo_sessions[str(entitlement.uuid)]
                    if not pseudo_session:
                        continue
                    enrollment = CourseEnrollment(user=user, course_id=pseudo_session['key'], mode=pseudo_session['type'])
                  # We only show email settings for entitlement cards if the entitlement has an associated enrollment
                  show_email_settings = is_fulfilled_entitlement and (entitlement_session.course_id in show_email_settings_for)
                else:
                  show_email_settings = (enrollment.course_id in show_email_settings_for)
                
                session_id = enrollment.course_id
                show_courseware_link = (session_id in show_courseware_links_for)
                cert_status = cert_statuses.get(session_id)
                can_refund_entitlement = entitlement and entitlement.is_entitlement_refundable()
                can_unenroll = (not cert_status) or cert_status.get('can_unenroll') if not unfulfilled_entitlement else False
                credit_status = credit_statuses.get(session_id)
                course_mode_info = all_course_modes.get(session_id)
                is_paid_course = True if entitlement else (session_id in enrolled_courses_either_paid)
                is_course_blocked = (session_id in block_courses)
                course_verification_status = verification_status_by_course.get(session_id, {})
                course_requirements = courses_requirements_not_met.get(session_id)
                related_programs = inverted_programs.get(unicode(entitlement.course_uuid if is_unfulfilled_entitlement else session_id))
                show_consent_link = (session_id in consent_required_courses)
                course_overview = enrollment.course_overview
                resume_button_url = resume_button_urls[dashboard_index]
                              
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['course_overview','is_course_blocked','course','is_unfulfilled_entitlement','entitlement_session','can_unenroll','pseudo_session','entitlement','related_programs','credit_status','is_paid_course','course_verification_status','can_refund_entitlement','resume_button_url','show_courseware_link','course_requirements','entitlement_days_until_expiration','entitlement_available_sessions','cert_status','show_email_settings','is_fulfilled_entitlement','show_consent_link','entitlement_expiration','course_mode_info','entitlement_expired_at','session_id','entitlement_expiration_date','enrollment'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n              ')
                runtime._include_file(context, u'dashboard/_dashboard_course_listing.html', _template_uri, course_overview=course_overview, course_card_index=dashboard_index, enrollment=enrollment, is_unfulfilled_entitlement=is_unfulfilled_entitlement, is_fulfilled_entitlement=is_fulfilled_entitlement, entitlement=entitlement, entitlement_session=entitlement_session, entitlement_available_sessions=entitlement_available_sessions, entitlement_expiration_date=entitlement_expiration_date, entitlement_expired_at=entitlement_expired_at, show_courseware_link=show_courseware_link, cert_status=cert_status, can_refund_entitlement=can_refund_entitlement, can_unenroll=can_unenroll, credit_status=credit_status, show_email_settings=show_email_settings, course_mode_info=course_mode_info, is_paid_course=is_paid_course, is_course_blocked=is_course_blocked, verification_status=course_verification_status, course_requirements=course_requirements, dashboard_index=dashboard_index, share_settings=share_settings, user=user, related_programs=related_programs, display_course_modes_on_dashboard=display_course_modes_on_dashboard, show_consent_link=show_consent_link, enterprise_customer_name=enterprise_customer_name, resume_button_url=resume_button_url)
                __M_writer(u'\n')
            __M_writer(u'\n            </ul>\n')
        else:
            __M_writer(u'            <div class="empty-dashboard-message">\n')
            if display_dashboard_courses:
                __M_writer(u'                <p>')
                __M_writer(filters.html_escape(filters.decode.utf8(_("You are not enrolled in any courses yet."))))
                __M_writer(u'</p>\n')
                if empty_dashboard_message:
                    __M_writer(u'                  <p class="custom-message">')
                    __M_writer(filters.decode.utf8(empty_dashboard_message ))
                    __M_writer(u'</p>\n')
                if settings.FEATURES.get('COURSES_ARE_BROWSABLE'):
                    __M_writer(u'                  <a class="btn btn-primary" href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('COURSES'))))
                    __M_writer(u'">\n                    ')
                    __M_writer(filters.html_escape(filters.decode.utf8(_("Explore courses"))))
                    __M_writer(u'\n                  </a>\n')
            else:
                __M_writer(u'              <p>')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Activate your account!"))))
                __M_writer(u'</p>\n              <p class="custom-message">')
                __M_writer(filters.decode.utf8( activate_account_message ))
                __M_writer(u'</p>\n')
            __M_writer(u'          </div>\n')
        __M_writer(u'\n')
        if staff_access and len(errored_courses) > 0:
            __M_writer(u'            <div id="course-errors">\n              <h2>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Course-loading errors"))))
            __M_writer(u'</h2>\n\n')
            for course_dir, errors in errored_courses.items():
                __M_writer(u'               <h3>')
                __M_writer(filters.html_escape(filters.decode.utf8(course_dir)))
                __M_writer(u'</h3>\n                   <ul>\n')
                for (msg, err) in errors:
                    __M_writer(u'                     <li>')
                    __M_writer(filters.html_escape(filters.decode.utf8(msg)))
                    __M_writer(u'\n                       <ul><li><pre>')
                    __M_writer(filters.html_escape(filters.decode.utf8(err)))
                    __M_writer(u'</pre></li></ul>\n                     </li>\n')
                __M_writer(u'                   </ul>\n')
            __M_writer(u'            </div>\n')
        __M_writer(u'        </div>\n      </div>\n      <div class="side-container">\n')
        if display_sidebar_account_activation_message:
            __M_writer(u'          <div class="sidebar-notification">\n            ')
            runtime._include_file(context, (static.get_template_path('registration/account_activation_sidebar_notice.html')), _template_uri)
            __M_writer(u'\n          </div>\n')
        __M_writer(u'\n')
        if settings.FEATURES.get('ENABLE_DASHBOARD_SEARCH'):
            __M_writer(u'          <div id="dashboard-search-bar" class="search-bar dashboard-search-bar" role="search" aria-label="Dashboard">\n            <form class="search-form">\n              <label for="dashboard-search-input">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Search Your Courses"))))
            __M_writer(u'</label>\n              <div class="search-field-wrapper">\n                <input id="dashboard-search-input" type="text" class="search-field"/>\n                <button type="submit" class="search-button" title="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Search'))))
            __M_writer(u'">\n                  <span class="icon fa fa-search" aria-hidden="true"></span>\n                </button>\n                <button type="button" class="cancel-button" title="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Clear search'))))
            __M_writer(u'">\n                  <span class="icon fa fa-remove" aria-hidden="true"></span>\n                </button>\n              </div>\n            </form>\n          </div>\n          <div id="dashboard-search-results" class="search-results dashboard-search-results"></div>\n')
        __M_writer(u'\n')
        if display_sidebar_on_dashboard:
            __M_writer(u'          <div class="profile-sidebar" id="profile-sidebar" role="region" aria-label="Account Status Info">\n            <header class="profile">\n              <h2 class="account-status-title sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Account Status Info"))))
            __M_writer(u': </h2>\n            </header>\n            <div class="user-info">\n              <ul>\n\n')
            if len(order_history_list):
                __M_writer(u'                <li class="order-history">\n                  <span class="title">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Order History"))))
                __M_writer(u'</span>\n')
                for order_history_item in order_history_list:
                    __M_writer(u'                    <span><a href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(order_history_item['receipt_url'])))
                    __M_writer(u'" target="_blank" class="edit-name">')
                    __M_writer(filters.html_escape(filters.decode.utf8(order_history_item['order_date'])))
                    __M_writer(u'</a></span>\n')
                __M_writer(u'                </li>\n')
            __M_writer(u'\n                ')
            runtime._include_file(context, (static.get_template_path('dashboard/_dashboard_status_verification.html')), _template_uri)
            __M_writer(u'\n\n              </ul>\n            </div>\n          </div>\n')
        __M_writer(u'      </div>\n    </div>\n</main>\n\n<div id="email-settings-modal" class="modal" aria-hidden="true">\n  <div class="inner-wrapper" role="dialog" aria-labelledby="email-settings-title">\n    <button class="close-modal">\n      <span class="icon fa fa-remove" aria-hidden="true"></span>\n      <span class="sr">\n')
        __M_writer(u'        ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Close"))))
        __M_writer(u'\n      </span>\n    </button>\n\n    <header>\n      <h2 id="email-settings-title">\n        ')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("Email Settings for {course_number}")).format(course_number=HTML('<span id="email_settings_course_number"></span>')))))
        __M_writer(u'\n        <span class="sr">,\n')
        __M_writer(u'          ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("window open"))))
        __M_writer(u'\n        </span>\n      </h2>\n      <hr/>\n    </header>\n\n    <form id="email_settings_form" method="post">\n      <input name="course_id" id="email_settings_course_id" type="hidden" />\n      <label><input type="checkbox" id="receive_emails" name="receive_emails" />')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Receive course emails"))))
        __M_writer(u' </label>\n      <div class="submit">\n        <input type="submit" id="submit" value="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Save Settings'))))
        __M_writer(u'" />\n      </div>\n    </form>\n  </div>\n</div>\n\n<div id="unenroll-modal" class="modal unenroll-modal" aria-hidden="true">\n  <div class="inner-wrapper" role="dialog" aria-labelledby="unenrollment-modal-title" aria-live="polite">\n    <button class="close-modal">\n      <span class="icon fa fa-remove" aria-hidden="true"></span>\n      <span class="sr">\n')
        __M_writer(u'        ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Close"))))
        __M_writer(u'\n      </span>\n    </button>\n\n    <header class="unenroll-header">\n      <h2 id="unenrollment-modal-title">\n        <span id=\'track-info\'></span>\n        <span id=\'refund-info\'></span>\n        <span class="sr">,\n')
        __M_writer(u'          ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("window open"))))
        __M_writer(u'\n        </span>\n      </h2>\n      <hr/>\n    </header>\n    <div id="unenroll_error" class="modal-form-error"></div>\n    <form id="unenroll_form" method="post" data-remote="true" action="')
        __M_writer(filters.html_escape(filters.decode.utf8(reverse('change_enrollment'))))
        __M_writer(u'">\n      <input name="course_id" id="unenroll_course_id" type="hidden" />\n      <input name="enrollment_action" type="hidden" value="unenroll" />\n      <div class="submit">\n        <input class="submit-button" name="submit" type="submit" value="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Unenroll'))))
        __M_writer(u'" />\n      </div>\n    </form>\n  </div>\n</div>\n\n')
        runtime._include_file(context, u'dashboard/_dashboard_entitlement_unenrollment_modal.html', _template_uri)
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagetitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pagetitle():
            return render_pagetitle(context)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(filters.decode.utf8(_("Dashboard"))))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_extras(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_extras():
            return render_header_extras(context)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n')
        for template_name in ["donation"]:
            __M_writer(u'<script type="text/template" id="')
            __M_writer(filters.html_escape(filters.decode.utf8(template_name)))
            __M_writer(u'-tpl">\n  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.include(path=u'dashboard/' + (template_name) + u'.underscore'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyclass():
            return render_bodyclass(context)
        __M_writer = context.writer()
        __M_writer(u'view-dashboard is-authenticated')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "learnerdashboard" 
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        redirect_message = context.get('redirect_message', UNDEFINED)
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  <script src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/commerce/credit.js'))))
        __M_writer(u'"></script>\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.js(group=u'dashboard'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n  <script type="text/javascript">\n    $(document).ready(function() {\n      edx.dashboard.legacy.init({\n        dashboard: "')
        __M_writer(js_escaped_string(reverse('dashboard') ))
        __M_writer(u'",\n        signInUser: "')
        __M_writer(js_escaped_string(reverse('signin_user') ))
        __M_writer(u'",\n        changeEmailSettings: "')
        __M_writer(js_escaped_string(reverse('change_email_settings') ))
        __M_writer(u'"\n      });\n    });\n  </script>\n  ')
        def ccall(caller):
            def body():
                marketing_link = context.get('marketing_link', UNDEFINED)
                __M_writer = context.writer()
                __M_writer(u'\n    UnenrollmentFactory({\n      urls: {\n        dashboard: "')
                __M_writer(js_escaped_string(reverse('dashboard') ))
                __M_writer(u'",\n        signInUser: "')
                __M_writer(js_escaped_string(reverse('signin_user') ))
                __M_writer(u'",\n        changeEmailSettings: "')
                __M_writer(js_escaped_string(reverse('change_email_settings') ))
                __M_writer(u'",\n        browseCourses: "')
                __M_writer(js_escaped_string(marketing_link('COURSES') ))
                __M_writer(u'"\n      },\n      isEdx: false\n    });\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'UnenrollmentFactory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                marketing_link = context.get('marketing_link', UNDEFINED)
                __M_writer = context.writer()
                __M_writer(u'\n')
                __M_writer(u'    $(document).ready(function() {\n      EntitlementUnenrollmentFactory({\n        dashboardPath: "')
                __M_writer(js_escaped_string(reverse('dashboard') ))
                __M_writer(u'",\n        signInPath: "')
                __M_writer(js_escaped_string(reverse('signin_user') ))
                __M_writer(u'",\n        browseCourses: "')
                __M_writer(js_escaped_string(marketing_link('COURSES') ))
                __M_writer(u'",\n        isEdx: false\n      });\n    });\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'EntitlementUnenrollmentFactory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        if settings.FEATURES.get('ENABLE_DASHBOARD_SEARCH'):
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    __M_writer(u'\n        DashboardSearchFactory();\n    ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'DashboardSearchFactory',module_name=u'course_search/js/dashboard_search_factory'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        if redirect_message:
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    __M_writer(u"\n        var banner = new MessageBannerView({urgency: 'low', type: 'warning'});\n        $('#content').prepend(banner.$el);\n        banner.showMessage(")
                    __M_writer(dump_js_escaped_json(redirect_message ))
                    __M_writer(u')\n    ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'MessageBannerView',module_name=u'js/views/message_banner'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 5, "41": 4, "47": 1, "102": 1, "103": 2, "104": 3, "105": 4, "106": 21, "107": 23, "114": 26, "119": 29, "124": 30, "129": 38, "134": 87, "135": 91, "136": 92, "137": 93, "138": 93, "139": 96, "140": 97, "141": 98, "142": 99, "143": 99, "144": 102, "145": 103, "146": 104, "147": 105, "148": 105, "149": 108, "150": 109, "151": 110, "152": 111, "153": 112, "154": 112, "155": 112, "156": 114, "157": 114, "158": 118, "159": 120, "160": 127, "161": 128, "162": 128, "163": 128, "164": 130, "165": 131, "166": 132, "167": 133, "176": 138, "177": 139, "178": 140, "179": 140, "235": 192, "236": 193, "237": 193, "238": 195, "239": 197, "240": 198, "241": 199, "242": 200, "243": 200, "244": 200, "245": 201, "246": 202, "247": 202, "248": 202, "249": 204, "250": 205, "251": 205, "252": 205, "253": 206, "254": 206, "255": 209, "256": 210, "257": 210, "258": 210, "259": 211, "260": 211, "261": 213, "262": 215, "263": 216, "264": 217, "265": 218, "266": 218, "267": 220, "268": 221, "269": 221, "270": 221, "271": 223, "272": 224, "273": 224, "274": 224, "275": 225, "276": 225, "277": 228, "278": 230, "279": 232, "280": 235, "281": 236, "282": 237, "283": 237, "284": 240, "285": 241, "286": 242, "287": 244, "288": 244, "289": 247, "290": 247, "291": 250, "292": 250, "293": 258, "294": 259, "295": 260, "296": 262, "297": 262, "298": 267, "299": 268, "300": 269, "301": 269, "302": 270, "303": 271, "304": 271, "305": 271, "306": 271, "307": 271, "308": 273, "309": 275, "310": 276, "311": 276, "312": 282, "313": 292, "314": 292, "315": 292, "316": 298, "317": 298, "318": 301, "319": 301, "320": 301, "321": 309, "322": 309, "323": 311, "324": 311, "325": 323, "326": 323, "327": 323, "328": 333, "329": 333, "330": 333, "331": 339, "332": 339, "333": 343, "334": 343, "335": 349, "336": 349, "342": 29, "348": 29, "354": 32, "361": 32, "362": 33, "363": 34, "364": 34, "365": 34, "373": 35, "376": 35, "382": 30, "388": 30, "394": 3, "398": 3, "405": 40, "414": 40, "415": 41, "416": 41, "424": 42, "427": 42, "428": 46, "429": 46, "430": 47, "431": 47, "432": 48, "433": 48, "438": 52, "439": 55, "440": 55, "441": 56, "442": 56, "443": 57, "444": 57, "445": 58, "446": 58, "451": 52, "454": 62, "459": 63, "460": 66, "461": 68, "462": 68, "463": 69, "464": 69, "465": 70, "466": 70, "471": 63, "474": 74, "475": 75, "476": 76, "480": 76, "485": 76, "488": 78, "489": 80, "490": 81, "494": 81, "495": 84, "496": 84, "501": 81, "504": 85, "510": 504}, "uri": "custome-theme/lms/templates/dashboard.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/themes/custome-theme/lms/templates/dashboard.html"}
__M_END_METADATA
"""
