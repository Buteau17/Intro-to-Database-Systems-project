from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("database", views.database_test, name="database"),   
    path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('show',views.show), 
    path('show/<int:page>',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  
  
