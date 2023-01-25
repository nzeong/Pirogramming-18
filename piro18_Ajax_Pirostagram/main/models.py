from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.IntegerField()
    dislike = models.IntegerField()
    


p = Post.objects.create(title="오로라", content="오로라는 태양에서 방출되는 플라즈마 입자가 지구 대기권 상층부의 자기장과 마찰하여 빛을 내는 광전 현상이다.", like="0", dislike="0")