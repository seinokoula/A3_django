# Generated by Django 4.1.4 on 2022-12-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
