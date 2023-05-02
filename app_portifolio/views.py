from django.views.generic import TemplateView

from .models import Formacao, Projetos, Skills, Experiencias 


class IndexView(TemplateView):
    
    template_name = 'index.html'
    
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['projetos'] = Projetos.objects.order_by('?').all()
        context['formacao'] = Formacao.objects.order_by('?').all()
        context['skills'] = Skills.objects.order_by('?').all()
        context['experiencias'] = Experiencias.objects.order_by('?').all()
        return context
