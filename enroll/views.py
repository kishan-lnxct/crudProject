from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import StudentRegistration
from .models import User


# Create your views here.
def add_show(request):

    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
        form = StudentRegistration()
        return redirect(reverse('add_show'))
    else:
        form = StudentRegistration()
    
    user_data = list(User.objects.all())
    return render(request, 'enroll/addandshow.html', {'form': form, 'user_data': user_data})

def delete_record(request, id):

    if request.method == 'POST':
        delete_user = User.objects.get(pk=id)
        delete_user.delete()

    return redirect('/')

def update_record(request, id):
    if request.method == 'POST':
        update_usr = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=update_usr)
        if form.is_valid():
            form.save()
        form = StudentRegistration()
        return redirect(reverse('add_show'))
    else:
        update_usr = User.objects.get(pk=id)
        form = StudentRegistration(instance=update_usr)

    return render(request, 'enroll/updatestudents.html', {'form': form})