# Generated by Django 3.1 on 2020-12-18 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailerapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcodepriceapi',
            name='BalanceQuantity',
            field=models.IntegerField(default=0.0, max_length=20),
            preserve_default=False,
        ),
    ]
