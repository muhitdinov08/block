from django.urls import path

from .views import AboutView, Post_Create_View, Post_Delete_View, Post_Detail_View, Register_view, Logout_view, \
    Login_view, home_page, profile_page

app_name = 'muhammadamin'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('home.html/', home_page, name='home_page'),
    path('about.html/', AboutView.as_view(), name='about_page'),
    path('profile.html/', profile_page, name='profile_page'),
    path('post_form.html/', Post_Create_View.as_view(), name='post_create_page'),
    path('register.html/', Register_view, name='register_page'),
    path('login.html/', Login_view, name='login_page'),
    path('logout/', Logout_view, name='logout_page'),
    path('post_detail.html/', Post_Detail_View, name='post_detail_page'),
    path('post_conifirm_delete.html/', Post_Delete_View, name='post_delete_page'),
]
