# Generated by Django 5.1.2 on 2024-10-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_participation_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='round',
            field=models.IntegerField(default=1),
        ),
    ]
