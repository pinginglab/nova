from django.views import View
from rest_framework.utils import json


class ContainerView(View):
    def post(self, request):
        data = request.body.decode('utf-8')
        data = json.loads(data)
