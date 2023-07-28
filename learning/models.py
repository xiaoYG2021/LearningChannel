from django.db import models
from django.contrib.auth.models import User


class Channel(models.Model):
    title = models.SlugField(max_length=20, primary_key=True)
    introduction = models.TextField()

    def __str__(self):
        return f'{self.title}频道：' \
               f'{self.introduction[:50]+"……" if len(self.introduction) > 50 else self.introduction}'

    class Meta:
        verbose_name = '频道'
        verbose_name_plural = '频道'


class Topic(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.channel.title}频道的主题：{self.name}'

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = '主题'


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'用户{self.owner.username}在主题“{self.topic.name}”的条目：' \
               f'{self.content[:50]+"……" if len(self.content) > 50 else self.content}'

    class Meta:
        verbose_name = '条目'
        verbose_name_plural = '条目'
