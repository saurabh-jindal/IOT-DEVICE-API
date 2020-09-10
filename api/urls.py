from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api_overview"),
    path('devices/', views.Devices.as_view()),
    path('devices/<str:device_id>/', views.DeviceDetail.as_view()),
    path('devices/<str:device_id>/readings/<str:p>/', views.DeviceDetail.as_view()),

]
