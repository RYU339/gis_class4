from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription', null=False)
    # CASCADE: 유저에 종속, 탈퇴하면 구독 정보도 다 날라감
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription', null=False)
    class Meta:
        unique_together = ['user', 'project']
        # 유저가 프로젝트를 두 번 구독할 수 없음