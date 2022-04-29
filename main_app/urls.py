from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'), #example path
	path('about/', views.about, name='about'),
	path('cars/', views.cars_index, name='index'),
	path('cars/<int:car_id>/', views.cars_detail, name='detail'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/signup/', views.signup, name='signup'),
	path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
]