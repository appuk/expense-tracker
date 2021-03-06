# Generated by Django 2.2 on 2020-04-18 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=30)),
                ('tax', models.FloatField(default=0)),
                ('tip', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('comments', models.CharField(max_length=100)),
            ],
        ),
    ]
