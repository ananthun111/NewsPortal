# Generated by Django 4.0.2 on 2022-02-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_post_thubarahalli_post_thubthumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thubthumbnail',
            field=models.ImageField(upload_to='thumbnail/uploads/'),
        ),
    ]