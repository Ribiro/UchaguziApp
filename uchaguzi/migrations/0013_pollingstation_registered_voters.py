# Generated by Django 3.0.8 on 2022-12-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uchaguzi', '0012_auto_20221205_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollingstation',
            name='registered_voters',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
