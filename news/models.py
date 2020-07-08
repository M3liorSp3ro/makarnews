from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    text = models.TextField("Текст")
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
