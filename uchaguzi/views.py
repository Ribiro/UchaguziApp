from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Candidate


# Create your views here.
def home_page(request):
    return render(request, 'uchaguzi/home.html')

@login_required
def candidates(request):
    context = {
        'candidates': Candidate.objects.all()
    }
    return render(request, 'uchaguzi/candidates.html', context)