from django.urls import path, include

from .views import index, courseThis, parserInfo, user_login, user_logout

urlpatterns = [
    path('', index, name='index'),
    path('cource/<int:courceID>', courseThis, name='courswThis'),
    path('parserInfo', parserInfo, name='parserInfo'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]