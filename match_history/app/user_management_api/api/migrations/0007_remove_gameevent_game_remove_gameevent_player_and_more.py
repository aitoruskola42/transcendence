# Generated by Django 5.1.1 on 2024-10-14 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_match_round'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameevent',
            name='game',
        ),
        migrations.RemoveField(
            model_name='gameevent',
            name='player',
        ),
        migrations.RemoveField(
            model_name='match',
            name='player1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='player2',
        ),
        migrations.RemoveField(
            model_name='match',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='match',
            name='winner',
        ),
        migrations.CreateModel(
            name='Match2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_score', models.IntegerField(default=0)),
                ('player2_score', models.IntegerField(default=0)),
                ('round', models.IntegerField(default=1)),
                ('order', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_2p_player1', to='api.participation')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_2p_player2', to='api.participation')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_2_players', to='api.tournament')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches_2p_won', to='api.participation')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Match4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_score', models.IntegerField(default=0)),
                ('player2_score', models.IntegerField(default=0)),
                ('player3_score', models.IntegerField(default=0)),
                ('player4_score', models.IntegerField(default=0)),
                ('round', models.IntegerField(default=1)),
                ('order', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_4p_player1', to='api.participation')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_4p_player2', to='api.participation')),
                ('player3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_4p_player3', to='api.participation')),
                ('player4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_4p_player4', to='api.participation')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_4_players', to='api.tournament')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches_4p_won', to='api.participation')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='GameEvent',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
    ]
