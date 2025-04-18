# Generated by Django 5.0.2 on 2024-03-14 18:39

import core.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionsDate',
            fields=[
                ('id', models.CharField(editable=False, max_length=25, primary_key=True, serialize=False, unique=True)),
                ('election_date', models.DateTimeField()),
                ('is_done', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Elections date',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Aspirant',
            fields=[
                ('id', models.CharField(editable=False, max_length=25, primary_key=True, serialize=False, unique=True)),
                ('post', models.CharField(max_length=30)),
                ('total_votes', models.PositiveIntegerField(default=0, editable=False)),
                ('aspirant_dp', models.ImageField(upload_to=core.models.user_path_directory)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.voter')),
            ],
            options={
                'ordering': ['name', 'post'],
            },
        ),
        migrations.CreateModel(
            name='VotingRecord',
            fields=[
                ('id', models.CharField(editable=False, max_length=25, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('elected_post', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='core.aspirant')),
                ('voter', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.voter')),
            ],
            options={
                'ordering': ['elected_post', 'voter'],
            },
        ),
    ]
