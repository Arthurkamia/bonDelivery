from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


from op.models import Category, Direction, Departement, Agent, Bonus

from import_export.admin import ImportExportModelAdmin


class MyAdminSite(admin.AdminSite):
    site_header = "Bon delivery administration"
    site_title = 'Bon delivery'
    index_title = 'Bienvenue dans votre site de délivrance de bon'

    def each_context(self, request):
        context = super().each_context(request)
        return context


class BonusInline(admin.TabularInline):
    model = Bonus
    list_display = ['agent', 'user', 'partenaire', 'code',  'valeur', 'valeur_deduite', 'create_at',  'expire_at',  'checko',  'status',  'check_at', ]
    readonly_fields = ('agent', 'code', 'partenaire', 'valeur_deduite',  'checko',  'check_at', 'user', )
    extra = 1
    show_change_link = True


class AgentAdmin(ImportExportModelAdmin):
    list_display = ['cuid', 'nom', 'prenom', 'category', 'direction', 'departement', 'status', ]
    list_filter = ['category', 'direction', 'departement', ]
   # readonly_fields = ('image_tag',)
    inlines = [BonusInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        for ob in obj.Agent_Bonus.all():
            if ob.user is None:
                ob.user = request.user
                ob.save()
        super().save_model(request, obj, form, change)


class BonusAdmin(ImportExportModelAdmin):
    list_display = ['agent', 'user', 'partenaire', 'code',  'valeur', 'valeur_deduite', 'create_at',  'expire_at',  'checko',  'status',  'check_at', ]
    #list_filter = ['category', 'agent', 'departement', ]
    readonly_fields = ('agent', 'code', 'partenaire', 'valeur_deduite',  'checko',  'check_at', 'user', )
    #inlines = [CarImageInline, CarVariantsInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.user is None:
            obj.user = request.user

        super().save_model(request, obj, form, change)

user = get_user_model()

admin.site = MyAdminSite()
admin.site.register(user)
admin.site.register(Group)
admin.site.register(Category)
admin.site.register(Direction)
admin.site.register(Departement)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Bonus, BonusAdmin)


admin.site.template_pack = 'admin/change'
