from django.db import models
from django.utils import timezone

class Post(models.Model):
    # models는 Post가 장고 모델임을 의미
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # ForeignKey 다른 모델에 대한 링크를 의미
    title = models.CharField(max_length=200)
    # CharField는 글자 수가 제한된 텍스트를 정의
    text = models.TextField()
    # TextField는 글자 수에 제한이 없는 텍스트를 위한 속성 
    created_date = models.DateTimeField(default=timezone.now)
    # DateTimeField는 날짜와 시간
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # Post의 제목을 리턴
        return self.title