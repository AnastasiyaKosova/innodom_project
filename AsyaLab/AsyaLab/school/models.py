from django.contrib import auth
from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model): #класс курсов
    title = models.CharField(verbose_name='Название курса', max_length=100, null=True)
    description = models.TextField(verbose_name='Описание курса', max_length=255, null=True)
    start_date = models.DateField(verbose_name='Начало курсов', null=True, )
    end_date = models.DateField(verbose_name='окончание курсов', null=True)
    image = models.ImageField(verbose_name="Картинка курсв", null=True, blank=True, upload_to='static/img/cources/')


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
# Create your models here.

class lesson(models.Model):
    course = models.ForeignKey(Courses, verbose_name="Курс", on_delete=models.CASCADE, null=True)
    title = models.CharField(verbose_name="Название урока", max_length=100, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


# Create your models here.


class material(models.Model):
    lesson = models.ForeignKey(lesson, verbose_name="Урок", on_delete=models.CASCADE, null=True)
    text = models.TextField(verbose_name="Текст", max_length=255, null=True)
    link = models.CharField(verbose_name="Ссылка", max_length=255, null=True)
    # presentation = models.FileField(verbose_name='Презентация', null=True, upload_to='static/presentation/')
    # presentation = models.FileField(upload_to='static/presentation/', help_text="Загрузите файл с презентацией к уроку",
    #                                verbose_name="Презентация", null=True)

    def __str__(self):
        return f'{self.lesson}'

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
# Create your models here.

class Students(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, null=True)
    cource = models.ForeignKey(Courses, verbose_name="Курс", on_delete=models.CASCADE, null=True)