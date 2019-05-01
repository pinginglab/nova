from django.contrib import admin

# from .models import EmailVerifyRecord, Banner
#
#
# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True
#
#
# class GlobalSettings(object):
#     site_title = "慕学后台管理系统"
#     site_footer = "慕学在线网"
#     menu_style = "accordion"
#
#
# class EmailVerifyRecordAdmin(object):
#     list_display = ['code', 'email', 'send_type', 'send_time']
#     search_fields = ['code', 'email', 'send_type']
#     list_filter = ['code', 'email', 'send_type', 'send_time']
#     model_icon = 'fa fa-address-book-o'
#
#
# class BannerAdmin(object):
#     list_display = ['title', 'image', 'url', 'index', 'add_time']
#     search_fields = ['title', 'image', 'url', 'index']
#     list_filter = ['title', 'image', 'url', 'index', 'add_time']
#
#
# admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
# admin.site.register(Banner, BannerAdmin)
# admin.site.register(BaseAdminView, BaseSetting)
# admin.site.register(CommAdminView, GlobalSettings)
