# Generated by Django 4.1 on 2022-09-10 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGerente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finca',
            name='nitFinca',
            field=models.IntegerField(),
        ),
    ]