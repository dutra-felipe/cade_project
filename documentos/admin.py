from django.contrib import admin
from .models import Documento

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_documento', 'tipo_processo', 'setor', 'ano', 'data_upload')
    list_filter = ('tipo_documento', 'tipo_processo', 'setor', 'ano')
    search_fields = ('titulo',)