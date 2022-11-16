from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    return render(request, 'uchaguzi/home.html')

@login_required
def candidates(request):
    return render(request, 'uchaguzi/candidates.html')