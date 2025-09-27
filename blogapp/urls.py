from django.urls import path
from . import views

app_name="blogapp"

urlpatterns=[
    path("", views.index ,name="index"),
    path("login/",views.login,name="login_page"),
    path("register/",views.register ,name='register_page'),
    path("main/",views.main,name="main_page"),
    path("contact/",views.contact,name="contact_page"),
    path('pageDetail/<str:slug>',views.pageDetail,name='Detail_page')
]