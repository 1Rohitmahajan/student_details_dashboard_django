# Generated by Django 4.2.6 on 2023-10-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=2)),
                ('college', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
