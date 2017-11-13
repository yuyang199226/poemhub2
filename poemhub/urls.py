"""poemhub URL Configuration

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
from poem import views
from django.views.static import serve
from poemhub import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home),
    url(r'^login/', views.log_in),
    url(r'^signup/', views.signup),
    url(r'^logout/', views.log_out),
    url(r'^changepwd',views.changepwd),
    url(r'^user_profile',views.user_profile),
    url(r'^modify_profile',views.modify_profile),
    url(r'^ajax_get_user_info',views.ajax_get_user_info),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),


]
