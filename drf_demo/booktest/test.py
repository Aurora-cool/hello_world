# 设置Django运行所依赖的环境变量
import os
import sys

sys.path.insert(0, '../')
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_demo.settings')

# 让Django进行一次初始化
import django
django.setup()

import json
from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer

# class Goods(object):
#
#     def __init__(self, name, price, stock):
#         self.name = name
#         self.price = price
#         self.stock = stock

# class GoodSerializer(serializers.Serializer):
#
#     name = serializers.CharField()
#     price = serializers.IntegerField()
#     stock = serializers.IntegerField(required=False)


if __name__ == '__main__':

    book = BookInfo.objects.get(id=1)
    serializer = BookInfoSerializer(book)
    res = serializer.data
    print(res)
    # # 准备多个对象数据
    # objects = [Goods('华为P40', 4900, 1000), Goods('小米10', 4300, 800)]
    # # 创建序列化器对象
    # serializers = GoodSerializer(objects, many=True)
    # # 获取序列化之后的数据
    # res = serializers.data
    # # 将数据进行格式化显示
    # res = json.dumps(res, indent=1, ensure_ascii=False)
    # print(res)

    # # 准备数据
    # req_data = {'name': '小米10', 'price': 4300}
    # # 创建序列化对象,转入待校验的参数
    # serializer = GoodSerializer(data=req_data)
    # # 调用is_valid进行数据校验,成功返回True, 失败返回False
    # res = serializer.is_valid()
    # if res:
    #     print('校验通过:', serializer.validated_data)
    # else:
    #     print('校验失败:', serializer.errors)
