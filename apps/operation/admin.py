# from django.contrib import admin
#
# from apps.operation.models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse
#
#
# class UserAskAdmin(object):
#     list_display = ['name', 'mobile', 'course_name', 'add_time']
#     search_fields = ['name', 'mobile', 'course_name']
#     list_filter = ['name', 'mobile', 'course_name', 'add_time']
#     model_icon = 'fa fa-flag'
#
# class CourseCommentsAdmin(object):
#     list_display = ['user', 'courses', 'comments', 'add_time']
#     search_fields = ['user', 'courses', 'comments']
#     list_filter = ['user__nick_name', 'course__name', 'comments', 'add_time']
#
#
# # 用户收藏
# class UserFavoriteAdmin(object):
#     list_display = ['user', 'fav_id', 'fav_type', 'add_time']
#     search_fields = ['user', 'fav_id', 'fav_type']
#     list_filter = ['user__nick_name', 'fav_id', 'fav_type', 'add_time']
#
#
# # 用户消息
# class UserMessageAdmin(object):
#     list_display = ['user', 'message', 'has_read', 'add_time']
#     search_fields = ['user', 'message', 'has_read']
#     # 这里的 user 不是 ForeignKey ，具体请看 models.py
#     list_filter = ['user', 'message', 'has_read', 'add_time']
#
#
# class UserCourseAdmin(object):
#     list_display = ['user', 'courses', 'add_time']
#     search_fields = ['user', 'courses']
#     list_filter = ['user__nick_name', 'course__name', 'add_time']
#
#
# admin.site.register(UserAsk, UserAskAdmin)
# admin.site.register(CourseComments, CourseCommentsAdmin)
# admin.site.register(UserFavorite, UserFavoriteAdmin)
# admin.site.register(UserMessage, UserMessageAdmin)
# admin.site.register(UserCourse, UserCourseAdmin)