# Generated by Django 2.1.5 on 2020-01-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_hunter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='votes_total',
            field=models.IntegerField(verbose_name=1),
        ),
    ]
