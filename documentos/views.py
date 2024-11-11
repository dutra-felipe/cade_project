from django.shortcuts import render
from .models import Documento


def busca_documentos(request):
    query = request.GET.get('q', '')
    tipo_documento = request.GET.getlist('tipo_documento')
    tipo_processo = request.GET.getlist('tipo_processo')
    setor = request.GET.getlist('setor')
    anos = request.GET.getlist('ano')

    documentos = Documento.objects.all()

    # Aplicar filtros
    if query:
        documentos = documentos.filter(titulo__icontains=query)

    if tipo_documento:
        documentos = documentos.filter(tipo_documento__in=tipo_documento)

    if tipo_processo:
        documentos = documentos.filter(tipo_processo__in=tipo_processo)

    if setor:
        documentos = documentos.filter(setor__in=setor)

    if anos:
        documentos = documentos.filter(ano__in=anos)

    # Pegar anos únicos para o filtro
    anos_disponiveis = Documento.objects.values_list('ano', flat=True).distinct().order_by('-ano')

    context = {
        'documentos': documentos,
        'query': query,
        'anos_disponiveis': anos_disponiveis,
        'filtros_ativos': {
            'tipo_documento': tipo_documento,
            'tipo_processo': tipo_processo,
            'setor': setor,
            'anos': anos,
        },
        'documento': Documento  # Adicionando o modelo ao context

    }

    return render(request, 'jurisprudencia.html', context)
