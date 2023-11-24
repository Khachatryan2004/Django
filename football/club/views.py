from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class LeagueListView(ListView):
    model = League
    template_name = 'index.html'
    context_object_name = 'leagues'


class LeagueDetailView(DetailView):
    model = League
    template_name = 'league_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        league = self.get_object()
        context['clubs'] = Club.objects.filter(league=league)
        return context



