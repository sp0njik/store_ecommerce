from django.urls import path, include

from store import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
]
