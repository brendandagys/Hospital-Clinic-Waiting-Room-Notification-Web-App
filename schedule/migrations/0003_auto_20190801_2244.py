# Generated by Django 2.2.3 on 2019-08-02 02:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_schedule_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='time',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_1',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_10',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_11',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_12',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_13',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_14',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_15',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_16',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_17',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_18',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_19',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_2',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_20',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_21',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_22',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_23',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_24',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_25',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_26',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_27',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_28',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_29',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_3',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_30',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_31',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_32',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_33',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_34',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_35',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_36',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_37',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_38',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_39',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_4',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_40',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_41',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_42',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_43',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_44',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_45',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_46',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_47',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_48',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_49',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_5',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_50',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_6',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_7',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_8',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='time_9',
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_1',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 1'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_10',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 10'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_11',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 11'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_12',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 12'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_13',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 13'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_14',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 14'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_15',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 15'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_16',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 16'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_17',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 17'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_18',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 18'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_19',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 19'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_2',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 2'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_20',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 20'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_21',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 21'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_22',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 22'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_23',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 23'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_24',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 24'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_25',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 25'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_26',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 26'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_27',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 27'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_28',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 28'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_29',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 29'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_3',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 3'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_30',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 30'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_31',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 31'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_32',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 32'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_33',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 33'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_34',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 34'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_35',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 35'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_36',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 36'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_37',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 37'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_38',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 38'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_39',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 39'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_4',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 4'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_40',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 40'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_41',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 41'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_42',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 42'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_43',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 43'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_44',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 44'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_45',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 45'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_46',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 46'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_47',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 47'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_48',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 48'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_49',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 49'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_5',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 5'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_50',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 50'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_6',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 6'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_7',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 7'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_8',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 8'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot_9',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'email': '', 'modality': '', 'name': '', 'phone': '', 'slot': '', 'status': ''}, verbose_name='Slot 9'),
        ),
    ]