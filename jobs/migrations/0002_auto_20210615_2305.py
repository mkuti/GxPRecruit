# Generated by Django 3.2.3 on 2021-06-15 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_contract',
            field=models.CharField(default='', max_length=254, null=True, verbose_name=(('Permanent', 'permanent'), ('6 Months', '6 months'), ('1 Year', '1 year'))),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_location',
            field=models.CharField(default='', max_length=254, null=True, verbose_name=(('Remote', 'remote'), ('Overseas', 'overseas'), ('Cork', 'cork'), ('Galway', 'galway'), ('Dublin', 'dublin'))),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_schedule',
            field=models.CharField(default='', max_length=254, null=True, verbose_name=(('Full Time', 'full time'), ('Part Time', 'part time'), ('20 Hours', '20 hours'))),
        ),
        migrations.DeleteModel(
            name='Contract',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
