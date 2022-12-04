from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Candidate, POResult, PollingStation
import pygal
from pygal.style import Style


# Create your views here.
def home_page(request):
    bar_chart = pygal.Bar()
    # Then create a bar graph
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Presidential Results'
    line_chart.add('Raila', 20.5)
    line_chart.add('Ruto', 36.7)
    line_chart.add('Wajackoyah', 6.3)
    line_chart.add('Mwaure', 4.5)
    line_chart.add('Muite', 80.3)
    chart = line_chart.render_data_uri()
    context = {
        'chart': chart
    }
    return render(request, 'uchaguzi/home.html', context)

@login_required
def candidates(request):
    po = request.user
    results = po.po_results.all()
    candidates = Candidate.objects.all()
    show_publish_button = False
    if len(results) == len(candidates):
        show_publish_button = True
        
    is_published = []
    published_status = ''
    for result in results:
        is_published.append(result.is_published)
        
    try:
        published_status = is_published[0]
    except:
        published_status = False
        
    candidates_data = []
    if results:
        for candidate in candidates:
            the_result = POResult.objects.filter(polling_station=po.polling_station, id_number=candidate.id_number)
            # print(the_result.first())                 
            candidates_data.append({
                'first_name': candidate.first_name,
                'last_name': candidate.last_name,
                'party': candidate.party,
                'id': candidate.id,
                'is_published': published_status,
                'po_result': the_result.first()
            })
    else:
        for candidate in candidates:
            candidates_data.append({
                'first_name': candidate.first_name,
                'last_name': candidate.last_name,
                'party': candidate.party,
                'id': candidate.id,
                'is_published': published_status,
                'po_result': None
            })
    candidates_data.reverse()
    published = str(published_status)
    print(published) 
    
    context = {
        'candidates': candidates_data,
        'show_publish_button': show_publish_button,
        'po': po,
        'published': published
    }
    return render(request, 'uchaguzi/candidates.html', context)

class POResultCreateView(LoginRequiredMixin, CreateView):
    template_name = 'uchaguzi/po_results.html'
    model = POResult
    success_url = '/candidates/'
    fields = ['votes']
    this_candidate = Candidate
    
    def form_valid(self, form):
        this_candidate = Candidate.objects.get(pk=self.kwargs['pk'])
        polling_station = PollingStation.objects.get(assigned_user=self.request.user)
        
        form.instance.candidate_first_name = this_candidate.first_name
        form.instance.candidate_middle_name = this_candidate.middle_name
        form.instance.candidate_last_name = this_candidate.last_name
        form.instance.polling_station = polling_station.name
        form.instance.id_number = this_candidate.id_number
        form.instance.assigned_user = self.request.user
        return super().form_valid(form)
    
@login_required
def confirm_publish_results(request):
    po = request.user
    results = po.po_results.all()
    print('hi')
    for result in results:
        print(result)
    context = {
        'results': results
    }
    return render(request, 'uchaguzi/publish_results.html', context)

@login_required
def publish_results(request):
    po = request.user
    results = po.po_results.all()
        
    for result in results:
        result.is_published = True
        result.save()
    return redirect('/candidates')    
        