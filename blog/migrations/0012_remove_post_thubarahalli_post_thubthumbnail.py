# Generated by Django 4.0.2 on 2022-02-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_meta_description_alter_post_thubarahalli'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thubarahalli',
        ),
        migrations.AddField(
            model_name='post',
            name='thubthumbnail',
            field=models.ImageField(default='', upload_to='thumbnail/uploads/'),
        ),
    ]