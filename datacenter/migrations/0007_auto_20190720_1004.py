from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0006_auto_20190702_1307'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Сhastisement',
            new_name='Chastisement',
        ),
    ]
