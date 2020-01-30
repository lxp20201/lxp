# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580361385.802675
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/widgets/header.html'
_template_uri = u'widgets/header.html'
_source_encoding = 'utf-8'
_exports = []



from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext as _
from openedx.core.djangoapps.lang_pref.api import header_language_selector_is_enabled, released_languages


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,online_help_token,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,online_help_token=online_help_token)
        csrf_token = context.get('csrf_token', UNDEFINED)
        context_course = context.get('context_course', UNDEFINED)
        context_library = context.get('context_library', UNDEFINED)
        current_url = context.get('current_url', UNDEFINED)
        get_online_help_info = context.get('get_online_help_info', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        len = context.get('len', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        LANGUAGE_CODE = context.get('LANGUAGE_CODE', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n<div class="wrapper-header wrapper" id="view-top">\n  <header class="primary" role="banner">\n\n    <div class="wrapper wrapper-l">\n      <h1 class="branding">\n        <a class="brand-link" href="/">\n          <img class="brand-image" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('images/studio-logo.png'))))
        __M_writer(u'" alt="')
        __M_writer(filters.html_escape(filters.decode.utf8(settings.STUDIO_NAME)))
        __M_writer(u'" />\n        </a>\n      </h1>\n\n')
        if context_course:
            __M_writer(u'      ')

            course_key = context_course.id
            index_url = reverse('course_handler', kwargs={'course_key_string': unicode(course_key)})
            course_team_url = reverse('course_team_handler', kwargs={'course_key_string': unicode(course_key)})
            assets_url = reverse('assets_handler', kwargs={'course_key_string': unicode(course_key)})
            textbooks_url = reverse('textbooks_list_handler', kwargs={'course_key_string': unicode(course_key)})
            videos_url = reverse('videos_handler', kwargs={'course_key_string': unicode(course_key)})
            import_url = reverse('import_handler', kwargs={'course_key_string': unicode(course_key)})
            course_info_url = reverse('course_info_handler', kwargs={'course_key_string': unicode(course_key)})
            export_url = reverse('export_handler', kwargs={'course_key_string': unicode(course_key)})
            settings_url = reverse('settings_handler', kwargs={'course_key_string': unicode(course_key)})
            grading_url = reverse('grading_handler', kwargs={'course_key_string': unicode(course_key)})
            advanced_settings_url = reverse('advanced_settings_handler', kwargs={'course_key_string': unicode(course_key)})
            tabs_url = reverse('tabs_handler', kwargs={'course_key_string': unicode(course_key)})
            certificates_url = ''
            if settings.FEATURES.get("CERTIFICATES_HTML_VIEW") and context_course.cert_html_view_enabled:
                certificates_url = reverse('certificates_list_handler', kwargs={'course_key_string': unicode(course_key)})
            checklists_url = reverse('checklists_handler', kwargs={'course_key_string': unicode(course_key)})
            
                  
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['assets_url','index_url','import_url','course_team_url','course_key','export_url','settings_url','textbooks_url','course_info_url','certificates_url','checklists_url','videos_url','grading_url','advanced_settings_url','tabs_url'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n      <h2 class="info-course">\n        <span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Current Course:"))))
            __M_writer(u'</span>\n        <a class="course-link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(index_url)))
            __M_writer(u'">\n          <span class="course-org">')
            __M_writer(filters.html_escape(filters.decode.utf8(context_course.display_org_with_default)))
            __M_writer(u'</span><span class="course-number">')
            __M_writer(filters.html_escape(filters.decode.utf8(context_course.display_number_with_default)))
            __M_writer(u'</span>\n          <span class="course-title" title="')
            __M_writer(filters.html_escape(filters.decode.utf8(context_course.display_name_with_default)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(context_course.display_name_with_default)))
            __M_writer(u'</span>\n        </a>\n      </h2>\n\n      <nav class="nav-course nav-dd ui-left" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Course'))))
            __M_writer(u'">\n        <h2 class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Course Navigation"))))
            __M_writer(u'</h2>\n        <ol>\n          <li class="nav-item nav-course-courseware">\n            <h3 class="title"><span class="label"><span class="label-prefix sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Course"))))
            __M_writer(u' </span>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Content"))))
            __M_writer(u'</span> <span class="icon fa fa-caret-down ui-toggle-dd" aria-hidden="true"></span></h3>\n\n            <div class="wrapper wrapper-nav-sub">\n              <div class="nav-sub">\n                <ul>\n                  <li class="nav-item nav-course-courseware-outline">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(index_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Outline"))))
            __M_writer(u'</a>\n                  </li>\n                  <li class="nav-item nav-course-courseware-updates">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_info_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Updates"))))
            __M_writer(u'</a>\n                  </li>\n                  <li class="nav-item nav-course-courseware-pages">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(tabs_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Pages"))))
            __M_writer(u'</a>\n                  </li>\n                  <li class="nav-item nav-course-courseware-uploads">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(assets_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Files & Uploads"))))
            __M_writer(u'</a>\n                  </li>\n                  <li class="nav-item nav-course-courseware-textbooks">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(textbooks_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Textbooks"))))
            __M_writer(u'</a>\n                  </li>\n')
            if context_course.video_pipeline_configured:
                __M_writer(u'                  <li class="nav-item nav-course-courseware-videos">\n                    <a href="')
                __M_writer(filters.html_escape(filters.decode.utf8(videos_url)))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Video Uploads"))))
                __M_writer(u'</a>\n                  </li>\n')
            __M_writer(u'                </ul>\n              </div>\n            </div>\n          </li>\n\n          <li class="nav-item nav-course-settings">\n            <h3 class="title"><span class="label"><span class="label-prefix sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Course"))))
            __M_writer(u' </span>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Settings"))))
            __M_writer(u'</span> <span class="icon fa fa-caret-down ui-toggle-dd" aria-hidden="true"></span></h3>\n\n            <div class="wrapper wrapper-nav-sub">\n              <div class="nav-sub">\n                <ul>\n                  <li class="nav-item nav-course-settings-schedule">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(settings_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Schedule & Details"))))
            __M_writer(u'</a>\n                  </li>\n                  <li class="nav-item nav-course-settings-grading">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(grading_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Grading"))))
            __M_writer(u'</a>\n                  </li>\n                  <li class="nav-item nav-course-settings-team">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_team_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Course Team"))))
            __M_writer(u'</a>\n                  </li>\n                  <li class="nav-item nav-course-settings-group-configurations">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('group_configurations_list_handler', kwargs={'course_key_string': unicode(course_key)}))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Group Configurations"))))
            __M_writer(u'</a>\n                  </li>\n                  <li class="nav-item nav-course-settings-advanced">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(advanced_settings_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Advanced Settings"))))
            __M_writer(u'</a>\n                  </li>\n')
            if certificates_url:
                __M_writer(u'                  <li class="nav-item nav-course-settings-certificates">\n                    <a href="')
                __M_writer(filters.html_escape(filters.decode.utf8(certificates_url)))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Certificates"))))
                __M_writer(u'</a>\n                  </li>\n')
            __M_writer(u'                </ul>\n              </div>\n            </div>\n          </li>\n\n          <li class="nav-item nav-course-tools">\n            <h3 class="title"><span class="label">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Tools"))))
            __M_writer(u'</span> <span class="icon fa fa-caret-down ui-toggle-dd" aria-hidden="true"></span></h3>\n            <div class="wrapper wrapper-nav-sub">\n              <div class="nav-sub">\n                <ul>\n                  <li class="nav-item nav-course-tools-import">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(import_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Import"))))
            __M_writer(u'</a>\n                  </li>\n                  <li class="nav-item nav-course-tools-export">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(export_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Export"))))
            __M_writer(u'</a>\n                  </li>\n')
            if settings.FEATURES.get('ENABLE_EXPORT_GIT') and context_course.giturl:
                __M_writer(u'                  <li class="nav-item nav-course-tools-export-git">\n                    <a href="')
                __M_writer(filters.html_escape(filters.decode.utf8(reverse('export_git', kwargs=dict(course_key_string=unicode(course_key))))))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Export to Git"))))
                __M_writer(u'</a>\n                  </li>\n')
            __M_writer(u'                  <li class="nav-item nav-course-tools-checklists">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(checklists_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Checklists"))))
            __M_writer(u'</a>\n                  </li>\n                </ul>\n              </div>\n            </div>\n          </li>\n        </ol>\n      </nav>\n')
        elif context_library:
            __M_writer(u'       ')

            library_key = context_library.location.course_key
            index_url = reverse('library_handler', kwargs={'library_key_string': unicode(library_key)})
            import_url = reverse('import_handler', kwargs={'course_key_string': unicode(library_key)})
            lib_users_url = reverse('manage_library_users', kwargs={'library_key_string': unicode(library_key)})
            export_url = reverse('export_handler', kwargs={'course_key_string': unicode(library_key)})
                  
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['library_key','import_url','lib_users_url','export_url','index_url'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n      <h2 class="info-course">\n        <span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Current Library:"))))
            __M_writer(u'</span>\n        <a class="course-link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(index_url)))
            __M_writer(u'">\n          <span class="course-org">')
            __M_writer(filters.html_escape(filters.decode.utf8(context_library.display_org_with_default)))
            __M_writer(u'</span><span class="course-number">')
            __M_writer(filters.html_escape(filters.decode.utf8(context_library.display_number_with_default)))
            __M_writer(u'</span>\n          <span class="course-title" title="')
            __M_writer(filters.html_escape(filters.decode.utf8(context_library.display_name_with_default)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(context_library.display_name_with_default)))
            __M_writer(u'</span>\n        </a>\n      </h2>\n\n      <nav class="nav-course nav-dd ui-left" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Course'))))
            __M_writer(u'">\n        <h2 class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Course Navigation"))))
            __M_writer(u'</h2>\n        <ol>\n\n          <li class="nav-item nav-library-settings">\n            <h3 class="title"><span class="label"><span class="label-prefix sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Library"))))
            __M_writer(u' </span>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Settings"))))
            __M_writer(u'</span> <span class="icon fa fa-caret-down ui-toggle-dd" aria-hidden="true"></span></h3>\n            <div class="wrapper wrapper-nav-sub">\n              <div class="nav-sub">\n                <ul>\n                  <li class="nav-item nav-library-settings-team">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(lib_users_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("User Access"))))
            __M_writer(u'</a>\n                  </li>\n                </ul>\n              </div>\n            </div>\n          </li>\n          <li class="nav-item nav-course-tools">\n            <h3 class="title"><span class="label">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Tools"))))
            __M_writer(u'</span> <span class="icon fa fa-caret-down ui-toggle-dd" aria-hidden="true"></span></h3>\n\n            <div class="wrapper wrapper-nav-sub">\n              <div class="nav-sub">\n                <ul>\n                  <li class="nav-item nav-course-tools-import">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(import_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Import"))))
            __M_writer(u'</a>\n                  </li>\n                  <li class="nav-item nav-course-tools-export">\n                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(export_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Export"))))
            __M_writer(u'</a>\n                  </li>\n                </ul>\n              </div>\n            </div>\n          </li>\n        </ol>\n      </nav>\n')
        __M_writer(u'    </div>\n\n    <div class="wrapper wrapper-r">\n')
        if header_language_selector_is_enabled():
            __M_writer(u'        ')
            languages = released_languages() 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['languages'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            if len(languages) > 1:
                __M_writer(u'        <nav class="user-language-selector" aria-label="')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Language preference'))))
                __M_writer(u'">\n          <form action="/i18n/setlang/" method="post" class="settings-language-form" id="language-settings-form">\n              <input type="hidden" id="csrf_token" name="csrfmiddlewaretoken" value="')
                __M_writer(filters.html_escape(filters.decode.utf8(csrf_token)))
                __M_writer(u'">\n')
                if user.is_authenticated:
                    __M_writer(u'              <input title="preference api" type="hidden" id="preference-api-url" class="url-endpoint" value="')
                    __M_writer(filters.html_escape(filters.decode.utf8(reverse('preferences_api', kwargs={'username': user.username}))))
                    __M_writer(u'" data-user-is-authenticated="true">\n')
                else:
                    __M_writer(u'              <input title="session update url" type="hidden" id="update-session-url" class="url-endpoint" value="')
                    __M_writer(filters.html_escape(filters.decode.utf8(reverse('session_language'))))
                    __M_writer(u'" data-user-is-authenticated="false">\n')
                __M_writer(u'              <label><span class="sr">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Choose Language"))))
                __M_writer(u'</span>\n              <select class="input select language-selector" id="settings-language-value" name="language">\n')
                for language in languages:
                    if language[0] == LANGUAGE_CODE:
                        __M_writer(u'                 <option value="')
                        __M_writer(filters.html_escape(filters.decode.utf8(language[0])))
                        __M_writer(u'" selected="selected">')
                        __M_writer(filters.html_escape(filters.decode.utf8(language[1])))
                        __M_writer(u'</option>\n')
                    else:
                        __M_writer(u'                 <option value="')
                        __M_writer(filters.html_escape(filters.decode.utf8(language[0])))
                        __M_writer(u'" >')
                        __M_writer(filters.html_escape(filters.decode.utf8(language[1])))
                        __M_writer(u'</option>\n')
                __M_writer(u'              </select>\n              </label>\n          </form>\n        </nav>\n')
        if user.is_authenticated:
            __M_writer(u'      <nav class="nav-account nav-is-signedin nav-dd ui-right" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Account'))))
            __M_writer(u'">\n        <h2 class="sr-only">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Account Navigation"))))
            __M_writer(u'</h2>\n        <ol>\n          <li class="nav-item nav-account-help">\n            <h3 class="title"><span class="label"><a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(get_online_help_info(online_help_token)['doc_url'])))
            __M_writer(u'" title="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Contextual Online Help'))))
            __M_writer(u'" target="_blank">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Help"))))
            __M_writer(u'</a></span></h3>\n          </li>\n          <li class="nav-item nav-account-user">\n            ')
            runtime._include_file(context, u'user_dropdown.html', _template_uri, online_help_token=online_help_token)
            __M_writer(u'\n          </li>\n        </ol>\n      </nav>\n\n')
        else:
            __M_writer(u'      ')

            register_url = settings.LMS_ROOT_URL + '/register'
                  
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['register_url'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n      <nav class="nav-not-signedin nav-pitch" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Account'))))
            __M_writer(u'">\n        <h2 class="sr-only">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Account Navigation"))))
            __M_writer(u'</h2>\n        <ol>\n          <li class="nav-item nav-not-signedin-help">\n            <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(get_online_help_info(online_help_token)['doc_url'])))
            __M_writer(u'" title="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Contextual Online Help'))))
            __M_writer(u'" target="_blank">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Help"))))
            __M_writer(u'</a>\n          </li>\n')
            if static.get_value('ALLOW_PUBLIC_ACCOUNT_CREATION', settings.FEATURES.get('ALLOW_PUBLIC_ACCOUNT_CREATION')):
                __M_writer(u'              <li class="nav-item nav-not-signedin-signup">\n                <a class="action action-signup" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(register_url)))
                __M_writer(u'?next=')
                __M_writer(filters.html_escape(filters.decode.utf8(current_url)))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Sign Up"))))
                __M_writer(u'</a>\n              </li>\n')
            __M_writer(u'          <li class="nav-item nav-not-signedin-signin">\n            <a class="action action-signin" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(settings.FRONTEND_LOGIN_URL)))
            __M_writer(u'?next=')
            __M_writer(filters.html_escape(filters.decode.utf8(current_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Sign In"))))
            __M_writer(u'</a>\n          </li>\n        </ol>\n      </nav>\n')
        __M_writer(u'    </div>\n  </header>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "30": 2, "33": 1, "49": 1, "50": 2, "51": 8, "52": 15, "53": 15, "54": 15, "55": 15, "56": 19, "57": 20, "58": 20, "81": 39, "82": 41, "83": 41, "84": 42, "85": 42, "86": 43, "87": 43, "88": 43, "89": 43, "90": 44, "91": 44, "92": 44, "93": 44, "94": 48, "95": 48, "96": 49, "97": 49, "98": 52, "99": 52, "100": 52, "101": 52, "102": 58, "103": 58, "104": 58, "105": 58, "106": 61, "107": 61, "108": 61, "109": 61, "110": 64, "111": 64, "112": 64, "113": 64, "114": 67, "115": 67, "116": 67, "117": 67, "118": 70, "119": 70, "120": 70, "121": 70, "122": 72, "123": 73, "124": 74, "125": 74, "126": 74, "127": 74, "128": 77, "129": 83, "130": 83, "131": 83, "132": 83, "133": 89, "134": 89, "135": 89, "136": 89, "137": 92, "138": 92, "139": 92, "140": 92, "141": 95, "142": 95, "143": 95, "144": 95, "145": 98, "146": 98, "147": 98, "148": 98, "149": 101, "150": 101, "151": 101, "152": 101, "153": 103, "154": 104, "155": 105, "156": 105, "157": 105, "158": 105, "159": 108, "160": 114, "161": 114, "162": 119, "163": 119, "164": 119, "165": 119, "166": 122, "167": 122, "168": 122, "169": 122, "170": 124, "171": 125, "172": 126, "173": 126, "174": 126, "175": 126, "176": 129, "177": 130, "178": 130, "179": 130, "180": 130, "181": 138, "182": 139, "183": 139, "193": 145, "194": 147, "195": 147, "196": 148, "197": 148, "198": 149, "199": 149, "200": 149, "201": 149, "202": 150, "203": 150, "204": 150, "205": 150, "206": 154, "207": 154, "208": 155, "209": 155, "210": 159, "211": 159, "212": 159, "213": 159, "214": 164, "215": 164, "216": 164, "217": 164, "218": 171, "219": 171, "220": 177, "221": 177, "222": 177, "223": 177, "224": 180, "225": 180, "226": 180, "227": 180, "228": 189, "229": 192, "230": 193, "231": 193, "235": 193, "236": 194, "237": 195, "238": 195, "239": 195, "240": 197, "241": 197, "242": 198, "243": 199, "244": 199, "245": 199, "246": 200, "247": 201, "248": 201, "249": 201, "250": 203, "251": 203, "252": 203, "253": 205, "254": 206, "255": 207, "256": 207, "257": 207, "258": 207, "259": 207, "260": 208, "261": 209, "262": 209, "263": 209, "264": 209, "265": 209, "266": 212, "267": 218, "268": 219, "269": 219, "270": 219, "271": 220, "272": 220, "273": 223, "274": 223, "275": 223, "276": 223, "277": 223, "278": 223, "279": 226, "280": 226, "281": 231, "282": 232, "283": 232, "289": 234, "290": 235, "291": 235, "292": 236, "293": 236, "294": 239, "295": 239, "296": 239, "297": 239, "298": 239, "299": 239, "300": 241, "301": 242, "302": 243, "303": 243, "304": 243, "305": 243, "306": 243, "307": 243, "308": 246, "309": 247, "310": 247, "311": 247, "312": 247, "313": 247, "314": 247, "315": 252, "321": 315}, "uri": "widgets/header.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/cms/templates/widgets/header.html"}
__M_END_METADATA
"""
