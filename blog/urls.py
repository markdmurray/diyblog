from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('blogs/', views.BlogListView.as_view(), name='bloglist'),
    path('bloggers', views.BloggerListView.as_view(), name='bloggerlist'),
    path('bloggers/<int:pk>', views.AuthorDetailView.as_view(), name='bloggerdetail'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blogdetail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggerview'),

]