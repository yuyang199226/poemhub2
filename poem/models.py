# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Poem(models.Model):
    '''古诗文表'''
    title = models.CharField(max_length=32,verbose_name='题目')
    content = models.TextField(verbose_name='内容')
    publish_date = models.DateField(verbose_name='发表日期',blank=True,null=True)
    appreciation = models.TextField(verbose_name='赏析',blank=True,null=True)
    translation = models.TextField(verbose_name='翻译',blank=True,null=True)
    up_count = models.IntegerField(verbose_name='点赞数',default=0)
    comment_count = models.IntegerField(verbose_name='评论数',default=0)
    author_name = models.CharField(verbose_name='作者名字',max_length=32)
    category = models.ForeignKey(to='Category',verbose_name='分类',blank=True,null=True,related_name='poems')

    author = models.ForeignKey(to='Author')
    class Meta:
        unique_together=('title','author_name')
    def __str__(self):
        return self.title

class Author(models.Model):
    '''诗人表'''
    name = models.CharField(max_length=64,unique=True)
    profile = models.TextField(verbose_name='个人简介',blank=True,null=True)
    quotation = models.TextField(verbose_name='典故',blank=True,null=True)
    def __str__(self):
        return self.name

class Rhesis(models.Model):
    '''名句表'''
    content = models.CharField(max_length=128,verbose_name='名句')
    poem_title =models.CharField(max_length=32,verbose_name='诗名')
    author_name = models.CharField(max_length=32,verbose_name='作者名')

    poem = models.ForeignKey(to='Poem',verbose_name='出自古诗')
    class Meta:
        unique_together = ('poem_title', 'content')

class Tags(models.Model):
    '''古诗的标签'''
    title = models.CharField(max_length=64,verbose_name='标签名')

    poem = models.ManyToManyField(to='Poem',verbose_name='诗')
    def __str__(self):
        return self.title

class Profile(models.Model):
    '''
    one-to-one link User model
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.CharField(verbose_name='昵称',max_length=32)
    love_poem = models.ManyToManyField(to='Poem',through='PoemUser')
    avator = models.ImageField(verbose_name='头像',upload_to='avators/',blank=True,null=True)
    gender = models.BooleanField(verbose_name='性别')
    bio = models.CharField(verbose_name='个人简介',max_length=64)
    rank = models.IntegerField(verbose_name='等级',default=1)

    def __str__(self):
        return self.nickname

class PoemUser(models.Model):
    '''用户与诗的中间表'''
    poem = models.ForeignKey(to='Poem',on_delete=models.CASCADE)
    user = models.ForeignKey(to='Profile',on_delete=models.CASCADE)
    love = models.BooleanField(verbose_name='喜欢',default=False)
    up = models.BooleanField(verbose_name='赞',default=False)

class PoemComment(models.Model):
    '''对诗的评论表'''
    content = models.CharField(verbose_name='评论内容',max_length=128)
    poem = models.ForeignKey(to='Poem',verbose_name='诗')
    user = models.ForeignKey(to='Profile',verbose_name='用户')
    parent = models.ForeignKey(to='PoemComment',verbose_name='父评论',blank=True,null=True)

class AuthorComment(models.Model):
    '''对作者的评论'''
    content = models.CharField(verbose_name='评论内容',max_length=128)
    author = models.ForeignKey(to='Author',verbose_name='作者')
    user = models.ForeignKey(to='Profile',verbose_name='用户')
    parent = models.ForeignKey(to='AuthorComment',verbose_name='父评论',blank=True,null=True)
    def __str__(self):
        return self.content

class Category(models.Model):
    '''分类'''
    CATEGORY_CHOICES = [
        (0,'唐诗'),
        (0,'宋词'),
        (0,'元曲'),
        (0,'元曲'),
        (0,'现代诗'),
        (0,'楚辞'),
    ]
    title = models.IntegerField(verbose_name='分类名',choices=CATEGORY_CHOICES)
    def __str__(self):
        return self.title













