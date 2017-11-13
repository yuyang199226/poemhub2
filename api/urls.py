from django.conf.urls import url,include
from django.contrib import admin
from api import views
urlpatterns = [

    url(r'^authors/', views.fill_authors),


]