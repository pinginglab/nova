from requests import Response
from rest_framework.views import APIView


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