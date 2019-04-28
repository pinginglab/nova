from django.contrib.auth.models import User
from requests import Response
from rest_framework.decorators import list_route, detail_route
from rest_framework.views import APIView


class UserView(APIView):
    # def get(self, request):
    #     # 获取参数数据
    #     get = request.GET
    #     # 获取参数 a
    #     a = get.get('a')
    #     print(a)
    #     # 返回信息
    #     d = {
    #         'status': 1,
    #         'message': 'success',
    #     }
    #     return Response(d)

    # @list_route()
    # def list(self, request, *args, **kwargs):
    #     users = User.objects.all()
    #     user_serializer = UserSerializer(users, many=True)
    #     return Response(user_serializer.data, status=status.HTTP_200_OK)
    #
    # @detail_route()
    # def create(self, request):
    #     serializer = UserSerializer(data=json.loads(request.body))
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass