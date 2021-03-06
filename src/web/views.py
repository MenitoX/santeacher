from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
def home_view(request, *args, **kwargs):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "home.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by= 3

class UserPostListView(ListView):
    model = Post
    template_name = 'home/user_post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by= 3
    
    def get_query_set (self):
        User =get_object_or_404 (User, username=self.kwargs.get('username'))
        return post.objects.filter(author=User).ordery_by('-date_posted')

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
   
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
   
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True    
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True    
        return False



def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'This is about us',
        'my_number': 123,
        'my_list': [124,'ta',54]
    }
    return render(request, "about.html", my_context)    
