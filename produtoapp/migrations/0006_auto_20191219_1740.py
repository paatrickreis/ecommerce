# Generated by Django 3.0.1 on 2019-12-19 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtoapp', '0005_produto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
