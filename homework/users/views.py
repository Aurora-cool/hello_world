from django.contrib.auth import login, authenticate
from django.views import View
import json
import re
from django.http import JsonResponse
from users.models import User
# Create your views here.


class LoginView(View):
    """用户登录"""

    def post(self, request):
        # 接受参数
        json_dict = json.loads(request.body)
        account = json_dict.get('username')
        password = json_dict.get('password')
        # 校验参数
        if not all([account, password]):
            return JsonResponse({'code': 400, 'errmsg': '缺少必传参数'})
        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$', account):
            return JsonResponse({'code': 400, 'errmsg': '参数username格式错误'})
        if not re.match(r'^[a-zA-Z0-9]{8,20}$', password):
            return JsonResponse({'code': 400, 'errmsg': '参数password格式错误'})
        # 实现多账号登录
        # 判断用户输入的账号是用户名还是手机号
        if re.match(r'^1[3-9]\d{9}$', account):
            User.USERNAME_FIELD = 'mobile'
        else:
            User.USERNAME_FIELD = 'username'

        # 判断是否认证成功
        user = authenticate(request=request, username=account, password=password)
        if not user:
            return JsonResponse({'code': 400, 'errmsg': '用户名或密码有误'})
        # 实现状态保持
        login(request, user)
        # 首页用户名展示
        response = JsonResponse({'code': 0, 'errmsg': '登录成功'})
        response.set_cookie('username', user.username, max_age=3600 * 24 * 14)
        # 响应结果
        return response
