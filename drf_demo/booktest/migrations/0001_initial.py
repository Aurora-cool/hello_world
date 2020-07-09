# Generated by Django 2.2.5 on 2020-07-09 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=20, verbose_name='标题')),
                ('bpub_date', models.DateField(verbose_name='发布日期')),
                ('bread', models.IntegerField(default=0, verbose_name='阅读量')),
                ('bcomment', models.IntegerField(default=0, verbose_name='评论量')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
            ],
            options={
                'db_table': 'tb_books',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20, verbose_name='名称')),
                ('hgender', models.SmallIntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别')),
                ('hcomment', models.CharField(max_length=200, null=True, verbose_name='备注')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.BookInfo', verbose_name='所属图书')),
            ],
            options={
                'db_table': 'tb_heros',
            },
        ),
    ]
