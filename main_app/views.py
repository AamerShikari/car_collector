from django.shortcuts import render, redirect

# Add the following import
import uuid
import boto3 
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Anime
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST': 
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('about')
    else: 
      error_message = 'Invalid sign up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def animes_index(request):
    animes = Anime.objects.filter(user=request.user)
    return render(request, 'animes/index.html', {'animes': animes})

def animes_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    return render(request, 'animes/detail.html', {'anime': anime})

class animeCreate(CreateView):
  model = Anime
  fields =['title','category','language','description']
  def form_valid(self, form):
    form.instance.user = self.request.user  # form.instance is the anime
    return super().form_valid(form)

class animeUpdate(UpdateView):
  model = Anime
  fields =['category','language','description']
  
class animeDelete(DeleteView):
  model = Anime
  success_url = '/animes/'
