# Generated by Django 4.1 on 2022-09-17 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAdmin', '0002_categhoras_proveedor_unidadmedida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categhoras',
            name='recargo',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4),
        ),
    ]
