# Generated by Django 2.2.2 on 2019-06-23 18:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0002_auto_20190623_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionable',
            name='ending',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]