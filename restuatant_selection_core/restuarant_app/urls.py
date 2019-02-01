from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<restaurant_id>[0-9]+)/details/$', views.details, name='details'),
    url(r'^get-suggestions/$', views.suggestions, name='suggestions')
]