from django.contrib.auth.models import User

from django.db import models
from django.template.defaultfilters import slugify

from django.utils.crypto import get_random_string


class Category(models.Model):
    name = models.CharField('titre',blank=None, null=False, max_length=40)
    slug = models.SlugField('slug',)
    status = models.BooleanField('status',default=True)
    create_at = models.DateTimeField('crééee le',auto_now=True)
    modify_at = models.DateTimeField('modifiée le',auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'


class Direction(models.Model):
    name = models.CharField(blank=None, null=False, max_length=40)
    slug = models.SlugField()
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    modify_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Departement(models.Model):
    name = models.CharField(blank=None, null=False, max_length=40)
    slug = models.SlugField()
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    modify_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Agent(models.Model):
    category = models.ForeignKey(Category, verbose_name='catégorie',on_delete=models.SET_NULL, related_name="User_Category", null=True, blank=True)
    direction = models.ForeignKey( Direction,verbose_name='direction', on_delete=models.SET_NULL, related_name="User_Direction", null=True, blank=True)
    departement = models.ForeignKey(Departement, verbose_name='département',on_delete=models.SET_NULL, related_name="User_Department", null=True, blank=True)
    cuid = models.CharField('cuid', blank=None, null=False, max_length=8)
    mail = models.EmailField('adresse e-mail', blank=None, null=False,)
    nom = models.CharField('nom de famiille', blank=None, null=False, default='Nom', max_length=50)
    prenom = models.CharField('prénom', blank=None, null=False, default='Prénom', max_length=50)
    image = models.ImageField("photo de l'agent", null=True, default="images/blogs/blog.jpg", upload_to="images/agent/")
    #slug = models.SlugField()
    status = models.BooleanField('status', default=True)
    create_at = models.DateTimeField('créé le', auto_now=True)
    modify_at = models.DateTimeField('modifié le', auto_now_add=True)

    def __str__(self):
        return self.nom + ' ' + self.prenom + ' ' + self.cuid

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'


class Bonus(models.Model):
    agent = models.ForeignKey(Agent, verbose_name='agent', on_delete=models.SET_NULL, related_name="Agent_Bonus", null=True, blank=True, editable=False,)
    user = models.ForeignKey(User, verbose_name='créateur', on_delete=models.SET_NULL, related_name="User_Bonus", null=True, blank=True, editable=False,)
    partenaire = models.ForeignKey(User, verbose_name='créditeur', on_delete=models.SET_NULL, related_name="Partenaire_Bonus", null=True, blank=True, editable=False,)
    code = models.CharField('code du bon', max_length=6, editable=False, unique=True )
    facture = models.ImageField('facture', null=True, upload_to="images/factures/", blank=True,editable=False,)
    valeur = models.FloatField('valeur du bon', null=True, blank=True)
    valeur_deduite = models.FloatField('valeur déduite', null=True, blank=True, editable=False,)
    #slug = models.SlugField(null=True, blank=True)
    status = models.BooleanField('status', default=True)
    checko = models.BooleanField('état', default=False, editable=False,)
    create_at = models.DateTimeField('créé le', auto_now=True)
    expire_at = models.DateTimeField('expire le', )
    check_at = models.DateTimeField('utilisé le', null=True, blank=True,editable=False)
    modify_at = models.DateTimeField('modifié le', auto_now_add=True)

    def __str__(self):
        return self.agent.nom

    class Meta:
        verbose_name = 'Bon'
        verbose_name_plural = 'Bons'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.code is None or self.code == '':
            self.code = get_random_string(6).upper()
        super().save(*args, **kwargs)