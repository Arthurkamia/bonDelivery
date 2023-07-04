# Generated by Django 4.2 on 2023-07-03 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('op', '0012_agent_mail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'verbose_name': 'Agent', 'verbose_name_plural': 'Agents'},
        ),
        migrations.AlterModelOptions(
            name='bonus',
            options={'verbose_name': 'Bon', 'verbose_name_plural': 'Bons'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Catégorie', 'verbose_name_plural': 'Catégories'},
        ),
        migrations.RemoveField(
            model_name='bonus',
            name='check',
        ),
        migrations.AddField(
            model_name='bonus',
            name='checko',
            field=models.BooleanField(default=False, editable=False, verbose_name='état'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_Category', to='op.category', verbose_name='catégorie'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='create_at',
            field=models.DateTimeField(auto_now=True, verbose_name='créé le'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='cuid',
            field=models.CharField(blank=None, max_length=8, verbose_name='cuid'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='departement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_Department', to='op.departement', verbose_name='département'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='direction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_Direction', to='op.direction', verbose_name='direction'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='image',
            field=models.ImageField(default='images/blogs/blog.jpg', null=True, upload_to='images/agent/', verbose_name="photo de l'agent"),
        ),
        migrations.AlterField(
            model_name='agent',
            name='mail',
            field=models.EmailField(blank=None, max_length=254, verbose_name='adresse e-mail'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='modify_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='modifié le'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='nom',
            field=models.CharField(blank=None, default='Nom', max_length=50, verbose_name='nom de famiille'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='prenom',
            field=models.CharField(blank=None, default='Prénom', max_length=50, verbose_name='prénom'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='status',
            field=models.BooleanField(default=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='agent',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Agent_Bonus', to='op.agent', verbose_name='agent'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='check_at',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='utilisé le'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='code',
            field=models.CharField(editable=False, max_length=6, unique=True, verbose_name='code du bon'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='create_at',
            field=models.DateTimeField(auto_now=True, verbose_name='créé le'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='expire_at',
            field=models.DateTimeField(verbose_name='expire le'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='facture',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='images/factures/', verbose_name='facture'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='modify_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='modifié le'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='partenaire',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Partenaire_Bonus', to=settings.AUTH_USER_MODEL, verbose_name='créditeur'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='status',
            field=models.BooleanField(default=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_Bonus', to=settings.AUTH_USER_MODEL, verbose_name='créateur'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='valeur',
            field=models.FloatField(blank=True, null=True, verbose_name='valeur du bon'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='valeur_deduite',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='valeur déduite'),
        ),
        migrations.AlterField(
            model_name='category',
            name='create_at',
            field=models.DateTimeField(auto_now=True, verbose_name='crééee le'),
        ),
        migrations.AlterField(
            model_name='category',
            name='modify_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='modifiée le'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=None, max_length=40, verbose_name='titre'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True, verbose_name='status'),
        ),
    ]
