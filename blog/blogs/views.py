from django.shortcuts import render,get_object_or_404
from . import models
# Create your views here.
def base(request):
    data = models.Blog.objects
    return render(request,'blog.html',{'data':data})
def blog_text(request,blog_id):
  #  blogs = models.Blog.objects
    blog = get_object_or_404(models.Blog,pk=blog_id)
    return render(request,'blog_text.html',{"blog":blog})