from django.shortcuts import render
from django.views import View

from apps.users.models import EmailVerifyRecord


# 用户进入到重置密码页面
class ResetView(View):
    def get(self, request, active_code):
        # 如果第二次进来，链接就失效
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for records in all_records:
                email = records.email
                return render(request, 'password_reset.html', {'email': email})
        return render(request, 'active_fail.html')