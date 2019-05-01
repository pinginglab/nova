# 用户修改密码
# 用户在个人中心修改密码
import json

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.views import View

from apps.users.forms import ModifyPwdForm
from apps.utils.mixin_utils import LoginRequiredMixin


class UpdatePwdView(LoginRequiredMixin, View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        res = dict()

        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            if pwd1 != pwd2:
                res['status'] = 'fail'
                res['msg'] = '两次密码不一致'
                return HttpResponse(json.dumps(res), content_type='application/json')

            user = request.user
            user.password = make_password(pwd2)
            user.save()

            res['status'] = 'success'
            res['msg'] = '密码修改成功'
        else:
            res = modify_form.errors

        return HttpResponse(json.dumps(res), content_type='application/json')