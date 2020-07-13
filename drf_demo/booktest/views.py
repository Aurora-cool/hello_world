from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from .models import BookInfo
from django.http import JsonResponse
from .serializers import BookInfoSerializer


# Create your views here.

"""GenericAPIView改写"""
# class BookListView(GenericAPIView):
#     """/books/"""
#     # 指定视图所使用的序列化器类
#     serializer_class = BookInfoSerializer
#     # 指定视图所使用的查询集
#     queryset = BookInfo.objects.all()
#
#     def get(self, request):
#         """
#         获取所以图书数据
#         1.查询数据库获取所有图书数据
#         2.将所以图书数据通过json进行返回
#         """
#         # 2.将所以图书数据通过json进行返回
#         queryset =  self.get_queryset()
#
#         serializer = self.get_serializer(queryset, many=True)
#
#         return Response(serializer.data)
#
#     def post(self, request):
#         """
#         新增一本图书数据
#         """
#         # 反序列化-参数校验
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         # 2.创建图书数据并保存到数据库
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class BookDetailView(GenericAPIView):
#
#     # 指定视图所使用的序列化器类
#     serializer_class = BookInfoSerializer
#     # 指定视图所使用的查询机
#     queryset = BookInfo.objects.all()
#
#     def get(self, request, pk):
#         """获取指定图书数据"""
#         # 1.查询数据库获取的指定的图书数据
#         instance = self.get_object()
#
#         # 2.将指定图书数据通过json进行返回
#         serializer = self.get_serializer(instance)
#
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         """修改指定图书数据"""
#         # 1.查询数据库获取指定的图书数据
#         instance = self.get_object()
#
#         # 反序列化-参数校验
#         serializer = self.get_serializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         # 3.修改图书数据并保存到数据库
#         # 反序列化保存
#         serializer.save()  # save()内部调用了序列化器类中的update方法
#
#         # 4.将修改图书数据通过json进行返回
#         return JsonResponse(serializer.data)
#
#     def delete(self, request, pk):
#         """删除指定图书数据"""
#         # 1.查询数据库获取指定的图书数据
#         instance = self.get_object()
#         # 2. 删除指定图书数据
#         instance.delete()
#         # 3. 返回响应
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""Mixin扩展类改写"""
# class BookListView(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    GenericAPIView):
#     # 指定视图所使用的序列化器类
#     serializer_class = BookInfoSerializer
#     # 指定视图所使用的查询集
#     queryset = BookInfo.objects.all()
#
#     def get(self, request):
#         """获取所以图书数据"""
#         return self.list(request)
#
#     def post(self, request):
#         """新增一个图书数据"""
#         return self.create(request)
#
#
# class BookDetailView(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      GenericAPIView):
#     """获取,修改,删除指定图书"""
#     # 指定视图所使用的序列化器类
#     serializer_class = BookInfoSerializer
#     # 指定视图所使用的查询集
#     queryset = BookInfo.objects.all()
#
#     def get(self, request, pk):
#         """获取指定图书"""
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         """修改指定图书"""
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         """删除指定图书"""
#         return self.destroy(request, pk)
