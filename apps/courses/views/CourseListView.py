from django.core.paginator import PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from pure_pagination import Paginator

from apps.courses.models import Course


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by('-add_time')

        # 热门课程排序
        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        # 课程搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_courses = all_courses.filter(
                Q(name__icontains=search_keywords) |
                Q(desc__icontains=search_keywords) |
                Q(detail__icontains=search_keywords)
            )

        # 课程排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_courses = all_courses.order_by('-students')
        elif sort == 'hot':
            all_courses = all_courses.order_by('-click_nums')

        # 对课程分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 9, request=request)

        courses = p.page(page)

        return render(request, 'course-list.html', {
            'all_courses': courses,
            'sort': sort,
            'hot_courses': hot_courses,

        })
