from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>', views.categories, name='category' ),
    path('<slug:slug>', views.article, name="article")
]
