from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LogoutView
from merge import settings
from django.contrib.auth import views as auth_views
app_name='blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('postform', views.post_form, name='post_form'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post_del/<slug:slug>/', views.post_del, name='post_del'),
    path('category/',views.category,name='category'),
    path('category/<slug:slug>',views.cat_ind,name='cat_ind'),
    path('tag/',views.tag,name='tag'),
    path('tag/<slug:slug>',views.tag_ind,name='tag_ind'),
    path('login/', views.Login, name ='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/', views.register, name ='register'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit',views.profile_edit,name="profile_edit"),
]