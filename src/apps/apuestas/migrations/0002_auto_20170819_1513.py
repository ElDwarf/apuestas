# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 15:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apuestas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apuestas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apuestas.Pregunta')),
            ],
        ),
        migrations.AlterField(
            model_name='respuestavalidas',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizada'),
        ),
        migrations.AddField(
            model_name='apuestas',
            name='respuesta_valida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuestas.RespuestaValidas'),
        ),
        migrations.AddField(
            model_name='apuestas',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='apuestas',
            unique_together=set([('user', 'pregunta')]),
        ),
    ]
