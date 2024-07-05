from django.shortcuts import render
from cetagory_app.forms import cetagory_form
# Create your views here.
def add_cetagory(request):
    if request.method == 'POST':
        form = cetagory_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    else:
        form = cetagory_form()
    return render(request,'cetagory.html',{'form':form})