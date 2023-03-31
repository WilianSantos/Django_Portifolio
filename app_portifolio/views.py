from django.shortcuts import render


class IndexView:
    
    template_name = 'index.html'
    
    def index(request):
    
        return render(request, 'index.html')
