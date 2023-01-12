from django.contrib import admin
from django.urls import path
from .views import listview,detailview,tagview,tableview

urlpatterns = [
  path('admin/',admin.site.urls),
  path('list/',listview,name='list'),
  path('detail/<int:pk>/',detailview,name='detail'),
  path('tag/',tagview,name='tag'),
  path('table/',tableview,name='table'),
]
