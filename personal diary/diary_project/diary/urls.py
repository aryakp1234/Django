# diary/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.diary_list, name='diary_list'),
    path('create/', views.diary_create, name='diary_create'),
    path('<int:pk>/', views.diary_detail, name='diary_detail'),
    path('<int:pk>/update/', views.diary_update, name='diary_update'),
    path('<int:pk>/delete/', views.diary_delete, name='diary_delete'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
