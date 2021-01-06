
from django.urls import path,re_path


from . import views


urlpatterns = [
    path('',views.index,name='indexpage'),
    path('post/', views.view_post, name='view_post'),
]
