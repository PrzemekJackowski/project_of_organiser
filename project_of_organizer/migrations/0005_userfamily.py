# Generated by Django 4.0.4 on 2022-05-31 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_of_organizer', '0004_remove_userinf_families'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_of_organizer.family')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]