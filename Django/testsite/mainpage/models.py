from django.db import models
from django.urls import reverse


class Places(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')  # поле не обязательно к заполнению
    creates_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name='Тип локации')


    def get_absolute_url(self):
        return reverse('views_places', kwargs={'place_id': self.pk})


    def myfunc(self):
        return 'Hello from model'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['-creates_at', 'title']


class Categories(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Тип локации')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('location', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title
