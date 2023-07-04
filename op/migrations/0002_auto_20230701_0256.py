# Generated by Django 3.2 on 2023-07-01 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('op', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='cuid',
            field=models.CharField(blank=None, max_length=6),
        ),
        migrations.AlterField(
            model_name='agent',
            name='departement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_Department', to='op.departement'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='direction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_Direction', to='op.direction'),
        ),
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(editable=False, max_length=6)),
                ('facture', models.ImageField(null=True, upload_to='images/factures/')),
                ('valeur', models.FloatField()),
                ('valeur_deduite', models.FloatField()),
                ('slug', models.SlugField()),
                ('status', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('expire_at', models.DateTimeField(auto_now=True)),
                ('modify_at', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_Category', to='op.agent')),
                ('partenaire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_Category', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]