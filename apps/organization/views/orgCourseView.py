# 机构课程列表页
from django.shortcuts import render
from django.views import View

from apps.operation.models import UserFavorite
from apps.organization.models import CourseOrg


class OrgCourseView(View):
    def get(self, request, org_id):
        current_page = "courses"
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_courses = course_org.course_set.all()
        return render(request, 'org-detail-course.html', {
            'all_courses': all_courses,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })