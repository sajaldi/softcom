
from django.contrib import admin
from ...models import Area


class AreasInline(admin.TabularInline):
    model=Area
    extra =1
    fields= ('nombre','principal')
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'principal')  # Muestra el nombre y principal en la lista
    inlines = [AreasInline]
    list_filter = ('principal',)  # Permite filtrar por el campo principal