from django.urls import path
from . import views

app_name='home_app'
urlpatterns = [
    path('panel/', views.Homepage.as_view(),name='panel'),

]