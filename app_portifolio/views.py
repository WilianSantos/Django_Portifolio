from django.views.generic import TemplateView

from .models import Project


class IndexView(TemplateView):
    
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['projeto'] = Project.objects.order_by('?').all()
        return context
