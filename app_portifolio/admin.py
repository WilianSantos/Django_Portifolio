from django.contrib import admin

from .models import Formacao, Projetos, Skills, Experiencias


admin.site.register(Projetos)    
admin.site.register(Formacao)
admin.site.register(Skills) 
admin.site.register(Experiencias)