# Generated by Django 3.2.2 on 2021-05-17 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='wpn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Item',
            new_name='clt',
        ),
    ]
