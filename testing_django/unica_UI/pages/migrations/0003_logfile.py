# Generated by Django 3.0.3 on 2020-03-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200225_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logfile',
            fields=[
                ('logfile', models.FileField(upload_to='logs/')),
                ('uploaded_at', models.DateField(primary_key=True, serialize=False)),
            ],
        ),
    ]
