# Generated by Django 3.0.5 on 2020-04-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200414_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sub_title',
            field=models.CharField(max_length=100, null='True'),
        ),
    ]
