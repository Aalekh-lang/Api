# Generated by Django 3.1 on 2020-12-19 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retailerapi', '0003_auto_20201220_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcodeprice',
            name='BalanceQuantity',
        ),
    ]
