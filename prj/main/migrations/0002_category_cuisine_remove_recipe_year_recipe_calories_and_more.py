# Generated by Django 5.1.6 on 2025-04-03 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='year',
        ),
        migrations.AddField(
            model_name='recipe',
            name='calories',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='difficulty',
            field=models.SmallIntegerField(choices=[(1, '★☆☆'), (2, '★★☆'), (3, '★★★')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipes/'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='nutrition_table',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(to='main.category'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cuisine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.cuisine'),
        ),
    ]
