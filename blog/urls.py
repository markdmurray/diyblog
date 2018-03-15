from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='homepage'),
    path('blog/blogs', views.BlogListView.as_view(), name='bloglist'),
    path('blogger/<int:pk>', views.AuthorDetailView.as_view(), name='authorbloglist'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blogdetail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggerview'),

]