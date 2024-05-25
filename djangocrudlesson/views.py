from django.shortcuts import render, redirect
from .models import Gender
from django.contrib import messages

# Create your views here.

def index_gender(request):
    genders = Gender.objects.all()

    context = {
        'genders': genders
    }
    return render(request, 'gender/index.html', context)

def create_gender(request):
    return render(request, 'gender/create.html')

def store_gender(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender) #insert into genders(gender) values(gender)
    messages.success(request, 'Gender successfully saved!')
    return redirect('/genders')

def show_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id) #SELECT * FROM genders WHERE gender_id = gender_id

    context = {
        'gender': gender,
    }

    return render(request, 'gender/show.html', context)

def edit_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)

    context = {
        'gender': gender,
    }

    return render(request, 'gender/edit.html', context)

def update_gender(request, gender_id):
    gender = request.POST.get('gender')

    Gender.objects.filter(pk=gender_id).update(gender=gender) #UPDATE genders SET gender = gender WHERE gender_id = gender_id
    messages.success(request, 'Gender Successfully Saved')


    return redirect("/genders")

def delete_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)

    context = {
        'gender': gender,
    }

    return render(request, 'gender/delete.html', context)

def destroy_gender(request, gender_id):
    Gender.objects.filter(pk=gender_id).delete() # DELETE FROM genders WHERE gender_id = gender_id
    messages.success(request, 'Gender Successfully Deleted')

    return redirect('/genders')