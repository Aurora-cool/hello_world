from rest_framework import serializers
from .models import BookInfo, HeroInfo
# 问题：
# 1. 在序列化发挥作用的有几个？5个
# 2. 在反序列化发挥作用的有几个？4个 btitle、bpub_date、bread、bcomment
# 3. data={'btitle': 'python', 'bpub_date': '2020-07-09'}，校验能不能通过？可以


# class BookInfoSerializer(serializers.Serializer):
#     """图书序列化器类"""
#     id = serializers.IntegerField(label='ID', read_only=True)
#     btitle = serializers.CharField(label='名称', max_length=20)
#     bpub_date = serializers.DateField(label='发布日期')
#     bread = serializers.IntegerField(label='阅读量', required=False)
#     bcomment = serializers.IntegerField(label='评论量', required=False)
#     heroinfo_set = serializers.StringRelatedField(label='英雄名',read_only=True, many=True)

# class HeroInfoSerializer(serializers.Serializer):
#     """英雄序列化器类"""
#     GENDER_CHOICES = (
#         (0, '男'),
#         (1, '女')
#     )
#     id = serializers.IntegerField(label='ID', read_only=True)
#     hname = serializers.CharField(label='名字', max_length=20)
#     hgender = serializers.ChoiceField(label='性别', choices=GENDER_CHOICES, required=False)
#     hcomment = serializers.CharField(label='描述信息', max_length=200, required=False)


class BookInfoSerializer(serializers.ModelSerializer):
    """图书序列化器类"""
    class Meta:
        model = BookInfo
        fields = '__all__'


class HeroInfoSerializer(serializers.ModelSerializer):
    """英雄序序列化器类"""
    class Meta:
        model = HeroInfo
        fields = '__all__'
