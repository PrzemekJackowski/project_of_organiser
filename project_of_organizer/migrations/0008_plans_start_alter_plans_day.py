# Generated by Django 4.0.4 on 2022-06-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_of_organizer', '0007_alter_infoaboutplan_info_alter_itemforplan_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='start',
            field=models.TimeField(default='12:00'),
        ),
        migrations.AlterField(
            model_name='plans',
            name='day',
            field=models.DateField(),
        ),
    ]
