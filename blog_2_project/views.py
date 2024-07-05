
from django.shortcuts import render
from post_app.models import add_post

def home(request):
    data = add_post.objects.all()
    print(data)
    return render(request,'home.html',{'data':data})