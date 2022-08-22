import mimetypes
import os
from wsgiref.util import FileWrapper

from django.http import StreamingHttpResponse
from django.shortcuts import render

from .models import Entrance
from .forms import EntranceForm

from .create_dv import create_doc


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

# Вот тут я пока застрял
def download_dv(request):
    entrances = Entrance.objects.all()
    form = EntranceForm()
    # if request.method == 'POST':
    #     id_entrance = request.POST.get('sample')  # Получаю номер id
    #     intention = Entrance.objects.get(pk=id_entrance)  # Передаю данные по id
    #     form = EntranceForm(intention=intention)  # форма с нужными данными из шаблона.

    doc = create_doc(form)

    filename = os.path.basename(doc)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(doc, 'rb'), chunk_size),
                                     content_type=mimetypes.guess_type(doc)[0])
    response['Content-Length'] = os.path.getsize(doc)
    response['Content-Disposition'] = "attachment; filename=%s" % filename

    content = {
        'title': 'Ремонт подъезда',
        'doc': doc
    }

    return render(request, 'my_job/dv.html', context=content)
