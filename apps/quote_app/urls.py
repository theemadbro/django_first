from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.quote_home),
    url(r'^/(?P<id>\d+)$', views.user),
    url(r'^/add/(?P<id>\d+)$', views.add),
    url(r'^/remove/(?P<id>\d+)$', views.remove)
]
