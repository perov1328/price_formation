# Generated by Django 5.0.1 on 2024-02-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_percentage',
            field=models.FloatField(blank=True, null=True, verbose_name='Процент скидки'),
        ),
    ]