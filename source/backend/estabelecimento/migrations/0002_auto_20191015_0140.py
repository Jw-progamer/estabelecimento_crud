# Generated by Django 2.2.5 on 2019-10-15 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='raio_distancia',
            field=models.IntegerField(),
        ),
    ]
