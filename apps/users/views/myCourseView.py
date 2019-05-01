from django.shortcuts import render
from django.views import View

from apps.operation.models import UserCourse
from apps.utils.mixin_utils import LoginRequiredMixin


class MyCourseView(LoginRequiredMixin, View):
    def get(self, request):
     user_courses = UserCourse.objects.filter(user=request.user)
     return render(request, 'usercenter-mycourse.html', {
         'user_courses': user_courses,
     })
