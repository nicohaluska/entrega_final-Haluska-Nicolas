from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'core/pages.html'
    context_object_name = 'posts'

from django.shortcuts import get_object_or_404, redirect
from .models import Post, Comentario

class PostDetailView(DetailView):
    model = Post
    template_name = 'core/page_detail.html'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        post = self.get_object()
        contenido = request.POST.get('contenido')

        if contenido:
            Comentario.objects.create(
                post=post,
                autor=request.user,
                contenido=contenido
            )

        return redirect('page_detail', pk=post.pk)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'core/page_form.html'
    success_url = reverse_lazy('pages')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
# Create your views here.
