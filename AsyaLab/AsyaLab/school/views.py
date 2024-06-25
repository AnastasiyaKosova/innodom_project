from .models import Courses, material, lesson, Students
from django.shortcuts import render
# import arrow
import requests
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


def user_login(request):
    context = {
        'text_login': 'вход'
    }
    if request.POST:
        print("post прошел!")
        username = request.POST["username"]
        password = request.POST["password"]
        user_aut = authenticate(request, username=username, password=password)
        print(user_aut)
        # user_cources = Students.objects.filter(user=user_aut)
        # print(user_cources)
        # context_courses = Courses.objects.filter(user_cources)
        # print(context_courses)

        if user_aut is not None:
            login(request, user=user_aut)
            print(f'Пользователь: {user_aut} авторизован.')
            context = {
                # 'curces': Courses.objects.filter()
            }
            print(context)
            # return render(request, "index.html", context)
            return redirect('index')

    return render(request, "login.html", context)


def index(request):
    if request.user.is_authenticated == True:
        user_aut = request.user
        print(f'Пользователь: {user_aut} авторизован.')

        if request.user.is_superuser:
            print('Вы под админом!')

            context = {
                'curces': Courses.objects.all()
            }
        else:
            user_cources = Students.objects.filter(user=user_aut)
            print(f"Колличество курсов пользователя {user_cources}")
            print(user_cources[0].cource)

            context = {
                'curces': Courses.objects.filter(title=user_cources[1].cource)
            }

        return render(request, "index.html", context)
    else:
        context = {
            'text_login': 'вход'
        }
        return render(request, "login.html", context)


def courseThis(request, courceID):
    nameCource = Courses.objects.filter(id=courceID)
    context = {
        'curces': Courses.objects.filter(id=courceID),
        'lesson': lesson.objects.filter(course=nameCource[0].id),
        'material': material.objects.all()
    }
    print(nameCource)
    return render(request, "course.html", context)
# Create your views here.



def parserInfo(request):
    import sqlite3
    from datetime import datetime


    def spent_time(timeOne, timeTwo):
        tDelta = timeTwo - timeOne
        return print(f"Выполнение заняло: {tDelta.seconds} сек.")

    # def second_to_date(sec):
    #     timestamp = 1713117890000 / 1000  # переводим из миллисекунд в секунды
    #     formatted_date = arrow.get(timestamp).format('YYYY-MM-DD HH:mm:ss')
    #     return formatted_date

    # timeStart = datetime.now()

    # URL для авторизации
    login_url = 'https://learn.innodom.by/api/user/auth'

    # Данные для аутентификации (логин и пароль)
    payload = {
        'email': 'potapenko@fastservice.by',
        'password': 'cb745576',
        'fingerprint': '1ef0300f8d576dd16eb2444f08225088'
    }
    session = requests.Session()
    # Отправляем POST-запрос с данными для аутентификации
    response = session.post(login_url, data=payload)

    # Проверяем успешность запроса
    if response.status_code == 200:
        print("Авторизация успешна!")
        # Здесь можно продолжить работу на сайте
    else:
        print("Ошибка при авторизации:", response.status_code)

    cousrses = session.get('https://learn.innodom.by/api/school/course/list')
    cousrsesJSON = cousrses.json()[0]
    cousses_page_list = []
    id_courses_list = []
    for i in cousrses.json():
        print(f'id: {i['id']}')
        id_courses_list.append(i['id'])
        print(f'Название курса: {i['name']}')
        print(f'Описание: {i['shortDescription']}')
        page = 'https://learn.innodom.by/students/' + str(i['id'])
        cousses_page_list.append(page)
        print(page)
        print()
        connection = sqlite3.connect("C:\AsyaLAB\AsyaLab\AsyaLab\db.sqlite3")
        cursor = connection.cursor()

        cursor.execute(
            f"INSERT INTO school_courses(title, description) VALUES('{i['name']}', '{i['shortDescription']}')")
        connection.commit()
    print(cousses_page_list)

    return render(request, "index.html")

def user_logout(request):
    logout(request)
    return redirect("login")
# parserInfo(requests)