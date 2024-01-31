from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import Create_Post_Form, Login_Form, Register_Form

from .models import About, Post


def profile_page(request):
    posts = Post.objects.all()
    return render(request, 'muhammadamin/profile.html', {"posts": posts})


# def about_page(request):
#     abouts = About.objects.all()
#     return render(request, 'muhammadamin/about.html', abouts)


class AboutView(View):
    def get(self, request):
        abouts = About.objects.all()
        return render(request, 'muhammadamin/about.html', {'abouts': abouts})


class Post_Create_View(View):
    model = Post
    form = Create_Post_Form
    fields = ["name", "books"]
    success_message = 'Post successfully created'
    template_name = "muhammadamin/post_form.html"

    def post(self, request):
        form = Create_Post_Form(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('muhammadamin:home_page')
        else:
            return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = Create_Post_Form()
        return render(request, self.template_name, {'form': form})


def Post_Detail_View(request):
    posts = Post.objects.all()
    return render(request, 'muhammadamin/post_detail.html', {"posts": posts})


def Post_Delete_View(request):
    if request.method == 'POST':
        request.POST.delete()
    return render(request, "muhammadamin/post_confirm_delete.html ")


def Register_view(request):
    if request.method == 'POST':
        form = Register_Form(data=request.POST)
        if form.is_valid():
            messages.success(request, "User successfully registered")
            return render(request, "muhammadamin/home.html")
        else:

            return render(request, "muhammadamin/register.html", context={"form": form})
    elif request.method == 'GET':
        form = Register_Form(request.GET)
        return render(request, "muhammadamin/register.html", context={"form": form})


def Login_view(request):
    if request.method == 'POST':
        form = Login_Form(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.COOKIES)
                messages.success(request, "user successfully logged in")
                return redirect("muhammadamin:home_page")
            else:
                messages.error(request, "Username or password wrong")
                return redirect("muhammadamin:login_page")
        else:
            messages.error(request, "User didn't login correctly")
            return render(request, "muhammadamin/login.html", context={"form": form})

    else:
        form = Login_Form(data=request.GET)
        return render(request, "muhammadamin/login.html", context={"form": form})


def Logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('muhammadamin:home_page ')
    else:
        logout(request)
        return render(request, "muhammadamin/home.html")


def home_page(request):
    return render(request, "muhammadamin/home.html")
