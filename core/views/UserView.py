import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from requests import Response
from rest_framework import status
from rest_framework.decorators import list_route, detail_route
from rest_framework.views import APIView

from core import serializers


class UserView(APIView):
    def get(self, request):
        # 获取参数数据
        get = request.GET
        # 获取参数 a
        a = get.get('a')
        print(a)
        # 返回信息
        d = {
            'status': 1,
            'message': 'success',
        }
        return Response(d)

    # @list_route()
    # def list(self, request):
    #     users = User.objects.all()
    #     return HttpResponse(json.loads(users), status=status.HTTP_200_OK)
    #
    # @detail_route()
    # def create(self, request):
    #     data = json.loads(request.body)
    #     username = data['username']
    #     password = data['password']
    #     email = data['email']
    #     user = User.objects.create_user(username, email, password)
    #     if user:
    #         i = User.objects.filter(username=user.username)
    #         return HttpResponse(json.loads(serializers.serialize("json", i)), status=status.HTTP_201_CREATED)
    #     else:
    #         return HttpResponse(request, status=status.HTTP_400_BAD_REQUEST)
    #
    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
    #
    # def destroy(self, request, pk=None):
    #     pass
