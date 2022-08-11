from django.shortcuts import render

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
            id_entrance = request.POST.get('sample')  # Получаю номер id

    else:
        content = {
            'title': 'Ремонт подъезда',
            'entrance': entrances,
            'form': form
        }

    return render(request, 'my_job/entrance.html', context=content, )


# Страница для вывода данных из шаблонов в формы.
def entrance_sample(request):
    entrances = Entrance.objects.all()
    form = EntranceForm()
    if request.method == 'POST':
        id_entrance = request.POST.get('sample')  # Получаю номер id
        intention = Entrance.objects.get(pk=id_entrance)  # Передаю данные по id
        form = EntranceForm(instance=intention)  # форма с нужными данными из шаблона.

    content = {
        'title': 'Ремонт подъезда',
        'entrance': entrances,
        'form': form
    }

    return render(request, 'my_job/entrance_sample.html', context=content)





def download_dv(request):
    Entrance.objects.get(id=id_entrance)
    doc = create_doc()
    content = {
        'title': 'Ремонт подъезда',
        'doc': doc
    }

    return render(request, 'my_job/dv.html', context=content)
