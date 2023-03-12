from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0002_remove_lesson_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='teacher_note',
            field=models.TextField(blank=True),
        ),
    ]
