# Generated by Django 5.0.3 on 2024-03-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='cambio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
