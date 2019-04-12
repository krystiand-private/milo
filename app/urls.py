"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^list$', views.UserList.as_view(), name='user_list'),
    url(r'^download-list$', views.download_list, name='download_list'),
    url(r'^delete/(?P<pk>\d+)$', views.UserDeleteView.as_view(), name='user_delete'),
    url(r'^edit/(?P<pk>\d+)$', views.UserUpdateView.as_view(), name='user_edit'),
    url(r'^view/(?P<pk>\d+)$', views.UserDetailView.as_view(), name='user_view'),
    url(r'^create$', views.UserCreateView.as_view(), name='user_create'),
    url(r'^$', RedirectView.as_view(url='/list')),
    path('accounts/', include('django.contrib.auth.urls')),
]
