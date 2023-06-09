from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year_of_study', models.IntegerField()),
                ('year_of_study_group', models.CharField(max_length=1)),
                ('timeslot', models.IntegerField()),
                ('room', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('teacher_note', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Schoolkid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('birthday', models.DateField(null=True)),
                ('year_started_education', models.IntegerField(null=True)),
                ('year_of_study', models.IntegerField(null=True)),
                ('year_of_study_group',
                 models.CharField(max_length=1, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year_of_study', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Сhastisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateField()),
                (
                    'schoolkid', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='datacenter.Schoolkid')),
                ('subject',
                 models.ForeignKey(
                     null=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     to='datacenter.Subject')),
                ('teacher',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='datacenter.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='mark',
            name='schoolkid',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Schoolkid'),
        ),
        migrations.AddField(
            model_name='mark',
            name='subject',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Subject'),
        ),
        migrations.AddField(
            model_name='mark',
            name='teacher',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Teacher'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Subject'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Teacher'),
        ),
        migrations.AddField(
            model_name='commendation',
            name='schoolkid',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Schoolkid'),
        ),
        migrations.AddField(
            model_name='commendation',
            name='subject',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Subject'),
        ),
        migrations.AddField(
            model_name='commendation',
            name='teacher',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='datacenter.Teacher'),
        ),
    ]
