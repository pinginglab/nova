from django.conf.urls import url

from apps.organization.views.addFavView import AddFavView
from apps.organization.views.addUserAskView import AddUserAskView
from apps.organization.views.orgCourseView import OrgCourseView
from apps.organization.views.orgDescView import OrgDescView
from apps.organization.views.orgHomeView import OrgHomeView
from apps.organization.views.orgTeacherView import OrgTeacherView
from apps.organization.views.orgView import OrgView
from apps.organization.views.teacherDetailView import TeacherDetailView
from apps.organization.views.teacherListView import TeacherListView

urlpatterns = [
    #课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    url(r'^courses/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),

    # 机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),

    # 讲师列表页
    url(r'^teacher/list$', TeacherListView.as_view(), name='teacher_list'),

    # 讲师详情页
    url(r'^teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name='teacher_detail'),
]