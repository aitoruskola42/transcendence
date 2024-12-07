# Generated by Django 5.1.1 on 2024-10-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_user_avatar_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiuser',
            name='avatar_image',
            field=models.ImageField(blank=True, default='avatars/default.jpg', null=True, upload_to='avatars/'),
        ),
    ]
