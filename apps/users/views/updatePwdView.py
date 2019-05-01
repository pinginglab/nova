import json

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.views import View

from apps.users.forms import ModifyPwdForm
from apps.utils.mixin_utils import LoginRequiredMixin



