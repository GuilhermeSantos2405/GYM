# Generated by Django 4.0.4 on 2022-04-27 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Propaganda',
        ),
        migrations.RemoveField(
            model_name='consultor',
            name='faculdade',
        ),
    ]
