# Generated by Django 4.0.4 on 2022-06-01 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_of_organizer', '0006_itemforplan_infoaboutplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoaboutplan',
            name='info',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='itemforplan',
            name='item',
            field=models.TextField(null=True),
        ),
    ]
