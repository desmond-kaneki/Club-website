# Generated by Django 2.2.6 on 2019-11-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20191101_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='img1',
            field=models.ImageField(null=True, upload_to='event_img/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='img2',
            field=models.ImageField(null=True, upload_to='event_img/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='img3',
            field=models.ImageField(null=True, upload_to='event_img/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='img4',
            field=models.ImageField(null=True, upload_to='event_img/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='img5',
            field=models.ImageField(null=True, upload_to='event_img/'),
        ),
    ]
