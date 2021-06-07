from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

def updates(request):
    context = {'posts': Post.objects.all()}
    return render(request, "updates/updates.html",context)

class PostListView(ListView):
    model = Post
    template_name = 'updates/updates.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
