# Generated by Django 5.0.2 on 2024-03-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.CharField(editable=False, max_length=25, primary_key=True, serialize=False, unique=True)),
                ('options', models.CharField(max_length=10)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
                'ordering': ['-date_created'],
            },
        ),
    ]
