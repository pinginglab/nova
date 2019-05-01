from django.conf.urls import url

from apps.organization.views.AddFavView import AddFavView
from apps.organization.views.AddUserAskView import AddUserAskView
from apps.organization.views.OrgCourseView import OrgCourseView
from apps.organization.views.OrgDescView import OrgDescView
from apps.organization.views.OrgHomeView import OrgHomeView
from apps.organization.views.OrgTeacherView import OrgTeacherView
from apps.organization.views.OrgView import OrgView
from apps.organization.views.TeacherDetailView import TeacherDetailView
from apps.organization.views.TeacherListView import TeacherListView

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