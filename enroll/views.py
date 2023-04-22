from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from .forms import StudentRegistration, UserRegistration
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
    p = Paginator(user_data, 4)

    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    context = {'page_obj': page_obj}

    return render(request, 'enroll/addandshow.html', {'form': form, 'user_data': user_data, 'context': context})

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

def student_register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
        form = UserRegistration()
        return redirect(reverse('student_register'))
    else:
        form = UserRegistration()
    
    return render(request, 'enroll/adduser.html', {'form': form})