from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Entrance
from .forms import EntranceForm


# Главная страница раздела моей работы.
def title_my_job(request):
    content = {
        'title': 'Раздел о работе',
    }
    return render(request, 'my_job/title_my_job.html', context=content)


#
def entrance(request):
    entrances = Entrance.objects.all()
    form = EntranceForm()

    if request.method == 'POST':

        content = {
            'title': 'Ремонт подъезда',
            'entrance': entrances,
            'form': form
        }

        form = EntranceForm(request.POST)
        if form.is_valid():
            Entrance.objects.create(**form.cleaned_data)  # Сохранение очищенных и провалидированных данных в шаблон.

    else:
        content = {
            'title': 'Ремонт подъезда',
            'entrance': entrances,
            'form': form
        }

    return render(request, 'my_job/entrance.html', context=content, )


# Функция для вывода данных из шаблонов в формы.
def entrance_sample(request):
    entrances = Entrance.objects.all()
    form = EntranceForm()
    if request.method == 'POST':
        id = request.POST.get('sample')  # Получаю номер id
        intention = Entrance.objects.get(pk=id)  # Передаю данные по id
        form = EntranceForm(instance=intention)  # форма с нужными данными из шаблона

    content = {
        'title': 'Ремонт подъезда',
        'entrance': entrances,
        'form': form
    }

    return render(request, 'my_job/entrance_sample.html', context=content)
