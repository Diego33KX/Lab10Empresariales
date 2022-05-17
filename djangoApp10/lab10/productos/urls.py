from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^productos/$',views.producto_list),
    url(r'^productos/(?P<pk>[0-9]+)/$', views.producto_detail),
]