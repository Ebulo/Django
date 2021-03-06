# Generated by Django 3.0.6 on 2020-06-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_merchant', models.BooleanField(default=False)),
                ('first_name', models.TextField(max_length=40)),
                ('username', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=20)),
                ('adhar', models.IntegerField(max_length=12)),
                ('gstin', models.CharField(max_length=20)),
                ('bank', models.IntegerField(max_length=20)),
                ('acc_name', models.CharField(max_length=40)),
                ('ifsc', models.CharField(max_length=20)),
            ],
        ),
    ]
