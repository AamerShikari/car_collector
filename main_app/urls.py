from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'), #example path
	path('about/', views.about, name='about'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/signup/', views.signup, name='signup'),
]