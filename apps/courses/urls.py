from django.conf.urls import url

from apps.courses.views.AddCommentView import AddCommentView
from apps.courses.views.AommentsView import CommentsView
from apps.courses.views.ContaineView import ContainerView
from apps.courses.views.CourseDetailView import CourseDetailView
from apps.courses.views.CourseInfoView import CourseInfoView
from apps.courses.views.CourseListView import CourseListView
from apps.courses.views.VideoPlayView import VideoPlayView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),

    # 实验列表页
    url(r'^test/$', ContainerView.as_view(), name='test_list'),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),

    # 课程info
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),

    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name='course_comment'),

    # 添加课程评论
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),

    # 播放视频
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name='video_play'),
]
