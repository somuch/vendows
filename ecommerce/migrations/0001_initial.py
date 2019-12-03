# Generated by Django 2.2.7 on 2019-12-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EcommIntegration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retailer_name', models.CharField(max_length=100)),
                ('retailer_id', models.CharField(max_length=150)),
                ('retailer_status', models.BooleanField(choices=[(0, 'OK'), (1, 'Not OK')], default=0)),
                ('bigcommerce_status', models.BooleanField(choices=[(0, 'OK'), (1, 'Not OK')], default=0)),
                ('woocommerce_status', models.BooleanField(choices=[(0, 'OK'), (1, 'Not OK')], default=0)),
                ('shopify_status', models.BooleanField(choices=[(0, 'OK'), (1, 'Not OK')], default=0)),
                ('update_at', models.DateTimeField()),
            ],
        ),
    ]
