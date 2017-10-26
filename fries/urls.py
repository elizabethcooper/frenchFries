from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^datetime/', views.current_date_time, name='current_date_time'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^welcome/', views.welcome, name='welcome'),
    url(r'^register/new', views.register_new_user, name='register_new_user'),
    url(r'^login/user', views.login_user, name='login_user'),
]