# Generated by Django 4.0.5 on 2022-07-26 15:35

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productsizeset',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='productsizeset',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='product.productsizeset', verbose_name='Набор размеров'),
        ),
        migrations.AlterUniqueTogether(
            name='productsizeset',
            unique_together={('parent', 'slug_set_size')},
        ),
        migrations.RemoveField(
            model_name='productsizeset',
            name='set_size',
        ),
    ]