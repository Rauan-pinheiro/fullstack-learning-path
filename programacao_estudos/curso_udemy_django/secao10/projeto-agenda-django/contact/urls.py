from contact import views
from django.urls import path

aoo_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]