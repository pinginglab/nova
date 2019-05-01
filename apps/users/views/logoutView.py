from django.core.urlresolvers import reverse

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views import View


# 用户登出
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))