# Generated by Django 3.1.3 on 2020-11-10 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('mail', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
                ('tel', models.PositiveIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], max_length=1)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('species', models.CharField(max_length=20)),
            ],
        ),
    ]