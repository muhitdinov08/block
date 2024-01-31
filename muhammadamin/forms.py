from django import forms
# from django.db.transaction import commit

from .models import Post, Author
from django.core.exceptions import ValidationError


class Create_Post_Form(forms.Form):
    title = forms.CharField(max_length=30)
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        models = Post
        fields = ['title', 'content']

    def save(self):
        title = self.cleaned_data['title']
        content = self.cleaned_data['content']
        Post.objects.create(title=title, content=content)


class Register_Form(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    email = forms.EmailField()
    password1 = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)

    def save(self, commit=True):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 == password2:
            user = super().save(commit)
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError("Password must be match")

    class Meta:
        models = Author
        fields = ['username', 'gender', 'age', 'first_name', 'last_name', 'email', 'posts']


class Login_Form(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)
