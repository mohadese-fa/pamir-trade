# Generated by Django 5.1 on 2024-11-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0034_productvariantclass_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticphotoclass',
            name='photo',
            field=models.ImageField(upload_to='images/staticPhoto'),
        ),
    ]