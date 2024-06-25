from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Courses, lesson, material, Students


@admin.register(Courses) #регистрация курсов
class Courses(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'start_date', 'end_date', 'image_corse_admin')
    # list_filter = ('id', 'companyName', 'phone', 'address', 'email', 'site')
    search_fields = ('title')
# Register your models here.

    readonly_fields = ["image_corse", "image_corse_admin"]

    def image_corse(self, obj):
        return mark_safe(f'<img width="200px" src="{obj.image.url}">')


    def image_corse_admin(self, obj):
        if obj.image.url:
            return mark_safe(f'<img width="100px" src="{obj.image.url}">')

    image_corse.short_description = "Картинка курсов"
    image_corse_admin.short_description = "Картинка курсов"


@admin.register(lesson)
class lesson(admin.ModelAdmin):
    list_display = ('id', 'course', 'title')
    # list_filter = ('id', 'companyName', 'phone', 'address', 'email', 'site')
    # search_fields = ('id', 'companyName', 'phone', 'address', 'email', 'site')
# Register your models here.



@admin.register(material)
class material(admin.ModelAdmin):
    list_display = ('id', 'lesson')
    # list_filter = ('id', 'companyName', 'phone', 'address', 'email', 'site')
    # search_fields = ('id', 'companyName', 'phone', 'address', 'email', 'site')
# Register your models here.

# @admin.register(User_cources)
# class User_cources(admin.ModelAdmin):
#     list_display = ("user", "cource")


@admin.register(Students)
class Studens(admin.ModelAdmin):
    list_display = ('id', 'user', 'cource')