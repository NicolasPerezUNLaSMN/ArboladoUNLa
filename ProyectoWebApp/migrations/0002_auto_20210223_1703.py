# Generated by Django 3.1.7 on 2021-02-23 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProyectoWebApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arbol',
            name='id',
        ),
        migrations.RemoveField(
            model_name='calle',
            name='id',
        ),
        migrations.RemoveField(
            model_name='coordenada',
            name='id',
        ),
        migrations.RemoveField(
            model_name='estadodelarbol',
            name='id',
        ),
        migrations.AddField(
            model_name='arbol',
            name='censo',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ProyectoWebApp.censo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calle',
            name='censo',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ProyectoWebApp.censo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coordenada',
            name='censo',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ProyectoWebApp.censo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estadodelarbol',
            name='arbol',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ProyectoWebApp.arbol'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagen',
            name='arbol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProyectoWebApp.arbol'),
        ),
        migrations.AlterField(
            model_name='censo',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]