"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.paragraphs, name='paragraph'),
    path('update_paragraph/<id>', views.update_paragraph, name='update_paragraph'),
    path('delete_paragraph/<id>', views.delete_paragraph, name='delete_paragraph'),
    path('', views.home, name='home'),	 

		 
	path('login/', views.login_page, name='login_page'), 
	path('register/', views.register_page, name='register'), 
    path('logout/', views.custom_logout, name="logout"),
]