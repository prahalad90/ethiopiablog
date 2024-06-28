from django.urls import path, re_path
from app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name = "contact"),
    path('<slug:slug>',views.blogcate,name = "blogcategory"),
    path('<slug:catslug>/<slug:slug>',views.post,name = "post"),
    path('travelguide/',views.travelguide,name = "travelguide"),
    path('<slug:slug>/',views.guidelinepage,name = "guideline"),
]