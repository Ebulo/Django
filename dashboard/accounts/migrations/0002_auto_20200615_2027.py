# Generated by Django 3.0.6 on 2020-06-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant_details',
            name='adhar',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='merchant_details',
            name='bank',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='merchant_details',
            name='phone',
            field=models.IntegerField(),
        ),
    ]