from django.shortcuts import render
from django.views.generic import ListView, DetailView

from core.models import *


class PollDetail(DetailView):
    model = Poll


class PollList(ListView):
    model = Poll


