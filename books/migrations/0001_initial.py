# Generated by Django 4.2.3 on 2023-07-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=40)),
                ('b_desc', models.CharField(max_length=500)),
                ('b_author', models.CharField(max_length=30)),
            ],
        ),
    ]
