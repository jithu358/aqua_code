# Generated by Django 5.0.7 on 2024-09-05 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_orders_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
