# Generated by Django 2.2.7 on 2019-12-02 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_at', models.DateTimeField(default=None, verbose_name='start at')),
                ('complete_at', models.DateTimeField(default=None, verbose_name='complete_at')),
                ('status', models.SmallIntegerField(choices=[(0, ''), (1, 'Success'), (2, 'Failed'), (3, 'Cancelled')], default=0)),
            ],
        ),
    ]
