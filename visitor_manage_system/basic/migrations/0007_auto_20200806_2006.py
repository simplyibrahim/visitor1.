# Generated by Django 3.0.8 on 2020-08-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_auto_20200806_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='Phone_no',
            field=models.CharField(default=91, max_length=10),
        ),
        migrations.AlterField(
            model_name='host',
            name='flat_no',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
