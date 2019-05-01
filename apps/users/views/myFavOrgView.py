from django.shortcuts import render
from django.views import View

from apps.operation.models import UserFavorite
from apps.organization.models import CourseOrg
from apps.utils.mixin_utils import LoginRequiredMixin


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