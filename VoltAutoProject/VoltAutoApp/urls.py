from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.cars, name='cars'),
    path('sellers/', views.sellers, name='sellers'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('create_car/', views.create_car, name='create_car'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('car/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
]