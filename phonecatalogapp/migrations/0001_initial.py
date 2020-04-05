# Generated by Django 3.0.5 on 2020-04-05 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('reg_date', models.DateField(verbose_name='registration date')),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
    ]