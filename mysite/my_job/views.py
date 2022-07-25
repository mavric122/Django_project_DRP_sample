from django.shortcuts import render


# Главная страница раздела моей работы.
def title_my_job(request):
    return render(request, 'web_site/title_my_job.html')
