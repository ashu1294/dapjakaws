# Generated by Django 2.2.6 on 2019-10-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainmentmodel',
            name='jumbotron',
            field=models.ImageField(default='no image', upload_to='static/'),
        ),
    ]