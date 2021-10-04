"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from api import views as api_views
from frontend import views as frontend_views
from service import views as service_views
from django.contrib.auth import login, logout, views as auth_views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'clients', api_views.ClientsViewSet)
router.register(r'employees', api_views.EmployeeViewSet)
router.register(r'expenses', api_views.ExpenseViewSet)
router.register(r'incomes', api_views.IncomeViewSet)
router.register(r'messages', api_views.MessageViewSet)
router.register(r'users', api_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', service_views.signup, name='signup'),
    path('login/', service_views.login, name='login'),
    path('logout/', service_views.logout, name='logout'),
    path('about/', frontend_views.about, name='about'),
    path('contacts/', frontend_views.contacts),
    path('employees/', frontend_views.employees, name='employees'),
    path('', frontend_views.landing, name='landing'),
    path('sert/', frontend_views.sert),
    # path('', frontend_views.index, name='home'),
    #api
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
