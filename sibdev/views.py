from django.shortcuts import render
from django.views.generic import TemplateView

from sibdev.models import UrlQueue, Results


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        results = Results.objects.all()
        context['results'] = results
        return context