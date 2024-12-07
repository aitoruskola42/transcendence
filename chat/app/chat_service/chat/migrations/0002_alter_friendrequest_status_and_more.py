# Generated by Django 5.1.2 on 2024-11-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Accepted')], default=0),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='user_recipient_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='user_sender_blocked',
            field=models.BooleanField(default=False),
        ),
    ]
