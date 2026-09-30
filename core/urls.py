"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.http import HttpResponse


def healthz(request):
    from django.db import connection
    connection.ensure_connection()
    return HttpResponse('ok', content_type='text/plain')

urlpatterns = [
    path('healthz/', healthz),
    path('favicon.ico', RedirectView.as_view(url='/static/members/images/rise-bird-hero.png', permanent=True)),
    # One sign-in for everyone: the admin login hands over to RISE's own page,
    # which applies verified-email rules.
    path('admin/login/', RedirectView.as_view(pattern_name='login', query_string=True)),
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
    path('accounts/', include('allauth.urls')),
]
