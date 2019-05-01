# 机构首页
from django.shortcuts import render
from django.views import View

from apps.operation.models import UserFavorite
from apps.organization.models import CourseOrg


class OrgHomeView(View):
    def get(self, request, org_id):
        current_page = "home"
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html', {
            'all_courses': all_courses,
            'all_teachers': all_teachers,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })