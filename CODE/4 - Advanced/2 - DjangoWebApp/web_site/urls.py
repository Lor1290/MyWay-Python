from django.urls import path
from . import views

urlpatterns = [
    path('', views.Pages.home, name = 'home_page'),
    path('about/', views.Pages.about, name = "about_page"),
    path('about/link/', views.Pages.email_page, name = "email_page"),
    path('link', views.Pages.link, name = "link_page"),
]