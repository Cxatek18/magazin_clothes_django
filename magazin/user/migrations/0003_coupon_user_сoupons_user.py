# Generated by Django 4.0.5 on 2022-08-15 13:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_сoupon', models.CharField(max_length=50, unique=True)),
                ('valid_from', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('valid_to', models.DateTimeField(auto_now=True, verbose_name='Дата обновления купона')),
                ('discount_сoupon', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Coupon',
                'verbose_name_plural': 'Coupons',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='сoupons_user',
            field=models.ManyToManyField(blank=True, related_name='сoupons_user', to='user.coupon', verbose_name='Купоны'),
        ),
    ]
