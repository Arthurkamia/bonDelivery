# Generated by Django 3.2 on 2023-07-01 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op', '0005_auto_20230701_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='code',
            field=models.CharField(editable=False, max_length=6, unique=True),
        ),
    ]
