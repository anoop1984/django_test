# Generated by Django 3.0.3 on 2020-02-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcheck',
            name='command',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='healthcheck',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='healthcheck',
            name='desc',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='healthcheck',
            name='verdict',
            field=models.CharField(max_length=264),
        ),
    ]
