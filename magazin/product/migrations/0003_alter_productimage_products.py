# Generated by Django 4.0.5 on 2022-07-14 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_productimage_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prodimg', to='product.product'),
        ),
    ]
