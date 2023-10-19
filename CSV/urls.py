
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # path('tocsv', views.tocsv),
    path('toxls', views.toxls),
    path('toxml', views.toxml),
    path('tohtml', views.tohtml),
    path('tojson', views.tojson),
]