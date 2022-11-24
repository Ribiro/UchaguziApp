# Generated by Django 3.0.8 on 2022-11-24 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uchaguzi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollingstation',
            name='admin',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='assigned_polling_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='uchaguzi.PollingStation'),
        ),
    ]
