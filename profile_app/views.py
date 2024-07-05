from django.shortcuts import render
from profile_app.forms import profile_form
# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        form = profile_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    else:
        form = profile_form()
    return render(request,'profile.html',{'form':form})