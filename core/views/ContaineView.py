import docker
from django.contrib.auth.decorators import login_required
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView


class ContainerView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def __init__(self):
        self.client = docker.from_env()

    @login_required
    def post(self, request):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        """
            create container for images
        """
        if data['method'] == 'c':
            image_name = data['image_name']
            # container_new = self.client.containers.run(image_name, detach=True, ports={'2222/tcp': 3333})
            container_new = self.client.containers.run("webgoat/webgoat-7.1", detach=True, ports={'8080/tcp': 3333})
            return Response(container_new.id)


