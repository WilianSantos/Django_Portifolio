# Generated by Django 4.1.7 on 2023-05-01 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portifolio', '0004_experiencias_formacao_projetos_skills_delete_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencias',
            name='cidade',
            field=models.CharField(max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='formacao',
            name='duracao_ano',
            field=models.CharField(max_length=20, verbose_name='Duração'),
        ),
    ]
