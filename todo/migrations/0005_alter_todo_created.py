# Generated by Django 4.0.5 on 2022-06-03 07:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]