from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^details/(?P<restaurant_id>[0-9]+)/$', views.details, name='details'),
    url(r'^get-suggestions/$', views.suggestions, name='suggestions'),
    url(r'^add-review/(?P<restaurant_id>[0-9]+)/$', views.review, name='review')
]