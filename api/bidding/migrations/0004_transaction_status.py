# Generated by Django 2.2.2 on 2019-06-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0003_auctionable_ending'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETE', 'Complete')], default='PENDING', max_length=128),
        ),
    ]
