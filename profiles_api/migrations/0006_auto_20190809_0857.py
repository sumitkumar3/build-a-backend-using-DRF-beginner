# Generated by Django 2.2 on 2019-08-09 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0005_auto_20190809_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilefeedstatus',
            name='user_profile',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
