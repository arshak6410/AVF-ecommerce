# Generated by Django 4.2.1 on 2023-07-24 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='images',
            field=models.ImageField(upload_to='photos/brant'),
        ),
    ]
