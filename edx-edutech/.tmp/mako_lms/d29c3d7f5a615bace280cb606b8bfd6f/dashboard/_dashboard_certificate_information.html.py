# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580284734.166838
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/dashboard/_dashboard_certificate_information.html'
_template_uri = u'dashboard/_dashboard_certificate_information.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text
from course_modes.models import CourseMode


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,cert_status,course_overview,enrollment,reverify_link,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(cert_status=cert_status,course_overview=course_overview,enrollment=enrollment,pageargs=pageargs,reverify_link=reverify_link)
        user_timezone = context.get('user_timezone', UNDEFINED)
        user_language = context.get('user_language', UNDEFINED)
        float = context.get('float', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')

        cert_name_short = course_overview.cert_name_short
        if cert_name_short == "":
          cert_name_short = settings.CERT_NAME_SHORT
        
        cert_name_long = course_overview.cert_name_long
        if cert_name_long == "":
          cert_name_long = settings.CERT_NAME_LONG
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['cert_name_long','cert_name_short'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')

        if cert_status['status'] == 'certificate_earned_but_not_available':
            status_css_class = 'course-status-processing'
        elif cert_status['status'] == 'generating':
            status_css_class = 'course-status-certrendering'
        elif cert_status['status'] == 'downloadable':
            status_css_class = 'course-status-certavailable'
        elif cert_status['status'] == 'notpassing':
            status_css_class = 'course-status-certnotavailable'
        else:
            status_css_class = 'course-status-processing'
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['status_css_class'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if cert_status['status'] != 'processing':
            if cert_status['status'] == 'certificate_earned_but_not_available':
                __M_writer(u'    <div class="message message-status ')
                __M_writer(filters.html_escape(filters.decode.utf8(status_css_class)))
                __M_writer(u' is-shown">\n      <p class="message-copy">\n        ')

                certificate_available_date_string = course_overview.certificate_available_date.strftime('%Y-%m-%dT%H:%M:%S%z')
                container_string = _("Your certificate will be available on or before {date}")
                format = 'shortDate'
                        
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['certificate_available_date_string','container_string','format'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n        <span class="info-date-block localized-datetime" data-language="')
                __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                __M_writer(u'" data-timezone="')
                __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                __M_writer(u'" data-datetime="')
                __M_writer(filters.html_escape(filters.decode.utf8(certificate_available_date_string)))
                __M_writer(u'" data-format=')
                __M_writer(filters.html_escape(filters.decode.utf8(format)))
                __M_writer(u' data-string="')
                __M_writer(filters.html_escape(filters.decode.utf8(container_string)))
                __M_writer(u'"></span>\n      </p>\n    </div>\n')
            else:
                __M_writer(u'    <div class="message message-status ')
                __M_writer(filters.html_escape(filters.decode.utf8(status_css_class)))
                __M_writer(u' is-shown">\n      <p class="message-copy">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Your final grade:"))))
                __M_writer(u'\n        <span class="grade-value">')
                __M_writer(filters.html_escape(filters.decode.utf8("{0:.0f}%".format(float(cert_status['grade'])*100))))
                __M_writer(u'</span>.\n\n')
                if cert_status['status'] == 'notpassing':
                    if enrollment.mode != 'audit':
                        __M_writer(u'            ')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Grade required for a {cert_name_short}:").format(cert_name_short=cert_name_short))))
                        __M_writer(u'\n')
                    else:
                        __M_writer(u'            ')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Grade required to pass this course:"))))
                        __M_writer(u'\n')
                    __M_writer(u'          <span class="grade-value">')
                    __M_writer(filters.html_escape(filters.decode.utf8("{0:.0f}%".format(float(course_overview.lowest_passing_grade)*100))))
                    __M_writer(u'</span>.\n')
                elif cert_status['status'] == 'restricted' and enrollment.mode == 'verified':
                    __M_writer(u'          <p class="message-copy">\n            ')
                    __M_writer(filters.html_escape(filters.decode.utf8(Text(_("Your verified {cert_name_long} is being held pending confirmation that the issuance of your {cert_name_short} is in compliance with strict U.S. embargoes on Iran, Cuba, Syria and Sudan. If you think our system has mistakenly identified you as being connected with one of those countries, please let us know by contacting {email}. If you would like a refund on your {cert_name_long}, please contact our billing address {billing_email}")).format(email=HTML('<a class="contact-link" href="mailto:{email}">{email}</a>.').format(email=settings.CONTACT_EMAIL), billing_email=HTML('<a class="contact-link" href="mailto:{email}">{email}</a>').format(email=settings.PAYMENT_SUPPORT_EMAIL), cert_name_short=cert_name_short, cert_name_long=cert_name_long))))
                    __M_writer(u'\n          </p>\n')
                elif cert_status['status'] == 'restricted':
                    __M_writer(u'          <p class="message-copy">\n            ')
                    __M_writer(filters.html_escape(filters.decode.utf8(Text(_("Your {cert_name_long} is being held pending confirmation that the issuance of your {cert_name_short} is in compliance with strict U.S. embargoes on Iran, Cuba, Syria and Sudan. If you think our system has mistakenly identified you as being connected with one of those countries, please let us know by contacting {email}.")).format(email=HTML('<a class="contact-link" href="mailto:{email}">{email}</a>.').format(email=settings.CONTACT_EMAIL), cert_name_short=cert_name_short, cert_name_long=cert_name_long))))
                    __M_writer(u'\n          </p>\n')
                elif cert_status['status'] == 'unverified':
                    __M_writer(u'          <p class="message-copy">\n            ')
                    __M_writer(filters.html_escape(filters.decode.utf8(Text(_("Your certificate was not issued because you do not have a current verified identity with {platform_name}. ")).format(platform_name=settings.PLATFORM_NAME))))
                    __M_writer(u'\n            <a href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(reverify_link)))
                    __M_writer(u'"> ')
                    __M_writer(filters.html_escape(filters.decode.utf8(Text(_("Verify your identity now.")))))
                    __M_writer(u'</a>\n          </p>\n')
                __M_writer(u'\n      </p>\n\n')
                if cert_status['status'] == 'generating' or cert_status['status'] == 'downloadable' or cert_status['show_survey_button']:
                    __M_writer(u'        <div class="wrapper-message-primary">\n          <ul class="actions actions-primary">\n')
                    if cert_status['status'] == 'generating':
                        __M_writer(u'              <li class="action">\n                <span class="disabled">\n                  ')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Your {cert_name_short} is Generating").format(cert_name_short=cert_name_short))))
                        __M_writer(u'\n                </span>\n              </li>\n')
                    elif cert_status['status'] == 'downloadable' and cert_status.get('show_cert_web_view', False):
                        __M_writer(u'              <li class="action action-certificate">\n                <a class="btn" href="')
                        __M_writer(filters.html_escape(filters.decode.utf8(cert_status['cert_web_view_url'])))
                        __M_writer(u'" target="_blank"\n                   title="')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('This link will open the certificate web view'))))
                        __M_writer(u'">\n                  ')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("View {cert_name_short}").format(cert_name_short=cert_name_short,))))
                        __M_writer(u'\n                </a>\n              </li>\n')
                    elif cert_status['status'] == 'downloadable' and enrollment.mode in CourseMode.NON_VERIFIED_MODES:
                        __M_writer(u'              <li class="action action-certificate">\n                <a class="btn" href="')
                        __M_writer(filters.html_escape(filters.decode.utf8(cert_status['download_url'])))
                        __M_writer(u'"\n                   title="')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('This link will open/download a PDF document'))))
                        __M_writer(u'">\n                  ')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Download {cert_name_short} (PDF)").format(cert_name_short=cert_name_short,))))
                        __M_writer(u'\n                </a>\n              </li>\n')
                    elif cert_status['status'] == 'downloadable' and enrollment.mode == 'verified' and cert_status['mode'] == 'honor':
                        __M_writer(u'              <li class="action">\n                <a class="btn" href="')
                        __M_writer(filters.html_escape(filters.decode.utf8(cert_status['download_url'])))
                        __M_writer(u'"\n                   title="')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('This link will open/download a PDF document'))))
                        __M_writer(u'">\n                  ')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Download Your {cert_name_short} (PDF)").format(cert_name_short=cert_name_short))))
                        __M_writer(u'\n                </a>\n              </li>\n')
                    elif cert_status['status'] == 'downloadable' and enrollment.mode in CourseMode.VERIFIED_MODES:
                        __M_writer(u'              <li class="action">\n                <a class="btn" href="')
                        __M_writer(filters.html_escape(filters.decode.utf8(cert_status['download_url'])))
                        __M_writer(u'"\n                   title="')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('This link will open/download a PDF document of your verified {cert_name_long}.').format(cert_name_long=cert_name_long))))
                        __M_writer(u'">\n                  ')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Download Your ID Verified {cert_name_short} (PDF)").format(cert_name_short=cert_name_short))))
                        __M_writer(u'\n                </a>\n              </li>\n')
                    __M_writer(u'\n')
                    if cert_status['show_survey_button']:
                        __M_writer(u'              <li class="action">\n                <a class="cta" href="')
                        __M_writer(filters.html_escape(filters.decode.utf8(cert_status['survey_url'])))
                        __M_writer(u'">\n                  ')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Complete our course feedback survey"))))
                        __M_writer(u'\n                </a>\n              </li>\n')
                    __M_writer(u'          </ul>\n        </div>\n\n')
                    if cert_status['status'] == 'downloadable' and cert_status['linked_in_url']:
                        __M_writer(u'          <ul class="actions actions-secondary">\n              <li class="action action-share">\n                <a class="action-linkedin-profile" target="_blank" href="')
                        __M_writer(filters.html_escape(filters.decode.utf8(cert_status['linked_in_url'])))
                        __M_writer(u'"\n                 title="')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('Add Certificate to LinkedIn Profile'))))
                        __M_writer(u'"\n                 data-course-id="')
                        __M_writer(filters.html_escape(filters.decode.utf8(course_overview.id)))
                        __M_writer(u'"\n                 data-certificate-mode="')
                        __M_writer(filters.html_escape(filters.decode.utf8(cert_status['mode'])))
                        __M_writer(u'"\n                >\n                  <img class="action-linkedin-profile-img"\n                       src="')
                        __M_writer(filters.html_escape(filters.decode.utf8(static.url('images/linkedin_add_to_profile.png'))))
                        __M_writer(u'"\n                       alt="')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('Share on LinkedIn'))))
                        __M_writer(u'">\n                </a>\n            </li>\n          </ul>\n')
                __M_writer(u'\n')
                if cert_status['status'] == 'downloadable' and enrollment.mode == 'verified' and cert_status['mode'] == 'honor':
                    __M_writer(u'        <div class="certificate-explanation">\n            ')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Since we did not have a valid set of verification photos from you when your {cert_name_long} was generated, we could not grant you a verified {cert_name_short}. An honor code {cert_name_short} has been granted instead.').format(cert_name_short=cert_name_short, cert_name_long=cert_name_long))))
                    __M_writer(u'\n        </div>\n')
                __M_writer(u'\n    </div>\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "29": 8, "32": 1, "42": 1, "43": 7, "44": 8, "45": 10, "57": 18, "58": 20, "73": 31, "74": 33, "75": 34, "76": 35, "77": 35, "78": 35, "79": 37, "87": 41, "88": 42, "89": 42, "90": 42, "91": 42, "92": 42, "93": 42, "94": 42, "95": 42, "96": 42, "97": 42, "98": 45, "99": 46, "100": 46, "101": 46, "102": 47, "103": 47, "104": 48, "105": 48, "106": 50, "107": 51, "108": 52, "109": 52, "110": 52, "111": 53, "112": 54, "113": 54, "114": 54, "115": 56, "116": 56, "117": 56, "118": 57, "119": 58, "120": 59, "121": 59, "122": 61, "123": 62, "124": 63, "125": 63, "126": 65, "127": 66, "128": 67, "129": 67, "130": 68, "131": 68, "132": 68, "133": 68, "134": 71, "135": 74, "136": 75, "137": 77, "138": 78, "139": 80, "140": 80, "141": 83, "142": 84, "143": 85, "144": 85, "145": 86, "146": 86, "147": 87, "148": 87, "149": 90, "150": 91, "151": 92, "152": 92, "153": 93, "154": 93, "155": 94, "156": 94, "157": 97, "158": 98, "159": 99, "160": 99, "161": 100, "162": 100, "163": 101, "164": 101, "165": 104, "166": 105, "167": 106, "168": 106, "169": 107, "170": 107, "171": 108, "172": 108, "173": 112, "174": 113, "175": 114, "176": 115, "177": 115, "178": 116, "179": 116, "180": 120, "181": 123, "182": 124, "183": 126, "184": 126, "185": 127, "186": 127, "187": 128, "188": 128, "189": 129, "190": 129, "191": 132, "192": 132, "193": 133, "194": 133, "195": 139, "196": 140, "197": 141, "198": 142, "199": 142, "200": 145, "201": 149, "207": 201}, "uri": "dashboard/_dashboard_certificate_information.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/dashboard/_dashboard_certificate_information.html"}
__M_END_METADATA
"""
