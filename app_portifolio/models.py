from django.db import models
import uuid

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Project(models.Model):
    projeto = models.CharField('Projeto', max_length=20)
    descricao = models.CharField('Descrição', max_length=20)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': (650, 350)})
    url = models.CharField('URL', max_length=60)
