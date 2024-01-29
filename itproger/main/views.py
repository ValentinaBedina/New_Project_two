from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Привет!', 'Добро пожаловать!'],
        'obj': {
            'car': 'BMW',
            'age': '22',
            'hobby': 'рисоваать'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
