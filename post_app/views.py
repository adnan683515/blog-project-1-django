from django.shortcuts import render,redirect
from post_app.forms import post_form
from post_app import models
# Create your views here.

def add_post(request):
    if request.method=='POST':
        form = post_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("homepage")
    else:
        form = post_form()
    return render(request,'post.html',{"form":form})


def edit_post(request,id):
    item = models.add_post.objects.get(pk=id)
    form = post_form(instance=item)
    
    if request.method=='POST':
        form = post_form(request.POST,instance=item)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('homepage')
        
    return render(request,'post.html',{"form":form})

def delete_post(request,id):
    post = models.add_post.objects.get(pk=id)
    post.delete()
    
    return redirect('homepage')
