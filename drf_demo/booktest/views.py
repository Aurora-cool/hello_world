import json

from django.shortcuts import render
from django.views import View
from .models import BookInfo
from django.http import JsonResponse, HttpResponse


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
        book_list = []
        for book in books:
            book_list.append({
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment
            })
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        """
        新增一本图书数据
        """
        # 1.获取参数并校验
        json_dict = json.loads(request.body)
        btitle = json_dict.get('btitle')
        bpub_date = json_dict.get('bpub_date')

        # TODO: 省略参数校验过程
        # 2.创建图书数据并保存到数据库
        book = BookInfo.objects.create(btitle=btitle,
                                       bpub_date=bpub_date)

        # 3.将新增图书数据通过json进行返回
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        }

        return JsonResponse(book_dict, status=201)


class BookDetailView(View):
    def get(self, request, pk):
        """获取指定图书数据"""
        # 1.查询数据库获取的指定的图书数据
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'detail': 'not found'}, status=404)

        # 2.将指定图书数据通过json进行返回
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        }

        return JsonResponse(book_dict)

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
        btitle = json_dict.get('btitle')
        bpub_date = json_dict.get('bpub_date')
        # TODO: 省略参数校验过程

        # 3.修改图书数据并保存到数据库
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()

        # 4.将修改图书数据通过json进行返回
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        }

        return JsonResponse(book_dict)

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
