# Generated by Django 3.2.5 on 2022-05-16 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sign_Up_Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobileno', models.BigIntegerField()),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]