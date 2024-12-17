"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task2.views import template_func, TemplateClass
from task4.views import task3_platform, task3_games, task3_cart, base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', template_func),
    path('class/', TemplateClass.as_view()),
    path('', task3_platform),
    path('platform/games/', task3_games),
    path('platform/cart/', task3_cart),
    path('base/', base)
]


