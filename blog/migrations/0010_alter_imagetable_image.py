# Generated by Django 4.0.2 on 2022-02-06 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_imagetable_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetable',
            name='image',
            field=models.ImageField(upload_to='images/uploads/'),
        ),
    ]
