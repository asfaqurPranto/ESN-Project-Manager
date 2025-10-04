from django.shortcuts import render
from django.shortcuts import render, redirect
#newly added
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
# Create your views here.
from Project_Section.models import Project
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# def test_func(request):
#     #return HttpResponse("This is a test response in text.")
#     return render(request, 'test.html')
def test_func(request):
    data = {
        "message": "This is a JSON response",
        "status": "success",
        "items": [1, 2, 3, 4]
    }
    return JsonResponse(data)



def register_func(request):

    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        country=request.POST.get('country')
        city=request.POST.get('city')
        profession=request.POST.get('profession')
        bio=request.POST.get('bio')

        # we will assign username as email(unique)
        username=email
        #print(first_name,last_name,email,password,country,city,profession,bio)
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')
        else:
            user=User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()

            #create a profile object
            profile=Profile.objects.get(user=user)
            profile.country=country
            profile.city=city
            profile.profession=profession
            profile.bio=bio
            profile.save()
            messages.success(request, 'User created successfully')
            return redirect('/')
            
    return render(request, 'register.html')



def login_func(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        #username=email
        #print(username,password)
        from django.contrib.auth import authenticate, login
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            # Redirect to a success page.
            return redirect('/home/')  # Redirect to the admin dashboard or any other page
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid email or password')
            return redirect('/')
    return render(request, 'login.html')



from datetime import date
@login_required(login_url='/')
def home_func(request):
    user=request.user
    #profile=Profile.objects.get(user=user)
    all_projects=Project.objects.all().order_by('-id')
    #all_projects.deadline= all_projects.deadline-(date.today()-all_projects.created_at.date()).days

    for project in all_projects:
        days_passed = (date.today() - project.created_at.date()).days
        days_remaining= project.deadline-days_passed
        if days_remaining < 0:
            days_remaining = 0
        project.days_remaining = days_remaining
    context={'all_projects':all_projects, 'user':user}
    return render(request, 'home.html', context)



@login_required(login_url='/')
def view_profile_func(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    print(user.first_name)
    context={'profile':profile}
    return render(request, 'view_profile.html', context)


@login_required(login_url='/')
def edit_profile_func(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    #print(user.first_name)
    #print(user.last_name)
    context={'profile':profile}
    return render(request, 'edit_profile.html', context)

@login_required(login_url='/')
def update_profile_func(request):
    if request.method == 'POST':
        user=request.user
        profile=Profile.objects.get(user=user)

        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone=request.POST.get('phone')
        education=request.POST.get('education')
        country=request.POST.get('country')
        city=request.POST.get('city')
        profession=request.POST.get('profession')
        bio=request.POST.get('bio')
        
        user.first_name=first_name
        user.last_name=last_name
        user.save()

        profile.phone=phone
        profile.education=education
        profile.country=country
        profile.city=city
        profile.profession=profession
        profile.bio=bio

        
        profile.save()
        
        messages.success(request, 'Profile updated successfully')
        return redirect('/view-profile/')
    return redirect('/edit-profile/')

@login_required(login_url='/')
def discover_people_func(request):
    user=request.user
    all_profiles=Profile.objects.all()
    context={'all_profiles':all_profiles}
    return render(request, 'discover_people.html', context)



from django.contrib.auth import logout
@login_required(login_url='/')
def signout_func(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')
def search_result_func(request):
    query = request.GET.get('q')
    user=request.user
    all_profiles=Profile.objects.filter(user__first_name__icontains=query) | Profile.objects.filter(user__last_name__icontains=query) | Profile.objects.filter(profession__icontains=query) | Profile.objects.filter(city__icontains=query) | Profile.objects.filter(country__icontains=query)
    context={'all_profiles':all_profiles, 'query':query}
    return render(request, 'discover_people.html', context)


@login_required(login_url='/')
def upcoming_features_func(request):
    return render(request, 'base_test.html')