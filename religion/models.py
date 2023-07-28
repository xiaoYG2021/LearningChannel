from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    owner = models.OneToOneField(User, models.CASCADE, primary_key=True)
    effective = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner.username}的{"有" if self.effective else "无"}效令牌'

    class Meta:
        verbose_name = '令牌'
        verbose_name_plural = '令牌'


class Branch(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    introduction = models.TextField()

    def __str__(self):
        return f'老教分部{self.name}：{self.introduction[:50]+"……" if len(self.introduction) > 50 else self.introduction}'

    class Meta:
        verbose_name = '老教分部'
        verbose_name_plural = '老教分部'


class Archbishop(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    introduction = models.TextField()

    def __str__(self):
        return f'教主{self.name}：{self.introduction[:50]+"……" if len(self.introduction) > 50 else self.introduction}'

    class Meta:
        verbose_name = '历届教主'
        verbose_name_plural = '历届教主'


class Event(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    value = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return f'老教事件：{self.name}'

    class Meta:
        verbose_name = '事件'
        verbose_name_plural = '事件'
