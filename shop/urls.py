from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.single, name='single'),
    path('<int:id>/update/', views.update_view, name='update'),
]
