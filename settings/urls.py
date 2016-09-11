from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

admin.site.site_header = 'Administracja'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'),
        url(r'^adminitration/', TemplateView.as_view(template_name='administration.html')))
]
