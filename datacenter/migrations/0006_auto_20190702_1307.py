from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0005_auto_20190702_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolkid',
            old_name='entry_year',
            new_name='fuzzzbuzzz',
        ),
        migrations.RenameField(
            model_name='schoolkid',
            old_name='group_letter',
            new_name='entry_year',
        ),
        migrations.RenameField(
            model_name='schoolkid',
            old_name='fuzzzbuzzz',
            new_name='group_letter',
        ),
    ]
