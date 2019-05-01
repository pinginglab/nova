from django.shortcuts import render
from django.views import View

from apps.courses.models import Course
from apps.operation.models import UserFavorite
from apps.utils.mixin_utils import LoginRequiredMixin


# 我收藏的课程
class MyFavCourseView(LoginRequiredMixin, View):
    def get(self, request):
        course_list = []
        fav_courses = UserFavorite.objects.filter(user=request.user, fav_type=1)
        for fav_course in fav_courses:
            course_id = fav_course.fav_id
            course = Course.objects.get(id=course_id)
            course_list.append(course)
        return render(request, 'usercenter-fav-course.html', {
            'course_list': course_list,
        })