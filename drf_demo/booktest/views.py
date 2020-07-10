import json
from django.views import View
from .models import BookInfo
from django.http import JsonResponse, HttpResponse
from .serializers import BookInfoSerializer


# Create your views here.


class BookListView(View):
    """/books/"""
    def get(self, request):
        """
        获取所以图书数据
        1.查询数据库获取所有图书数据
        2.将所以图书数据通过json进行返回
        """
        # 1.查询数据库获取所有图书数据
        books = BookInfo.objects.all()
        # 2.将所以图书数据通过json进行返回
        serializer = BookInfoSerializer(books, many=True)

        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """
        新增一本图书数据
        """
        # 1.获取参数并校验
        json_dict = json.loads(request.body)
        # 反序列化-参数校验
        serializer = BookInfoSerializer(data=json_dict)
        serializer.is_valid(raise_exception=True)
        # 2.创建图书数据并保存到数据库
        serializer.save()

        return JsonResponse(serializer.data, status=201)


class BookDetailView(View):
    def get(self, request, pk):
        """获取指定图书数据"""
        # 1.查询数据库获取的指定的图书数据
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'detail': 'not found'}, status=404)

        # 2.将指定图书数据通过json进行返回
        serializer = BookInfoSerializer(book)

        return JsonResponse(serializer.data)

    def put(self, request, pk):
        """修改指定图书数据"""
        # 1.查询数据库获取指定的图书数据
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            # 图书不存在
            return JsonResponse({'detail': 'not found'}, status=404)

        # 2.获取参数并进行校验
        json_dict = json.loads(request.body)

        # 反序列化-参数校验
        serializer = BookInfoSerializer(book, data=json_dict)
        serializer.is_valid(raise_exception=True)

        # 3.修改图书数据并保存到数据库
        # 反序列化保存
        serializer.save()  # save()内部调用了序列化器类中的update方法

        # 4.将修改图书数据通过json进行返回
        return JsonResponse(serializer.data)

    def delete(self, request, pk):
        """删除指定图书数据"""
        # 1.查询数据库获取指定的图书数据
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            # 图书不存在
            return JsonResponse({'detail': 'not found'}, status=404)
        # 2. 删除指定图书数据
        book.delete()
        # 3. 返回响应
        return HttpResponse(status=204)
