from  . import views
from django.urls import path

urlpatterns = [
    path('',views.base),
    path('<int:blog_id>/',views.blog_text),
]