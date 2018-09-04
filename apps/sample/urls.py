from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$', views.SampleCreate.as_view(), name='sample_add'),
    url(r'^(?P<pk>[^/]+)/change/$', views.SampleUpdate.as_view(), name='sample_change'),
    url(r'^$', views.SampleList.as_view(), name='sample_list'),
    url(r'^getPanelField/', views.getPanelFields, name='get_field'),
    # url(r'^index/',views.index,name='index'),
]