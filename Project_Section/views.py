from email import message
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
#newly added
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib import messages

from Project_Section.models import Project
from Profile_Section.models import Profile
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def create_project_func(request):
    return render(request, 'create_project.html')

@login_required(login_url='/')
def add_project_func(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        deadline=request.POST.get('deadline')
        tags=request.POST.get('tags')

        #get the user
        user=request.user
        #print(user)

        #create a project object
        project=Project.objects.create(creater=user, title=title, description=description, deadline=deadline, tags=tags)
        project.save()
        messages.success(request, 'Project created successfully')
        return redirect('/home/')
    return redirect('/home/')

from datetime import date
@login_required(login_url='/')
def project_description_func(request, pid):
    project = Project.objects.get(id=pid)
    #days_remaining = (project.deadline - date.today()).days
    days_passed = (date.today() - project.created_at.date()).days
    days_remaining= project.deadline-days_passed
    print(days_remaining)
    if days_remaining < 0:
        days_remaining = 0
    project.days_remaining = days_remaining
    return render(request, 'project_description.html', {'project': project, 'days_remaining': days_remaining})

@login_required(login_url='/')
def project_func(request, pid):
    return render(request, 'test.html')


import logging

from Project_Section.models import Message
logger = logging.getLogger(__name__)
@login_required(login_url='/')
def project_discussion_func(request, pid):
    #return HttpResponse("View called")
    if request.method == 'POST':
        message_text = request.POST.get('message_text')
        user = request.user
        project = Project.objects.get(id=pid)
    
        msg=Message.objects.create(sender=user, project=project, content=message_text)
        msg.save()
        if msg.id:
            print("Message created successfully:")
        else:
            print("Message was not created.")

        return redirect(f'/project-discussion/{pid}/')

    all_messages = Message.objects.filter(project__id=pid).order_by('created_at')
    project = Project.objects.get(id=pid)
    project_title=project.title
    user=request.user
    return render(request, 'project_discussion.html', {'all_messages': all_messages, 'user': user, 'pid': pid, 'project': project, 'project_title': project_title})

 #   return render(request, 'project_discussion.html', {'pid': pid})       