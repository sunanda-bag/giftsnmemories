# Generated by Django 3.1.7 on 2021-10-11 13:55

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20211010_2255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='premadeproduct',
            options={'verbose_name_plural': '9. Premade Products'},
        ),
        migrations.AlterModelOptions(
            name='premadeproductvariation',
            options={'verbose_name_plural': '9. Premade Products Variation'},
        ),
        migrations.AddField(
            model_name='premadeproduct',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='premadeproductvariation',
            name='image1',
            field=models.ImageField(upload_to=product.models.premade_productvariation_image),
        ),
        migrations.AlterField(
            model_name='premadeproductvariation',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='premadeproductvariation',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='image1',
            field=models.ImageField(upload_to=product.models.product_variation_image),
        ),
    ]