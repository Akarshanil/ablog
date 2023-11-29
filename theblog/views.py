from django.shortcuts import render,get_object_or_404
from .models import post,category,Command
from django.views.generic  import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import postform,Editform,Editcommentform
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

# Create your views here.
# def home(request):
#     return render(request,"home.html",{})

class HomeView(ListView):
    model = post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-publication_date']

    def get_context_data(self, *args, **kwargs):                    #the get the data to the html page
            cart_menu = category.objects.all()
            context = super(HomeView, self).get_context_data(*args, **kwargs)
            context["cart_menu"] = cart_menu
            return context



class  ArticleDetailView(DetailView):
    model = post
    template_name = "article_detail.html"

    def get_context_data(self, *args, **kwargs):  # the get the data to the html page
        cart_menu = category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff=get_object_or_404(post,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        liked=False
        if stuff.like.filter(id=self.request.user.id).exists():
            liked=True
        context['liked']=liked
        context["cart_menu"] = cart_menu
        context["total_likes"] =total_likes
        return context
class AddPostView(CreateView):
    model = post
    form_class = postform
    template_name = "add_post.html"
    # fields = '__all__'
    # fields = ('title','body')
class AddCategoryView(CreateView):
    model = category
     # form_class = postform
    template_name = "add_category.html"
    fields = '__all__'
    # fields = ('title','body')
class UpdatePostView(UpdateView):
    model = post
    form_class = Editform
    template_name = 'update.html'
    # fields = ['title','title_tag','body']
class DeletePostView(DeleteView):
    model = post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
def CategoryView(request,cats):
    print(cats.replace('-', ' '))
    cart_menu = category.objects.all()
    category_post = post.objects.filter(category=cats.replace('-', ' '))
    return render(request,"categories.html",{'cats':cats.title().replace('-', ' '),"category_post":category_post,'cart_menu':cart_menu})
def CategoryListView(request):
    cart_menu_list = category.objects.all()
    return render(request,"categories_list.html",{'cart_menu_list':cart_menu_list})
def LikeView(request, pk):
    Post = get_object_or_404(post, id=request.POST.get('post_id'))
    liked = False
    if Post.like.filter(id=request.user.id).exists():
        Post.like.remove(request.user)
    else:
        Post.like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
class AddcommentView(CreateView):
    model = Command
    form_class = Editcommentform
    template_name = "addcomments.html"
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)


