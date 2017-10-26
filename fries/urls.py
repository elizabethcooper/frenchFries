from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^datetime/', views.current_date_time, name='current_date_time'),
    url(r'^page/', views.current_date_time_page, name='current_date_time_page'),
]