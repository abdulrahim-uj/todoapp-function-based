# Generated by Django 4.1.3 on 2022-11-24 16:21

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
                ('name', models.CharField(max_length=128)),
                ('priority', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]
