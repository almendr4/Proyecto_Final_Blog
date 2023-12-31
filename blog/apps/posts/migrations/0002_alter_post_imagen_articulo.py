# Generated by Django 4.2.3 on 2023-07-12 12:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, default='static/post_default.png', null=True, upload_to='media/post'),
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('resumen', models.TextField()),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, default='media/articulo/default_articulo.jpg', null=True, upload_to='media/articulo')),
                ('estado', models.BooleanField(default=True)),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('categoria', models.ForeignKey(default='Sin categoria', null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.categoria')),
            ],
            options={
                'ordering': ('-publicado',),
            },
        ),
    ]
