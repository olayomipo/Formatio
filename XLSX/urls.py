
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tocsv', views.tocsv),
    path('tojson', views.tojson),
    path('toxml', views.toxml),
    path('tohtml', views.tohtml),
    # path('toxls', views.toxls),
]