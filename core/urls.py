from django.urls import path
from .views import Home, ProfileList

app_name = 'core'

urlpatterns = [
    path('', Home.as_view()),
    path('profile/', ProfileList.as_view(), name='profile_list')
]
