from django.urls import path
from . import views
from .views import api
#from .views import get_data

urlpatterns = [path('', views.home, name= "index"),
               path('result', views.api, name = 'result'),
               ]