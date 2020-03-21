"""rest_api_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers
from rest_app_demo.views import NoteViewSet
from rest_app_demo import views

router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register('note', views.NoteViewSet)
# router.register('important', views.ImportantNoteSet)
# router.register('non_important', views.NonImportantNoteSet)

urlpatterns = [
    path('note/', include(router.urls)),
    path('admin/', admin.site.urls),

]
