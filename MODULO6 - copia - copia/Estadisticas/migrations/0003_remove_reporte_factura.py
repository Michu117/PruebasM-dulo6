# Generated by Django 5.1.4 on 2025-01-19 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estadisticas', '0002_item_factura_producto_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporte',
            name='factura',
        ),
    ]
