# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580297646.636522
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/courseware/progress.html'
_template_uri = 'courseware/progress.html'
_source_encoding = 'utf-8'
_exports = [u'certificate_block', u'bodyclass', 'online_help_token', u'pagetitle', u'js_extra', u'headextra']



from course_modes.models import CourseMode
from lms.djangoapps.certificates.models import CertificateStatuses
from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text
from django.urls import reverse
from django.conf import settings
from django.utils.http import urlquote_plus
from six import text_type

from openedx.features.enterprise_support.utils import get_enterprise_learner_generic_name


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'/static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

    ns = runtime.TemplateNamespace(u'progress_graph', context._clean_inheritance_tokens(), templateuri=u'/courseware/progress_graph.js', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'progress_graph')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/main.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        loop = __M_loop = runtime.LoopStack()
        def certificate_block():
            return render_certificate_block(context._locals(__M_locals))
        int = context.get('int', UNDEFINED)
        float = context.get('float', UNDEFINED)
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        course = context.get('course', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        unicode = context.get('unicode', UNDEFINED)
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        credit_course_requirements = context.get('credit_course_requirements', UNDEFINED)
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        studio_url = context.get('studio_url', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        course_expiration_fragment = context.get('course_expiration_fragment', UNDEFINED)
        user_timezone = context.get('user_timezone', UNDEFINED)
        len = context.get('len', UNDEFINED)
        student = context.get('student', UNDEFINED)
        user_language = context.get('user_language', UNDEFINED)
        staff_access = context.get('staff_access', UNDEFINED)
        certificate_data = context.get('certificate_data', UNDEFINED)
        progress_graph = _mako_get_namespace(context, 'progress_graph')
        request = context.get('request', UNDEFINED)
        grade_summary = context.get('grade_summary', UNDEFINED)
        def headextra():
            return render_headextra(context._locals(__M_locals))
        courseware_summary = context.get('courseware_summary', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')

        username = get_enterprise_learner_generic_name(request) or student.username
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['username'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headextra'):
            context['self'].headextra(**pageargs)
        

        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n\n')
        runtime._include_file(context, u'/courseware/course_navigation.html', _template_uri, active_page='progress')
        __M_writer(u'\n\n<main id="main" aria-label="Content" tabindex="-1">\n    <div class="container">\n        <div class="profile-wrapper">\n            <section class="course-info" id="course-info-progress"\n')
        if getattr(course, 'language'):
            __M_writer(u'                lang="')
            __M_writer(filters.html_escape(filters.decode.utf8(course.language)))
            __M_writer(u'"\n')
        __M_writer(u'              >\n')
        if staff_access and studio_url is not None:
            __M_writer(u'                <div class="wrap-instructor-info">\n                    <a class="instructor-info-action studio-view" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(studio_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("View Grading in studio"))))
            __M_writer(u'</a>\n                </div>\n')
        __M_writer(u'                <h2 class="hd hd-2 progress-certificates-title">\n                    ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Course Progress for Student '{username}' ({email})").format(username=username, email=student.email))))
        __M_writer(u'\n                </h2>\n')
        if course_expiration_fragment:
            __M_writer(u'                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(course_expiration_fragment.content))))
            __M_writer(u'\n')
        __M_writer(u'                <div class="wrapper-msg wrapper-auto-cert">\n                    <div id="errors-info" class="errors-info"></div>\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'certificate_block'):
            context['self'].certificate_block(**pageargs)
        

        __M_writer(u'\n                </div>\n\n')
        if not course.disable_progress_graph:
            __M_writer(u'                <div class="grade-detail-graph" id="grade-detail-graph"></div>\n')
        __M_writer(u'\n')
        if credit_course_requirements:
            __M_writer(u'                <section class="credit-eligibility">\n                    <h3 class="hd hd-4 eligibility-heading">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Requirements for Course Credit"))))
            __M_writer(u'</h3>\n                    <div class="credit-eligibility-container">\n')
            if credit_course_requirements['eligibility_status'] == 'not_eligible':
                __M_writer(u'                        <span class="eligibility_msg">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("{student_name}, you are no longer eligible for credit in this course.").format(student_name=student.profile.name))))
                __M_writer(u'</span>\n')
            elif credit_course_requirements['eligibility_status'] == 'eligible':
                __M_writer(u'                        <span class="eligibility_msg">\n                            ')
                __M_writer(filters.html_escape(filters.decode.utf8(Text(_("{student_name}, you have met the requirements for credit in this course. {a_start}Go to your dashboard{a_end} to purchase course credit.")).format(
                                student_name=student.profile.name,
                                a_start=HTML("<a href={url}>").format(url=reverse('dashboard')),
                                a_end=HTML("</a>")
                            ))))
                __M_writer(u'\n                        </span>\n')
            elif credit_course_requirements['eligibility_status'] == 'partial_eligible':
                __M_writer(u'                        <span>')
                __M_writer(filters.html_escape(filters.decode.utf8(_("{student_name}, you have not yet met the requirements for credit.").format(student_name=student.profile.name))))
                __M_writer(u'</span>\n')
            __M_writer(u'\n                        <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(settings.CREDIT_HELP_LINK_URL)))
            __M_writer(u'" class="credit-help">\n                            <span class="fa fa-question" aria-hidden="true"></span>\n                            <span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Information about course credit requirements"))))
            __M_writer(u'</span>\n                        </a><br />\n\n                        <div class="requirement-container" data-eligible="')
            __M_writer(filters.html_escape(filters.decode.utf8(credit_course_requirements['eligibility_status'])))
            __M_writer(u'">\n')
            for requirement in credit_course_requirements['requirements']:
                __M_writer(u'                            <div class="requirement">\n                                <div class="requirement-name">\n                                    ')
                __M_writer(filters.html_escape(filters.decode.utf8(_(requirement['display_name']))))
                __M_writer(u'\n')
                if requirement['namespace'] == 'grade':
                    __M_writer(u'                                    <span>')
                    __M_writer(filters.html_escape(filters.decode.utf8(int(requirement['criteria']['min_grade'] * 100))))
                    __M_writer(u'%</span>\n')
                __M_writer(u'                                </div>\n                                <div class="requirement-status">\n')
                if requirement['status']:
                    if requirement['status'] == 'submitted':
                        __M_writer(u'                                        <span class="requirement-submitted">')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Verification Submitted"))))
                        __M_writer(u'</span>\n')
                    elif requirement['status'] == 'failed':
                        __M_writer(u'                                        <span class="fa fa-times" aria-hidden="true"></span>\n                                        <span>')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Verification Failed" ))))
                        __M_writer(u'</span>\n')
                    elif requirement['status'] == 'declined':
                        __M_writer(u'                                        <span class="fa fa-times" aria-hidden="true"></span>\n                                        <span>')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Verification Declined" ))))
                        __M_writer(u'</span>\n')
                    elif requirement['status'] == 'satisfied':
                        __M_writer(u'                                        <span class="fa fa-check" aria-hidden="true"></span>\n                                        <span class="localized-datetime" data-datetime="')
                        __M_writer(filters.html_escape(filters.decode.utf8(requirement['status_date'])))
                        __M_writer(u'" data-string="')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('Completed by {date}'))))
                        __M_writer(u'" data-timezone="')
                        __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                        __M_writer(u'" data-language="')
                        __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                        __M_writer(u'"></span>\n')
                else:
                    __M_writer(u'                                    <span class="not-achieve">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_("Upcoming"))))
                    __M_writer(u'</span>\n')
                __M_writer(u'                                </div>\n                            </div>\n')
            __M_writer(u'                        </div>\n                        <button class="detail-collapse">\n                            <span class="fa fa-caret-up" aria-hidden="true"></span>\n                            <span class="requirement-detail">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Less"))))
            __M_writer(u'</span>\n                        </button>\n                    </div>\n                </section>\n')
        __M_writer(u'\n')
        if courseware_summary:
            __M_writer(u'                <section class="chapters">\n                    <h2 class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Details for each chapter'))))
            __M_writer(u'</h2>\n')
            loop = __M_loop._enter(courseware_summary)
            try:
                for chapter in loop:
                    if not chapter['display_name'] == "hidden":
                        __M_writer(u'                        <section aria-labelledby="chapter_')
                        __M_writer(filters.html_escape(filters.decode.utf8(loop.index)))
                        __M_writer(u'">\n                            <h3 class="hd hd-3" id="chapter_')
                        __M_writer(filters.html_escape(filters.decode.utf8(loop.index)))
                        __M_writer(u'">')
                        __M_writer(filters.html_escape(filters.decode.utf8( chapter['display_name'])))
                        __M_writer(u'</h3>\n                            <div class="sections">\n')
                        for section in chapter['sections']:
                            __M_writer(u'                                    <div>\n                                        ')

                            earned = section.all_total.earned
                            total = section.all_total.possible
                            
                            percentageString = "{0:.0%}".format(section.percent_graded) if earned > 0 and total > 0 else ""
                            
                            
                            __M_locals_builtin_stored = __M_locals_builtin()
                            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['percentageString','total','earned'] if __M_key in __M_locals_builtin_stored]))
                            __M_writer(u'\n                                        <h4 class="hd hd-4">\n                                            <a href="')
                            __M_writer(filters.html_escape(filters.decode.utf8(reverse('courseware_section', kwargs=dict(course_id=text_type(course.id), chapter=chapter['url_name'], section=section.url_name)))))
                            __M_writer(u'">\n                                                ')
                            __M_writer(filters.html_escape(filters.decode.utf8( section.display_name)))
                            __M_writer(u'\n')
                            if total > 0 or earned > 0:
                                __M_writer(u'                                                <span class="sr">\n                                                    ')
                                __M_writer(filters.html_escape(filters.decode.utf8(_("{earned} of {total} possible points").format(earned='{:.3n}'.format(float(earned)), total='{:.3n}'.format(float(total))))))
                                __M_writer(u'\n                                                </span>\n')
                            __M_writer(u'                                            </a>\n')
                            if total > 0 or earned > 0:
                                __M_writer(u'                                            <span> ')
                                __M_writer(filters.html_escape(filters.decode.utf8("({0:.3n}/{1:.3n}) {2}".format( float(earned), float(total), percentageString ))))
                                __M_writer(u'</span>\n')
                            __M_writer(u'                                        </h4>\n                                        <p>\n')
                            if section.format is not None:
                                __M_writer(u'                                                ')
                                __M_writer(filters.html_escape(filters.decode.utf8(section.format)))
                                __M_writer(u'\n')
                            if section.due is not None:
                                __M_writer(u'                                                <em class="localized-datetime" data-datetime="')
                                __M_writer(filters.html_escape(filters.decode.utf8(section.due)))
                                __M_writer(u'" data-string="')
                                __M_writer(filters.html_escape(filters.decode.utf8(_('due {date}'))))
                                __M_writer(u'" data-timezone="')
                                __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                                __M_writer(u'" data-language="')
                                __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                                __M_writer(u'"></em>\n')
                            __M_writer(u'                                        </p>\n                                        <p class="override-notice">\n')
                            if section.override is not None:
                                if section.format is not None and section.format == "Exam":
                                    __M_writer(u'                                                    ')
                                    __M_writer(filters.html_escape(filters.decode.utf8(_("Suspicious activity detected during proctored exam review. Exam score 0."))))
                                    __M_writer(u'\n')
                                else:
                                    __M_writer(u'                                                    ')
                                    __M_writer(filters.html_escape(filters.decode.utf8(_("Section grade has been overridden."))))
                                    __M_writer(u'\n')
                            __M_writer(u'                                        </p>\n')
                            if len(section.problem_scores.values()) > 0:
                                if section.show_grades(staff_access):
                                    __M_writer(u'                                          <dl class="scores">\n                                              <dt class="hd hd-6">')
                                    __M_writer(filters.html_escape(filters.decode.utf8( _("Problem Scores: ") if section.graded else _("Practice Scores: "))))
                                    __M_writer(u'</dt>\n')
                                    for score in section.problem_scores.values():
                                        __M_writer(u'                                              <dd>')
                                        __M_writer(filters.html_escape(filters.decode.utf8("{0:.3n}/{1:.3n}".format(float(score.earned),float(score.possible)))))
                                        __M_writer(u'</dd>\n')
                                    __M_writer(u'                                          </dl>\n')
                                else:
                                    __M_writer(u'                                            <p class="hide-scores">\n')
                                    if section.show_correctness == 'past_due':
                                        if section.graded:
                                            __M_writer(u'                                                  ')
                                            __M_writer(filters.html_escape(filters.decode.utf8(_("Problem scores are hidden until the due date."))))
                                            __M_writer(u'\n')
                                        else:
                                            __M_writer(u'                                                  ')
                                            __M_writer(filters.html_escape(filters.decode.utf8(_("Practice scores are hidden until the due date."))))
                                            __M_writer(u'\n')
                                    else:
                                        if section.graded:
                                            __M_writer(u'                                                  ')
                                            __M_writer(filters.html_escape(filters.decode.utf8(_("Problem scores are hidden."))))
                                            __M_writer(u'\n')
                                        else:
                                            __M_writer(u'                                                  ')
                                            __M_writer(filters.html_escape(filters.decode.utf8(_("Practice scores are hidden."))))
                                            __M_writer(u'\n')
                                    __M_writer(u'                                            </p>\n')
                            else:
                                __M_writer(u'                                        <p class="no-scores">')
                                __M_writer(filters.html_escape(filters.decode.utf8(_("No problem scores in this section"))))
                                __M_writer(u'</p>\n')
                            __M_writer(u'                                    </div>\n')
                        __M_writer(u'                            </div>\n                        </section>\n')
            finally:
                loop = __M_loop._exit()
            __M_writer(u'                </section>\n')
        __M_writer(u'            </section>\n        </div>\n    </div>\n</main>\n')
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


def render_certificate_block(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        certificate_data = context.get('certificate_data', UNDEFINED)
        course = context.get('course', UNDEFINED)
        def certificate_block():
            return render_certificate_block(context)
        unicode = context.get('unicode', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if certificate_data:
            __M_writer(u'                        <div class="auto-cert-message" id="course-success">\n                            <div class="has-actions">\n                                ')
            post_url = reverse('generate_user_cert', args=[unicode(course.id)]) 
            
            __M_writer(u'\n                                <div class="msg-content">\n                                    <h4 class="hd hd-4 title">')
            __M_writer(filters.html_escape(filters.decode.utf8(_(certificate_data.title))))
            __M_writer(u'</h4>\n                                    <p class="copy">')
            __M_writer(filters.html_escape(filters.decode.utf8(_(certificate_data.msg))))
            __M_writer(u'</p>\n                                </div>\n                                <div class="msg-actions">\n')
            if certificate_data.cert_web_view_url:
                __M_writer(u'                                    <a class="btn" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(certificate_data.cert_web_view_url)))
                __M_writer(u'" target="_blank">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("View Certificate"))))
                __M_writer(u' <span class="sr">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Opens in a new browser window"))))
                __M_writer(u'</span></a>\n')
            elif certificate_data.cert_status == CertificateStatuses.downloadable and certificate_data.download_url:
                __M_writer(u'                                    <a class="btn" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(certificate_data.download_url)))
                __M_writer(u'" target="_blank">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Download Your Certificate"))))
                __M_writer(u' <span class="sr">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Opens in a new browser window"))))
                __M_writer(u'</span></a>\n')
            elif certificate_data.cert_status == CertificateStatuses.requesting:
                __M_writer(u'                                    <button class="btn generate_certs" data-endpoint="')
                __M_writer(filters.html_escape(filters.decode.utf8(post_url)))
                __M_writer(u'" id="btn_generate_cert">')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Request Certificate'))))
                __M_writer(u'</button>\n')
            __M_writer(u'                                </div>\n                            </div>\n                        </div>\n')
        __M_writer(u'                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyclass():
            return render_bodyclass(context)
        __M_writer = context.writer()
        __M_writer(u'view-in-course view-progress')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "progress" 
        
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
        __M_writer(filters.html_escape(filters.decode.utf8(_("{course_number} Progress").format(course_number=course.display_number_with_default))))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        course = context.get('course', UNDEFINED)
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        grade_summary = context.get('grade_summary', UNDEFINED)
        progress_graph = _mako_get_namespace(context, 'progress_graph')
        __M_writer = context.writer()
        __M_writer(u'\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/flot/jquery.flot.js'))))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/flot/jquery.flot.stack.js'))))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/flot/jquery.flot.symbol.js'))))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/courseware/certificates_api.js'))))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/courseware/credit_progress.js'))))
        __M_writer(u'"></script>\n<script>\n')
        __M_writer(u'    ')
        __M_writer(filters.html_escape(filters.decode.utf8(progress_graph.body(grade_summary, course.grade_cutoffs, "grade-detail-graph", not course.no_grade, not course.no_grade))))
        __M_writer(u'\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headextra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headextra():
            return render_headextra(context)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-course-vendor'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-course'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 5, "36": 3, "39": 30, "45": 1, "81": 1, "82": 2, "83": 3, "84": 4, "85": 16, "86": 18, "92": 20, "97": 22, "102": 27, "103": 30, "108": 32, "113": 46, "114": 48, "115": 48, "116": 54, "117": 55, "118": 55, "119": 55, "120": 57, "121": 58, "122": 59, "123": 60, "124": 60, "125": 60, "126": 60, "127": 63, "128": 64, "129": 64, "130": 66, "131": 67, "132": 67, "133": 67, "134": 69, "139": 92, "140": 95, "141": 96, "142": 98, "143": 99, "144": 100, "145": 101, "146": 101, "147": 103, "148": 104, "149": 104, "150": 104, "151": 105, "152": 106, "153": 107, "158": 111, "159": 113, "160": 114, "161": 114, "162": 114, "163": 116, "164": 117, "165": 117, "166": 119, "167": 119, "168": 122, "169": 122, "170": 123, "171": 124, "172": 126, "173": 126, "174": 127, "175": 128, "176": 128, "177": 128, "178": 130, "179": 132, "180": 133, "181": 134, "182": 134, "183": 134, "184": 135, "185": 136, "186": 137, "187": 137, "188": 138, "189": 139, "190": 140, "191": 140, "192": 141, "193": 142, "194": 143, "195": 143, "196": 143, "197": 143, "198": 143, "199": 143, "200": 143, "201": 143, "202": 145, "203": 146, "204": 146, "205": 146, "206": 148, "207": 151, "208": 154, "209": 154, "210": 159, "211": 160, "212": 161, "213": 162, "214": 162, "215": 163, "218": 164, "219": 165, "220": 165, "221": 165, "222": 166, "223": 166, "224": 166, "225": 166, "226": 168, "227": 169, "228": 170, "237": 175, "238": 177, "239": 177, "240": 178, "241": 178, "242": 179, "243": 180, "244": 181, "245": 181, "246": 184, "247": 185, "248": 186, "249": 186, "250": 186, "251": 188, "252": 190, "253": 191, "254": 191, "255": 191, "256": 193, "257": 194, "258": 194, "259": 194, "260": 194, "261": 194, "262": 194, "263": 194, "264": 194, "265": 194, "266": 196, "267": 198, "268": 199, "269": 200, "270": 200, "271": 200, "272": 201, "273": 202, "274": 202, "275": 202, "276": 205, "277": 206, "278": 207, "279": 208, "280": 209, "281": 209, "282": 210, "283": 211, "284": 211, "285": 211, "286": 213, "287": 214, "288": 215, "289": 216, "290": 217, "291": 218, "292": 218, "293": 218, "294": 219, "295": 220, "296": 220, "297": 220, "298": 222, "299": 223, "300": 224, "301": 224, "302": 224, "303": 225, "304": 226, "305": 226, "306": 226, "307": 229, "308": 231, "309": 232, "310": 232, "311": 232, "312": 234, "313": 236, "316": 240, "317": 242, "321": 246, "326": 246, "329": 248, "335": 71, "344": 71, "345": 72, "346": 73, "347": 75, "349": 75, "350": 77, "351": 77, "352": 78, "353": 78, "354": 81, "355": 82, "356": 82, "357": 82, "358": 82, "359": 82, "360": 82, "361": 82, "362": 83, "363": 84, "364": 84, "365": 84, "366": 84, "367": 84, "368": 84, "369": 84, "370": 85, "371": 86, "372": 86, "373": 86, "374": 86, "375": 86, "376": 88, "377": 92, "383": 22, "389": 22, "395": 4, "399": 4, "406": 32, "413": 32, "419": 34, "429": 34, "430": 35, "431": 35, "432": 36, "433": 36, "434": 37, "435": 37, "436": 38, "437": 38, "438": 39, "439": 39, "440": 44, "441": 44, "442": 44, "448": 24, "455": 24, "463": 25, "466": 25, "474": 26, "477": 26, "483": 477}, "uri": "courseware/progress.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/courseware/progress.html"}
__M_END_METADATA
"""
