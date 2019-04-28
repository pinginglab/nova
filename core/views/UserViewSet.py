# ViewSets define the view behavior.
# import json
#
# from django.contrib.auth.models import User
# from rest_framework import viewsets, status
# from rest_framework.decorators import detail_route, list_route
# from rest_framework.response import Response
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     @list_route()
#     def list(self, request, *args, **kwargs):
#         users = User.objects.all()
#         return Response(json.loads(users), status=status.HTTP_200_OK)
#
#     @detail_route()
#     def create(self, request):
#         data = json.loads(request.body)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # else:
#         #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         print(data)
#
#     def retrieve(self, request, pk=None):
#         pass
#
#     def update(self, request, pk=None):
#         pass
#
#     def partial_update(self, request, pk=None):
#         pass
#
#     def destroy(self, request, pk=None):
#         pass

