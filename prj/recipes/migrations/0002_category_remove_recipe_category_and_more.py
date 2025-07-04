# Generated by Django 5.2.3 on 2025-06-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='nutrients',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(to='recipes.category'),
        ),
    ]
