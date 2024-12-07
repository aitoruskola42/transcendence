# Generated by Django 5.1.2 on 2024-10-18 20:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_match4_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_type', models.CharField(choices=[('INDIVIDUAL', 'Partida Individual'), ('SEMIFINAL', 'Semifinal de Torneo'), ('FINAL', 'Final de Torneo')], max_length=20)),
                ('tournament_id', models.IntegerField(default=0)),
                ('player1_id', models.IntegerField()),
                ('player2_id', models.IntegerField()),
                ('player1_display_name', models.CharField(max_length=100)),
                ('player2_display_name', models.CharField(max_length=100)),
                ('player1_score', models.IntegerField(default=0)),
                ('player2_score', models.IntegerField(default=0)),
                ('winner_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='match4',
            name='player1',
        ),
        migrations.RemoveField(
            model_name='match4',
            name='player2',
        ),
        migrations.RemoveField(
            model_name='match4',
            name='player3',
        ),
        migrations.RemoveField(
            model_name='match4',
            name='player4',
        ),
        migrations.RemoveField(
            model_name='match4',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='match4',
            name='winner',
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='participation',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='user',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='creator',
            new_name='winner_id',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='max_participants',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='status',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='tournament_type',
        ),
        migrations.DeleteModel(
            name='Match2',
        ),
        migrations.DeleteModel(
            name='Match4',
        ),
        migrations.DeleteModel(
            name='Participation',
        ),
    ]
