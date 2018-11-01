from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

#models.py에 정의된 모델을 가져옴

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

'''
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
'''

def post_new(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        #method가 POST인 경우 폼에서 받은 데이터를 PostForm으로 넘겨줌
        if form.is_valid():
            post = form.save(commit=False)
            #폼 저장
            post.author = request.user
            #작성자 추가
            post.published_date = timezone.now()
            #작성 시간 추가
            post.save()    
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(request.POST)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #get_object_or_404을 호출하여 수정하고자 하는 글의 Post 모델 인스턴스를 가져옴
    #pk는 원하는 포스트를 찾는데 사용(primary key)
    if request.method =="POST":
        form = PostForm(request.POST, instance=post)
        #method가 POST인 경우 폼에서 받은 데이터를 PostForm으로 넘겨줌
        if form.is_valid():
            post = form.save(commit=False)
            #폼 저장
            post.author = request.user
            #작성자 추가
            post.published_date = timezone.now()
            #작성 시간 추가
            post.save()    
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
