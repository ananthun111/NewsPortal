# Generated by Django 4.0.2 on 2022-02-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_imagetable_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetable',
            name='image',
            field=models.ImageField(upload_to='images/uploads/% Y/% m/% d/'),
        ),
    ]
