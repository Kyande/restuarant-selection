from django.conf.urls import url

from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.index, name='index'),
    url(r'^suggestions/', views.suggestions, name='suggestions'),
    url(r'^about-us/', views.about_us, name='about-us')
=======
    url(r'^$', views.home, name='home'),
    url(r'^(?P<restaurant_id>[0-9]+)/details/$', views.details, name='details'),
    url(r'^get-suggestions/$', views.suggestions, name='suggestions')
>>>>>>> ui-for-clips
]