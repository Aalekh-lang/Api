# Generated by Django 3.1 on 2021-01-05 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailerapi', '0010_productrevenuedeatils_paymentmode_narration'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcodepriceapi',
            name='Retailer_ID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productrevenuedeatils_paymentmode',
            name='Retailer_ID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
