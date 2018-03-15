from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='homepage'),
    path('blog/blogs', views.BlogListView.as_view(), name='bloglist'),
    path('blogger/<int:pk>', views.AuthorDetailView.as_view(), name='authorbloglist'),

]