from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "fecha_creacion")
    search_fields = ("titulo",)
    ordering = ("-fecha_creacion",)
