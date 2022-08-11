from django.shortcuts import render


# from .parser import url, status_request, stasus_req
#
# status_requests = stasus_req()
#

def title_menu(request):
    return render(request, 'web_site/title.html')

#
# def parser(request):
#     if status_requests == 200:
#         status = 'Статус: Сервер отвечает'
#     else:
#         status = 'Статус: Нет соединения'
#     data = {'url': url,
#             'status_request': status}
#
#     return render(request, 'web_site/parser.html', context=data)
#
#
# def status_request_parser(request):
#     data = {'url': url,
#             'status_request': status_request}
#
#     return render(request, 'web_site/status_request_parser.html', context=data)
