# Generated by Django 5.0.3 on 2024-03-17 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_factura_cambio'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='monto_ingresado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='factura',
            name='cambio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]