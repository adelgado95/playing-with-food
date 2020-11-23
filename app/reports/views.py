import requests

from django.views.generic.base import TemplateView
from django.template import loader
from django.shortcuts import render, redirect
from pwfbackend import settings



class IndexView(TemplateView):
    template_name = 'reports/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

