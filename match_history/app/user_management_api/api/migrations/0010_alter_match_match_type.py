# Generated by Django 5.1.2 on 2024-10-19 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_match_remove_match4_player1_remove_match4_player2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_type',
            field=models.CharField(choices=[('INDIVIDUAL', 'INDIVIDUAL'), ('SEMIFINAL', 'SEMIFINAL'), ('FINAL', 'FINAL')], max_length=20),
        ),
    ]
