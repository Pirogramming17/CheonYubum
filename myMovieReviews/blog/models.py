from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='영화 제목')
    direct = models.CharField(max_length=50, verbose_name='영화 감독')
    comeout = models.DateTimeField()
    maincha = models.CharField(max_length=50, verbose_name='주연 배우')
    genre = models.CharField(max_length=50, verbose_name='#Genre')
    score = models.IntegerField(verbose_name='평점')
    runnintime = models.CharField(max_length=50, verbose_name='러닝타임')
    review = models.TextField(verbose_name='REVIEW')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)