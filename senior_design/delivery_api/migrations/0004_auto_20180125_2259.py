# Generated by Django 2.0 on 2018-01-25 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_api', '0003_auto_20180125_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]