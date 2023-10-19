"""
URL configuration for formatio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

from django.conf.urls.static import static
from django.conf import settings


handler404 = 'IMG.views.handler404'
handler500 = 'IMG.views.handler500'

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('csv/', include('CSV.urls')),
    path('img/', include('IMG.urls')),
    path('xls/', include('XLSX.urls')),
    path('json/', include('JSON.urls')),
    # path('download/<path:path>', views.download_file, name="download_files"),
    path('download/<path:path>', views.download_file, name="download_file"),
    # path('downloads/<path:path>', views.download_files, name="download_files"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
