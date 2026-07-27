from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost


# Список всех статей
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'posts'   # в шаблоне переменная posts

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

# Детальная страница одной статьи
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
    context_object_name = 'post'    # в шаблоне переменная post

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj

# Создание новой статьи (форма + сохранение)
class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']   # поля в форме
    template_name = 'blog/blogpost_form.html'
    success_url = reverse_lazy('blog:list')   # перенаправление после создания


# Редактирование статьи (форма с данными + сохранение)
class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blogpost_form.html'


    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk': self.object.pk})


# Удаление статьи (подтверждение + удаление)
class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_delete.html'
    success_url = reverse_lazy('blog:list')