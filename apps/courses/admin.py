# from django.contrib import admin
# from apps.courses.models import CourseResource, Lesson, Course, BannerCourse, Video
#
#
# class LessonInline:
#     model = Lesson
#     extra = 0
#
#
# # 添加课程的时候可以顺便添加课程资源
# class CourseResourceInline:
#     model = CourseResource
#     extra = 0
#
#
# class CourseAdmin(object):
#     list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'get_zj_nums', 'add_time']
#     search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
#     list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
#     model_icon = 'fa fa-graduation-cap'
#     list_editable = ['degree', 'desc']
#
#     # Inline # 添加课程的时候可以顺便添加章节、课程资源
#     inlines = [LessonInline, CourseResourceInline]
#
#     refresh_times = [3, 5]
#
#     # 重新在这里写一遍的原因是，避免数据重复
#     def queryset(self):
#         qs = super(CourseAdmin, self).queryset()
#         qs = qs.filter(is_banner=False)
#         return qs
#
#     def save_models(self):
#         # 在保存课程的时候统计课程机构的课程数
#         obj = self.new_obj
#         obj.save()
#         if obj.course_org is not None:
#             course_org = obj.course_org
#             course_org.course_nums = Course.objects.filter(course_org=course_org).count()
#             course_org.save()
#
#
# class BannerCourseAdmin(object):
#     list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
#                     'click_n0=ums', 'add_time']
#     search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
#                     'click_nums']
#     list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
#                     'click_nums', 'add_time']
#
#
#
#     #Inline # 添加课程的时候可以顺便添加章节、课程资源
#     inlines = [LessonInline, CourseResourceInline]
#
#     #把轮播图从 User model 里转移到 Course model 里
#     def queryset(self):
#         qs = super(BannerCourseAdmin, self).queryset()
#         qs = qs.filter(is_banner=True)
#         return qs
#
#
# class LessonAdmin(object):
#     list_display = ['courses', 'name', 'add_time']
#     search_fields = ['courses', 'name']
#     list_filter = ['course__name', 'name', 'add_time']
#
#
# class VideoAdmin(object):
#     list_display = ['lesson', 'name', 'add_time']
#     search_fields = ['lesson', 'name']
#     list_filter = ['lesson', 'name', 'add_time']
#
#
# class CourseResourceAdmin(object):
#     list_display = ['courses', 'name', 'download', 'add_time']
#     search_fields = ['courses', 'download', 'name']
#     list_filter = ['course__name', 'name', 'download', 'add_time']
#
#
# admin.site.register(Course, CourseAdmin)
# admin.site.register(BannerCourse, BannerCourseAdmin)
# admin.site.register(Lesson, LessonAdmin)
# admin.site.register(Video, VideoAdmin)
# admin.site.register(CourseResource, CourseResourceAdmin)
