from django.shortcuts import render
from django.db.models import Q
from django.views.generic import View, TemplateView, DetailView, ListView, CreateView, UpdateView, FormView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.db.models import Count
from blog.models import Blog, Category, Comment
from blog.forms import CommentForm
from django.views.generic import DetailView

# Create your views here.

def blog(request):

    qs = Blog.objects.all()
    categories = Category.objects.all()
    most_pop = Blog.objects.annotate(num_coms=Count('blogs')).order_by('-num_coms')[:4]

    context = {
        'title' : "Blogs",
        'blogs' : qs,
        'most_popular' : most_pop,
        'categories' : categories,
    }

    return render(request, "blog.html", context=context)


def blog_detail(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()

    qs = Blog.objects.get(pk=pk)
    qs_com = Comment.objects.filter(blog=pk)
    categories = Category.objects.all()
    most_pop = Blog.objects.annotate(num_coms=Count('blogs')).order_by('-num_coms')[:4]


    context = {
        'blog' : qs,
        'form': CommentForm,
        'comments': qs_com,
        'categories': categories,
        'most_popular': most_pop,
    }

    return render(request, "blog_detail.html", context=context)



# Generic views
class BlogList(ListView):
    model = Blog
    template_name = 'blog.html'
    paginate_by = 1
    context_object_name = 'blogs'


    def get_queryset(self):
        queryset = Blog.objects.all()
        if self.request.GET.get("category_name"):
            queryset = Blog.objects.filter(
                category__title=self.request.GET.get("category_name"))
        return queryset

    def categories(self):
        categories = Category.objects.all()
        return categories

    def pop_blog(self):
        most_pop = Blog.objects.annotate(num_coms=Count('blogs')).order_by('-num_coms')[:1]
        return most_pop


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Blog's List"
        # context['blogs'] = self.get_queryset()
        context['categories'] = self.categories()
        context['most_popular'] = self.pop_blog()
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                comment = Comment(
                    message=request.POST.get('message'),
                    blog=Blog.objects.get(pk=self.kwargs.get('pk')),
                    user_comment=request.user,
                    author = request.user.first_name,
                )
            except:
                comment = Comment(
                    message=request.POST.get('message'),
                    blog=Blog.objects.get(pk=self.kwargs.get('pk')),
                    author = request.POST.get('author'),
                )
            comment.save()

            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = CommentForm
            return HttpResponseRedirect(self.request.path_info)
        else:
            form = CommentForm()
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Blog Detail"
        context['form'] = CommentForm
        context['categories'] = Category.objects.all()
        context['most_popular'] = Blog.objects.annotate(num_coms=Count('blogs')).order_by('-num_coms')[:1]
        context['comments'] = Comment.objects.filter(
            blog_id=self.kwargs.get('pk'))
        return context





    
    

    
