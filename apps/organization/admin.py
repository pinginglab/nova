# from django.contrib import admin
#
# from apps.organization.models import CityDict, CourseOrg, Teacher
#
#
# class CityDictAdmin(object):
#     list_display = ['name', 'desc', 'add_time']
#     search_fields = ['name', 'desc']
#     list_filter = ['name', 'desc', 'add_time']
#     model_icon = 'fa fa-telegram'
#
#
# class CourseOrgAdmin(object):
#     list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
#     search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
#     list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city__name', 'add_time']
#
#
# class TeacherAdmin(object):
#     list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']
#     search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
#     list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']
#
#
# admin.site.register(CityDict, CityDictAdmin)
# admin.site.register(CourseOrg, CourseOrgAdmin)
# admin.site.register(Teacher, TeacherAdmin)