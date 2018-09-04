from django.urls import path
from django.conf.urls import url

from user.views import UserLogin, LogoutView

urlpatterns = [

	url('^login/', UserLogin.as_view(), name='login'),
	url('^logout/$', LogoutView.as_view(), name='logout'),

]
