# Generated by Django 4.0.4 on 2022-04-28 20:13

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_alter_consultor_options_alter_dieta_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='suplementacao',
            name='link_imagem',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='suplementacao',
            name='link_propaganda',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='consultor',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to='img', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='descricao',
            field=models.TextField(max_length=800, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='home',
            name='descricao',
            field=models.TextField(max_length=800, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='suplementacao',
            name='descricao',
            field=models.TextField(max_length=800, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='treinos',
            name='descricao',
            field=models.TextField(max_length=800, verbose_name='descrição'),
        ),
    ]