# Generated by Django 4.2.4 on 2023-08-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('is_notified', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('due_date',),
            },
        ),
    ]
