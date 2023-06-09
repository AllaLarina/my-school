from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('datacenter', '0007_auto_20190720_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolkid',
            name='entry_year',
            field=models.IntegerField(null=True,
                                      verbose_name='год начала обучения'),
        ),
        migrations.AlterField(
            model_name='schoolkid',
            name='group_letter',
            field=models.CharField(max_length=1, blank=True,
                                   verbose_name='литера класса'),
        ),
    ]
