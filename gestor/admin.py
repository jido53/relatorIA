# gestor/admin.py
from django.contrib import admin
from .models import Case, Document, Stage, Entity, Summary, UserProfile, Jurisdiction, CaseType, EntityType


@admin.register(EntityType)
class EntityTypeAdmin(admin.ModelAdmin):
  list_display = ('name', 'description')
  search_fields = ('name', )


# Configuración del modelo Entity en el administrador
@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
  list_display = ('entity_type', 'value', 'description', 'document',
                  'parent_entity')
  search_fields = ('value', 'entity_type__name', 'description')
  list_filter = ('entity_type', 'document')
  autocomplete_fields = ['parent_entity'
                         ]  # Habilita búsqueda en entidades relacionadas


admin.site.register(Case)
admin.site.register(Document)
admin.site.register(Stage)
#admin.site.register(Entity)
admin.site.register(Summary)
admin.site.register(UserProfile)
admin.site.register(Jurisdiction)
admin.site.register(CaseType)
