from django.shortcuts import render
from author_app.forms import author_form
# Create your views here.

def add_author(request):
    if request.method=='POST':
        form = author_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    else:
        form = author_form() 
    return render(request,'author.html',{'form':form})