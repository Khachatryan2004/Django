from django.urls import path
from .views import *


urlpatterns = [
    path('', LeagueListView.as_view(), name='league'),
    path('<int:pk>/', LeagueDetailView.as_view(), name='league-detail'),

]
