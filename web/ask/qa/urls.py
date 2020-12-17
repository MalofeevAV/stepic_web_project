from django.conf.urls import url

from django.urls import path

from qa.views import test

urlpatterns = [
	path('', test, name='test'),
]