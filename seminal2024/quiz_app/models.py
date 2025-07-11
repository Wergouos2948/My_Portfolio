from django.db import models
import uuid

# Create your models here.
class Page(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4,editable=False, verbose_name="ID")
    source = models.CharField(max_length=500, verbose_name='出典')
    source_text = models.TextField(max_length=5000, verbose_name="出典元本文", default='')
    quiz_text = models.TextField(max_length=1000, verbose_name='クイズ')
    correct = models.CharField(max_length=100, verbose_name='正解')
    incorrect_1 = models.CharField(max_length=100, verbose_name='不正解1')
    incorrect_2 = models.CharField(max_length=100, verbose_name='不正解2')

    def __str__(self):
        return self.quiz_text