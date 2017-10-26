from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^datetime/', views.current_date_time, name='current_date_time'),
    url(r'^welcome/', views.welcome, name='welcome'),
    url(r'^register/new', views.register_new_user, name='register_new_user'),
    url(r'^login/user', views.login_user, name='login_user'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^image/', views.image, name='image')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
