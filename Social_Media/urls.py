"""
URL configuration for Social_Media project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#newly added
from Profile_Section.views import *
from Project_Section.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    #path('profile/', include('Profile_Section.urls')),
    path('test/',test_func, name='test'),


    path('',login_func, name='login'),
    path('register/',register_func, name='register'),
    path('home/',home_func, name='home'),

    path('view-profile/',view_profile_func, name='view-profile'),
    path('edit-profile/',edit_profile_func, name='edit-profile'),
    path('update-profile/',update_profile_func, name='update-profile'),

    path('discover-people/',discover_people_func, name='discover-people'),
    path('search-result/',search_result_func, name='search-result'),

    path('sign-out/',signout_func, name='sign-out'),
    path('upcoming-features/',upcoming_features_func, name='upcoming-features'),

    
    # Project Section URLs: functions are in Project_Section/views.py
    path('create-project/',create_project_func, name='create-project'),
    path('add-project/',add_project_func, name='add-project'),
    path('project-description/<int:pid>/',project_description_func, name='project-description'),
    path('project/<int:pid>/',project_func, name='project'),
    path('project-discussion/<int:pid>/',project_discussion_func, name='project-discussion'),
    
    

]
