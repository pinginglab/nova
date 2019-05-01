import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from apps.users.forms import UserInfoForm
from apps.utils.mixin_utils import LoginRequiredMixin


# pingusers
class UserInfoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'usercenter-info.html')

    # 用户修改昵称，手机号，地址，生日
    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        res = dict()

        if user_info_form.is_valid():
            user_info_form.save()
            res['status'] = 'success'

        else:
            res = user_info_form.errors

        return HttpResponse(json.dumps(res), content_type='application/json')