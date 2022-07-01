from re import U
from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name: str = 'post_list.html'


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')
    template_name: str = 'post_form.html'


class PostDetailView(DetailView):
    model = Post
    template_name: str = 'post_detail.html'

class PostUpdateView(UpdateView):
    moodel = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')
    template_name: str = 'post_form.html'

class PostDeleteView(DeleteView):
    moodel = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')
    template_name: str = 'post_confirm_delete.html'
