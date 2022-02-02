from unicodedata import name
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Home(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'index.html')

@method_decorator(login_required, name='dispatch')
class ProfileList(View):
  def get(self, request, *args, **kwargs):
    profiles = request.user.profiles.all
    return render(request, 'profileList.html', {
      'profiles': profiles
    })