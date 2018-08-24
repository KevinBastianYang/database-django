
"""DC URL Configuration

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
from  myview import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^search-post$',search.search_post),
    url(r'^login/',views.login),

    url(r'^$',views.index),
    url(r'^home$',views.index),
    url(r'^team$', views.team),
    url(r'^project$', views.project),
    url(r'^search_drug$',views.search_drug),
    url(r'^search_com$',views.search_com),
    url(r'^search_target$',views.search_target),
    url(r'^drug/',views.drug),
    url(r'^combination/',views.combination),
    url(r'^target/',views.target)
]
urlpatterns += staticfiles_urlpatterns()