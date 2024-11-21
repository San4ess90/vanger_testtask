from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Slider


class HomePageView(TemplateView):
    template_name = 'site_nasa/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = Slider.objects.all()
        return context
