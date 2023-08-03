# Generated by Django 4.2.3 on 2023-08-03 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_articulo_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(default=None, limit_choices_to={'nombre__isnull': False}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.categoria'),
        ),
    ]