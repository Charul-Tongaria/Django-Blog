from .models import Category, Comment, Post, Tag
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})


def post_detail(request,slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(parent=None)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            print(comment_form)
            new_comment = comment_form.save(commit=False)
            parent_id = request.POST.get("parent_id")
            parent_obj = Comment.objects.filter(id = parent_id).first()
            new_comment.parent = parent_obj
            new_comment.post = post
            new_comment.author = request.user
            new_comment.published_date = timezone.now()
            parent_id = request.POST.get('comment_id') #reply-section
            comment_qs = None
            if parent_id:
                comment_qs = Comment.objects.get(id=parent_id)
            new_comment.parent = comment_qs
            new_comment.save()
            
    comment_form = CommentForm()
    return render(request, template_name, {'post': post, 'comments': comments, 'new_comment': new_comment, 'form': comment_form})


def post_form(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
       
        post.save()
        form.save_m2m()
        return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_del(request,slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('blog:post_list')


def category(request):
    cat = Category.objects.order_by('created_date')
    return render(request,'blog/category.html',{'cat':cat})


def cat_ind(request,slug):
    cat= get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=cat)
    return render(request, 'blog/cat_ind.html',{'posts':posts})


def tag(request):
    tag = Tag.objects.order_by('created_date')
    return render(request, 'blog/tag.html', {'tag':tag})
    #return render(request,'blog/tag.html',{'tag':tag})


def tag_ind(request,slug):
    tag= get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tag=tag)
    return render(request, 'blog/tag_ind.html',{'posts':posts})


def register(request):
    msg=None
    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        msg="Something is wrong"
        if form.is_valid():
            form.save()
            return redirect('blog:login')
    form = UserCreationForm()
    return render(request,'blog/register.html',{'form': form,'msg':msg})

   
def Login(request):
    if request.method == 'POST':   
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Welcome {username} !!')
            return redirect('/')
        else:
            messages.info(request, f'Account done not exit. Please sign in')
    form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form':form, 'title':'log in'}) 


def profile(request):
    args={'user':request.user} 
    return render(request, 'blog/profile.html', args)


def profile_edit(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request, 'blog/edit_profile.html', args)


#def Logoutview(request):
 #  logout(request)
  # return redirect('blog:logout')

def logoutUser(request):
    logout(request)
    return redirect('/login/')
