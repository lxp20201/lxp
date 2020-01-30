# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1580296499.858837
_enable_loop = True
_template_filename = u'/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/student_account/account_settings.html'
_template_uri = 'student_account/account_settings.html'
_source_encoding = 'utf-8'
_exports = [u'pagetitle', u'headextra', u'js_extra', 'online_help_token']



import json

from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext as _

from openedx.core.djangolib.js_utils import dump_js_escaped_json, js_escaped_string
from openedx.core.djangolib.markup import HTML
from webpack_loader.templatetags.webpack_loader import render_bundle
from openedx.core.djangoapps.user_api.accounts.utils import is_secondary_email_feature_enabled_for_user


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'/static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/main.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        static = _mako_get_namespace(context, 'static')
        user = context.get('user', UNDEFINED)
        def headextra():
            return render_headextra(context._locals(__M_locals))
        auth = context.get('auth', UNDEFINED)
        duplicate_provider = context.get('duplicate_provider', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer(u'\n\n')
        if duplicate_provider:
            __M_writer(u'    <section>\n        ')
            runtime._include_file(context, u'/dashboard/_dashboard_third_party_error.html', _template_uri)
            __M_writer(u'\n    </section>\n')
        __M_writer(u'\n<div class="wrapper-account-settings"></div>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headextra'):
            context['self'].headextra(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

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
        __M_writer(filters.html_escape(filters.decode.utf8(_("Account Settings"))))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headextra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headextra():
            return render_headextra(context)
        static = _mako_get_namespace(context, 'static')
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
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
        __M_writer(u'\n    <link type="text/css" rel="stylesheet" href="')
        __M_writer(filters.html_escape(filters.decode.utf8(STATIC_URL)))
        __M_writer(u'paragon/static/paragon.min.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        user = context.get('user', UNDEFINED)
        auth = context.get('auth', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                password_reset_support_link = context.get('password_reset_support_link', UNDEFINED)
                extended_profile_fields = context.get('extended_profile_fields', UNDEFINED)
                enterprise_name = context.get('enterprise_name', UNDEFINED)
                user_preferences_api_url = context.get('user_preferences_api_url', UNDEFINED)
                fields = context.get('fields', UNDEFINED)
                enterprise_readonly_account_fields = context.get('enterprise_readonly_account_fields', UNDEFINED)
                sync_learner_profile_data = context.get('sync_learner_profile_data', UNDEFINED)
                edx_support_url = context.get('edx_support_url', UNDEFINED)
                bool = context.get('bool', UNDEFINED)
                user_accounts_api_url = context.get('user_accounts_api_url', UNDEFINED)
                enable_account_deletion = context.get('enable_account_deletion', UNDEFINED)
                order_history = context.get('order_history', UNDEFINED)
                __M_writer = context.writer()
                __M_writer(u'\n    var fieldsData = ')
                __M_writer(dump_js_escaped_json( fields ))
                __M_writer(u',\n        ordersHistoryData = ')
                __M_writer(dump_js_escaped_json( order_history ))
                __M_writer(u',\n        authData = ')
                __M_writer(dump_js_escaped_json( auth ))
                __M_writer(u",\n        platformName = '")
                __M_writer(js_escaped_string( static.get_platform_name() ))
                __M_writer(u"',\n        contactEmail = '")
                __M_writer(js_escaped_string( static.get_contact_email_address() ))
                __M_writer(u"',\n        allowEmailChange = ")
                __M_writer(dump_js_escaped_json( bool(settings.FEATURES['ALLOW_EMAIL_ADDRESS_CHANGE']) ))
                __M_writer(u',\n        socialPlatforms = ')
                __M_writer(dump_js_escaped_json( settings.SOCIAL_PLATFORMS ))
                __M_writer(u',\n\n        syncLearnerProfileData = ')
                __M_writer(dump_js_escaped_json( bool(sync_learner_profile_data) ))
                __M_writer(u",\n        enterpriseName = '")
                __M_writer(js_escaped_string( enterprise_name ))
                __M_writer(u"',\n        enterpriseReadonlyAccountFields = ")
                __M_writer(dump_js_escaped_json( enterprise_readonly_account_fields ))
                __M_writer(u",\n        edxSupportUrl = '")
                __M_writer(js_escaped_string( edx_support_url ))
                __M_writer(u"',\n        extendedProfileFields = ")
                __M_writer(dump_js_escaped_json( extended_profile_fields ))
                __M_writer(u',\n        displayAccountDeletion = ')
                __M_writer(dump_js_escaped_json( enable_account_deletion ))
                __M_writer(u';\n        isSecondaryEmailFeatureEnabled = ')
                __M_writer(dump_js_escaped_json( bool(is_secondary_email_feature_enabled_for_user(user)) ))
                __M_writer(u",\n\n    AccountSettingsFactory(\n        fieldsData,\n        ordersHistoryData,\n        authData,\n        '")
                __M_writer(js_escaped_string( password_reset_support_link ))
                __M_writer(u"',\n        '")
                __M_writer(js_escaped_string( user_accounts_api_url ))
                __M_writer(u"',\n        '")
                __M_writer(js_escaped_string( user_preferences_api_url ))
                __M_writer(u"',\n        ")
                __M_writer(dump_js_escaped_json( user.id ))
                __M_writer(u',\n        platformName,\n        contactEmail,\n        allowEmailChange,\n        socialPlatforms,\n\n        syncLearnerProfileData,\n        enterpriseName,\n        enterpriseReadonlyAccountFields,\n        edxSupportUrl,\n        extendedProfileFields,\n        displayAccountDeletion,\n        isSecondaryEmailFeatureEnabled\n    );\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'AccountSettingsFactory',module_name=u'js/student_account/views/account_settings_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n<script type="text/javascript">\n     window.auth = ')
        __M_writer(dump_js_escaped_json( auth ))
        __M_writer(u';\n     window.isActive = ')
        __M_writer(dump_js_escaped_json( user.is_active ))
        __M_writer(u';\n</script>\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'StudentAccountDeletionInitializer'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "learneraccountsettings" 
        
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"196": 73, "136": 34, "16": 3, "222": 17, "197": 76, "152": 35, "153": 36, "154": 36, "155": 37, "156": 37, "157": 38, "158": 38, "159": 39, "160": 39, "161": 40, "162": 40, "163": 41, "36": 18, "165": 42, "166": 42, "167": 44, "168": 44, "169": 45, "42": 1, "171": 46, "172": 46, "173": 47, "174": 47, "175": 48, "176": 48, "177": 49, "178": 49, "179": 50, "180": 50, "181": 56, "182": 56, "183": 57, "184": 57, "185": 58, "58": 1, "59": 14, "60": 16, "61": 17, "62": 18, "198": 76, "193": 35, "67": 20, "68": 22, "69": 23, "70": 24, "71": 24, "72": 27, "204": 79, "77": 32, "209": 79, "82": 81, "212": 80, "199": 77, "88": 20, "164": 41, "218": 17, "186": 58, "94": 20, "187": 59, "100": 29, "229": 222, "188": 59, "108": 29, "116": 30, "119": 30, "120": 31, "121": 31, "200": 77, "170": 45, "127": 34}, "uri": "student_account/account_settings.html", "filename": "/home/css/edx-edutech/apps/edx/edx-platform/lms/templates/student_account/account_settings.html"}
__M_END_METADATA
"""
