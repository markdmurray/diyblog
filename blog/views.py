from django.shortcuts import render
from django.views import generic
from .models import Author, Blog, BlogComment
from django.shortcuts import get_object_or_404
# Create your views here.

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.ListView):
    model = Blog
    template_name = 'authordetailview.html'
    context_object_name = 'authordetail'

    def get_queryset(self):
        id = self.kwargs['pk']
        target_author=get_object_or_404(Author, pk = id)
        return Blog.objects.filter(author=target_author)

class BlogListView(generic.ListView):
    model = Blog
    template_name = 'bloglistview.html'
    context_object_name = 'bloglist'

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blogdetailview.html'
    context_object_name = 'blogdetail'

    def get_queryset(self):
        id = self.kwargs['pk']
        target_blog = get_object_or_404(Blog, pk = id)
        return Blog.objects.filter(title = target_blog)

class BloggerListView(generic.ListView):
    model = Author
    template_name = 'bloggerlist.html'
    context_object_name = 'bloggerview'

def index(request):
    return render(request,'index.html',
    )