# Generated by Django 4.1.5 on 2023-02-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_alter_productdetail_prod_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='purchase_number',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
