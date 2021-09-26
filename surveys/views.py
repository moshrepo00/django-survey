from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Survey
from django.shortcuts import render 


def index(request):
    survey_list = Survey.objects.order_by('-published')[:5]
    context = {'survey_list': survey_list}
    return render(request, 'surveys/index.html', context)

def detail(request, survey_id):
    try:
        survey = Survey.objects.get(pk=survey_id)
    except Survey.DoesNotExist:
        raise Http404('Survey does not exist')
    return render(request, 'surveys/detail.html', {'survey': survey})

def create(request):
    return HttpResponse(f'You have arrived at the create page')