# Generated by Django 2.2.7 on 2019-12-03 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20191203_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecommintegration',
            name='bigcommerce_status',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ecommintegration',
            name='retailer_status',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='ecommintegration',
            name='shopify_status',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ecommintegration',
            name='woocommerce_status',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
