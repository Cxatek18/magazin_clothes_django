# Generated by Django 4.0.5 on 2022-08-15 13:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_coupon_user_сoupons_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount_сoupon',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25000)]),
        ),
    ]
