from django.urls import path
from .views import home, add_item,  delete_item, edit_item


app_name = "singnle_app"

urlpatterns = [
    path('', home, name='home'),
    path('add-item/', add_item, name='add-item'),
    path('edit-item/<int:pk>/', edit_item, name='edit-item'),
    path('delete-item/<int:pk>/', delete_item, name='delete-item'),
   
    
]