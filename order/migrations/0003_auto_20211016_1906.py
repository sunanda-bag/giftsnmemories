# Generated by Django 3.1.7 on 2021-10-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20211016_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxtype',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cardtype',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
