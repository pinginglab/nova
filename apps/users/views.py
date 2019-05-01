# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.hashers import make_password

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import UserProfile, EmailVerifyRecord, Banner
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm, UploadImageForm, UserInfoForm


import json





































# 发送修改邮箱时的邮箱验证码
class SendEmailCodeView(LoginRequiredMixin, View):
    def get(self, request):
        email = request.GET.get('email', '')

        res = dict()
        if UserProfile.objects.filter(email=email):
            res['email'] = '邮箱已注册'
            return HttpResponse(json.dumps(res), content_type='application/json')
        send_register_email(email, 'update_email')
        res['status'] = 'success'
        res['msg'] = '发送验证码成功'
        return HttpResponse(json.dumps(res), content_type='application/json')


# 修改个人邮箱
class UpdateEmailView(LoginRequiredMixin, View):
    def post(self, request):
        email = request.POST.get('email', '')
        code = request.POST.get('code', '')

        existed_records = EmailVerifyRecord.objects.filter(email=email, code=code, send_type='update_email')
        res = dict()
        if existed_records:
            user = request.user
            user.email = email
            user.save()
            res['status'] = 'success'
            res['msg'] = '邮箱修改成功！'
        else:
            res['status'] = 'fail'
            res['msg'] = '验证码出错！'

        return HttpResponse(json.dumps(res), content_type='application/json')


# 我的课程
class MyCourseView(LoginRequiredMixin, View):
    def get(self, request):
     user_courses = UserCourse.objects.filter(user=request.user)
     return render(request, 'usercenter-mycourse.html', {
         'user_courses': user_courses,
     })


# 我收藏的课程机构
class MyFavOrgView(LoginRequiredMixin, View):
    def get(self, request):
     org_list = []
     fav_orgs = UserFavorite.objects.filter(user=request.user, fav_type=2)
     for fav_org in fav_orgs:
         org_id = fav_org.fav_id
         org = CourseOrg.objects.get(id=org_id)
         org_list.append(org)
     return render(request, 'usercenter-fav-org.html', {
         'org_list': org_list,
     })


# 我收藏的授课讲师
class MyFavTeacherView(LoginRequiredMixin, View):
    def get(self, request):
        teacher_list = []
        fav_teachers = UserFavorite.objects.filter(user=request.user, fav_type=3)
        for fav_teacher in fav_teachers:
            teacher_id = fav_teacher.fav_id
            teacher = Teacher.objects.get(id=teacher_id)
            teacher_list.append(teacher)
        return render(request, 'usercenter-fav-teacher.html', {
            'teacher_list': teacher_list,
        })


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


# 我的消息
class MyMessageView(LoginRequiredMixin, View):
    def get(self, request):
        # 如果 user = 0 ，代表全局消息，所有用户都能收到
        all_message = UserMessage.objects.filter(user=request.user.id)

        #进入到我的消息页面后，把已读的消息清空
        all_unread_message = UserMessage.objects.filter(user=request.user.id, has_read=False)
        for unread_message in all_unread_message:
            unread_message.has_read = True
            unread_message.save()

        # 对个人消息分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_message, 2, request=request)
        messages = p.page(page)

        return render(request, 'usercenter-message.html', {
            'messages': messages,
        })


# 慕学在线网首页
class IndexView(View):
    def get(self, request):
        # 取出轮播图
        all_banners = Banner.objects.all().order_by('index')
        courses = Course.objects.filter(is_banner=False)[:6]
        banner_courses = Course.objects.filter(is_banner=True)[:3]
        course_orgs = CourseOrg.objects.all()[:15]
        return render(request, 'index.html', {
            'all_banners': all_banners,
            'courses': courses,
            'banner_courses': banner_courses,
            'course_orgs': course_orgs,
        })


# 全局 404 处理函数
def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


# 全局 500 处理函数
def page_error(request):
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response