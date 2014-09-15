from django.conf.urls import patterns, include, url
from website.views import SignupPage, IndexView
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='home_page'),
                       )
