from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    preview = models.ImageField(upload_to='courses/preview/', blank=True, null=True, verbose_name='превью')
    description = models.TextField(blank=True, verbose_name='описание')

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')
    preview = models.ImageField(upload_to='lessons/preview/', blank=True, null=True, verbose_name='превью')
    video_url = models.URLField(blank=True, verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name='курс')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return self.title