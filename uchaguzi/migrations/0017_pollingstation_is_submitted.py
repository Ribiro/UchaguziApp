# Generated by Django 3.0.8 on 2022-12-06 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uchaguzi', '0016_auto_20221206_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollingstation',
            name='is_submitted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
