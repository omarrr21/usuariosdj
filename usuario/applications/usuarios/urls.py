from django.urls import path
from . import views

app_name='usuarios_app'
urlpatterns = [
    path('register/', views.Userregisterview.as_view(),name='registro'),
    path('login/', views.Loginuser.as_view(), name='loginuser'),

]