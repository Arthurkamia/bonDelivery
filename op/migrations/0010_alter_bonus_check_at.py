# Generated by Django 3.2 on 2023-07-01 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op', '0009_bonus_check_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='check_at',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
