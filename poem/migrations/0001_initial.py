# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 07:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('profile', models.TextField(verbose_name='个人简介')),
                ('quotation', models.TextField(verbose_name='典故')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=128, verbose_name='评论内容')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poem.Author', verbose_name='作者')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poem.AuthorComment', verbose_name='父评论')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField(choices=[(0, '唐诗'), (0, '宋词'), (0, '元曲'), (0, '元曲'), (0, '现代诗'), (0, '楚辞')], verbose_name='分类名')),
            ],
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='题目')),
                ('content', models.TextField(verbose_name='内容')),
                ('publish_date', models.DateField(blank=True, null=True, verbose_name='发表日期')),
                ('appreciation', models.CharField(max_length=256, verbose_name='赏析')),
                ('translation', models.TextField(blank=True, null=True, verbose_name='翻译')),
                ('up_count', models.IntegerField(default=0, verbose_name='点赞数')),
                ('comment_count', models.IntegerField(default=0, verbose_name='评论数')),
                ('author_name', models.CharField(max_length=32, verbose_name='作者名字')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poem.Author')),
            ],
        ),
        migrations.CreateModel(
            name='PoemComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=128, verbose_name='评论内容')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poem.PoemComment', verbose_name='父评论')),
                ('poem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poem.Poem', verbose_name='诗')),
            ],
        ),
        migrations.CreateModel(
            name='PoemUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('love', models.BooleanField(default=False, verbose_name='喜欢')),
                ('up', models.BooleanField(default=False, verbose_name='赞')),
                ('poem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poem.Poem')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32, verbose_name='昵称')),
                ('avator', models.ImageField(blank=True, null=True, upload_to='avators/', verbose_name='头像')),
                ('gender', models.BooleanField(verbose_name='性别')),
                ('bio', models.CharField(max_length=64, verbose_name='个人简介')),
                ('rank', models.IntegerField(default=1, verbose_name='等级')),
                ('love_poem', models.ManyToManyField(through='poem.PoemUser', to='poem.Poem')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rhesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=128, verbose_name='名句')),
                ('poem_title', models.CharField(max_length=32, verbose_name='诗名')),
                ('author_name', models.CharField(max_length=32, verbose_name='作者名')),
                ('poem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poem.Poem', verbose_name='出自古诗')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标签名')),
                ('poem', models.ManyToManyField(to='poem.Poem', verbose_name='诗')),
            ],
        ),
        migrations.AddField(
            model_name='poemuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poem.Profile'),
        ),
        migrations.AddField(
            model_name='poemcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poem.Profile', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='category',
            name='poems',
            field=models.ManyToManyField(related_name='categoties', to='poem.Poem', verbose_name='诗'),
        ),
        migrations.AddField(
            model_name='authorcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poem.Profile', verbose_name='用户'),
        ),
    ]
