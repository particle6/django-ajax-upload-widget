from django.conf.urls import *

from .views import upload

urlpatterns = [
	url(r'^$', upload, name='ajax-upload')
]