# Generated by Django 2.2.6 on 2019-11-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='event_img/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='event_img/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='event_img/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='event_img/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='img5',
            field=models.ImageField(blank=True, null=True, upload_to='event_img/'),
        ),
    ]
