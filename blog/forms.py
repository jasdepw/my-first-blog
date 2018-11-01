from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    #ModelForm 형식의 Form 생성
    class Meta:
        model = Post
        fields = ('title', 'text')
        #Form을 만들기 위해 사용할 model을 알려줌

