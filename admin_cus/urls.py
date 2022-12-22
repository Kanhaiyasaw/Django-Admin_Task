from django.urls import path
from admin_cus import views
urlpatterns = [
    path('', views.index, name="index")
]