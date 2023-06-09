from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0003_auto_20190627_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commendation',
            old_name='date',
            new_name='created'
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='year_of_study_group',
            new_name='group_letter',
        ),
        migrations.RenameField(
            model_name='mark',
            old_name='date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='schoolkid',
            old_name='year_of_study_group',
            new_name='group_letter',
        ),
        migrations.RenameField(
            model_name='schoolkid',
            old_name='year_started_education',
            new_name='entry_year',
        ),
        migrations.RenameField(
            model_name='сhastisement',
            old_name='date',
            new_name='created',
        ),
    ]
