from django.db import models


# 계정정보 모델
class Account(models.Model):
    gender_options = (
        ('male', 'MAN'),
        ('female', 'WOMAN')
    )

    username = models.CharField(max_length=20, unique=True)
    pw = models.CharField(max_length=20)
    email = models.EmailField()
    birth = models.CharField(max_length=6)
    gender = models.CharField(max_length=8, choices=gender_options)
    score = models.IntegerField(default=0)


# 산 정보 모델
class Mountains(models.Model):
    name = models.CharField(max_length=20)
    avg_time = models.CharField(max_length=10)


# Post된 산 글 모델
class PostMountain(models.Model):
    imgpath = models.CharField(max_length=50, default='')
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    body = models.TextField(max_length=200)
    star = models.IntegerField(default=0)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)


# 개인이 등산한 산 목록
class MyList(models.Model):
    m_name = models.CharField(max_length=20)
    course = models.CharField(max_length=20, null=True)
    time = models.CharField(max_length=10)
    score = models.IntegerField(default=1)


