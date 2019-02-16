from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from main.models import AGAMember

class ListAGAMembers(LoginRequiredMixin, ListView):
    """List all AGA Members
    
    Associated Template: templates/main/agamembers_list.html
    
    """
    model = AGAMember
