from django.urls import path
from .views import LandingView, ListView, DetailView, CreateView, EditView, DeleteView

app_name="computadoras"

urlpatterns = [
    path('edit/<int:computer_id>', EditView.as_view(), name="edit"),
    path('detail/<int:computer_id>', DetailView.as_view(), name="detail"),
    path('delete/<int:computer_id>', DeleteView.as_view(), name="delete"),
    path('create', CreateView.as_view(), name="create"),
    path('', LandingView.as_view(),name="landing"),
    path('list', ListView.as_view(), name="list"),

]