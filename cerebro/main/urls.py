from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('members', views.ListAGAMembers.as_view(), name='list_aga_members'), # Member List
]
