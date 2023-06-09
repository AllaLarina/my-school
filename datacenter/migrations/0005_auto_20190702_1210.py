import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('datacenter', '0004_auto_20190702_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commendation',
            name='created',
            field=models.DateField(db_index=True, verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='commendation',
            name='schoolkid',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Schoolkid', verbose_name='ученик'),
        ),
        migrations.AlterField(
            model_name='commendation',
            name='subject',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='datacenter.Subject',
                verbose_name='предмет'),
        ),
        migrations.AlterField(
            model_name='commendation',
            name='teacher',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Teacher', verbose_name='учитель'),
        ),
        migrations.AlterField(
            model_name='commendation',
            name='text',
            field=models.TextField(verbose_name='похвала'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateField(db_index=True, verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='group_letter',
            field=models.CharField(db_index=True, max_length=1,
                                   verbose_name='литера класса'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='room',
            field=models.CharField(db_index=True,
                                   help_text='Класс где проходят занятия.',
                                   max_length=50, verbose_name='класс'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Subject',
                verbose_name='предмет'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Teacher',
                verbose_name='учитель'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='timeslot',
            field=models.IntegerField(
                db_index=True,
                help_text='Номер слота в расписании уроков на этот день.',
                verbose_name='слот'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='year_of_study',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='mark',
            name='created',
            field=models.DateField(verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='points',
            field=models.IntegerField(verbose_name='оценка'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='schoolkid',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Schoolkid', verbose_name='ученик'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='subject',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Subject', verbose_name='предмет'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='teacher',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Teacher', verbose_name='учитель'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='teacher_note',
            field=models.TextField(blank=True, verbose_name='комментарий'),
        ),
        migrations.AlterField(
            model_name='schoolkid',
            name='birthday',
            field=models.DateField(null=True, verbose_name='день рождения'),
        ),
        migrations.AlterField(
            model_name='schoolkid',
            name='entry_year',
            field=models.IntegerField(null=True,
                                      verbose_name='год начала обучения'),
        ),
        migrations.AlterField(
            model_name='schoolkid',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='schoolkid',
            name='group_letter',
            field=models.CharField(max_length=1, blank=True,
                                   verbose_name='литера класса'),
        ),
        migrations.AlterField(
            model_name='schoolkid',
            name='year_of_study',
            field=models.IntegerField(null=True, verbose_name='год обучения'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(max_length=200, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='year_of_study',
            field=models.IntegerField(db_index=True, null=True,
                                      verbose_name='год обучения'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birthday',
            field=models.DateField(null=True, verbose_name='день рождения'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='сhastisement',
            name='created',
            field=models.DateField(db_index=True, verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='сhastisement',
            name='schoolkid',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Schoolkid', verbose_name='ученик'),
        ),
        migrations.AlterField(
            model_name='сhastisement',
            name='subject',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='datacenter.Subject',
                verbose_name='предмет'),
        ),
        migrations.AlterField(
            model_name='сhastisement',
            name='teacher',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Teacher', verbose_name='учитель'),
        ),
        migrations.AlterField(
            model_name='сhastisement',
            name='text',
            field=models.TextField(verbose_name='замечание'),
        ),
    ]
