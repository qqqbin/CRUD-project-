from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.main, name='main'),
    path('detail/<str:id>/', blog.views.detail, name='detail'),
    path('read/', blog.views.read, name='read'),
    path('write/create', blog.views.create, name='create'),
    path('edit/<str:id>/', blog.views.edit, name='edit'),
    path('delete/<str:id>/', blog.views.delete, name='delete'),
    path('hashtag/', blog.views.hashtagform, name='hashtag'),
    path('<int:hashtag_id>/search/', blog.views.search, name='search'),

]
