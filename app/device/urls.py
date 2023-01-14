from django.urls import path
from . import views

app_name = 'device'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('devices', views.deviceListView, name = 'list'),
    path('devices-test', views.deviceTestView, name = 'test'),
    path('detail/<int:id>/', views.deviceDetailView, name='detail'),
]