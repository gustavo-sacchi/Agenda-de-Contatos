from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('perfil_user/', views.perfil_user, name='perfil_user'),
    # path('<int:user_id>', views.perfil_user, name='perfil_user')

]
