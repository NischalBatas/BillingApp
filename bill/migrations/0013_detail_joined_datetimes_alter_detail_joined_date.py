# Generated by Django 4.1.5 on 2023-02-03 18:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0012_remove_detail_purchase_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='joined_datetimes',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detail',
            name='joined_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
