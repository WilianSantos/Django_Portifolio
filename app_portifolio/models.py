from django.db import models
import uuid

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Projetos(models.Model):
    projeto = models.CharField('Projeto', max_length=20)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': (650, 350)})
    url = models.CharField('URL', max_length=60)
    
    def __str__(self):
        return self.projeto
    
    
class Formacao(models.Model):
    duracao_ano = models.CharField('Duração', max_length=20)
    formacao = models.CharField('Formação', max_length=100)
    universidade = models.CharField('Universidade', max_length=100)
    local = models.CharField('Local', max_length=100)
    
    def __str__(self):
        return self.formacao
    
    
class Skills(models.Model):
    nome = models.CharField('Nome', max_length=15)
    porcentagem = models.IntegerField('Porcentagem')
    
    def __str__(self):
        return self.nome
    
    
class Experiencias(models.Model):
    proficao = models.CharField('Profição', max_length=50)
    duracao_ano = models.CharField('Duração', max_length=15)
    empresa = models.CharField('Empresa', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    
    def __str__(self):
        return self.proficao
