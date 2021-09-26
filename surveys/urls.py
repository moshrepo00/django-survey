from django.urls import path
from . import views

app_name = 'surveys'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:survey_id>/', views.detail, name='detail')
]