from django.db import models
from django.contrib.auth.models import User


homepage_default_content = '这个家伙很懒，什么也没有留下。'


class Homepage(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        content = (self.content[:50]+'……' if len(self.content) > 50 else self.content) \
            if self.content else homepage_default_content
        return f'用户{self.owner.username}的个人主页：{content}'

    class Meta:
        verbose_name = '个人主页'
        verbose_name_plural = '个人主页'
