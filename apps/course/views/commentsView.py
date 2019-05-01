# 课程评论
from django.shortcuts import render
from django.views import View

from apps.course.models import Course
from apps.utils.mixin_utils import LoginRequiredMixin


class CommentsView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.all()

        return render(request, 'course-comment.html', {
            'course': course,
            'course_resources': all_resources,
            'all_comments': all_comments,
        })