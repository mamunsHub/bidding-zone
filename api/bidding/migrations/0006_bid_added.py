# Generated by Django 2.2.2 on 2019-06-27 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0005_auctionableimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]