# Create your models here.
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    # model 바꾸면 마이그레이션
    # model-forms-views순서로 작성