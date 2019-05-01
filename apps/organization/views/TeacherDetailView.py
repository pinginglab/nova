# 讲师详情
from django.shortcuts import render
from django.views import View

from apps.courses.models import Course
from apps.operation.models import UserFavorite
from apps.organization.models import Teacher


class TeacherDetailView(View):
    def get(self, request, teacher_id):
        sorted_teacher = Teacher.objects.all().order_by('-click_nums')[:3]

        teacher = Teacher.objects.get(id=int(teacher_id))
        teacher.click_nums += 1
        teacher.save()
        all_courses = Course.objects.filter(teacher=teacher)

        has_teacher_faved = False
        # 注意这里有个坑就是 teacher_id 是字符串，teacher.id 是数字
        if UserFavorite.objects.filter(user=request.user, fav_type=3, fav_id=teacher.id):
            has_teacher_faved = True

        has_org_faved = False
        if UserFavorite.objects.filter(user=request.user, fav_type=2, fav_id=teacher.org.id):
            has_org_faved = True

        return render(request, 'teacher-detail.html', {
            'teacher': teacher,
            'all_courses': all_courses,
            'sorted_teacher': sorted_teacher,
            'has_teacher_faved': has_teacher_faved,
            'has_org_faved': has_org_faved,
        })