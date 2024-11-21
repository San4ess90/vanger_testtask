from django.db import models
from filer.fields.image import FilerImageField
from easy_thumbnails.fields import ThumbnailerImageField


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = FilerImageField(on_delete=models.CASCADE, verbose_name='Изображение')
    thumbnail = ThumbnailerImageField(upload_to='thumbnails/', verbose_name='Миниатюра')
    order = models.IntegerField(default=0, blank=False, null=False,verbose_name='Сортировка')

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'
        ordering = ['order']

    def __str__(self):
        return self.title
