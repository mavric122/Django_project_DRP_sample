from django.urls import path
from my_job.views import title_my_job, entrance, entrance_sample, download_dv

urlpatterns = [
    path('', title_my_job),
    path('/entrance', entrance),
    path('/entrance/sample', entrance_sample),
    path('/entrance/sample/dv', download_dv),

]
