from django import forms
from .models import Posts

class PostUpdateForm(forms.ModelForm):
    title = forms.CharField(required=False)
    content = forms.CharField(required=False)
    username = forms.CharField(required=False)
    password = forms.CharField(required=False)

    class Meta:
        model = Posts
        # 수업 자료 화면 순서대로 배치
        fields = ['title', 'content', 'username', 'password']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("제목을 입력해주세요.")
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("내용을 입력해주세요.")
        return content

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("비밀번호를 입력해주세요.")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("글쓴이를 입력해주세요.")
        return username