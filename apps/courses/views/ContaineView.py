import json
import random
import socket

import docker
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import authentication, permissions


def IsOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        # s.shutdown(2)
        # 利用shutdown()函数使socket双向数据传输变为单向数据传输。shutdown()需要一个单独的参数，
        # 该参数表示了如何关闭socket。具体为：0表示禁止将来读；1表示禁止将来写；2表示禁止将来读和写。
        return True
    except:
        return False


class ContainerView(View):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def __init__(self):
        self.client = docker.from_env()

    # @login_required
    def get(self, request):
        # data = request.body.decode('utf-8')
        # data = json.loads(data)
        """
            create container for images
        """
        # if data['method'] == 'c':
        #     image_name = data['image_name']
        # container_new = self.client.containers.run("webgoat/webgoat-7.1", detach=True, ports={'8080/tcp': 3333})
        # return render(request, 'test-list.html', {
        #     'containerid': container_new.id
        # })
        ip = '0.0.0.0'
        while True:
            port = random.randint(10000, 30000)
            if not IsOpen(ip, port.__str__()):
                container_new = self.client.containers.run("webgoat/webgoat-7.1", detach=True, ports={'8080/tcp': port})
                # return Response(container_new.id)
                #         return render(request, 'test-list.html', {
                #             'containerid': container_new.id
                #         })
                return HttpResponse({"port": port, "containerid": container_new.id}.__str__())
            else:
                continue
